#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import random
import RT10yy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import advSettingsWin_FlexibleUserKeys
from gen import RT10yy_gendef
from run import RT10yy_rundef
from utils import sound

class secBootUiSettingsFlexibleUserKeys(advSettingsWin_FlexibleUserKeys.advSettingsWin_FlexibleUserKeys):

    def __init__(self, parent):
        advSettingsWin_FlexibleUserKeys.advSettingsWin_FlexibleUserKeys.__init__(self, parent)
        self._setLanguage()
        userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_UserKeys)
        self.userKeyCtrlDict = userKeyCtrlDict.copy()
        self.userKeyCmdDict = userKeyCmdDict.copy()
        self.engine0FacStart = [None] * RT10yy_uidef.kMaxFacRegionCount
        self.engine0FacLength = [None] * RT10yy_uidef.kMaxFacRegionCount
        self.engine1FacStart = [None] * RT10yy_uidef.kMaxFacRegionCount
        self.engine1FacLength = [None] * RT10yy_uidef.kMaxFacRegionCount
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_encryptionOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_encryptionOpt'][langIndex])
        self.m_staticText_engineSel.SetLabel(uilang.kSubLanguageContentDict['sText_engineSel'][langIndex])
        self.m_staticText_beeEngKeySel.SetLabel(uilang.kSubLanguageContentDict['sText_beeEngKeySel'][langIndex])
        self.m_staticText_imageType.SetLabel(uilang.kSubLanguageContentDict['sText_imageType'][langIndex])
        self.m_staticText_xipBaseAddr.SetLabel(uilang.kSubLanguageContentDict['sText_xipBaseAddr'][langIndex])
        self.m_notebook_engine0Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_engine0Info'][langIndex])
        self.m_staticText_engine0keySource.SetLabel(uilang.kSubLanguageContentDict['sText_engine0keySource'][langIndex])
        self.m_staticText_engine0UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_engine0UserKeyData'][langIndex])
        self.m_staticText_engine0AesMode.SetLabel(uilang.kSubLanguageContentDict['sText_engine0AesMode'][langIndex])
        self.m_staticText_engine0FacCnt.SetLabel(uilang.kSubLanguageContentDict['sText_engine0FacCnt'][langIndex])
        self.m_staticText_engine0Fac0Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac0Start'][langIndex])
        self.m_staticText_engine0Fac0Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac0Length'][langIndex])
        self.m_staticText_engine0Fac1Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac1Start'][langIndex])
        self.m_staticText_engine0Fac1Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac1Length'][langIndex])
        self.m_staticText_engine0Fac2Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac2Start'][langIndex])
        self.m_staticText_engine0Fac2Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Fac2Length'][langIndex])
        self.m_staticText_engine0AccessPermision.SetLabel(uilang.kSubLanguageContentDict['sText_engine0AccessPermision'][langIndex])
        self.m_staticText_engine0Lock.SetLabel(uilang.kSubLanguageContentDict['sText_engine0Lock'][langIndex])
        self.m_notebook_engine1Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_engine1Info'][langIndex])
        self.m_staticText_engine1keySource.SetLabel(uilang.kSubLanguageContentDict['sText_engine1keySource'][langIndex])
        self.m_staticText_engine1UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_engine1UserKeyData'][langIndex])
        self.m_staticText_engine1AesMode.SetLabel(uilang.kSubLanguageContentDict['sText_engine1AesMode'][langIndex])
        self.m_staticText_engine1FacCnt.SetLabel(uilang.kSubLanguageContentDict['sText_engine1FacCnt'][langIndex])
        self.m_staticText_engine1Fac0Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac0Start'][langIndex])
        self.m_staticText_engine1Fac0Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac0Length'][langIndex])
        self.m_staticText_engine1Fac1Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac1Start'][langIndex])
        self.m_staticText_engine1Fac1Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac1Length'][langIndex])
        self.m_staticText_engine1Fac2Start.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac2Start'][langIndex])
        self.m_staticText_engine1Fac2Length.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Fac2Length'][langIndex])
        self.m_staticText_engine1AccessPermision.SetLabel(uilang.kSubLanguageContentDict['sText_engine1AccessPermision'][langIndex])
        self.m_staticText_engine1Lock.SetLabel(uilang.kSubLanguageContentDict['sText_engine1Lock'][langIndex])
        self.m_button_genRandomKey.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_genRandomKey'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_cancel'][langIndex])

    def _getDek128ContentFromBinFile( self, filename ):
        if os.path.isfile(filename):
            dek128Content = ''
            with open(filename, 'rb') as fileObj:
                var8Value = fileObj.read(16)
                for i in range(16):
                    temp = str(hex(ord(var8Value[15 - i]) & 0xFF))
                    if len(temp) >= 4 and temp[0:2] == '0x':
                        dek128Content += temp[2:4]
                    else:
                        return None
                fileObj.close()
            return dek128Content
        else:
            return None

    def setNecessaryInfo( self, mcuDevice, xipBaseAddr ):
        if self.userKeyCtrlDict['mcu_device'] != mcuDevice:
            keySource = None
            engineSel = None
            if mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT1011:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT1011
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT1011
            elif mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT1015:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT1015
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT1015
            elif mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT102x:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT102x
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT102x
            elif mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT105x:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT105x
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT105x
            elif mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT106x:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT106x
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT106x
            elif mcuDevice == RT10yy_uidef.kMcuDevice_iMXRT1064:
                keySource = RT10yy_uidef.kSupportedKeySource_iMXRT1064
                engineSel = RT10yy_uidef.kSupportedEngineSel_iMXRT1064
            else:
                pass
            self.m_choice_engineSel.Clear()
            self.m_choice_engineSel.SetItems(engineSel)
            self.m_choice_engineSel.SetSelection(0)
            self._changeEngineSelection()
            self.m_choice_xipBaseAddr.Clear()
            xipBaseAddr = [str(hex(xipBaseAddr))]
            self.m_choice_xipBaseAddr.SetItems(xipBaseAddr)
            self.m_choice_xipBaseAddr.SetSelection(0)
            self.m_choice_engine0keySource.Clear()
            self.m_choice_engine1keySource.Clear()
            self.m_choice_engine0keySource.SetItems(keySource)
            self.m_choice_engine1keySource.SetItems(keySource)
            self.m_choice_engine0keySource.SetSelection(0)
            self.m_choice_engine1keySource.SetSelection(0)
            self._recoverLastSettings()
            self.userKeyCtrlDict['mcu_device'] = mcuDevice

    def _recoverLastSettings ( self ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0:
            self.m_choice_engineSel.SetSelection(0)
            self._recoverEngineInfo(0)
            self._updateKeySourceInfoField(0)
            self._updateFacRangeInfoField(0)
            self._updateEngineInfoField(0, True)
            self._updateEngineInfoField(1, False)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1:
            self.m_choice_engineSel.SetSelection(1)
            self._recoverEngineInfo(1)
            self._updateKeySourceInfoField(1)
            self._updateFacRangeInfoField(1)
            self._updateEngineInfoField(0, False)
            self._updateEngineInfoField(1, True)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self.m_choice_engineSel.SetSelection(2)
            self._recoverEngineInfo(0)
            self._updateKeySourceInfoField(0)
            self._updateFacRangeInfoField(0)
            self._recoverEngineInfo(1)
            self._updateKeySourceInfoField(1)
            self._updateFacRangeInfoField(1)
            self._updateEngineInfoField(0, True)
            self._updateEngineInfoField(1, True)
        else:
            pass
        self.m_choice_beeEngKeySel.SetSelection(int(self.userKeyCmdDict['use_zero_key']))
        self.m_choice_imageType.SetSelection(int(self.userKeyCmdDict['is_boot_image']))

    def _getEngineSelection( self ):
        self.userKeyCtrlDict['engine_sel'] = self.m_choice_engineSel.GetString(self.m_choice_engineSel.GetSelection())

    def _getBeeEngKeySelection( self ):
        self.userKeyCmdDict['use_zero_key'] = str(self.m_choice_beeEngKeySel.GetSelection())

    def _getImageType( self ):
        self.userKeyCmdDict['is_boot_image'] = str(self.m_choice_imageType.GetSelection())

    def _getXipBaseAddr( self ):
        self.userKeyCmdDict['base_addr'] = self.m_choice_xipBaseAddr.GetString(self.m_choice_xipBaseAddr.GetSelection())

    def _getKeySource( self, engineIndex=0 ):
        if engineIndex == 0:
            self.userKeyCtrlDict['engine0_key_src'] = self.m_choice_engine0keySource.GetString(self.m_choice_engine0keySource.GetSelection())
        elif engineIndex == 1:
            self.userKeyCtrlDict['engine1_key_src'] = self.m_choice_engine1keySource.GetString(self.m_choice_engine1keySource.GetSelection())
        else:
            pass

    def _validateKeyData( self, engineIndex, keyDat ):
        status = False
        if len(keyDat) == 32:
            try:
                val32 = int(keyDat, 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! Region %d Key data should be exactly 128bits (32 chars)' %(engineIndex))
        return status, keyDat

    def _getUserKeyData( self, engineIndex=0 ):
        validateStatus = False
        if engineIndex == 0:
            validateStatus, self.userKeyCmdDict['engine0_key'] = self._validateKeyData(engineIndex, self.m_textCtrl_engine0UserKeyData.GetLineText(0))
        elif engineIndex == 1:
            if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                if self.userKeyCtrlDict['engine1_key_src'] == self.userKeyCtrlDict['engine0_key_src']:
                    validateStatus, self.userKeyCmdDict['engine1_key'] = self._validateKeyData(engineIndex, self.m_textCtrl_engine0UserKeyData.GetLineText(0))
                else:
                    validateStatus, self.userKeyCmdDict['engine1_key'] = self._validateKeyData(engineIndex, self.m_textCtrl_engine1UserKeyData.GetLineText(0))
            else:
                validateStatus, self.userKeyCmdDict['engine1_key'] = self._validateKeyData(engineIndex, self.m_textCtrl_engine1UserKeyData.GetLineText(0))
        else:
            pass
        return validateStatus

    def _getAesMode( self, engineIndex=0 ):
        if engineIndex == 0:
            aesMode = self.m_choice_engine0AesMode.GetString(self.m_choice_engine0AesMode.GetSelection())
            if aesMode == 'ECB':
                self.userKeyCmdDict['engine0_arg'] = '0'
            elif aesMode == 'CTR':
                self.userKeyCmdDict['engine0_arg'] = '1'
            else:
                pass
        elif engineIndex == 1:
            aesMode = self.m_choice_engine1AesMode.GetString(self.m_choice_engine1AesMode.GetSelection())
            if aesMode == 'ECB':
                self.userKeyCmdDict['engine1_arg'] = '0'
            elif aesMode == 'CTR':
                self.userKeyCmdDict['engine1_arg'] = '1'
            else:
                pass
        else:
            pass

    def _getFacCount( self, engineIndex=0 ):
        if engineIndex == 0:
            self.userKeyCtrlDict['engine0_fac_cnt'] = self.m_choice_engine0FacCnt.GetSelection() + 1
        elif engineIndex == 1:
            self.userKeyCtrlDict['engine1_fac_cnt'] = self.m_choice_engine1FacCnt.GetSelection() + 1
        else:
            pass

    def _getAccessPermision( self, engineIndex=0 ):
        if engineIndex == 0:
            self.userKeyCmdDict['engine0_arg'] += str(self.m_choice_engine0AccessPermision.GetSelection()) + ']'
        elif engineIndex == 1:
            self.userKeyCmdDict['engine1_arg'] += str(self.m_choice_engine1AccessPermision.GetSelection()) + ']'
        else:
            pass

    def _validateEngineRange( self, engineInfoStr ):
        status = False
        val32 = None
        if len(engineInfoStr) > 2 and engineInfoStr[0:2] == '0x':
            try:
                val32 = int(engineInfoStr[2:len(engineInfoStr)], 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x5000')
        return status, val32

    def _getEngineRange( self, engineIndex=0, facIndex=0 ):
        if engineIndex == 0:
            if facIndex == 0:
                validateStatus, self.engine0FacStart[0] = self._validateEngineRange(self.m_textCtrl_engine0Fac0Start.GetLineText(0))
                if validateStatus:
                    if self.engine0FacStart[0] < RT10yy_rundef.kBootDeviceMemBase_FlexspiNor + RT10yy_gendef.kIvtOffset_NOR:
                        self.popupMsgBox('Engine 0 Protected region 0 start address shouldn\'t less than 0x%x' %(RT10yy_rundef.kBootDeviceMemBase_FlexspiNor + RT10yy_gendef.kIvtOffset_NOR))
                        return False
                else:
                    return False
                validateStatus, self.engine0FacLength[0] = self._validateEngineRange(self.m_textCtrl_engine0Fac0Length.GetLineText(0))
                if validateStatus:
                    if self.engine0FacLength[0] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 0 Protected region 0 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine0_arg'] += ',[' + self.m_textCtrl_engine0Fac0Start.GetLineText(0) + ',' + self.m_textCtrl_engine0Fac0Length.GetLineText(0) + ','
            elif facIndex == 1:
                validateStatus, self.engine0FacStart[1] = self._validateEngineRange(self.m_textCtrl_engine0Fac1Start.GetLineText(0))
                if validateStatus:
                    if self.engine0FacStart[1] < self.engine0FacStart[0] + self.engine0FacLength[0]:
                        self.popupMsgBox('Engine 0 Protected region 1 start address shouldn\'t less than Engine 0 Protected region 0 end address 0x%x' %(self.engine0FacStart[0] + self.engine0FacLength[0]))
                        return False
                else:
                    return False
                validateStatus, self.engine0FacLength[1] = self._validateEngineRange(self.m_textCtrl_engine0Fac1Length.GetLineText(0))
                if validateStatus:
                    if self.engine0FacLength[1] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 0 Protected region 1 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine0_arg'] += ',[' + self.m_textCtrl_engine0Fac1Start.GetLineText(0) + ',' + self.m_textCtrl_engine0Fac1Length.GetLineText(0) + ','
            elif facIndex == 2:
                validateStatus, self.engine0FacStart[2] = self._validateEngineRange(self.m_textCtrl_engine0Fac2Start.GetLineText(0))
                if validateStatus:
                    if self.engine0FacStart[2] < self.engine0FacStart[1] + self.engine0FacLength[1]:
                        self.popupMsgBox('Engine 0 Protected region 2 start address shouldn\'t less than Engine 0 Protected region 1 end address 0x%x' %(self.engine0FacStart[1] + self.engine0FacLength[1]))
                        return False
                else:
                    return False
                validateStatus, self.engine0FacLength[2] = self._validateEngineRange(self.m_textCtrl_engine0Fac2Length.GetLineText(0))
                if validateStatus:
                    if self.engine0FacLength[2] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 0 Protected region 2 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine0_arg'] += ',[' + self.m_textCtrl_engine0Fac2Start.GetLineText(0) + ',' + self.m_textCtrl_engine0Fac2Length.GetLineText(0) + ','
            else:
                pass
        elif engineIndex == 1:
            if facIndex == 0:
                validateStatus, self.engine1FacStart[0] = self._validateEngineRange(self.m_textCtrl_engine1Fac0Start.GetLineText(0))
                if validateStatus:
                    if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                        if self.engine0FacStart[2] != None:
                            if self.engine1FacStart[0] < self.engine0FacStart[2] + self.engine0FacLength[2]:
                                self.popupMsgBox('Engine 1 Protected region 0 start address shouldn\'t less than Engine 0 Protected region 2 end address 0x%x' %(self.engine0FacStart[2] + self.engine0FacLength[2]))
                                return False
                        elif self.engine0FacStart[1] != None:
                            if self.engine1FacStart[0] < self.engine0FacStart[1] + self.engine0FacLength[1]:
                                self.popupMsgBox('Engine 1 Protected region 0 start address shouldn\'t less than Engine 0 Protected region 1 end address 0x%x' %(self.engine0FacStart[1] + self.engine0FacLength[1]))
                                return False
                        elif self.engine0FacStart[0] != None:
                            if self.engine1FacStart[0] < self.engine0FacStart[0] + self.engine0FacLength[0]:
                                self.popupMsgBox('Engine 1 Protected region 0 start address shouldn\'t less than Engine 0 Protected region 0 end address 0x%x' %(self.engine0FacStart[0] + self.engine0FacLength[0]))
                                return False
                        else:
                            pass
                        # startRegion = self.engine0FacStart[2] + self.engine0FacLength[2]
                    else:
                        if self.engine1FacStart[0] < RT10yy_rundef.kBootDeviceMemBase_FlexspiNor + RT10yy_gendef.kIvtOffset_NOR:
                            self.popupMsgBox('Engine 1 Protected region 0 start address shouldn\'t less than 0x%x' %(RT10yy_rundef.kBootDeviceMemBase_FlexspiNor + RT10yy_gendef.kIvtOffset_NOR))
                            return False
                else:
                    return False
                validateStatus, self.engine1FacLength[0] = self._validateEngineRange(self.m_textCtrl_engine1Fac0Length.GetLineText(0))
                if validateStatus:
                    if self.engine1FacLength[0] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 1 Protected region 0 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine1_arg'] += ',[' + self.m_textCtrl_engine1Fac0Start.GetLineText(0) + ',' + self.m_textCtrl_engine1Fac0Length.GetLineText(0) + ','
            elif facIndex == 1:
                validateStatus, self.engine1FacStart[1] = self._validateEngineRange(self.m_textCtrl_engine1Fac1Start.GetLineText(0))
                if validateStatus:
                    if self.engine1FacStart[1] < self.engine1FacStart[0] + self.engine1FacLength[0]:
                        self.popupMsgBox('Engine 1 Protected region 1 start address shouldn\'t less than Engine 1 Protected region 0 end address 0x%x' %(self.engine1FacStart[0] + self.engine1FacLength[0]))
                        return False
                else:
                    return False
                validateStatus, self.engine1FacLength[1] = self._validateEngineRange(self.m_textCtrl_engine1Fac1Length.GetLineText(0))
                if validateStatus:
                    if self.engine1FacLength[1] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 1 Protected region 1 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine1_arg'] += ',[' + self.m_textCtrl_engine1Fac1Start.GetLineText(0) + ',' + self.m_textCtrl_engine1Fac1Length.GetLineText(0) + ','
            elif facIndex == 2:
                validateStatus, self.engine1FacStart[2] = self._validateEngineRange(self.m_textCtrl_engine1Fac2Start.GetLineText(0))
                if validateStatus:
                    if self.engine1FacStart[2] < self.engine1FacStart[1] + self.engine1FacLength[1]:
                        self.popupMsgBox('Engine 1 Protected region 2 start address shouldn\'t less than Engine 1 Protected region 1 end address 0x%x' %(self.engine1FacStart[1] + self.engine1FacLength[1]))
                        return False
                else:
                    return False
                validateStatus, self.engine1FacLength[2] = self._validateEngineRange(self.m_textCtrl_engine1Fac2Length.GetLineText(0))
                if validateStatus:
                    if self.engine1FacLength[2] % RT10yy_gendef.kSecFacRegionAlignedUnit != 0:
                        self.popupMsgBox('Engine 1 Protected region 2 length should be aligned with %dKB' %(RT10yy_gendef.kSecFacRegionAlignedUnit / 0x400))
                        return False
                else:
                    return False
                self.userKeyCmdDict['engine1_arg'] += ',[' + self.m_textCtrl_engine1Fac2Start.GetLineText(0) + ',' + self.m_textCtrl_engine1Fac2Length.GetLineText(0) + ','
            else:
                pass
        else:
            pass
        return True

    def _getEngineLock( self, engineIndex=0 ):
        if engineIndex == 0:
            self.userKeyCmdDict['engine0_lock'] = str(self.m_choice_engine0Lock.GetSelection())
        elif engineIndex == 1:
            self.userKeyCmdDict['engine1_lock'] = str(self.m_choice_engine1Lock.GetSelection())
        else:
            pass

    def _getEngineArg( self, engineIndex=0 ):
        self._getFacCount(engineIndex)
        self._getAesMode(engineIndex)
        facCnt = 0
        if engineIndex == 0:
            facCnt = self.userKeyCtrlDict['engine0_fac_cnt']
        elif engineIndex == 1:
            facCnt = self.userKeyCtrlDict['engine1_fac_cnt']
        else:
            pass
        for i in range(facCnt):
            status = self._getEngineRange(engineIndex, i)
            if not status:
                self.engine0FacStart = [None] * RT10yy_uidef.kMaxFacRegionCount
                self.engine0FacLength = [None] * RT10yy_uidef.kMaxFacRegionCount
                self.engine1FacStart = [None] * RT10yy_uidef.kMaxFacRegionCount
                self.engine1FacLength = [None] * RT10yy_uidef.kMaxFacRegionCount
                return False
            self._getAccessPermision(engineIndex)
        return True

    def _getEngineInfo( self, engineIndex=0 ):
        self._getKeySource(engineIndex)
        if not self._getUserKeyData(engineIndex):
            return False
        if not self._getEngineArg(engineIndex):
            return False
        self._getEngineLock(engineIndex)
        return True

    def _recoverEngineArg( self, engineIndex ):
        if engineIndex == 0:
            self.m_choice_engine0FacCnt.SetSelection(self.userKeyCtrlDict['engine0_fac_cnt'] - 1)
            if self.userKeyCmdDict['engine0_arg'][0] == '1':
                self.m_choice_engine0AesMode.SetSelection(0)
            locStart = 0
            locEnd = 0
            if self.userKeyCtrlDict['engine0_fac_cnt'] > 0:
                self.m_textCtrl_engine0Fac0Start.Clear()
                locStart = self.userKeyCmdDict['engine0_arg'].find('[')
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart)
                self.m_textCtrl_engine0Fac0Start.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine0Fac0Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine0Fac0Length.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
            if self.userKeyCtrlDict['engine0_fac_cnt'] > 1:
                self.m_textCtrl_engine0Fac1Start.Clear()
                locStart = self.userKeyCmdDict['engine0_arg'].find('[', locEnd)
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart)
                self.m_textCtrl_engine0Fac1Start.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine0Fac1Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine0Fac1Length.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
            if self.userKeyCtrlDict['engine0_fac_cnt'] > 2:
                self.m_textCtrl_engine0Fac2Start.Clear()
                locStart = self.userKeyCmdDict['engine0_arg'].find('[', locEnd)
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart)
                self.m_textCtrl_engine0Fac2Start.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine0Fac2Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine0_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine0Fac2Length.write(self.userKeyCmdDict['engine0_arg'][locStart+1:locEnd])
            locEnd = self.userKeyCmdDict['engine0_arg'].find(']', locEnd)
            self.m_choice_engine0AccessPermision.SetSelection(int(self.userKeyCmdDict['engine0_arg'][locEnd-1:locEnd]))
        elif engineIndex == 1:
            self.m_choice_engine1FacCnt.SetSelection(self.userKeyCtrlDict['engine1_fac_cnt'] - 1)
            if self.userKeyCmdDict['engine1_arg'][0] == '1':
                self.m_choice_engine1AesMode.SetSelection(0)
            locStart = 0
            locEnd = 0
            if self.userKeyCtrlDict['engine1_fac_cnt'] > 0:
                self.m_textCtrl_engine1Fac0Start.Clear()
                locStart = self.userKeyCmdDict['engine1_arg'].find('[')
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart)
                self.m_textCtrl_engine1Fac0Start.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine1Fac0Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine1Fac0Length.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
            if self.userKeyCtrlDict['engine1_fac_cnt'] > 1:
                self.m_textCtrl_engine1Fac1Start.Clear()
                locStart = self.userKeyCmdDict['engine1_arg'].find('[', locEnd)
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart)
                self.m_textCtrl_engine1Fac1Start.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine1Fac1Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine1Fac1Length.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
            if self.userKeyCtrlDict['engine1_fac_cnt'] > 2:
                self.m_textCtrl_engine1Fac2Start.Clear()
                locStart = self.userKeyCmdDict['engine1_arg'].find('[', locEnd)
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart)
                self.m_textCtrl_engine1Fac2Start.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
                self.m_textCtrl_engine1Fac2Length.Clear()
                locStart = locEnd
                locEnd = self.userKeyCmdDict['engine1_arg'].find(',', locStart + 1)
                self.m_textCtrl_engine1Fac2Length.write(self.userKeyCmdDict['engine1_arg'][locStart+1:locEnd])
            locEnd = self.userKeyCmdDict['engine1_arg'].find(']', locEnd)
            self.m_choice_engine1AccessPermision.SetSelection(int(self.userKeyCmdDict['engine1_arg'][locEnd-1:locEnd]))
        else:
            pass

    def _recoverEngineInfo( self, engineIndex ):
        if engineIndex == 0:
            if self.m_choice_engine0keySource.GetCount() == 2:
                if self.userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                    self.m_choice_engine0keySource.SetSelection(0)
                elif self.userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                    self.m_choice_engine0keySource.SetSelection(1)
                else:
                    pass
            else:
                self.m_choice_engine0keySource.SetSelection(0)
            self.m_textCtrl_engine0UserKeyData.Clear()
            if self.userKeyCmdDict['engine0_key'] != None:
                self.m_textCtrl_engine0UserKeyData.write(self.userKeyCmdDict['engine0_key'])
            self._recoverEngineArg(0)
            if self.userKeyCmdDict['engine0_lock'] == 'No Lock':
                self.m_choice_engine0Lock.SetSelection(0)
        elif engineIndex == 1:
            if self.m_choice_engine1keySource.GetCount() == 2:
                if self.userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                    self.m_choice_engine1keySource.SetSelection(0)
                elif self.userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                    self.m_choice_engine1keySource.SetSelection(1)
                else:
                    pass
            else:
                self.m_choice_engine1keySource.SetSelection(0)
            self.m_textCtrl_engine1UserKeyData.Clear()
            if self.userKeyCmdDict['engine1_key'] != None:
                self.m_textCtrl_engine1UserKeyData.write(self.userKeyCmdDict['engine1_key'])
            self._recoverEngineArg(1)
            if self.userKeyCmdDict['engine1_lock'] == 'No Lock':
                self.m_choice_engine1Lock.SetSelection(0)
        else:
            pass

    def _updateKeySourceInfoField ( self, engineIndex=0 ):
        if engineIndex == 0:
            self.m_textCtrl_engine0UserKeyData.Enable( True )
            if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                if self.userKeyCtrlDict['engine1_key_src'] == self.userKeyCtrlDict['engine0_key_src']:
                    self.m_textCtrl_engine1UserKeyData.Enable( False )
                    self.m_textCtrl_engine1UserKeyData.Clear()
                else:
                    self.m_textCtrl_engine1UserKeyData.Enable( True )
        elif engineIndex == 1:
            if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                if self.userKeyCtrlDict['engine1_key_src'] == self.userKeyCtrlDict['engine0_key_src']:
                    self.m_textCtrl_engine1UserKeyData.Enable( False )
                    self.m_textCtrl_engine1UserKeyData.Clear()
                else:
                    self.m_textCtrl_engine1UserKeyData.Enable( True )
            else:
                self.m_textCtrl_engine1UserKeyData.Enable( True )
        else:
            pass

    def _updateFacRangeInfoField ( self, engineIndex=0 ):
        if engineIndex == 0:
            if self.userKeyCtrlDict['engine0_fac_cnt'] < 1:
                self.m_textCtrl_engine0Fac0Start.Enable( False )
                self.m_textCtrl_engine0Fac0Length.Enable( False )
            else:
                self.m_textCtrl_engine0Fac0Start.Enable( True )
                self.m_textCtrl_engine0Fac0Length.Enable( True )
            if self.userKeyCtrlDict['engine0_fac_cnt'] < 2:
                self.m_textCtrl_engine0Fac1Start.Enable( False )
                self.m_textCtrl_engine0Fac1Length.Enable( False )
            else:
                self.m_textCtrl_engine0Fac1Start.Enable( True )
                self.m_textCtrl_engine0Fac1Length.Enable( True )
            if self.userKeyCtrlDict['engine0_fac_cnt'] < 3:
                self.m_textCtrl_engine0Fac2Start.Enable( False )
                self.m_textCtrl_engine0Fac2Length.Enable( False )
            else:
                self.m_textCtrl_engine0Fac2Start.Enable( True )
                self.m_textCtrl_engine0Fac2Length.Enable( True )
        elif engineIndex == 1:
            if self.userKeyCtrlDict['engine1_fac_cnt'] < 1:
                self.m_textCtrl_engine1Fac0Start.Enable( False )
                self.m_textCtrl_engine1Fac0Length.Enable( False )
            else:
                self.m_textCtrl_engine1Fac0Start.Enable( True )
                self.m_textCtrl_engine1Fac0Length.Enable( True )
            if self.userKeyCtrlDict['engine1_fac_cnt'] < 2:
                self.m_textCtrl_engine1Fac1Start.Enable( False )
                self.m_textCtrl_engine1Fac1Length.Enable( False )
            else:
                self.m_textCtrl_engine1Fac1Start.Enable( True )
                self.m_textCtrl_engine1Fac1Length.Enable( True )
            if self.userKeyCtrlDict['engine1_fac_cnt'] < 3:
                self.m_textCtrl_engine1Fac2Start.Enable( False )
                self.m_textCtrl_engine1Fac2Length.Enable( False )
            else:
                self.m_textCtrl_engine1Fac2Start.Enable( True )
                self.m_textCtrl_engine1Fac2Length.Enable( True )
        else:
            pass

    def _updateEngineInfoField ( self, engineIndex=0, isEngineEnabled=False ):
        if engineIndex == 0:
            if isEngineEnabled:
                self.m_choice_engine0keySource.Enable( True )
                self.m_textCtrl_engine0UserKeyData.Enable( True )
                self.m_choice_engine0AesMode.Enable( True )
                self.m_choice_engine0FacCnt.Enable( True )
                self.m_textCtrl_engine0Fac0Start.Enable( True )
                self.m_textCtrl_engine0Fac0Length.Enable( True )
                self.m_textCtrl_engine0Fac1Start.Enable( True )
                self.m_textCtrl_engine0Fac1Length.Enable( True )
                self.m_textCtrl_engine0Fac2Start.Enable( True )
                self.m_textCtrl_engine0Fac2Length.Enable( True )
                self.m_choice_engine0AccessPermision.Enable( True )
                self.m_choice_engine0Lock.Enable( True )

                self._getKeySource(0)
                self._updateKeySourceInfoField(0)
                self._getFacCount(0)
                self._updateFacRangeInfoField(0)
            else:
                self.m_choice_engine0keySource.Enable( False )
                self.m_textCtrl_engine0UserKeyData.Enable( False )
                self.m_choice_engine0AesMode.Enable( False )
                self.m_choice_engine0FacCnt.Enable( False )
                self.m_textCtrl_engine0Fac0Start.Enable( False )
                self.m_textCtrl_engine0Fac0Length.Enable( False )
                self.m_textCtrl_engine0Fac1Start.Enable( False )
                self.m_textCtrl_engine0Fac1Length.Enable( False )
                self.m_textCtrl_engine0Fac2Start.Enable( False )
                self.m_textCtrl_engine0Fac2Length.Enable( False )
                self.m_choice_engine0AccessPermision.Enable( False )
                self.m_choice_engine0Lock.Enable( False )
        elif engineIndex == 1:
            if isEngineEnabled:
                self.m_choice_engine1keySource.Enable( True )
                self.m_textCtrl_engine1UserKeyData.Enable( True )
                self.m_choice_engine1AesMode.Enable( True )
                self.m_choice_engine1FacCnt.Enable( True )
                self.m_textCtrl_engine1Fac0Start.Enable( True )
                self.m_textCtrl_engine1Fac0Length.Enable( True )
                self.m_textCtrl_engine1Fac1Start.Enable( True )
                self.m_textCtrl_engine1Fac1Length.Enable( True )
                self.m_textCtrl_engine1Fac2Start.Enable( True )
                self.m_textCtrl_engine1Fac2Length.Enable( True )
                self.m_choice_engine1AccessPermision.Enable( True )
                self.m_choice_engine1Lock.Enable( True )

                self._getKeySource(1)
                self._updateKeySourceInfoField(1)
                self._getFacCount(1)
                self._updateFacRangeInfoField(1)
            else:
                self.m_choice_engine1keySource.Enable( False )
                self.m_textCtrl_engine1UserKeyData.Enable( False )
                self.m_choice_engine1AesMode.Enable( False )
                self.m_choice_engine1FacCnt.Enable( False )
                self.m_textCtrl_engine1Fac0Start.Enable( False )
                self.m_textCtrl_engine1Fac0Length.Enable( False )
                self.m_textCtrl_engine1Fac1Start.Enable( False )
                self.m_textCtrl_engine1Fac1Length.Enable( False )
                self.m_textCtrl_engine1Fac2Start.Enable( False )
                self.m_textCtrl_engine1Fac2Length.Enable( False )
                self.m_choice_engine1AccessPermision.Enable( False )
                self.m_choice_engine1Lock.Enable( False )
        else:
            pass

    def _changeEngineSelection( self ):
        self._getEngineSelection()
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0:
            self._updateEngineInfoField(0, True)
            self._updateEngineInfoField(1, False)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1:
            self._updateEngineInfoField(0, False)
            self._updateEngineInfoField(1, True)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self._updateEngineInfoField(0, True)
            self._updateEngineInfoField(1, True)
        else:
            pass

    def callbackChangeEngineSelection( self, event ):
        self._changeEngineSelection()

    def callbackChangeEngine0KeySource( self, event ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0 or \
           self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self._getKeySource(0)
            self._updateKeySourceInfoField(0)

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def callbackChangeEngine0FacCnt( self, event ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0:
            self._getFacCount(0)
            self._updateFacRangeInfoField(0)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            region0FacCnt = self.m_choice_engine0FacCnt.GetSelection() + 1
            if region0FacCnt + self.userKeyCtrlDict['engine1_fac_cnt'] > RT10yy_uidef.kMaxFacRegionCount:
                self.m_choice_engine0FacCnt.SetSelection(self.userKeyCtrlDict['engine0_fac_cnt'] - 1)
                self.popupMsgBox('The sum of Protected Region count of Engine0 and Engine1 must be no more than ' + str(RT10yy_uidef.kMaxFacRegionCount))
            else:
                self._getFacCount(0)
                self._updateFacRangeInfoField(0)
        else:
            pass

    def callbackChangeEngine1KeySource( self, event ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1 or \
           self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self._getKeySource(1)
            self._updateKeySourceInfoField(1)


    def callbackChangeEngine1FacCnt( self, event ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1:
            self._getFacCount(1)
            self._updateFacRangeInfoField(1)
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            region1FacCnt = self.m_choice_engine1FacCnt.GetSelection() + 1
            if region1FacCnt + self.userKeyCtrlDict['engine0_fac_cnt'] > RT10yy_uidef.kMaxFacRegionCount:
                self.m_choice_engine1FacCnt.SetSelection(self.userKeyCtrlDict['engine1_fac_cnt'] - 1)
                self.popupMsgBox('The sum of Protected Region count of Engine0 and Engine1 must be no more than ' + str(RT10yy_uidef.kMaxFacRegionCount))
            else:
                self._getFacCount(1)
                self._updateFacRangeInfoField(1)
        else:
            pass

    def _genRandomUserKeyData( self ):
        userKey = ''
        for i in range(32):
            userKey += random.choice('0123456789abcdef')
        return userKey

    def callbackGenRandomUserKey( self, event ):
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0:
            self.m_textCtrl_engine0UserKeyData.Clear()
            self.m_textCtrl_engine0UserKeyData.write(self._genRandomUserKeyData())
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1:
            self.m_textCtrl_engine1UserKeyData.Clear()
            self.m_textCtrl_engine1UserKeyData.write(self._genRandomUserKeyData())
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self.m_textCtrl_engine0UserKeyData.Clear()
            self.m_textCtrl_engine0UserKeyData.write(self._genRandomUserKeyData())
            self.m_textCtrl_engine1UserKeyData.Clear()
            self.m_textCtrl_engine1UserKeyData.write(self._genRandomUserKeyData())
        else:
            pass

    def callbackOk( self, event ):
        self._getEngineSelection()
        if self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0:
            if not self._getEngineInfo(0):
                return
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1:
            if not self._getEngineInfo(1):
                return
        elif self.userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            if not self._getEngineInfo(0):
                return
            if not self._getEngineInfo(1):
                return
        else:
            pass
        self._getBeeEngKeySelection()
        self._getImageType()
        self._getXipBaseAddr()
        #print 'base_addr=' + self.userKeyCmdDict['base_addr']
        #print 'engine0_key=' + self.userKeyCmdDict['engine0_key'] + \
        #      ' engine0_arg=' + self.userKeyCmdDict['engine0_arg'] + \
        #      ' engine0_lock=' + self.userKeyCmdDict['engine0_lock']
        #print 'engine1_key=' + self.userKeyCmdDict['engine1_key'] + \
        #      ' engine1_arg=' + self.userKeyCmdDict['engine1_arg'] + \
        #      ' engine1_lock=' + self.userKeyCmdDict['engine1_lock']
        #print 'use_zero_key=' + self.userKeyCmdDict['use_zero_key']
        #print 'is_boot_image=' + self.userKeyCmdDict['is_boot_image']
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_UserKeys, self.userKeyCtrlDict, self.userKeyCmdDict)
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
