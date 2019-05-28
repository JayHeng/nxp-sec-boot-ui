#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import efuseWin_MiscConf0

class secBootUiEfuseMiscConf0(efuseWin_MiscConf0.efuseWin_MiscConf0):

    def __init__(self, parent):
        efuseWin_MiscConf0.efuseWin_MiscConf0.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x6d0_miscconf0_bit19_16'].keys():
            self.m_staticText_bit19_16.SetLabel(key)
            self.m_choice_bit19_16.Clear()
            self.m_choice_bit19_16.SetItems(efuseDescDiffDict['0x6d0_miscconf0_bit19_16'][key])
            self.m_choice_bit19_16.SetSelection(0)
        self._recoverLastSettings()

    def _convertLongIntHexText( self, hexText ):
        lastStr = hexText[len(hexText) - 1]
        if lastStr == 'l' or lastStr == 'L':
            return hexText[0:len(hexText) - 1]
        else:
            return hexText

    def _recoverLastSettings ( self ):
        self.m_textCtrl_bit5_0.Clear()
        self.m_textCtrl_bit5_0.write(self._convertLongIntHexText(str(hex(self.efuseDict['0x6d0_miscConf0'] & 0x0000003f))))
        self.m_staticText_bit5_0.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit6.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000040) >> 6)
        self.m_staticText_bit6.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit7.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000080) >> 7)
        self.m_staticText_bit7.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)

        self.m_choice_bit11_8.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x00000f00) >> 8)
        self.m_staticText_bit11_8.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit12.Enable( False )
        self.m_choice_bit15_13.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x0000e000) >> 13)
        self.m_staticText_bit15_13.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)

        self.m_choice_bit19_16.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x000f0000) >> 16)
        self.m_staticText_bit19_16.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit21_20.Enable( False )
        self.m_choice_bit23_22.Enable( False )

        self.m_choice_bit24.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x01000000) >> 24)
        self.m_staticText_bit24.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit26_25.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x06000000) >> 25)
        self.m_staticText_bit26_25.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit27.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x08000000) >> 27)
        self.m_staticText_bit27.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit29_28.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0x30000000) >> 28)
        self.m_staticText_bit29_28.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit31_30.SetSelection((self.efuseDict['0x6d0_miscConf0'] & 0xc0000000) >> 30)
        self.m_staticText_bit31_30.SetBackgroundColour(uidef_efuse.kEfuseFieldColor_Valid)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _getEfuseWord( self ):
        padSettingStr = self.m_textCtrl_bit5_0.GetLineText(0)
        padSetting = 0
        if len(padSettingStr) >= 3 and padSettingStr[0:2] == '0x':
            padSetting = int(padSettingStr[2:len(padSettingStr)], 16)
            if padSetting >= 0x40:
                self.popupMsgBox('Illegal input detected! The input value should be in range [0, 63]')
                return False
        else:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x20')
            return False
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffffc0) | padSetting
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfffff0ff) | (self.m_choice_bit11_8.GetSelection() << 8)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xffff1fff) | (self.m_choice_bit15_13.GetSelection() << 13)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfff0ffff) | (self.m_choice_bit19_16.GetSelection() << 16)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xfeffffff) | (self.m_choice_bit24.GetSelection() << 24)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xf9ffffff) | (self.m_choice_bit26_25.GetSelection() << 25)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xf7ffffff) | (self.m_choice_bit27.GetSelection() << 27)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0xcfffffff) | (self.m_choice_bit29_28.GetSelection() << 28)
        self.efuseDict['0x6d0_miscConf0'] = (self.efuseDict['0x6d0_miscConf0'] & 0x3fffffff) | (self.m_choice_bit31_30.GetSelection() << 30)
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

