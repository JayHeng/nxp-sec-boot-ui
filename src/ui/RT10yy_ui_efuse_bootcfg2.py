#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import uivar
import RTyyyy_uidef_efuse
sys.path.append(os.path.abspath(".."))
from win import RT10yy_efuseWin_BootCfg2

class secBootUiEfuseBootCfg2(RT10yy_efuseWin_BootCfg2.efuseWin_BootCfg2):

    def __init__(self, parent):
        RT10yy_efuseWin_BootCfg2.efuseWin_BootCfg2.__init__(self, parent)
        efuseDict = uivar.getEfuseSettings()
        self.efuseDict = efuseDict.copy()

    def setNecessaryInfo( self, efuseDescDiffDict ):
        for key in efuseDescDiffDict['0x470_bootcfg2_bit0'].keys():
            self.m_staticText_bit0.SetLabel(key)
            self.m_choice_bit0.Clear()
            self.m_choice_bit0.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit0'][key])
            self.m_choice_bit0.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit3'].keys():
            self.m_staticText_bit3.SetLabel(key)
            self.m_choice_bit3.Clear()
            self.m_choice_bit3.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit3'][key])
            self.m_choice_bit3.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit5'].keys():
            self.m_staticText_bit5.SetLabel(key)
            self.m_choice_bit5.Clear()
            self.m_choice_bit5.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit5'][key])
            self.m_choice_bit5.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit6'].keys():
            self.m_staticText_bit6.SetLabel(key)
            self.m_choice_bit6.Clear()
            self.m_choice_bit6.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit6'][key])
            self.m_choice_bit6.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit7'].keys():
            self.m_staticText_bit7.SetLabel(key)
            self.m_choice_bit7.Clear()
            self.m_choice_bit7.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit7'][key])
            self.m_choice_bit7.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit8'].keys():
            self.m_staticText_bit8.SetLabel(key)
            self.m_choice_bit8.Clear()
            self.m_choice_bit8.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit8'][key])
            self.m_choice_bit8.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit9'].keys():
            self.m_staticText_bit9.SetLabel(key)
            self.m_choice_bit9.Clear()
            self.m_choice_bit9.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit9'][key])
            self.m_choice_bit9.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit11'].keys():
            self.m_staticText_bit11.SetLabel(key)
            self.m_choice_bit11.Clear()
            self.m_choice_bit11.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit11'][key])
            self.m_choice_bit11.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit12'].keys():
            self.m_staticText_bit12.SetLabel(key)
            self.m_choice_bit12.Clear()
            self.m_choice_bit12.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit12'][key])
            self.m_choice_bit12.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit13'].keys():
            self.m_staticText_bit13.SetLabel(key)
            self.m_choice_bit13.Clear()
            self.m_choice_bit13.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit13'][key])
            self.m_choice_bit13.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit14'].keys():
            self.m_staticText_bit14.SetLabel(key)
            self.m_choice_bit14.Clear()
            self.m_choice_bit14.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit14'][key])
            self.m_choice_bit14.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit15'].keys():
            self.m_staticText_bit15.SetLabel(key)
            self.m_choice_bit15.Clear()
            self.m_choice_bit15.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit15'][key])
            self.m_choice_bit15.SetSelection(0)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit30_24'].keys():
            self.m_staticText_bit30_24.SetLabel(key)
        for key in efuseDescDiffDict['0x470_bootcfg2_bit31'].keys():
            self.m_staticText_bit31.SetLabel(key)
            self.m_choice_bit31.Clear()
            self.m_choice_bit31.SetItems(efuseDescDiffDict['0x470_bootcfg2_bit31'][key])
            self.m_choice_bit31.SetSelection(0)
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
            self.m_choice_bit0.SetSelection(self.efuseDict['0x470_bootCfg2'] & 0x00000001)
            self.m_staticText_bit0.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit0.Enable( False )
        self.m_choice_bit1.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000002) >> 1)
        self.m_staticText_bit1.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit2.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000004) >> 2)
        self.m_staticText_bit2.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit3Str = self.m_choice_bit3.GetString(self.m_choice_bit3.GetSelection())
        if bit3Str[0] != 'x':
            self.m_choice_bit3.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000008) >> 3)
            self.m_staticText_bit3.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit3.Enable( False )
        self.m_choice_bit4.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000010) >> 4)
        self.m_staticText_bit4.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit5Str = self.m_choice_bit5.GetString(self.m_choice_bit5.GetSelection())
        if bit5Str[0] != 'x':
            self.m_choice_bit5.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000020) >> 5)
            self.m_staticText_bit5.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit5.Enable( False )
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.m_choice_bit6.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000040) >> 6)
            self.m_staticText_bit6.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit6.Enable( False )
        bit7Str = self.m_choice_bit7.GetString(self.m_choice_bit7.GetSelection())
        if bit7Str[0] != 'x':
            self.m_choice_bit7.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000080) >> 7)
            self.m_staticText_bit7.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit7.Enable( False )
        bit8Str = self.m_choice_bit8.GetString(self.m_choice_bit8.GetSelection())
        if bit8Str[0] != 'x':
            self.m_choice_bit8.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000100) >> 8)
            self.m_staticText_bit8.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit8.Enable( False )
        bit9Str = self.m_choice_bit9.GetString(self.m_choice_bit9.GetSelection())
        if bit9Str[0] != 'x':
            self.m_choice_bit9.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000200) >> 9)
            self.m_staticText_bit9.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit9.Enable( False )
        self.m_choice_bit10.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000400) >> 10)
        self.m_staticText_bit10.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        bit11Str = self.m_choice_bit11.GetString(self.m_choice_bit11.GetSelection())
        if bit11Str[0] != 'x':
            self.m_choice_bit11.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00000800) >> 11)
            self.m_staticText_bit11.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit11.Enable( False )
        bit12Str = self.m_choice_bit12.GetString(self.m_choice_bit12.GetSelection())
        if bit12Str[0] != 'x':
            self.m_choice_bit12.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00001000) >> 12)
            self.m_staticText_bit12.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit12.Enable( False )
        bit13Str = self.m_choice_bit13.GetString(self.m_choice_bit13.GetSelection())
        if bit13Str[0] != 'x':
            self.m_choice_bit13.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00002000) >> 13)
            self.m_staticText_bit13.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit13.Enable( False )
        bit14Str = self.m_choice_bit14.GetString(self.m_choice_bit14.GetSelection())
        if bit14Str[0] != 'x':
            self.m_choice_bit14.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00004000) >> 14)
            self.m_staticText_bit14.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit14.Enable( False )
        bit15Str = self.m_choice_bit15.GetString(self.m_choice_bit15.GetSelection())
        if bit15Str[0] != 'x':
            self.m_choice_bit15.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00008000) >> 15)
            self.m_staticText_bit15.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit15.Enable( False )

        self.m_textCtrl_bit19_16.Clear()
        self.m_textCtrl_bit19_16.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x470_bootCfg2'] & 0x000f0000) >> 16))))
        self.m_staticText_bit19_16.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit20.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00100000) >> 20)
        self.m_staticText_bit20.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit22_21.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x00600000) >> 21)
        self.m_staticText_bit22_21.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        self.m_choice_bit23.Enable( False )

        bit30_24Label = self.m_staticText_bit30_24.GetLabel()
        if bit30_24Label != 'Reserved':
            self.m_textCtrl_bit30_24.Clear()
            self.m_textCtrl_bit30_24.write(self._convertLongIntHexText(str(hex((self.efuseDict['0x470_bootCfg2'] & 0x7f000000) >> 24))))
            self.m_staticText_bit30_24.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_textCtrl_bit30_24.Enable( False )
        bit31Str = self.m_choice_bit31.GetString(self.m_choice_bit31.GetSelection())
        if bit31Str[0] != 'x':
            self.m_choice_bit31.SetSelection((self.efuseDict['0x470_bootCfg2'] & 0x80000000) >> 31)
            self.m_staticText_bit31.SetBackgroundColour(RTyyyy_uidef_efuse.kEfuseFieldColor_Valid)
        else:
            self.m_choice_bit31.Enable( False )

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _getEfuseWord( self ):
        bit0Str = self.m_choice_bit0.GetString(self.m_choice_bit0.GetSelection())
        if bit0Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffe) | self.m_choice_bit0.GetSelection()
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffd) | (self.m_choice_bit1.GetSelection() << 1)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffffb) | (self.m_choice_bit2.GetSelection() << 2)
        bit3Str = self.m_choice_bit3.GetString(self.m_choice_bit3.GetSelection())
        if bit3Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffff7) | (self.m_choice_bit3.GetSelection() << 3)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffef) | (self.m_choice_bit4.GetSelection() << 4)
        bit5Str = self.m_choice_bit5.GetString(self.m_choice_bit5.GetSelection())
        if bit5Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffdf) | (self.m_choice_bit5.GetSelection() << 5)
        bit6Str = self.m_choice_bit6.GetString(self.m_choice_bit6.GetSelection())
        if bit6Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffffbf) | (self.m_choice_bit6.GetSelection() << 6)
        bit7Str = self.m_choice_bit7.GetString(self.m_choice_bit7.GetSelection())
        if bit7Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffff7f) | (self.m_choice_bit7.GetSelection() << 7)
        bit8Str = self.m_choice_bit8.GetString(self.m_choice_bit8.GetSelection())
        if bit8Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffeff) | (self.m_choice_bit8.GetSelection() << 8)
        bit9Str = self.m_choice_bit9.GetString(self.m_choice_bit9.GetSelection())
        if bit9Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffdff) | (self.m_choice_bit9.GetSelection() << 9)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffffbff) | (self.m_choice_bit10.GetSelection() << 10)
        bit11Str = self.m_choice_bit11.GetString(self.m_choice_bit11.GetSelection())
        if bit11Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfffff7ff) | (self.m_choice_bit11.GetSelection() << 11)
        bit12Str = self.m_choice_bit12.GetString(self.m_choice_bit12.GetSelection())
        if bit12Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffefff) | (self.m_choice_bit12.GetSelection() << 12)
        bit13Str = self.m_choice_bit13.GetString(self.m_choice_bit13.GetSelection())
        if bit13Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffdfff) | (self.m_choice_bit13.GetSelection() << 13)
        bit14Str = self.m_choice_bit14.GetString(self.m_choice_bit14.GetSelection())
        if bit14Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffffbfff) | (self.m_choice_bit14.GetSelection() << 14)
        bit15Str = self.m_choice_bit15.GetString(self.m_choice_bit15.GetSelection())
        if bit15Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffff7fff) | (self.m_choice_bit15.GetSelection() << 15)
        failurePinStr = self.m_textCtrl_bit19_16.GetLineText(0)
        failurePin = 0
        if len(failurePinStr) >= 3 and failurePinStr[0:2] == '0x':
            failurePin = int(failurePinStr[2:len(failurePinStr)], 16)
            if failurePin >= 0x10:
                self.popupMsgBox('Illegal input detected! The input value should be in range [0, 15]')
                return False
        else:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x2')
            return False
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xfff0ffff) | (failurePin << 16)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xffefffff) | (self.m_choice_bit23.GetSelection() << 20)
        self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0xff9fffff) | (self.m_choice_bit22_21.GetSelection() << 21)
        bit30_24Label = self.m_staticText_bit30_24.GetLabel()
        if bit30_24Label != 'Reserved':
            emmc4p4DllDelaylineStr = self.m_textCtrl_bit30_24.GetLineText(0)
            emmc4p4DllDelayline = 0
            if len(emmc4p4DllDelaylineStr) >= 3 and emmc4p4DllDelaylineStr[0:2] == '0x':
                emmc4p4DllDelayline = int(emmc4p4DllDelaylineStr[2:len(emmc4p4DllDelaylineStr)], 16)
                if emmc4p4DllDelayline >= 0x80:
                    self.popupMsgBox('Illegal input detected! The input value should be in range [0, 127]')
                    return False
            else:
                self.popupMsgBox('Illegal input detected! You should input like this format: 0x20')
                return False
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0x80ffffff) | (emmc4p4DllDelayline << 24)
        bit31Str = self.m_choice_bit31.GetString(self.m_choice_bit31.GetSelection())
        if bit31Str[0] != 'x':
            self.efuseDict['0x470_bootCfg2'] = (self.efuseDict['0x470_bootCfg2'] & 0x7fffffff) | (self.m_choice_bit31.GetSelection() << 31)
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

