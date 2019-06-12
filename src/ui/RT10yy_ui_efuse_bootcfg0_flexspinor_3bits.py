#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_BootCfg0_FlexspiNor_3bits

class secBootUiEfuseBootCfg0FlexspiNor3bits(RT10yy_efuseWin_BootCfg0_FlexspiNor_3bits.efuseWin_BootCfg0_FlexspiNor_3bits):

    def __init__(self, parent):
        RT10yy_efuseWin_BootCfg0_FlexspiNor_3bits.efuseWin_BootCfg0_FlexspiNor_3bits.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        self.m_choice_bit0.SetSelection(self.efuseDict['0x450_bootCfg0'] & 0x00000001)
        self.m_staticText_bit0.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit2_1.SetSelection((self.efuseDict['0x450_bootCfg0'] & 0x00000006) >> 1)
        self.m_staticText_bit2_1.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit3.Enable( False )
        self.m_choice_bit4.Enable( False )
        self.m_choice_bit5.Enable( False )
        self.m_choice_bit6.Enable( False )
        self.m_choice_bit7.Enable( False )
        self.m_choice_bit8.Enable( False )
        self.m_choice_bit9.Enable( False )
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
        self.efuseDict['0x450_bootCfg0'] = (self.efuseDict['0x450_bootCfg0'] & 0xfffffff9) | (self.m_choice_bit3_1.GetSelection() << 1)

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

