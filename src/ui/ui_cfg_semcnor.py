#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_SemcNor
from utils import sound

class secBootUiSemcNor(bootDeviceWin_SemcNor.bootDeviceWin_SemcNor):
    def __init__(self, parent):
        bootDeviceWin_SemcNor.bootDeviceWin_SemcNor.__init__(self, parent)
        semcNorOpt, semcNorSetting, semcNorDeviceModel = uivar.getBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_SemcNor)
        self.semcNorOpt = semcNorOpt
        self.semcNorSetting = semcNorSetting
        self.semcNorDeviceModel = semcNorDeviceModel
        self._recoverSemcNorLastSettings()

    def _getTimingMode( self ):
        txt = self.m_choice_CFITimingMode.GetString(self.m_choice_CFITimingMode.GetSelection())
        if txt == 'Safe mode':
            val = 0x0
        elif txt == 'Fast mode':
            val = 0x1
        elif txt == 'User defined':
            val = 0x2
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFFF3) | (val << 2)

    def _getADVPolarity( self ):
        txt = self.m_choice_AdvPolarity.GetString(self.m_choice_AdvPolarity.GetSelection())
        if txt == 'Low active':
            val = 0x0
        elif txt == 'High active':
            val = 0x1
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFBFF) | (val << 10)

    def _getDataPortSize( self ):
        txt = self.m_choice_ioPortSize.GetString(self.m_choice_ioPortSize.GetSelection())
        if txt == 'x8 bits':
            val = 0x0
        elif txt == 'x8 bits':
            val = 0x1
        elif txt == 'x16 bits':
            val = 0x2
        elif txt == 'x24 bits':
            val = 0x3
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)

    def _getPCSPort( self ):
        txt = self.m_choice_PcsPort.GetString(self.m_choice_PcsPort.GetSelection())
        if txt == 'CSX0':
            val = 0x0
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFF8FFF) | (val << 12)

    def _getCommandSet( self ):
        txt = self.m_choice_CommandSet.GetString(self.m_choice_CommandSet.GetSelection())
        if txt == 'MT28EW':
            val = 0x0
        elif txt == 'MT28GU':
            val = 0x1
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFFFC) | (val << 0)

    def _recoverSemcNorLastSettings ( self ):
        self.m_choice_deviceMode_SEMCNOR.SetSelection(self.m_choice_deviceMode_SEMCNOR.FindString(self.semcNorDeviceModel))

        TimingMode = (self.semcNorOpt & 0x0000000C) >> 2
        self.m_choice_CFITimingMode.SetSelection(TimingMode)

        ADVPolarity = (self.semcNorOpt & 0x00000400) >> 10
        self.m_choice_AdvPolarity.SetSelection(ADVPolarity)

        DataPortSize = (self.semcNorOpt & 0x00000300) >> 8
        if DataPortSize == 0:
            DataPortSize = 1
        self.m_choice_ioPortSize.SetSelection(DataPortSize-1)
        print(DataPortSize)

        PCSPort = (self.semcNorOpt & 0x00007000) >> 12
        self.m_choice_PcsPort.SetSelection(PCSPort)

        CommandSet = (self.semcNorOpt & 0x00000003) >> 0
        self.m_choice_CommandSet.SetSelection(CommandSet)



    def callbackUseTypicalDeviceModel_SEMCNOR( self, event ):
        txt = self.m_choice_deviceMode_SEMCNOR.GetString(self.m_choice_deviceMode_SEMCNOR.GetSelection())
        self.semcNorDeviceModel = txt
        if txt == uidef.kSemcNorDevice_Micron_MT28EW128ABA:
            self.semcNorOpt = uidef.kSemcNorOpt0_Micron_MT28EW128ABA
        elif txt == uidef.kSemcNorDevice_Micron_MT28UG128ABA:
            self.semcNorOpt = uidef.kSemcNorOpt0_Micron_MT28UG128ABA
        else:
            pass
        if txt != 'No':
            self._recoverSemcNorLastSettings()


    def callbackOk( self, event ):
        self._getTimingMode()
        self._getADVPolarity()
        self._getDataPortSize()
        self._getPCSPort()
        self._getCommandSet()
        uivar.setBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_SemcNor, self.semcNorOpt, self.semcNorSetting, self.semcNorDeviceModel)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        print( hex(self.semcNorOpt),self.semcNorSetting,self.semcNorDeviceModel)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

