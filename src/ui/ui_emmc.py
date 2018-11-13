#! /usr/bin/env python
import wx
import sys
import os
import uivar
import uidef
sys.path.append(os.path.abspath("../.."))
from gui import bootDeviceWin_EMMC

class secBootUiUsdhcMmc(bootDeviceWin_EMMC.bootDeviceWin_EMMC):
    def __init__(self, parent):
        bootDeviceWin_EMMC.bootDeviceWin_EMMC.__init__(self, parent)
        usdhcMmcOpt = uivar.getVar(uidef.kBootDevice_UsdhcMmc)
        self.usdhcMmcOpt = usdhcMmcOpt

    def _getBootConfig( self ):
        txt = self.m_choice_BOOT_CONFIG.GetString(self.m_choice_BOOT_CONFIG.GetSelection())
        if txt == 'Ignored':
            val = 0x1
        elif txt == 'Be Written into device':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)


    def _getBootAck( self ):
        txt = self.m_choice_BOOT_ACK.GetString(self.m_choice_BOOT_ACK.GetSelection())
        if txt == 'NO ACK':
            val = 0x1
        elif txt == 'ACK':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getBootBus( self ):
        txt = self.m_choice_Boot_BusCondition.GetString(self.m_choice_Boot_BusCondition.GetSelection())
        if txt == 'Reset to x1,SDR,Normal':
            val = 0x1
        elif txt == 'Retain boot config':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getBootMode( self ):
        txt = self.m_choice_BOOT_MODE.GetString(self.m_choice_BOOT_MODE.GetSelection())
        if txt == 'Normal':
            val = 0x1
        elif txt == 'HS':
            val = 0x2
        elif txt == 'DDR':
            val = 0x3
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getPartitionAccess( self ):
        txt = self.m_choice_PARTITION_ACCESS.GetString(self.m_choice_PARTITION_ACCESS.GetSelection())
        if txt == 'User data area':
            val = 0x1
        elif txt == 'Boot partition 1':
            val = 0x2
        elif txt == 'Boot partition 2':
            val = 0x3
        elif txt == 'RPMB':
            val = 0x4
        elif txt == 'General Purpose parition 1':
            val = 0x5
        elif txt == 'General Purpose parition 2':
            val = 0x6
        elif txt == 'General Purpose parition 3':
            val = 0x7
        elif txt == 'General Purpose parition 4':
            val = 0x8
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getBusWidth( self ):
        txt = self.m_choice_BUS_WIDTH.GetString(self.m_choice_BUS_WIDTH.GetSelection())
        if txt == 'x1 SDR':
            val = 0x1
        elif txt == 'x4 SDR':
            val = 0x2
        elif txt == 'x8 SDR':
            val = 0x3
        elif txt == 'x4 DDR':
            val = 0x4
        elif txt == 'x8 DDR':
            val = 0x5
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getBootPartition( self ):
        txt = self.m_choice_BOOT_PARTITION.GetString(self.m_choice_BOOT_PARTITION.GetSelection())
        if txt == 'Not enabled':
            val = 0x1
        elif txt == 'Boot partition 1':
            val = 0x2
        elif txt == 'Boot partition 2':
            val = 0x3
        elif txt == 'User data area':
            val = 0x4
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrUpTime( self ):
        txt = self.m_choice_PWR_UP.GetString(self.m_choice_PWR_UP.GetSelection())
        if txt == '5ms':
            val = 0x1
        elif txt == '2.5ms':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getBootBusWidth( self ):
        txt = self.m_choice_BOOT_BUS.GetString(self.m_choice_BOOT_BUS.GetSelection())
        if txt == 'x1(SDR),x4(DDR)':
            val = 0x1
        elif txt == 'x4(SDR,DDR)':
            val = 0x2
        elif txt == 'x8(SDR,DDR)':
            val = 0x3
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrDownTime( self ):
        txt = self.m_choice_PWR_DOWN.GetString(self.m_choice_PWR_DOWN.GetSelection())
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
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _get1V8( self ):
        txt = self.m_choice_1V8.GetString(self.m_choice_1V8.GetSelection())
        if txt == 'not set vselect pin':
            val = 0x1
        elif txt == 'set vselect pin high':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getTiming( self ):
        txt = self.m_choice_TIMING.GetString(self.m_choice_TIMING.GetSelection())
        if txt == 'Normal':
            val = 0x1
        elif txt == 'HS':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrCycle( self ):
        txt = self.m_choice_PWR_CYCLE.GetString(self.m_choice_PWR_CYCLE.GetSelection())
        if txt == 'disable':
            val = 0x1
        elif txt == 'enable':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def _getPwrPolarity( self ):
        txt = self.m_choice_PWR_POLARITY.GetString(self.m_choice_PWR_POLARITY.GetSelection())
        if txt == 'Power down when uSDHC.RST set low':
            val = 0x1
        elif txt == 'Power down when uSDHC.RST set high':
            val = 0x2
        else:
            pass
        self.usdhcMmcOpt = (self.usdhcMmcOpt & 0xFFFFFCFF) | (val << 8)

    def cancel_of_EMMC(self, event):
        uivar.global_count[6] = 0
        self.Show(False)

    def apply_of_EMMC(self, event):
        self._getBootConfig()
        self._getBootAck()
        self._getBootBus()
        self._getBootMode()
        self._getPartitionAccess()
        self._getBusWidth()
        self._getBootPartition()
        self._getPwrUpTime()
        self._getBootBusWidth()
        self._getPwrDownTime()
        self._get1V8()
        self._getTiming()
        self._getPwrCycle()
        self._getPwrPolarity()
        uivar.global_count[6] = 1
        self.Show(False)

    def OnClose_EMMC(self, event):
        ret = wx.MessageBox('Do you really want to leave?', 'Confirm', wx.OK | wx.CANCEL)
        uivar.global_count[6] = 1
        if ret == wx.OK:
            self.Show(False)