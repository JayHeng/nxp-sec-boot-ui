#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_BootCfg1

class secBootUiEfuseBootCfg1(RT10yy_efuseWin_BootCfg1.efuseWin_BootCfg1):

    def __init__(self, parent):
        RT10yy_efuseWin_BootCfg1.efuseWin_BootCfg1.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x460_bootcfg1_bit6'].keys():
            self.m_staticText_bit6.SetLabel(key)
            self.m_choice_bit6.Clear()
            self.m_choice_bit6.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit6'][key])
            self.m_choice_bit6.SetSelection(0)
        for key in efuseDescDiffDict['0x460_bootcfg1_bit13_12'].keys():
            self.m_staticText_bit13_12.SetLabel(key)
            self.m_choice_bit13_12.Clear()
            self.m_choice_bit13_12.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit13_12'][key])
            self.m_choice_bit13_12.SetSelection(0)
        for key in efuseDescDiffDict['0x460_bootcfg1_bit15_14'].keys():
            self.m_staticText_bit15_14.SetLabel(key)
            self.m_choice_bit15_14.Clear()
            self.m_choice_bit15_14.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit15_14'][key])
            self.m_choice_bit15_14.SetSelection(0)
        for key in efuseDescDiffDict['0x460_bootcfg1_bit24'].keys():
            self.m_staticText_bit24.SetLabel(key)
            self.m_choice_bit24.Clear()
            self.m_choice_bit24.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit24'][key])
            self.m_choice_bit24.SetSelection(0)
        for key in efuseDescDiffDict['0x460_bootcfg1_bit29'].keys():
            self.m_staticText_bit29.SetLabel(key)
            self.m_choice_bit29.Clear()
            self.m_choice_bit29.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit29'][key])
            self.m_choice_bit29.SetSelection(0)
        for key in efuseDescDiffDict['0x460_bootcfg1_bit31_30'].keys():
            self.m_staticText_bit31_30.SetLabel(key)
            self.m_choice_bit31_30.Clear()
            self.m_choice_bit31_30.SetItems(efuseDescDiffDict['0x460_bootcfg1_bit31_30'][key])
            self.m_choice_bit31_30.SetSelection(0)
        self._recoverLastSettings()

    def _convertLongIntHexText( self, hexText ):
        lastStr = hexText[len(hexText) - 1]
        if lastStr == 'l' or lastStr == 'L':
            return hexText[0:len(hexText) - 1]
        else:
            return hexText

    def _recoverLastSettings ( self ):
        self.m_choice_bit0.Enable( False )
        self.m_choice_bit1.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000002) >> 1)
        self.m_staticText_bit1.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit2.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000004) >> 2)
        self.m_staticText_bit2.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit3.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000008) >> 3)
        self.m_staticText_bit3.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit4.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000010) >> 4)
        self.m_staticText_bit4.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit5.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000020) >> 5)
        self.m_staticText_bit5.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.m_choice_bit6.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00000040) >> 6)
            self.m_staticText_bit6.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit6.Enable( False )
        self.m_choice_bit7.Enable( False )

        self.m_textCtrl_bit11_8.Clear()
        self.m_textCtrl_bit11_8.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x460_bootCfg1'] & 0x00000f00) >> 8))))
        self.m_staticText_bit11_8.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit13_12.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00003000) >> 12)
        self.m_staticText_bit13_12.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit15_14.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x0000c000) >> 14)
        self.m_staticText_bit15_14.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)

        self.m_choice_bit16.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00010000) >> 16)
        self.m_staticText_bit16.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit17.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00020000) >> 17)
        self.m_staticText_bit17.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit18.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00040000) >> 18)
        self.m_staticText_bit18.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit19.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00080000) >> 19)
        self.m_staticText_bit19.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit20.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00100000) >> 20)
        self.m_staticText_bit20.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit21.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00200000) >> 21)
        self.m_staticText_bit21.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit23_22.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x00c00000) >> 22)
        self.m_staticText_bit23_22.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)

        bit24Str = self.m_choice_bit24.GetString(self.m_choice_bit24.GetSelection())
        if bit24Str[0] != 'x':
            self.m_choice_bit24.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x01000000) >> 24)
            self.m_staticText_bit24.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit24.Enable( False )
        self.m_choice_bit25.Enable( False )
        self.m_choice_bit26.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x04000000) >> 26)
        self.m_staticText_bit26.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit27.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x08000000) >> 27)
        self.m_staticText_bit27.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit28.Enable( False )
        bit29Str = self.m_choice_bit29.GetString(self.m_choice_bit29.GetSelection())
        if bit29Str[0] != 'x':
            self.m_choice_bit29.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0x20000000) >> 29)
            self.m_staticText_bit29.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit29.Enable( False )
        bit31_30Str = self.m_choice_bit31_30.GetString(self.m_choice_bit31_30.GetSelection())
        if bit31_30Str[0] != 'x':
            self.m_choice_bit31_30.SetSelection((self.efuseDict['0x460_bootCfg1'] & 0xc0000000) >> 30)
            self.m_staticText_bit31_30.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit31_30.Enable( False )

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _getEfuseWord( self ):
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffffffd) | (self.m_choice_bit1.GetSelection() << 1)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffffffb) | (self.m_choice_bit2.GetSelection() << 2)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffffff7) | (self.m_choice_bit3.GetSelection() << 3)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffffffef) | (self.m_choice_bit4.GetSelection() << 4)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffffffdf) | (self.m_choice_bit5.GetSelection() << 5)
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)

        sdramConfigOptionsStr = self.m_textCtrl_bit11_8.GetLineText(0)
        sdramConfigOptions = 0
        if len(sdramConfigOptionsStr) >= 3 and sdramConfigOptionsStr[0:2] == '0x':
            sdramConfigOptions = int(sdramConfigOptionsStr[2:len(sdramConfigOptionsStr)], 16)
            if sdramConfigOptions >= 0x10:
                self.popupMsgBox('Illegal input detected! The input value should be in range [0, 15]')
                return False
        else:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x2')
            return False
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffff0ff) | (sdramConfigOptions<< 8)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffffcfff) | (self.m_choice_bit13_12.GetSelection() << 12)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffff3fff) | (self.m_choice_bit15_14.GetSelection() << 14)

        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffeffff) | (self.m_choice_bit16.GetSelection() << 16)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffdffff) | (self.m_choice_bit17.GetSelection() << 17)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfffbffff) | (self.m_choice_bit18.GetSelection() << 18)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfff7ffff) | (self.m_choice_bit19.GetSelection() << 19)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffefffff) | (self.m_choice_bit20.GetSelection() << 20)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xffdfffff) | (self.m_choice_bit21.GetSelection() << 21)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xff3fffff) | (self.m_choice_bit23_22.GetSelection() << 22)

        bit24Str = self.m_choice_bit24.GetString(self.m_choice_bit24.GetSelection())
        if bit24Str[0] != 'x':
            self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfeffffff) | (self.m_choice_bit24.GetSelection() << 24)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xfbffffff) | (self.m_choice_bit26.GetSelection() << 26)
        self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xf7ffffff) | (self.m_choice_bit27.GetSelection() << 27)
        bit29Str = self.m_choice_bit29.GetString(self.m_choice_bit29.GetSelection())
        if bit29Str[0] != 'x':
            self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0xdfffffff) | (self.m_choice_bit29.GetSelection() << 29)
        bit31_30Str = self.m_choice_bit31_30.GetString(self.m_choice_bit31_30.GetSelection())
        if bit31_30Str[0] != 'x':
            self.efuseDict['0x460_bootCfg1'] = (self.efuseDict['0x460_bootCfg1'] & 0x3fffffff) | (self.m_choice_bit31_30.GetSelection() << 30)
        return True

    def callbackOk( self, event ):
        if not self._getEfuseWord():
            return
        uivar.setEfuseSettings(self.efuseDict)
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

