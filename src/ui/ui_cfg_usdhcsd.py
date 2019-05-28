#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RT10yy_uidef
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_UsdhcSd
from utils import sound

class secBootUiUsdhcSd(bootDeviceWin_UsdhcSd.bootDeviceWin_UsdhcSd):
    def __init__(self, parent):
        bootDeviceWin_UsdhcSd.bootDeviceWin_UsdhcSd.__init__(self, parent)
        self._setLanguage()
        usdhcSdOpt = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_UsdhcSd)
        self.usdhcSdOpt = usdhcSdOpt
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_sdOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_sdOpt'][langIndex])
        self.m_staticText_busWidth.SetLabel(uilang.kSubLanguageContentDict['sText_busWidth'][langIndex])
        self.m_staticText_timingInterface.SetLabel(uilang.kSubLanguageContentDict['sText_timingInterface'][langIndex])
        self.m_staticText_enablePowerCycle.SetLabel(uilang.kSubLanguageContentDict['sText_enablePowerCycle'][langIndex])
        self.m_staticText_powerPolarity.SetLabel(uilang.kSubLanguageContentDict['sText_powerPolarity'][langIndex])
        self.m_staticText_powerUpTime.SetLabel(uilang.kSubLanguageContentDict['sText_powerUpTime'][langIndex])
        self.m_staticText_powerDownTime.SetLabel(uilang.kSubLanguageContentDict['sText_powerDownTime'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_usdhcsd_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_usdhcsd_cancel'][langIndex])

    def _recoverLastSettings ( self ):
        busWidth = (self.usdhcSdOpt & 0x00000100) >> 8
        self.m_choice_busWidth.SetSelection(busWidth)

        timingInterface = (self.usdhcSdOpt & 0x00007000) >> 12
        self.m_choice_timingInterface.SetSelection(timingInterface)

        enablePowerCycle = (self.usdhcSdOpt & 0x00080000) >> 19
        self.m_choice_enablePowerCycle.SetSelection(enablePowerCycle)

        powerPolarity = (self.usdhcSdOpt & 0x00800000) >> 23
        self.m_choice_powerPolarity.SetSelection(powerPolarity)

        powerUpTime = (self.usdhcSdOpt & 0x00100000) >> 20
        self.m_choice_powerUpTime.SetSelection(powerUpTime)

        powerDownTime = (self.usdhcSdOpt & 0x03000000) >> 24
        self.m_choice_powerDownTime.SetSelection(powerDownTime)

    def _getBusWidth( self ):
        txt = self.m_choice_busWidth.GetString(self.m_choice_busWidth.GetSelection())
        if txt == '1bit':
            val = 0x0
        elif txt == '4bit':
            val = 0x1
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFFFFFEFF) | (val << 8)

    def _getTimingInterface( self ):
        txt = self.m_choice_timingInterface.GetString(self.m_choice_timingInterface.GetSelection())
        if txt == 'SDR12/Normal':
            val = 0x0
        elif txt == 'SDR25/HighSpeed':
            val = 0x1
        elif txt == 'SDR50':
            val = 0x2
        elif txt == 'SDR104':
            val = 0x3
        elif txt == 'DDR50':
            val = 0x4
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFFFF8FFF) | (val << 12)

    def _getEnablePowerCycle( self ):
        txt = self.m_choice_enablePowerCycle.GetString(self.m_choice_enablePowerCycle.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Yes':
            val = 0x1
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFFF7FFFF) | (val << 19)

    def _getPowerPolarity( self ):
        txt = self.m_choice_powerPolarity.GetString(self.m_choice_powerPolarity.GetSelection())
        if txt == 'RST Low-Disable':
            val = 0x0
        elif txt == 'RST High-Disable':
            val = 0x1
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFF7FFFFF) | (val << 23)

    def _getPowerUpTime( self ):
        txt = self.m_choice_powerUpTime.GetString(self.m_choice_powerUpTime.GetSelection())
        if txt == '5ms':
            val = 0x0
        elif txt == '2.5ms':
            val = 0x1
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFFEFFFFF) | (val << 20)

    def _getPowerDownTime( self ):
        txt = self.m_choice_powerDownTime.GetString(self.m_choice_powerDownTime.GetSelection())
        if txt == '20ms':
            val = 0x0
        elif txt == '10ms':
            val = 0x1
        elif txt == '5ms':
            val = 0x2
        elif txt == '2.5ms':
            val = 0x3
        else:
            pass
        self.usdhcSdOpt = (self.usdhcSdOpt & 0xFCFFFFFF) | (val << 24)

    def callbackOk( self, event ):
        self._getBusWidth()
        self._getTimingInterface()
        self._getEnablePowerCycle()
        self._getPowerPolarity()
        self._getPowerUpTime()
        self._getPowerDownTime()
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_UsdhcSd, self.usdhcSdOpt)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], RT10yy_uidef.kSoundEffectFilename_Progress)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

