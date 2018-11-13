#! /usr/bin/env python
import wx
import sys
import os
import uivar
import uidef
sys.path.append(os.path.abspath("../.."))
from gui import bootDeviceWin_SemcNor

class secBootUiSemcNor(bootDeviceWin_SemcNor.bootDeviceWin_SemcNor):
    def __init__(self, parent):
        bootDeviceWin_SemcNor.bootDeviceWin_SemcNor.__init__(self, parent)
        semcNorOpt, semcNorSetting = uivar.getVar(uidef.kBootDevice_SemcNor)
        self.semcNorOpt = semcNorOpt
        self.semcNorSetting = semcNorSetting

    def _getPCSPort( self ):
        txt = self.m_choice_PCS_Port.GetString(self.m_choice_PCS_Port.GetSelection())
        if txt == 'CSX0':
            val = 0x1
        elif txt == 'CSX1':
            val = 0x2
        elif txt == 'CSX2':
            val = 0x3
        elif txt == 'CSX3':
            val = 0x4
        elif txt == 'A8':
            val = 0x5
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)


    def _getADVPolarity( self ):
        txt = self.m_choice_ADV_Polarity.GetString(self.m_choice_ADV_Polarity.GetSelection())
        if txt == 'Low active':
            val = 0x1
        elif txt == 'High active':
            val = 0x2
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)


    def _getDataPortSize( self ):
        txt = self.m_choice_DataPort_Size.GetString(self.m_choice_DataPort_Size.GetSelection())
        if txt == '8bits':
            val = 0x1
        elif txt == '8bits':
            val = 0x2
        elif txt == '16bits':
            val = 0x3
        elif txt == '24bits':
            val = 0x4
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)



    def _getTimingMode( self ):
        txt = self.m_choice_Timing_Mode.GetString(self.m_choice_Timing_Mode.GetSelection())
        if txt == 'Safe mode':
            val = 0x1
        elif txt == 'Fast mode':
            val = 0x2
        elif txt == 'User defined(Field 0x04-0x19)':
            val = 0x3
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)

    def _getCommandSet( self ):
        txt = self.m_choice_Command_Set.GetString(self.m_choice_Command_Set.GetSelection())
        if txt == 'EPSCD-As Micron MT28EW':
            val = 0x1
        elif txt == 'SFMCD-As Micron MT28GU':
            val = 0x2
        else:
            pass
        self.semcNorOpt = (self.semcNorOpt & 0xFFFFFCFF) | (val << 8)

    def cancel_of_SEMC_NOR(self, event):
        uivar.global_count[3] = 0
        self.Show(False)

    def apply_of_SEMC_NOR(self, event):
        self._getPCSPort()
        self._getADVPolarity()
        self._getDataPortSize()
        self._getTimingMode()
        self._getCommandSet()
        uivar.setVar(uidef.kBootDevice_SemcNor, self.semcNorOpt, self.semcNorSetting)
        uivar.global_count[3] = 1
        self.Show(False)

    def OnClose_SEMC_NOR(self, event):
        ret = wx.MessageBox('Do you really want to leave?', 'Confirm', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            uivar.global_count[3] = 1
            self.Show(False)