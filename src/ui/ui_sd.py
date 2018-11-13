#! /usr/bin/env python
import wx
import sys
import os
import uivar
import uidef
sys.path.append(os.path.abspath("../.."))
from gui import bootDeviceWin_SD

class secBootUiUsdhcSd(bootDeviceWin_SD.bootDeviceWin_SD):
    def __init__(self, parent):
        bootDeviceWin_SD.bootDeviceWin_SD.__init__(self, parent)
        usdhcSDOpt = uivar.getVar(uidef.kBootDevice_UsdhcSd)
        self.usdhcSDOpt = usdhcSDOpt

    def _getBusWidth( self ):
        val = int(self.m_textCtrl_BUS_WIDTH.GetLineText(0))
        if val > 16:
            wx.MessageBox('Width Error', 'Confirm', wx.OK)
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFF0FF) | (val << 8)

    def _getTimingMode( self ):
        txt = self.m_choice_TIMING.GetString(self.m_choice_TIMING.GetSelection())
        if txt == 'Normal/SDR12':
            val = 0x1
        elif txt == 'High/SDR25':
            val = 0x2
        elif txt == 'SDR50':
            val = 0x3
        elif txt == 'SDR104':
            val = 0x3
        else:
            pass
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrUpTime( self ):
        txt = self.m_choice_PWR_UP.GetString(self.m_choice_PWR_UP.GetSelection())
        if txt == '5ms':
            val = 0x1
        elif txt == '2.5ms':
            val = 0x2
        else:
            pass
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrCycle( self ):
        txt = self.m_choice_PWR_CYCLE.GetString(self.m_choice_PWR_CYCLE.GetSelection())
        if txt == 'disable for non-UHSI timing':
            val = 0x1
        elif txt == 'enable for non-UHSI timing':
            val = 0x2
        else:
            pass
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrDownTime( self ):
        txt = self.m_choice_Query_PWR_DOWN.GetString(self.m_choice_Query_PWR_DOWN.GetSelection())
        if txt == '20ms':
            val = 0x1
        elif txt == '10ms':
            val = 0x2
        elif txt == '5ms':
            val = 0x3
        elif txt == '2.5ms':
            val = 0x4
        else:
            pass
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrPolarity( self ):
        txt = self.m_choice_PWR_POLARITY.GetString(self.m_choice_PWR_POLARITY.GetSelection())
        if txt == 'Power down when uSDHC.RST set low':
            val = 0x1
        elif txt == 'Power down when uSDHC.RST set high':
            val = 0x2
        else:
            pass
        self.usdhcSDOpt = (self.usdhcSDOpt & 0xFFFFFCFF) | (val << 8)

    def cancel_of_SD(self, event):
        uivar.global_count[5] = 0
        self.Show(False)

    def apply_of_SD(self, event):
        self._getBusWidth()
        self._getTimingMode()
        self._getPwrUpTime()
        self._getPwrCycle()
        self._getPwrDownTime()
        self._getPwrPolarity()
        uivar.global_count[5] = 1
        uivar.setVar(uidef.kBootDevice_UsdhcSd, self.usdhcSDOpt)
        self.Show(False)

    def OnClose_SD(self, event):
        ret = wx.MessageBox('Do you really want to leave Sd?', 'Confirm', wx.OK | wx.CANCEL)
        uivar.global_count[5] = 1
        if ret == wx.OK:
            self.Show(False)