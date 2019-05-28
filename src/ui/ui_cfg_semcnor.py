#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RT10yy_uidef
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_SemcNor

class secBootUiSemcNor(bootDeviceWin_SemcNor.bootDeviceWin_SemcNor):
    def __init__(self, parent):
        bootDeviceWin_SemcNor.bootDeviceWin_SemcNor.__init__(self, parent)
        semcNorOpt, semcNorSetting = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_SemcNor)
        self.semcNorOpt = semcNorOpt
        self.semcNorSetting = semcNorSetting

    def _getPCSPort( self ):
        txt = self.m_choice_PCS_Port.GetString(self.m_choice_PCS_Port.GetSelection())
        if txt == 'CSX0':
            val = 0x0
        elif txt == 'CSX1':
            val = 0x1
        elif txt == 'CSX2':
            val = 0x2
        elif txt == 'CSX3':
            val = 0x3
        elif txt == 'A8':
            val = 0x4
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFF8FFF) | (val << 12)


    def _getADVPolarity( self ):
        txt = self.m_choice_ADV_Polarity.GetString(self.m_choice_ADV_Polarity.GetSelection())
        if txt == 'Low active':
            val = 0x0
        elif txt == 'High active':
            val = 0x1
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFBFF) | (val << 10)


    def _getDataPortSize( self ):
        txt = self.m_choice_DataPort_Size.GetString(self.m_choice_DataPort_Size.GetSelection())
        if txt == '8bits':
            val = 0x0
        elif txt == '8bits':
            val = 0x1
        elif txt == '16bits':
            val = 0x2
        elif txt == '24bits':
            val = 0x3
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)



    def _getTimingMode( self ):
        txt = self.m_choice_Timing_Mode.GetString(self.m_choice_Timing_Mode.GetSelection())
        if txt == 'Safe mode':
            val = 0x0
        elif txt == 'Fast mode':
            val = 0x1
        elif txt == 'User defined(Field 0x04-0x19)':
            val = 0x2
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFFF3) | (val << 2)

    def _getCommandSet( self ):
        txt = self.m_choice_Command_Set.GetString(self.m_choice_Command_Set.GetSelection())
        if txt == 'EPSCD-As Micron MT28EW':
            val = 0x0
        elif txt == 'SFMCD-As Micron MT28GU':
            val = 0x1
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFFFC) | (val << 2)

    def cancel_of_SEMC_NOR(self, event):
        self.Show(False)

    def apply_of_SEMC_NOR(self, event):
        self._getPCSPort()
        self._getADVPolarity()
        self._getDataPortSize()
        self._getTimingMode()
        self._getCommandSet()
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_SemcNor, self.semcNorOpt, self.semcNorSetting)
        self.Show(False)

    def OnClose_SEMC_NOR(self, event):
        ret = wx.MessageBox('Do you really want to leave?', 'Confirm', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            self.Show(False)