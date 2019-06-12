#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_BootCfg0_FlexspiNor_10bits

class secBootUiEfuseBootCfg0FlexspiNor10bits(RT10yy_efuseWin_BootCfg0_FlexspiNor_10bits.efuseWin_BootCfg0_FlexspiNor_10bits):

    def __init__(self, parent):
        RT10yy_efuseWin_BootCfg0_FlexspiNor_10bits.efuseWin_BootCfg0_FlexspiNor_10bits.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x450_bootcfg0_bit7_4'].keys():
            self.m_staticText_bit7_4.SetLabel(key)
            self.m_choice_bit7_4.Clear()
            self.m_choice_bit7_4.SetItems(efuseDescDiffDict['0x450_bootcfg0_bit7_4'][key])
            self.m_choice_bit7_4.SetSelection(0)
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        self.m_choice_bit0.SetSelection(self.efuseDict['0x450_bootCfg0'] & 0x00000001)
        self.m_staticText_bit0.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit3_1.SetSelection((self.efuseDict['0x450_bootCfg0'] & 0x0000000e) >> 1)
        self.m_staticText_bit3_1.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit7_4.SetSelection((self.efuseDict['0x450_bootCfg0'] & 0x000000f0) >> 4)
        self.m_staticText_bit7_4.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit9_8.SetSelection((self.efuseDict['0x450_bootCfg0'] & 0x00000300) >> 8)
        self.m_staticText_bit9_8.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit10.Enable( False )
        self.m_choice_bit11.Enable( False )
        self.m_choice_bit12.Enable( False )
        self.m_choice_bit13.Enable( False )
        self.m_choice_bit14.Enable( False )
        self.m_choice_bit15.Enable( False )
        self.m_choice_bit16.Enable( False )
        self.m_choice_bit17.Enable( False )
        self.m_choice_bit18.Enable( False )
        self.m_choice_bit19.Enable( False )
        self.m_choice_bit20.Enable( False )
        self.m_choice_bit21.Enable( False )
        self.m_choice_bit22.Enable( False )
        self.m_choice_bit23.Enable( False )
        self.m_choice_bit24.Enable( False )
        self.m_choice_bit25.Enable( False )
        self.m_choice_bit26.Enable( False )
        self.m_choice_bit27.Enable( False )
        self.m_choice_bit28.Enable( False )
        self.m_choice_bit29.Enable( False )
        self.m_choice_bit30.Enable( False )
        self.m_choice_bit31.Enable( False )

    def _getEfuseWord( self ):
        self.efuseDict['0x450_bootCfg0'] = (self.efuseDict['0x450_bootCfg0'] & 0xfffffffe) | self.m_choice_bit0.GetSelection()
        self.efuseDict['0x450_bootCfg0'] = (self.efuseDict['0x450_bootCfg0'] & 0xfffffff1) | (self.m_choice_bit3_1.GetSelection() << 1)
        self.efuseDict['0x450_bootCfg0'] = (self.efuseDict['0x450_bootCfg0'] & 0xffffff0f) | (self.m_choice_bit7_4.GetSelection() << 4)
        self.efuseDict['0x450_bootCfg0'] = (self.efuseDict['0x450_bootCfg0'] & 0xfffffcff) | (self.m_choice_bit9_8.GetSelection() << 8)

    def callbackOk( self, event ):
        self._getEfuseWord()
        uivar.setEfuseSettings(self.efuseDict)
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

