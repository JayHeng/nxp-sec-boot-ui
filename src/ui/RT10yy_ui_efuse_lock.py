#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_Lock

class secBootUiEfuseLock(RT10yy_efuseWin_Lock.efuseWin_Lock):

    def __init__(self, parent):
        RT10yy_efuseWin_Lock.efuseWin_Lock.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x400_lock_bit7'].keys():
            self.m_staticText_bit7.SetLabel(key)
            self.m_choice_bit7.Clear()
            self.m_choice_bit7.SetItems(efuseDescDiffDict['0x400_lock_bit7'][key])
            self.m_choice_bit7.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit14'].keys():
            self.m_staticText_bit14.SetLabel(key)
            self.m_choice_bit14.Clear()
            self.m_choice_bit14.SetItems(efuseDescDiffDict['0x400_lock_bit14'][key])
            self.m_choice_bit14.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit15'].keys():
            self.m_staticText_bit15.SetLabel(key)
            self.m_choice_bit15.Clear()
            self.m_choice_bit15.SetItems(efuseDescDiffDict['0x400_lock_bit15'][key])
            self.m_choice_bit15.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit17'].keys():
            self.m_staticText_bit17.SetLabel(key)
            self.m_choice_bit17.Clear()
            self.m_choice_bit17.SetItems(efuseDescDiffDict['0x400_lock_bit17'][key])
            self.m_choice_bit17.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit20'].keys():
            self.m_staticText_bit20.SetLabel(key)
            self.m_choice_bit20.Clear()
            self.m_choice_bit20.SetItems(efuseDescDiffDict['0x400_lock_bit20'][key])
            self.m_choice_bit20.SetSelection(0)
        for key in efuseDescDiffDict['0x400_lock_bit25_24'].keys():
            self.m_staticText_bit25_24.SetLabel(key)
            self.m_choice_bit25_24.Clear()
            self.m_choice_bit25_24.SetItems(efuseDescDiffDict['0x400_lock_bit25_24'][key])
            self.m_choice_bit25_24.SetSelection(0)
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        self.m_choice_bit1_0.SetSelection(self.efuseDict['0x400_lock'] & 0x00000003)
        self.m_staticText_bit1_0.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit3_2.SetSelection((self.efuseDict['0x400_lock'] & 0x0000000c) >> 2)
        self.m_staticText_bit3_2.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit5_4.SetSelection((self.efuseDict['0x400_lock'] & 0x00000030) >> 4)
        self.m_staticText_bit5_4.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit6.SetSelection((self.efuseDict['0x400_lock'] & 0x00000040) >> 6)
        self.m_staticText_bit6.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit7Str = self.m_choice_bit7.GetString(self.m_choice_bit7.GetSelection())
        if bit7Str[0] != 'x':
            self.m_choice_bit7.SetSelection((self.efuseDict['0x400_lock'] & 0x00000080) >> 7)
            self.m_staticText_bit7.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit7.Enable( False )
        self.m_choice_bit9_8.SetSelection((self.efuseDict['0x400_lock'] & 0x00000300) >> 8)
        self.m_staticText_bit9_8.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit11_10.SetSelection((self.efuseDict['0x400_lock'] & 0x00000c00) >> 10)
        self.m_staticText_bit11_10.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit13_12.SetSelection((self.efuseDict['0x400_lock'] & 0x00003000) >> 12)
        self.m_staticText_bit13_12.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit14Str = self.m_choice_bit14.GetString(self.m_choice_bit14.GetSelection())
        if bit14Str[0] != 'x':
            self.m_choice_bit14.SetSelection((self.efuseDict['0x400_lock'] & 0x00004000) >> 14)
            self.m_staticText_bit14.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit14.Enable( False )
        self.m_choice_bit15.SetSelection((self.efuseDict['0x400_lock'] & 0x00008000) >> 15)
        self.m_staticText_bit15.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit16.SetSelection((self.efuseDict['0x400_lock'] & 0x00010000) >> 16)
        self.m_staticText_bit16.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit17Str = self.m_choice_bit17.GetString(self.m_choice_bit17.GetSelection())
        if bit17Str[0] != 'x':
            self.m_choice_bit17.SetSelection((self.efuseDict['0x400_lock'] & 0x00020000) >> 17)
            self.m_staticText_bit17.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit17.Enable( False )
        self.m_choice_bit19_18.SetSelection((self.efuseDict['0x400_lock'] & 0x000c0000) >> 18)
        self.m_staticText_bit19_18.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit20Str = self.m_choice_bit20.GetString(self.m_choice_bit20.GetSelection())
        if bit20Str[0] != 'x':
            self.m_choice_bit20.SetSelection((self.efuseDict['0x400_lock'] & 0x00100000) >> 20)
            self.m_staticText_bit20.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit20.Enable( False )
        self.m_choice_bit21.SetSelection((self.efuseDict['0x400_lock'] & 0x00200000) >> 21)
        self.m_staticText_bit21.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit22.SetSelection((self.efuseDict['0x400_lock'] & 0x00400000) >> 22)
        self.m_staticText_bit22.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit23.SetSelection((self.efuseDict['0x400_lock'] & 0x00800000) >> 23)
        self.m_staticText_bit23.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit25_24Str = self.m_choice_bit25_24.GetString(self.m_choice_bit25_24.GetSelection())
        if bit25_24Str[0] != 'x':
            self.m_choice_bit25_24.SetSelection((self.efuseDict['0x400_lock'] & 0x03000000) >> 24)
            self.m_staticText_bit25_24.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit25_24.Enable( False )
        self.m_choice_bit27_26.SetSelection((self.efuseDict['0x400_lock'] & 0x0c000000) >> 26)
        self.m_staticText_bit27_26.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit29_28.Enable( False )
        self.m_choice_bit30.Enable( False )
        self.m_choice_bit31.SetSelection((self.efuseDict['0x400_lock'] & 0x80000000) >> 31)
        self.m_staticText_bit31.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)

    def _getEfuseWord( self ):
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffffffc) | self.m_choice_bit1_0.GetSelection()
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffffff3) | (self.m_choice_bit3_2.GetSelection() << 2)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffffffcf) | (self.m_choice_bit5_4.GetSelection() << 4)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)
        bit7Str = self.m_choice_bit7.GetString(self.m_choice_bit7.GetSelection())
        if bit7Str[0] != 'x':
            self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffffcff) | (self.m_choice_bit9_8.GetSelection() << 8)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffff3ff) | (self.m_choice_bit11_10.GetSelection() << 10)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffffcfff) | (self.m_choice_bit13_12.GetSelection() << 12)
        bit14Str = self.m_choice_bit14.GetString(self.m_choice_bit14.GetSelection())
        if bit14Str[0] != 'x':
            self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffffbfff) | (self.m_choice_bit14.GetSelection() << 14)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffff7fff) | (self.m_choice_bit15.GetSelection() << 15)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffeffff) | (self.m_choice_bit16.GetSelection() << 16)
        bit17Str = self.m_choice_bit17.GetString(self.m_choice_bit17.GetSelection())
        if bit17Str[0] != 'x':
            self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfffdffff) | (self.m_choice_bit17.GetSelection() << 17)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfff3ffff) | (self.m_choice_bit19_18.GetSelection() << 18)
        bit20Str = self.m_choice_bit20.GetString(self.m_choice_bit20.GetSelection())
        if bit20Str[0] != 'x':
            self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffefffff) | (self.m_choice_bit20.GetSelection() << 20)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffdfffff) | (self.m_choice_bit21.GetSelection() << 21)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xffbfffff) | (self.m_choice_bit22.GetSelection() << 22)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xff7fffff) | (self.m_choice_bit23.GetSelection() << 23)
        bit25_24Str = self.m_choice_bit25_24.GetString(self.m_choice_bit25_24.GetSelection())
        if bit25_24Str[0] != 'x':
            self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xfcffffff) | (self.m_choice_bit25_24.GetSelection() << 24)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0xf3ffffff) | (self.m_choice_bit27_26.GetSelection() << 26)
        self.efuseDict['0x400_lock'] = (self.efuseDict['0x400_lock'] & 0x7fffffff) | (self.m_choice_bit31.GetSelection() << 31)

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

