#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_MiscConf1_FlexspiNor

class secBootUiEfuseMiscConf1FlexspiNor(RT10yy_efuseWin_MiscConf1_FlexspiNor.efuseWin_MiscConf1_FlexspiNor):

    def __init__(self, parent):
        RT10yy_efuseWin_MiscConf1_FlexspiNor.efuseWin_MiscConf1_FlexspiNor.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit0'].keys():
            self.m_staticText_bit0.SetLabel(key)
            self.m_choice_bit0.Clear()
            self.m_choice_bit0.SetItems(efuseDescDiffDict['0x6e0_miscconf1_bit0'][key])
            self.m_choice_bit0.SetSelection(0)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit3_1'].keys():
            self.m_staticText_bit3_1.SetLabel(key)
            self.m_choice_bit3_1.Clear()
            self.m_choice_bit3_1.SetItems(efuseDescDiffDict['0x6e0_miscconf1_bit3_1'][key])
            self.m_choice_bit3_1.SetSelection(0)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit5_4'].keys():
            self.m_staticText_bit5_4.SetLabel(key)
            self.m_choice_bit5_4.Clear()
            self.m_choice_bit5_4.SetItems(efuseDescDiffDict['0x6e0_miscconf1_bit5_4'][key])
            self.m_choice_bit5_4.SetSelection(0)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit6'].keys():
            self.m_staticText_bit6.SetLabel(key)
            self.m_choice_bit6.Clear()
            self.m_choice_bit6.SetItems(efuseDescDiffDict['0x6e0_miscconf1_bit6'][key])
            self.m_choice_bit6.SetSelection(0)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit11_8'].keys():
            self.m_staticText_bit11_8.SetLabel(key)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit15_12'].keys():
            self.m_staticText_bit15_12.SetLabel(key)
            self.m_choice_bit15_12.Clear()
            self.m_choice_bit15_12.SetItems(efuseDescDiffDict['0x6e0_miscconf1_bit15_12'][key])
            self.m_choice_bit15_12.SetSelection(0)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit23_16'].keys():
            self.m_staticText_bit23_16.SetLabel(key)
        for key in efuseDescDiffDict['0x6e0_miscconf1_bit31_24'].keys():
            self.m_staticText_bit31_24.SetLabel(key)
        self._recoverLastSettings()

    def _convertLongIntHexText( self, hexText ):
        lastStr = hexText[len(hexText) - 1]
        if lastStr == 'l' or lastStr == 'L':
            return hexText[0:len(hexText) - 1]
        else:
            return hexText

    def _recoverLastSettings ( self ):
        bit0Str = self.m_choice_bit0.GetString(self.m_choice_bit0.GetSelection())
        if bit0Str[0] != 'x':
            self.m_choice_bit0.SetSelection(self.efuseDict['0x6e0_miscConf1'] & 0x00000001)
            self.m_staticText_bit0.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit0.Enable( False )
        bit3_1Str = self.m_choice_bit3_1.GetString(self.m_choice_bit3_1.GetSelection())
        if bit3_1Str[0] != 'x':
            self.m_choice_bit3_1.SetSelection((self.efuseDict['0x6e0_miscConf1'] & 0x0000000e) >> 1)
            self.m_staticText_bit3_1.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit3_1.Enable( False )
        bit5_4Str = self.m_choice_bit5_4.GetString(self.m_choice_bit5_4.GetSelection())
        if bit5_4Str[0] != 'x':
            self.m_choice_bit5_4.SetSelection((self.efuseDict['0x6e0_miscConf1'] & 0x00000030) >> 4)
            self.m_staticText_bit5_4.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit5_4.Enable( False )
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.m_choice_bit6.SetSelection((self.efuseDict['0x6e0_miscConf1'] & 0x00000040) >> 6)
            self.m_staticText_bit6.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit6.Enable( False )
        self.m_choice_bit7.SetSelection((self.efuseDict['0x6e0_miscConf1'] & 0x00000080) >> 7)
        self.m_staticText_bit7.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit11_8Label = self.m_staticText_bit11_8.GetLabel()
        if bit11_8Label != 'Reserved':
            self.m_textCtrl_bit11_8.Clear()
            self.m_textCtrl_bit11_8.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x6e0_miscConf1'] & 0x00000f00) >> 8))))
            self.m_staticText_bit11_8.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_textCtrl_bit11_8.Enable( False )
        bit15_12Str = self.m_choice_bit15_12.GetString(self.m_choice_bit15_12.GetSelection())
        if bit15_12Str[0] != 'x':
            self.m_choice_bit15_12.SetSelection((self.efuseDict['0x6e0_miscConf1'] & 0x0000f000) >> 12)
            self.m_staticText_bit15_12.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit15_12.Enable( False )
        bit23_16Label = self.m_staticText_bit23_16.GetLabel()
        if bit23_16Label != 'Reserved':
            self.m_textCtrl_bit23_16.Clear()
            self.m_textCtrl_bit23_16.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x6e0_miscConf1'] & 0x00ff0000) >> 16))))
            self.m_staticText_bit23_16.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_textCtrl_bit23_16.Enable( False )
        bit31_24Label = self.m_staticText_bit31_24.GetLabel()
        if bit31_24Label != 'Reserved':
            self.m_textCtrl_bit31_24.Clear()
            self.m_textCtrl_bit31_24.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x6e0_miscConf1'] & 0xff000000) >> 24))))
            self.m_staticText_bit31_24.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_textCtrl_bit31_24.Enable( False )

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _getEfuseWord( self ):
        bit0Str = self.m_choice_bit0.GetString(self.m_choice_bit0.GetSelection())
        if bit0Str[0] != 'x':
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xfffffffe) | self.m_choice_bit0.GetSelection()
        bit3_1Str = self.m_choice_bit3_1.GetString(self.m_choice_bit3_1.GetSelection())
        if bit3_1Str[0] != 'x':
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xfffffff1) | (self.m_choice_bit3_1.GetSelection() << 1)
        bit5_4Str = self.m_choice_bit5_4.GetString(self.m_choice_bit5_4.GetSelection())
        if bit5_4Str[0] != 'x':
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xffffffcf) | (self.m_choice_bit5_4.GetSelection() << 4)
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xffffffdf) | (self.m_choice_bit6.GetSelection() << 6)
        self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        bit11_8Label = self.m_staticText_bit11_8.GetLabel()
        if bit11_8Label != 'Reserved':
            xSpiFlashDummyCycleStr = self.m_textCtrl_bit11_8.GetLineText(0)
            xSpiFlashDummyCycle = 0
            if len(xSpiFlashDummyCycleStr) >= 3 and xSpiFlashDummyCycleStr[0:2] == '0x':
                xSpiFlashDummyCycle = int(xSpiFlashDummyCycleStr[2:len(xSpiFlashDummyCycleStr)], 16)
                if xSpiFlashDummyCycle >= 0x10:
                    self.popupMsgBox('Illegal input detected! The input value should be in range [0, 15]')
                    return False
            else:
                self.popupMsgBox('Illegal input detected! You should input like this format: 0x2')
                return False
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xfffff0ff) | (xSpiFlashDummyCycle << 8)
        bit15_12Str = self.m_choice_bit15_12.GetString(self.m_choice_bit15_12.GetSelection())
        if bit15_12Str[0] != 'x':
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xffff0fff) | self.m_choice_bit15_12.GetSelection()
        bit23_16Label = self.m_staticText_bit23_16.GetLabel()
        if bit23_16Label != 'Reserved':
            flexspiNorSecondaryImageOffsetStr = self.m_textCtrl_bit23_16.GetLineText(0)
            flexspiNorSecondaryImageOffset = 0
            if len(flexspiNorSecondaryImageOffsetStr) >= 3 and flexspiNorSecondaryImageOffsetStr[0:2] == '0x':
                flexspiNorSecondaryImageOffset = int(flexspiNorSecondaryImageOffsetStr[2:len(flexspiNorSecondaryImageOffsetStr)], 16)
                if flexspiNorSecondaryImageOffset >= 0x100:
                    self.popupMsgBox('Illegal input detected! The input value should be in range [0, 255]')
                    return False
            else:
                self.popupMsgBox('Illegal input detected! You should input like this format: 0x20')
                return False
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0xff00ffff) | (flexspiNorSecondaryImageOffset << 16)
        bit31_24Label = self.m_staticText_bit31_24.GetLabel()
        if bit31_24Label != 'Reserved':
            btPinSelStr = self.m_textCtrl_bit31_24.GetLineText(0)
            btPinSel = 0
            if len(btPinSelStr) >= 3 and btPinSelStr[0:2] == '0x':
                btPinSel = int(btPinSelStr[2:len(btPinSelStr)], 16)
                if btPinSel >= 0x100:
                    self.popupMsgBox('Illegal input detected! The input value should be in range [0, 255]')
                    return False
            else:
                self.popupMsgBox('Illegal input detected! You should input like this format: 0x20')
                return False
            self.efuseDict['0x6e0_miscConf1'] = (self.efuseDict['0x6e0_miscConf1'] & 0x00ffffff) | (btPinSel << 24)
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

