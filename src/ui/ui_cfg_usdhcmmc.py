#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import RT10yy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_UsdhcMmc
from utils import sound

class secBootUiUsdhcMmc(bootDeviceWin_UsdhcMmc.bootDeviceWin_UsdhcMmc):
    def __init__(self, parent):
        bootDeviceWin_UsdhcMmc.bootDeviceWin_UsdhcMmc.__init__(self, parent)
        self._setLanguage()
        usdhcMmcOpt0, usdhcMmcOpt1 = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_UsdhcMmc)
        self.usdhcMmcOpt0 = usdhcMmcOpt0
        self.usdhcMmcOpt1 = usdhcMmcOpt1
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_mmcOpt0.SetPageText(0, uilang.kSubLanguageContentDict['panel_mmcOpt0'][langIndex])
        self.m_staticText_busWidth.SetLabel(uilang.kSubLanguageContentDict['sText_busWidth'][langIndex])
        self.m_staticText_timingInterface.SetLabel(uilang.kSubLanguageContentDict['sText_timingInterface'][langIndex])
        self.m_staticText_partitionAccess.SetLabel(uilang.kSubLanguageContentDict['sText_partitionAccess'][langIndex])
        self.m_staticText_enableBootConfig.SetLabel(uilang.kSubLanguageContentDict['sText_enableBootConfig'][langIndex])
        self.m_staticText_bootBusWidth.SetLabel(uilang.kSubLanguageContentDict['sText_bootBusWidth'][langIndex])
        self.m_staticText_bootMode.SetLabel(uilang.kSubLanguageContentDict['sText_bootMode'][langIndex])
        self.m_staticText_enableBootPartition.SetLabel(uilang.kSubLanguageContentDict['sText_enableBootPartition'][langIndex])
        self.m_staticText_enableBootAck.SetLabel(uilang.kSubLanguageContentDict['sText_enableBootAck'][langIndex])
        self.m_staticText_resetBootBusConditions.SetLabel(uilang.kSubLanguageContentDict['sText_resetBootBusConditions'][langIndex])
        self.m_notebook_mmcOpt1.SetPageText(0, uilang.kSubLanguageContentDict['panel_mmcOpt1'][langIndex])
        self.m_staticText_enable1V8.SetLabel(uilang.kSubLanguageContentDict['sText_enable1V8'][langIndex])
        self.m_staticText_enablePowerCycle.SetLabel(uilang.kSubLanguageContentDict['sText_enablePowerCycle'][langIndex])
        self.m_staticText_powerPolarity.SetLabel(uilang.kSubLanguageContentDict['sText_powerPolarity'][langIndex])
        self.m_staticText_powerUpTime.SetLabel(uilang.kSubLanguageContentDict['sText_powerUpTime'][langIndex])
        self.m_staticText_powerDownTime.SetLabel(uilang.kSubLanguageContentDict['sText_powerDownTime'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_usdhcmmc_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_usdhcmmc_cancel'][langIndex])

    def _updateBootCfgField ( self, isEnabled ):
        if isEnabled:
            self.m_choice_bootBusWidth.Enable( True )
            self.m_choice_bootMode.Enable( True )
            self.m_choice_enableBootPartition.Enable( True )
            self.m_choice_enableBootAck.Enable( True )
            self.m_choice_resetBootBusConditions.Enable( True )
        else:
            self.m_choice_bootBusWidth.Enable( False )
            self.m_choice_bootMode.Enable( False )
            self.m_choice_enableBootPartition.Enable( False )
            self.m_choice_enableBootAck.Enable( False )
            self.m_choice_resetBootBusConditions.Enable( False )

    def _recoverLastSettings ( self ):
        busWidth = (self.usdhcMmcOpt0 & 0x00000100) >> 8
        if busWidth <= 2:
            self.m_choice_busWidth.SetSelection(busWidth)
        elif busWidth >= 5:
            self.m_choice_busWidth.SetSelection(busWidth - 2)
        else:
            pass

        timingInterface = (self.usdhcMmcOpt0 & 0x00007000) >> 12
        self.m_choice_timingInterface.SetSelection(timingInterface)

        partitionAccess = (self.usdhcMmcOpt0 & 0x07000000) >> 24
        self.m_choice_partitionAccess.SetSelection(partitionAccess)

        enableBootConfig = self.usdhcMmcOpt0 & 0x00000001
        self.m_choice_enableBootConfig.SetSelection(enableBootConfig)
        if enableBootConfig == 0:
            self._updateBootCfgField(False)
        else:
            self._updateBootCfgField(True)

            bootBusWidth = (self.usdhcMmcOpt0 & 0x00030000) >> 16
            self.m_choice_bootBusWidth.SetSelection(bootBusWidth)

            bootMode = (self.usdhcMmcOpt0 & 0x00000030) >> 4
            self.m_choice_bootMode.SetSelection(bootMode)

            enableBootPartition = (self.usdhcMmcOpt0 & 0x00700000) >> 20
            if enableBootPartition <= 2:
                self.m_choice_enableBootPartition.SetSelection(enableBootPartition)
            elif enableBootPartition >= 7:
                self.m_choice_enableBootPartition.SetSelection(enableBootPartition - 4)
            else:
                pass

            enableBootAck = (self.usdhcMmcOpt0 & 0x00000004) >> 2
            self.m_choice_enableBootAck.SetSelection(enableBootAck)

            resetBootBusConditions = (self.usdhcMmcOpt0 & 0x00000008) >> 3
            self.m_choice_resetBootBusConditions.SetSelection(resetBootBusConditions)

        enable1V8 = (self.usdhcMmcOpt1 & 0x00040000) >> 18
        self.m_choice_enable1V8.SetSelection(enable1V8)

        enablePowerCycle = (self.usdhcMmcOpt1 & 0x00080000) >> 19
        self.m_choice_enablePowerCycle.SetSelection(enablePowerCycle)

        powerPolarity = (self.usdhcMmcOpt1 & 0x00800000) >> 23
        self.m_choice_powerPolarity.SetSelection(powerPolarity)

        powerUpTime = (self.usdhcMmcOpt1 & 0x00100000) >> 20
        self.m_choice_powerUpTime.SetSelection(powerUpTime)

        powerDownTime = (self.usdhcMmcOpt1 & 0x03000000) >> 24
        self.m_choice_powerDownTime.SetSelection(powerDownTime)

    def _getBusWidth( self ):
        txt = self.m_choice_busWidth.GetString(self.m_choice_busWidth.GetSelection())
        if txt == '1bit':
            val = 0x0
        elif txt == '4bit':
            val = 0x1
        elif txt == '8bit':
            val = 0x2
        elif txt == '4bit DDR':
            val = 0x5
        elif txt == '8bit DDR':
            val = 0x6
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFFF0FF) | (val << 8)

    def _getTimingInterface( self ):
        txt = self.m_choice_timingInterface.GetString(self.m_choice_timingInterface.GetSelection())
        if txt == 'Non-HighSpeed':
            val = 0x0
        elif txt == 'HighSpeed':
            val = 0x1
        elif txt == 'HighSpeed 200':
            val = 0x2
        elif txt == 'HighSpeed 400':
            val = 0x3
        elif txt == 'HighSpeed 26MHz':
            val = 0x4
        elif txt == 'HighSpeed 52MHz':
            val = 0x5
        elif txt == 'HighSpeed DDR52':
            val = 0x6
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFF0FFF) | (val << 12)

    def _getPartitionAccess( self ):
        txt = self.m_choice_partitionAccess.GetString(self.m_choice_partitionAccess.GetSelection())
        if txt == 'User Area Normal':
            val = 0x0
        elif txt == 'Read/Write Boot1':
            val = 0x1
        elif txt == 'Read/Write Boot2':
            val = 0x2
        elif txt == 'Replay Protected Mem Block':
            val = 0x3
        elif txt == 'General Purpose1':
            val = 0x4
        elif txt == 'General Purpose2':
            val = 0x5
        elif txt == 'General Purpose3':
            val = 0x6
        elif txt == 'General Purpose4':
            val = 0x7
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xF8FFFFFF) | (val << 24)

    def _getEnableBootConfig( self ):
        txt = self.m_choice_enableBootConfig.GetString(self.m_choice_enableBootConfig.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Yes':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFFFFFE) | (val << 0)

    def _getBootBusWidth( self ):
        txt = self.m_choice_bootBusWidth.GetString(self.m_choice_bootBusWidth.GetSelection())
        if txt == '1bit-SDR, 4bit-DDR':
            val = 0x0
        elif txt == '4bit-SDR, 4bit-DDR':
            val = 0x1
        elif txt == '8bit-SDR, 8bit-DDR':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFCFFFF) | (val << 16)

    def _getBootMode( self ):
        txt = self.m_choice_bootMode.GetString(self.m_choice_bootMode.GetSelection())
        if txt == 'SDR Non-HighSpeed':
            val = 0x0
        elif txt == 'SDR HighSpeed':
            val = 0x1
        elif txt == 'DDR':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFFFFCF) | (val << 4)

    def _getEnableBootPartition( self ):
        txt = self.m_choice_enableBootPartition.GetString(self.m_choice_enableBootPartition.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Boot1':
            val = 0x1
        elif txt == 'Boot2':
            val = 0x2
        elif txt == 'User Area':
            val = 0x7
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFF8FFFFF) | (val << 20)

    def _getEnableBootAck( self ):
        txt = self.m_choice_enableBootAck.GetString(self.m_choice_enableBootAck.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Yes':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFFFFFB) | (val << 2)

    def _getResetBootBusConditions( self ):
        txt = self.m_choice_resetBootBusConditions.GetString(self.m_choice_resetBootBusConditions.GetSelection())
        if txt == 'Reset to 1bit-SDR':
            val = 0x0
        elif txt == 'Retain Boot Bus Width':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt0 = (self.usdhcMmcOpt0 & 0xFFFFFFF7) | (val << 3)

    def _getEnable1V8( self ):
        txt = self.m_choice_enable1V8.GetString(self.m_choice_enable1V8.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Yes':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt1 = (self.usdhcMmcOpt1 & 0xFFFBFFFF) | (val << 18)

    def _getEnablePowerCycle( self ):
        txt = self.m_choice_enablePowerCycle.GetString(self.m_choice_enablePowerCycle.GetSelection())
        if txt == 'No':
            val = 0x0
        elif txt == 'Yes':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt1 = (self.usdhcMmcOpt1 & 0xFFF7FFFF) | (val << 19)

    def _getPowerPolarity( self ):
        txt = self.m_choice_powerPolarity.GetString(self.m_choice_powerPolarity.GetSelection())
        if txt == 'RST Low-Disable':
            val = 0x0
        elif txt == 'RST High-Disable':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt1 = (self.usdhcMmcOpt1 & 0xFF7FFFFF) | (val << 23)

    def _getPowerUpTime( self ):
        txt = self.m_choice_powerUpTime.GetString(self.m_choice_powerUpTime.GetSelection())
        if txt == '5ms':
            val = 0x0
        elif txt == '2.5ms':
            val = 0x1
        else:
            pass
        self.usdhcMmcOpt1 = (self.usdhcMmcOpt1 & 0xFFEFFFFF) | (val << 20)

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
        self.usdhcMmcOpt1 = (self.usdhcMmcOpt1 & 0xFCFFFFFF) | (val << 24)

    def callbackEnableBootConfig( self, event ):
        txt = self.m_choice_enableBootConfig.GetString(self.m_choice_enableBootConfig.GetSelection())
        if txt == 'No':
            self._updateBootCfgField(False)
        elif txt == 'Yes':
            self._updateBootCfgField(True)
        else:
            pass

    def callbackOk( self, event ):
        self._getBusWidth()
        self._getTimingInterface()
        self._getPartitionAccess()
        self._getEnableBootConfig()
        enableBootConfig = self.usdhcMmcOpt0 & 0x00000001
        if enableBootConfig:
            self._getBootBusWidth()
            self._getBootMode()
            self._getEnableBootPartition()
            self._getEnableBootAck()
            self._getResetBootBusConditions()
        self._getEnable1V8()
        self._getEnablePowerCycle()
        self._getPowerPolarity()
        self._getPowerUpTime()
        self._getPowerDownTime()
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_UsdhcMmc, self.usdhcMmcOpt0, self.usdhcMmcOpt1)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], uidef.kSoundEffectFilename_Progress)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)