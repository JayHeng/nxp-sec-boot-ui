#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import advSettingsWin_FixedOtpmkKey
from gen import RTyyyy_gendef
from run import RTyyyy_rundef
from utils import sound

class secBootUiSettingsFixedOtpmkKey(advSettingsWin_FixedOtpmkKey.advSettingsWin_FixedOtpmkKey):

    def __init__(self, parent):
        advSettingsWin_FixedOtpmkKey.advSettingsWin_FixedOtpmkKey.__init__(self, parent)
        self._setLanguage()
        otpmkKeyOpt, otpmkEncryptedRegionStartList, otpmkEncryptedRegionLengthList = uivar.getAdvancedSettings(uidef.kAdvancedSettings_OtpmkKey)
        self.otpmkKeyOpt = otpmkKeyOpt
        self.otpmkEncryptedRegionStartList = otpmkEncryptedRegionStartList[:]
        self.otpmkEncryptedRegionLengthList = otpmkEncryptedRegionLengthList[:]
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_encryptionOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_encryptionOpt'][langIndex])
        self.m_staticText_keySource.SetLabel(uilang.kSubLanguageContentDict['sText_keySource'][langIndex])
        self.m_staticText_aesMode.SetLabel(uilang.kSubLanguageContentDict['sText_aesMode'][langIndex])
        self.m_staticText_regionCnt.SetLabel(uilang.kSubLanguageContentDict['sText_regionCnt'][langIndex])
        self.m_notebook_regionInfo.SetPageText(0, uilang.kSubLanguageContentDict['panel_regionInfo'][langIndex])
        self.m_staticText_regionStart.SetLabel(uilang.kSubLanguageContentDict['sText_regionStart'][langIndex])
        self.m_staticText_regionLength.SetLabel(uilang.kSubLanguageContentDict['sText_regionLength'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_otpmkkey_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_otpmkkey_cancel'][langIndex])

    def _updateRegionInfoField ( self, regionCnt ):
        if regionCnt < 1:
            self.m_textCtrl_region0Start.Enable( False )
            self.m_textCtrl_region0Length.Enable( False )
        else:
            self.m_textCtrl_region0Start.Enable( True )
            self.m_textCtrl_region0Length.Enable( True )
        if regionCnt < 2:
            self.m_textCtrl_region1Start.Enable( False )
            self.m_textCtrl_region1Length.Enable( False )
        else:
            self.m_textCtrl_region1Start.Enable( True )
            self.m_textCtrl_region1Length.Enable( True )
        if regionCnt < 3:
            self.m_textCtrl_region2Start.Enable( False )
            self.m_textCtrl_region2Length.Enable( False )
        else:
            self.m_textCtrl_region2Start.Enable( True )
            self.m_textCtrl_region2Length.Enable( True )

    def _recoverLastSettings ( self ):
        keySource = (self.otpmkKeyOpt & 0x0F000000) >> 24
        self.m_choice_keySource.SetSelection(keySource)

        aesMode = (self.otpmkKeyOpt & 0x00F00000) >> 20
        if aesMode == 1:
            self.m_choice_aesMode.SetSelection(0)

        encryptedRegionCnt = (self.otpmkKeyOpt & 0x000F0000) >> 16
        self.m_choice_regionCnt.SetSelection(encryptedRegionCnt)

        self._updateRegionInfoField(encryptedRegionCnt)

        if encryptedRegionCnt > 0:
            self.m_textCtrl_region0Start.Clear()
            self.m_textCtrl_region0Length.Clear()
            self.m_textCtrl_region0Start.write(str(hex(self.otpmkEncryptedRegionStartList[0])))
            self.m_textCtrl_region0Length.write(str(hex(self.otpmkEncryptedRegionLengthList[0])))
        if encryptedRegionCnt > 1:
            self.m_textCtrl_region1Start.Clear()
            self.m_textCtrl_region1Length.Clear()
            self.m_textCtrl_region1Start.write(str(hex(self.otpmkEncryptedRegionStartList[1])))
            self.m_textCtrl_region1Length.write(str(hex(self.otpmkEncryptedRegionLengthList[1])))
        if encryptedRegionCnt > 2:
            self.m_textCtrl_region2Start.Clear()
            self.m_textCtrl_region2Length.Clear()
            self.m_textCtrl_region2Start.write(str(hex(self.otpmkEncryptedRegionStartList[2])))
            self.m_textCtrl_region2Length.write(str(hex(self.otpmkEncryptedRegionLengthList[2])))

    def _getKeySource( self ):
        txt = self.m_choice_keySource.GetString(self.m_choice_keySource.GetSelection())
        if txt == 'Fuse OTPMK - SNVS':
            val = 0x0
        else:
            pass
        self.otpmkKeyOpt = (self.otpmkKeyOpt & 0xF0FFFFFF) | (val << 24)

    def _getAesMode( self ):
        txt = self.m_choice_aesMode.GetString(self.m_choice_aesMode.GetSelection())
        if txt == 'ECB':
            val = 0x0
        elif txt == 'CTR':
            val = 0x1
        else:
            pass
        self.otpmkKeyOpt = (self.otpmkKeyOpt & 0xFF0FFFFF) | (val << 20)

    def _getEncryptedRegionCount( self ):
        txt = self.m_choice_regionCnt.GetString(self.m_choice_regionCnt.GetSelection())
        val = int(txt[0])
        self.otpmkKeyOpt = (self.otpmkKeyOpt & 0xFFF0FFFF) | (val << 16)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _convertRegionInfoToVal32( self, regionInfoStr ):
        status = False
        val32 = None
        if len(regionInfoStr) > 2 and regionInfoStr[0:2] == '0x':
            try:
                val32 = int(regionInfoStr[2:len(regionInfoStr)], 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x5000')
        return status, val32

    def _getEncryptedRegionInfo( self ):
        convertStatus = False
        txt = self.m_choice_regionCnt.GetString(self.m_choice_regionCnt.GetSelection())
        regionCnt = int(txt[0])
        if regionCnt > 0:
            convertStatus, self.otpmkEncryptedRegionStartList[0] = self._convertRegionInfoToVal32(self.m_textCtrl_region0Start.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionStartList[0] < RTyyyy_rundef.kBootDeviceMemBase_FlexspiNor + RTyyyy_gendef.kIvtOffset_NOR:
                    self.popupMsgBox('FAC Region 0 start address shouldn\'t less than 0x%x' %(RTyyyy_rundef.kBootDeviceMemBase_FlexspiNor + RTyyyy_gendef.kIvtOffset_NOR))
                    return False
            else:
                return False
            convertStatus, self.otpmkEncryptedRegionLengthList[0] = self._convertRegionInfoToVal32(self.m_textCtrl_region0Length.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionLengthList[0] % RTyyyy_gendef.kSecFacRegionAlignedUnit != 0:
                    self.popupMsgBox('FAC Region 0 length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit / 0x400))
                    return False
            else:
                return False
        else:
            self.otpmkEncryptedRegionStartList[0] = None
            self.otpmkEncryptedRegionLengthList[0] = None
        if regionCnt > 1:
            convertStatus, self.otpmkEncryptedRegionStartList[1] = self._convertRegionInfoToVal32(self.m_textCtrl_region1Start.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionStartList[1] < self.otpmkEncryptedRegionStartList[0] + self.otpmkEncryptedRegionLengthList[0]:
                    self.popupMsgBox('FAC Region 1 start address shouldn\'t less than FAC region 0 end address 0x%x' %(self.otpmkEncryptedRegionStartList[0] + self.otpmkEncryptedRegionLengthList[0]))
                    return False
            else:
                return False
            convertStatus, self.otpmkEncryptedRegionLengthList[1] = self._convertRegionInfoToVal32(self.m_textCtrl_region1Length.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionLengthList[1] % RTyyyy_gendef.kSecFacRegionAlignedUnit != 0:
                    self.popupMsgBox('FAC Region 1 length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit / 0x400))
                    return False
            else:
                return False
        else:
            self.otpmkEncryptedRegionStartList[1] = None
            self.otpmkEncryptedRegionLengthList[1] = None
        if regionCnt > 2:
            convertStatus, self.otpmkEncryptedRegionStartList[2] = self._convertRegionInfoToVal32(self.m_textCtrl_region2Start.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionStartList[2] < self.otpmkEncryptedRegionStartList[1] + self.otpmkEncryptedRegionLengthList[1]:
                    self.popupMsgBox('FAC Region 2 start address shouldn\'t less than FAC region 1 end address 0x%x' %(self.otpmkEncryptedRegionStartList[1] + self.otpmkEncryptedRegionLengthList[1]))
                    return False
            else:
                return False
            convertStatus, self.otpmkEncryptedRegionLengthList[2] = self._convertRegionInfoToVal32(self.m_textCtrl_region2Length.GetLineText(0))
            if convertStatus:
                if self.otpmkEncryptedRegionLengthList[2] % RTyyyy_gendef.kSecFacRegionAlignedUnit != 0:
                    self.popupMsgBox('FAC Region 2 length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit / 0x400))
                    return False
            else:
                return False
        else:
            self.otpmkEncryptedRegionStartList[2] = None
            self.otpmkEncryptedRegionLengthList[2] = None
        return True

    def callbackChangeRegionCount( self, event ):
        txt = self.m_choice_regionCnt.GetString(self.m_choice_regionCnt.GetSelection())
        regionCnt = int(txt[0])
        self._updateRegionInfoField(regionCnt)

    def callbackOk( self, event ):
        self._getKeySource()
        self._getAesMode()
        self._getEncryptedRegionCount()
        if not self._getEncryptedRegionInfo():
            return
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_OtpmkKey, self.otpmkKeyOpt, self.otpmkEncryptedRegionStartList, self.otpmkEncryptedRegionLengthList)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], uidef.kSoundEffectFilename_Progress)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)
