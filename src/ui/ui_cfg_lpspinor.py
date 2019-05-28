#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import math
import RT10yy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_LpspiNor
from utils import sound

class secBootUiCfgLpspiNor(bootDeviceWin_LpspiNor.bootDeviceWin_LpspiNor):
    def __init__(self, parent):
        bootDeviceWin_LpspiNor.bootDeviceWin_LpspiNor.__init__(self, parent)
        self._setLanguage()
        lpspiNorOpt0, lpspiNorOpt1 = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_LpspiNor)
        #1. Prepare SPI NOR/EEPROM option block
        # bit [31:28] tag, fixed to 0x0c
        # bit [27:24] Size, (bytes/4) - 1
        # bit [23:20] SPI instance
        # bit [19:16] PCS index
        # bit [15:12] Flash type, 0-SPI NOR, 1-SPI EEPROM
        # bit [11:08] Flash size(Bytes) 0 - 512K, 1-1M, 2-2M, 3-4M, 4-8M
        #             13-64K, 14-128K, 15-256K, etc.
        # bit [07:04] Sector size (Bytes), 0-4K, 1-8K, 2-32K, 3-64K,
        #             4-128K, 5-256K
        # bit [03:00] Page size (Bytes) 0-256, 1-512

        self.lpspiNorOpt0 = lpspiNorOpt0
        self.lpspiNorOpt1 = lpspiNorOpt1
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_memOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_memOpt'][langIndex])
        self.m_staticText_deviceType.SetLabel(uilang.kSubLanguageContentDict['sText_deviceType'][langIndex])
        self.m_staticText_pageSize.SetLabel(uilang.kSubLanguageContentDict['sText_pageSize'][langIndex])
        self.m_staticText_sectorSize.SetLabel(uilang.kSubLanguageContentDict['sText_sectorSize'][langIndex])
        self.m_staticText_totalSize.SetLabel(uilang.kSubLanguageContentDict['sText_totalSize'][langIndex])
        self.m_notebook_spiOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_spiOpt'][langIndex])
        self.m_staticText_spiIndex.SetLabel(uilang.kSubLanguageContentDict['sText_spiIndex'][langIndex])
        self.m_staticText_spiPcs.SetLabel(uilang.kSubLanguageContentDict['sText_spiPcs'][langIndex])
        self.m_staticText_spiSpeed.SetLabel(uilang.kSubLanguageContentDict['sText_spiSpeed'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_lpspinor_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_lpspinor_cancel'][langIndex])

    def _recoverLastSettings ( self ):
        deviceType = (self.lpspiNorOpt0 & 0x0000F000) >> 12
        self.m_choice_deviceType.SetSelection(deviceType)

        pageSize = (self.lpspiNorOpt0 & 0x0000000F) >> 0
        if pageSize <= 2:
            self.m_choice_pageSize.SetSelection(pageSize + 3)
        else:
            self.m_choice_pageSize.SetSelection(pageSize - 3)

        sectorSize = (self.lpspiNorOpt0 & 0x000000F0) >> 4
        self.m_choice_sectorSize.SetSelection(sectorSize)

        totalSize = (self.lpspiNorOpt0 & 0x00000F00) >> 8
        if totalSize <= 11:
            self.m_choice_totalSize.SetSelection(totalSize + 4)
        else:
            self.m_choice_totalSize.SetSelection(totalSize - 12)

        spiIndex = (self.lpspiNorOpt0 & 0x00F00000) >> 20
        self.m_choice_spiIndex.SetSelection(spiIndex - 1)

        spiPcs = (self.lpspiNorOpt0 & 0x000F0000) >> 16
        self.m_choice_spiPcs.SetSelection(spiPcs)

        spiSpeed = (self.lpspiNorOpt1 & 0x0000000F) >> 0
        self.m_choice_spiSpeed.SetSelection(spiSpeed)

    def _getDeviceType( self ):
        txt = self.m_choice_deviceType.GetString(self.m_choice_deviceType.GetSelection())
        if txt == '1bit NOR Flash':
            val = 0x0
        elif txt == 'EEPROM':
            val = 0x1
        else:
            pass
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFFFF0FFF) | (val << 12)

    def _getPageSize( self ):
        val = int(self.m_choice_pageSize.GetString(self.m_choice_pageSize.GetSelection()))
        val = int(math.log(val, 2))
        if val >= 8:
            val -= 8
        elif val >= 5:
            val -= 2
        else:
            pass
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFFFFFFF0) | (val << 0)

    def _getSectorSize( self ):
        val = int(self.m_choice_sectorSize.GetString(self.m_choice_sectorSize.GetSelection()))
        val = int(math.log(val, 2))
        if val <= 3:
            val -= 2
        else:
            val -= 3
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFFFFFF0F) | (val << 4)

    def _getTotalSize( self ):
        val = int(self.m_choice_totalSize.GetString(self.m_choice_totalSize.GetSelection()))
        val = int(math.log(val, 2))
        if val >= 9:
            val -= 9
        elif val >= 5:
            val += 7
        else:
            pass
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFFFFF0FF) | (val << 8)

    def _getSpiIndex( self ):
        val = int(self.m_choice_spiIndex.GetString(self.m_choice_spiIndex.GetSelection()))
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFF0FFFFF) | (val << 20)

    def _getSpiPcs( self ):
        val = int(self.m_choice_spiPcs.GetString(self.m_choice_spiPcs.GetSelection()))
        self.lpspiNorOpt0 = (self.lpspiNorOpt0 & 0xFFF0FFFF) | (val << 16)

    def _getSpiSpeed( self ):
        txt = self.m_choice_spiSpeed.GetString(self.m_choice_spiSpeed.GetSelection())
        if txt == '20MHz':
            val = 0x0
        elif txt == '10MHz':
            val = 0x1
        elif txt == '5MHz':
            val = 0x2
        elif txt == '2MHz':
            val = 0x3
        else:
            pass
        self.lpspiNorOpt1 = (self.lpspiNorOpt1 & 0xFFFFFFF0) | (val << 0)

    def callbackOk(self, event):
        self._getDeviceType()
        self._getPageSize()
        self._getSectorSize()
        self._getTotalSize()
        self._getSpiIndex()
        self._getSpiPcs()
        self._getSpiSpeed()
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_LpspiNor, self.lpspiNorOpt0, self.lpspiNorOpt1)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], uidef.kSoundEffectFilename_Progress)

    def callbackCancel(self, event):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)
