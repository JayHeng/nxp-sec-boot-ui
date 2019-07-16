#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import random
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import advSettingsWin_FlexibleUserKeys_Otfad
from gen import RTyyyy_gendef
from run import RTyyyy_rundef
from utils import sound

class secBootUiSettingsFlexibleUserKeysOtfad(advSettingsWin_FlexibleUserKeys_Otfad.advSettingsWin_FlexibleUserKeys_Otfad):

    def __init__(self, parent):
        advSettingsWin_FlexibleUserKeys_Otfad.advSettingsWin_FlexibleUserKeys_Otfad.__init__(self, parent)
        self._setLanguage()
        userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_UserKeys)
        self.userKeyCtrlDict = userKeyCtrlDict.copy()
        self.userKeyCmdDict = userKeyCmdDict.copy()
        self.regionFacStart = [None] * RTyyyy_uidef.kMaxFacRegionCount_Otfad
        self.regionFacLength = [None] * RTyyyy_uidef.kMaxFacRegionCount_Otfad
        self.xipBaseAddr = None
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_encryptionOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_encryptionOpt'][langIndex])
        self.m_staticText_totalRegions.SetLabel(uilang.kSubLanguageContentDict['sText_totalRegions'][langIndex])
        self.m_staticText_xipBaseAddr.SetLabel(uilang.kSubLanguageContentDict['sText_xipBaseAddr'][langIndex])
        self.m_staticText_kekSource.SetLabel(uilang.kSubLanguageContentDict['sText_kekSource'][langIndex])
        self.m_staticText_kekData.SetLabel(uilang.kSubLanguageContentDict['sText_kekData'][langIndex])
        self.m_staticText_scrambleAlgo.SetLabel(uilang.kSubLanguageContentDict['sText_scrambleAlgo'][langIndex])
        self.m_staticText_scrambleAlignment.SetLabel(uilang.kSubLanguageContentDict['sText_scrambleAlignment'][langIndex])
        self.m_notebook_region0Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_region0Info'][langIndex])
        self.m_staticText_region0UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxUserKeyData'][langIndex])
        self.m_staticText_region0CounterData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxCounterData'][langIndex])
        self.m_staticText_region0FacStart.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacStart'][langIndex])
        self.m_staticText_region0FacLength.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacLength'][langIndex])
        self.m_staticText_region0Lock.SetLabel(uilang.kSubLanguageContentDict['sText_enginexLock'][langIndex])
        self.m_notebook_region1Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_region1Info'][langIndex])
        self.m_staticText_region1UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxUserKeyData'][langIndex])
        self.m_staticText_region1CounterData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxCounterData'][langIndex])
        self.m_staticText_region1FacStart.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacStart'][langIndex])
        self.m_staticText_region1FacLength.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacLength'][langIndex])
        self.m_staticText_region1Lock.SetLabel(uilang.kSubLanguageContentDict['sText_enginexLock'][langIndex])
        self.m_notebook_region2Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_region2Info'][langIndex])
        self.m_staticText_region2UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxUserKeyData'][langIndex])
        self.m_staticText_region2CounterData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxCounterData'][langIndex])
        self.m_staticText_region2FacStart.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacStart'][langIndex])
        self.m_staticText_region2FacLength.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacLength'][langIndex])
        self.m_staticText_region2Lock.SetLabel(uilang.kSubLanguageContentDict['sText_enginexLock'][langIndex])
        self.m_notebook_region3Info.SetPageText(0, uilang.kSubLanguageContentDict['panel_region3Info'][langIndex])
        self.m_staticText_region3UserKeyData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxUserKeyData'][langIndex])
        self.m_staticText_region3CounterData.SetLabel(uilang.kSubLanguageContentDict['sText_regionxCounterData'][langIndex])
        self.m_staticText_region3FacStart.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacStart'][langIndex])
        self.m_staticText_region3FacLength.SetLabel(uilang.kSubLanguageContentDict['sText_regionxFacLength'][langIndex])
        self.m_staticText_region3Lock.SetLabel(uilang.kSubLanguageContentDict['sText_enginexLock'][langIndex])
        self.m_button_genRandomKek.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_genRandomKek'][langIndex])
        self.m_button_genRandomKey.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_genRandomKey'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_userkeys_cancel'][langIndex])

    def setNecessaryInfo( self, mcuDevice, xipBaseAddr ):
        self.xipBaseAddr = xipBaseAddr
        if self.userKeyCtrlDict['mcu_device'] != mcuDevice:
            self.m_choice_xipBaseAddr.Clear()
            xipBaseAddr = [str(hex(xipBaseAddr))]
            self.m_choice_xipBaseAddr.SetItems(xipBaseAddr)
            self.m_choice_xipBaseAddr.SetSelection(0)
            self._recoverLastSettings()
            self.userKeyCtrlDict['mcu_device'] = mcuDevice

    def _recoverLastSettings ( self ):
        self.m_choice_totalRegions.SetSelection(self.userKeyCtrlDict['total_regions'] - 1)
        if self.userKeyCtrlDict['kek_src'] == RTyyyy_uidef.kUserKeySource_SW_GP2:
            self.m_choice_kekSource.SetSelection(0)
        self.m_textCtrl_kekData.Clear()
        if self.userKeyCmdDict['kek'] != None:
            self.m_textCtrl_kekData.write(self.userKeyCmdDict['kek'])
        self.m_textCtrl_scrambleAlgo.Clear()
        self.m_textCtrl_scrambleAlignment.Clear()
        if self.userKeyCmdDict['scramble_arg'] != None:
            loc = self.userKeyCmdDict['scramble_arg'].find(',', 0)
            self.m_textCtrl_scrambleAlgo.write(self.userKeyCmdDict['scramble_arg'][0:loc])
            self.m_textCtrl_scrambleAlignment.write(self.userKeyCmdDict['scramble_arg'][loc+1:len(self.userKeyCmdDict['scramble_arg'])])
        self._changeTotalRegions()
        for i in range(self.userKeyCtrlDict['total_regions']):
            self._recoverRegionInfo(i)

    def _getTotalRegions( self ):
        self.userKeyCtrlDict['total_regions'] = int(self.m_choice_totalRegions.GetString(self.m_choice_totalRegions.GetSelection()))

    def _getXipBaseAddr( self ):
        self.userKeyCmdDict['base_addr'] = self.m_choice_xipBaseAddr.GetString(self.m_choice_xipBaseAddr.GetSelection())

    def _getKekSource( self ):
        self.userKeyCtrlDict['kek_src'] = self.m_choice_kekSource.GetString(self.m_choice_kekSource.GetSelection())

    def _validateKeyData( self, regionIndex, keyDat ):
        status = False
        if len(keyDat) == 32:
            try:
                val32 = int(keyDat, 16)
                status = True
            except:
                pass
        if not status:
            if regionIndex != None:
                self.popupMsgBox('Illegal input detected! Region %d Key data should be exactly 128bits (32 chars)' %(regionIndex))
            else:
                self.popupMsgBox('Illegal input detected! Kek data should be exactly 128bits (32 chars)')
        return status, keyDat

    def _getKekData( self ):
        validateStatus, self.userKeyCmdDict['kek'] = self._validateKeyData(None, self.m_textCtrl_kekData.GetLineText(0))
        return validateStatus

    def _validateScrambleRange( self, scrambleInfoStr, bitLength ):
        status = False
        val32 = None
        if len(scrambleInfoStr) > 2 and scrambleInfoStr[0:2] == '0x':
            try:
                val32 = long(scrambleInfoStr[2:len(scrambleInfoStr)], 16)
                status = True
            except:
                pass
        else:
            pass
        if not status:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x5000 for Scramble Data')
        else:
            if val32 > (long(1) << bitLength):
                status = False
                self.popupMsgBox('Illegal input detected! Scramble data should be exactly %dbits' %(bitLength))
        return status

    def _getScrambleAlgo( self ):
        self.userKeyCmdDict['scramble_arg'] = None
        scrambleAlgoStr = self.m_textCtrl_scrambleAlgo.GetLineText(0)
        validateStatus = True
        if len(scrambleAlgoStr):
            validateStatus = self._validateScrambleRange(scrambleAlgoStr, 32)
            if validateStatus:
                self.userKeyCmdDict['scramble_arg'] = scrambleAlgoStr
        return validateStatus

    def _getScrambleAlignment( self ):
        validateStatus = True
        if self.userKeyCmdDict['scramble_arg'] != None:
            scrambleAlignmentStr = self.m_textCtrl_scrambleAlignment.GetLineText(0)
            validateStatus = self._validateScrambleRange(scrambleAlignmentStr, 8)
            if validateStatus:
                self.userKeyCmdDict['scramble_arg'] += ',' + scrambleAlignmentStr
            else:
                self.userKeyCmdDict['scramble_arg'] = None
        return validateStatus

    def _getScrambleArg( self ):
        if not self._getScrambleAlgo():
            return False
        if not self._getScrambleAlignment():
            return False
        return True

    def _getUserKeyData( self, regionIndex=0 ):
        if regionIndex == 0:
            userKeyStr = self.m_textCtrl_region0UserKeyData.GetLineText(0)
        elif regionIndex == 1:
            userKeyStr = self.m_textCtrl_region1UserKeyData.GetLineText(0)
        elif regionIndex == 2:
            userKeyStr = self.m_textCtrl_region2UserKeyData.GetLineText(0)
        elif regionIndex == 3:
            userKeyStr = self.m_textCtrl_region3UserKeyData.GetLineText(0)
        else:
            pass
        validateStatus, userKeyStr = self._validateKeyData(regionIndex, userKeyStr)
        if validateStatus:
            if regionIndex == 0:
                self.userKeyCmdDict['otfad_arg'] = '[' + userKeyStr
            else:
                self.userKeyCmdDict['otfad_arg'] += ',[' + userKeyStr
        return validateStatus

    def _validateCounterData( self, regionIndex, counterDat ):
        status = False
        if len(counterDat) == 16:
            try:
                val32 = int(counterDat, 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! Region %d Counter data should be exactly 64bits (16 chars)' %(regionIndex))
        return status, counterDat

    def _getCounterData( self, regionIndex=0 ):
        if regionIndex == 0:
            counterStr = self.m_textCtrl_region0CounterData.GetLineText(0)
        elif regionIndex == 1:
            counterStr = self.m_textCtrl_region1CounterData.GetLineText(0)
        elif regionIndex == 2:
            counterStr = self.m_textCtrl_region2CounterData.GetLineText(0)
        elif regionIndex == 3:
            counterStr = self.m_textCtrl_region3CounterData.GetLineText(0)
        else:
            pass
        validateStatus, counterStr = self._validateCounterData(regionIndex, counterStr)
        if validateStatus:
            self.userKeyCmdDict['otfad_arg'] += ',' + counterStr
        return validateStatus

    def _validateRegionRange( self, regionInfoStr ):
        status = False
        val32 = None
        if len(regionInfoStr) > 2 and regionInfoStr[0:2] == '0x':
            try:
                val32 = int(regionInfoStr[2:len(regionInfoStr)], 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox('Illegal input detected! You should input like this format: 0x5000 for Protected Region')
        return status, val32

    def _getRegionRange( self, regionIndex=0 ):
        if regionIndex == 0:
            validateStatus, self.regionFacStart[0] = self._validateRegionRange(self.m_textCtrl_region0FacStart.GetLineText(0))
            if validateStatus:
                if self.regionFacStart[0] < self.xipBaseAddr + RTyyyy_gendef.kIvtOffset_NOR:
                    self.popupMsgBox('Region 0 Protected region start address shouldn\'t less than 0x%x' %(self.xipBaseAddr + RTyyyy_gendef.kIvtOffset_NOR))
                    return False
            else:
                return False
            validateStatus, self.regionFacLength[0] = self._validateRegionRange(self.m_textCtrl_region0FacLength.GetLineText(0))
            if validateStatus:
                if self.regionFacLength[0] % RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad != 0:
                    self.popupMsgBox('Region 0 Protected region length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad / 0x400))
                    return False
            else:
                return False
            self.userKeyCmdDict['otfad_arg'] += ',' + self.m_textCtrl_region0FacStart.GetLineText(0) + ',' + self.m_textCtrl_region0FacLength.GetLineText(0) + ']'
        elif regionIndex == 1:
            validateStatus, self.regionFacStart[1] = self._validateRegionRange(self.m_textCtrl_region1FacStart.GetLineText(0))
            if validateStatus:
                if self.regionFacStart[1] < self.regionFacStart[0] + self.regionFacLength[0]:
                    self.popupMsgBox('Region 1 Protected region start address shouldn\'t less than Region 0 Protected region end address 0x%x' %(self.regionFacStart[0] + self.regionFacLength[0]))
                    return False
            else:
                return False
            validateStatus, self.regionFacLength[1] = self._validateRegionRange(self.m_textCtrl_region1FacLength.GetLineText(0))
            if validateStatus:
                if self.regionFacLength[1] % RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad != 0:
                    self.popupMsgBox('Region 1 Protected region length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad / 0x400))
                    return False
            else:
                return False
            self.userKeyCmdDict['otfad_arg'] += ',' + self.m_textCtrl_region1FacStart.GetLineText(0) + ',' + self.m_textCtrl_region1FacLength.GetLineText(0) + ']'
        elif regionIndex == 2:
            validateStatus, self.regionFacStart[2] = self._validateRegionRange(self.m_textCtrl_region2FacStart.GetLineText(0))
            if validateStatus:
                if self.regionFacStart[2] < self.regionFacStart[1] + self.regionFacLength[1]:
                    self.popupMsgBox('Region 2 Protected region start address shouldn\'t less than Region 1 Protected region end address 0x%x' %(self.regionFacStart[1] + self.regionFacLength[1]))
                    return False
            else:
                return False
            validateStatus, self.regionFacLength[2] = self._validateRegionRange(self.m_textCtrl_region2FacLength.GetLineText(0))
            if validateStatus:
                if self.regionFacLength[2] % RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad != 0:
                    self.popupMsgBox('Region 2 Protected region length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad / 0x400))
                    return False
            else:
                return False
            self.userKeyCmdDict['otfad_arg'] += ',' + self.m_textCtrl_region2FacStart.GetLineText(0) + ',' + self.m_textCtrl_region2FacLength.GetLineText(0) + ']'
        elif regionIndex == 3:
            validateStatus, self.regionFacStart[3] = self._validateRegionRange(self.m_textCtrl_region3FacStart.GetLineText(0))
            if validateStatus:
                if self.regionFacStart[3] < self.regionFacStart[2] + self.regionFacLength[2]:
                    self.popupMsgBox('Region 3 Protected region start address shouldn\'t less than Region 2 Protected region end address 0x%x' %(self.regionFacStart[2] + self.regionFacLength[2]))
                    return False
            else:
                return False
            validateStatus, self.regionFacLength[3] = self._validateRegionRange(self.m_textCtrl_region3FacLength.GetLineText(0))
            if validateStatus:
                if self.regionFacLength[3] % RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad != 0:
                    self.popupMsgBox('Region 3 Protected region length should be aligned with %dKB' %(RTyyyy_gendef.kSecFacRegionAlignedUnit_Otfad / 0x400))
                    return False
            else:
                return False
            self.userKeyCmdDict['otfad_arg'] += ',' + self.m_textCtrl_region3FacStart.GetLineText(0) + ',' + self.m_textCtrl_region3FacLength.GetLineText(0) + ']'
        else:
            pass
        return True

    def _getOtfadArg( self, regionIndex=0 ):
        if not self._getUserKeyData(regionIndex):
            return False
        if not self._getCounterData(regionIndex):
            return False
        status = self._getRegionRange(regionIndex)
        if not status:
            self.regionFacStart = [None] * RTyyyy_uidef.kMaxFacRegionCount_Otfad
            self.regionFacLength = [None] * RTyyyy_uidef.kMaxFacRegionCount_Otfad
            return False
        return True

    def _getRegionLock( self, regionIndex=0 ):
        if regionIndex == 0:
            self.userKeyCmdDict['otfad_ctx_lock'] = str(self.m_choice_region0Lock.GetSelection())
        elif regionIndex == 1:
            self.userKeyCmdDict['otfad_ctx_lock'] += ',' + str(self.m_choice_region1Lock.GetSelection())
        elif regionIndex == 2:
            self.userKeyCmdDict['otfad_ctx_lock'] += ',' + str(self.m_choice_region2Lock.GetSelection())
        elif regionIndex == 3:
            self.userKeyCmdDict['otfad_ctx_lock'] += ',' + str(self.m_choice_region3Lock.GetSelection())
        else:
            pass

    def _getRegionInfo( self, regionIndex=0 ):
        if not self._getOtfadArg(regionIndex):
            return False
        self._getRegionLock(regionIndex)
        return True

    def _recoverRegionArg( self, regionIndex ):
        region_otfad_arg = ''
        locStart = 0
        locEnd = 0
        for i in range(regionIndex + 1):
            locStart = self.userKeyCmdDict['otfad_arg'].find('[', locEnd)
            locEnd = self.userKeyCmdDict['otfad_arg'].find(']', locStart)
        region_otfad_arg = self.userKeyCmdDict['otfad_arg'][locStart:locEnd+1]
        locStart = region_otfad_arg.find(',', 0)
        locEnd = locStart
        userKeyData = region_otfad_arg[1:locEnd]
        locEnd = region_otfad_arg.find(',', locEnd + 1)
        counterData = region_otfad_arg[locStart+1:locEnd]
        locStart = locEnd
        locEnd = region_otfad_arg.find(',', locStart + 1)
        facStartStr = region_otfad_arg[locStart+1:locEnd]
        facLengthStr = region_otfad_arg[locEnd+1:len(region_otfad_arg)-1]
        if regionIndex == 0:
            self.m_textCtrl_region0UserKeyData.Clear()
            self.m_textCtrl_region0UserKeyData.write(userKeyData)
            self.m_textCtrl_region0CounterData.Clear()
            self.m_textCtrl_region0CounterData.write(counterData)
            self.m_textCtrl_region0FacStart.Clear()
            self.m_textCtrl_region0FacStart.write(facStartStr)
            self.m_textCtrl_region0FacLength.Clear()
            self.m_textCtrl_region0FacLength.write(facLengthStr)
        elif regionIndex == 1:
            self.m_textCtrl_region1UserKeyData.Clear()
            self.m_textCtrl_region1UserKeyData.write(userKeyData)
            self.m_textCtrl_region1CounterData.Clear()
            self.m_textCtrl_region1CounterData.write(counterData)
            self.m_textCtrl_region1FacStart.Clear()
            self.m_textCtrl_region1FacStart.write(facStartStr)
            self.m_textCtrl_region1FacLength.Clear()
            self.m_textCtrl_region1FacLength.write(facLengthStr)
        elif regionIndex == 2:
            self.m_textCtrl_region2UserKeyData.Clear()
            self.m_textCtrl_region2UserKeyData.write(userKeyData)
            self.m_textCtrl_region2CounterData.Clear()
            self.m_textCtrl_region2CounterData.write(counterData)
            self.m_textCtrl_region2FacStart.Clear()
            self.m_textCtrl_region2FacStart.write(facStartStr)
            self.m_textCtrl_region2FacLength.Clear()
            self.m_textCtrl_region2FacLength.write(facLengthStr)
        elif regionIndex == 3:
            self.m_textCtrl_region3UserKeyData.Clear()
            self.m_textCtrl_region3UserKeyData.write(userKeyData)
            self.m_textCtrl_region3CounterData.Clear()
            self.m_textCtrl_region3CounterData.write(counterData)
            self.m_textCtrl_region3FacStart.Clear()
            self.m_textCtrl_region3FacStart.write(facStartStr)
            self.m_textCtrl_region3FacLength.Clear()
            self.m_textCtrl_region3FacLength.write(facLengthStr)
        else:
            pass

    def _recoverRegionInfo( self, regionIndex ):
        self._recoverRegionArg(regionIndex)
        lock = int(self.userKeyCmdDict['otfad_ctx_lock'][regionIndex * 2])
        if regionIndex == 0:
            self.m_choice_region0Lock.SetSelection(lock)
        elif regionIndex == 1:
            self.m_choice_region1Lock.SetSelection(lock)
        elif regionIndex == 2:
            self.m_choice_region2Lock.SetSelection(lock)
        elif regionIndex == 3:
            self.m_choice_region3Lock.SetSelection(lock)
        else:
            pass

    def _updateRegionInfoField ( self, regionIndex=0, isRegionEnabled=False ):
        if regionIndex == 0:
            if isRegionEnabled:
                self.m_textCtrl_region0UserKeyData.Enable( True )
                self.m_textCtrl_region0CounterData.Enable( True )
                self.m_textCtrl_region0FacStart.Enable( True )
                self.m_textCtrl_region0FacLength.Enable( True )
                self.m_choice_region0Lock.Enable( True )
            else:
                self.m_textCtrl_region0UserKeyData.Enable( False )
                self.m_textCtrl_region0CounterData.Enable( False )
                self.m_textCtrl_region0FacStart.Enable( False )
                self.m_textCtrl_region0FacLength.Enable( False )
                self.m_choice_region0Lock.Enable( False )
        elif regionIndex == 1:
            if isRegionEnabled:
                self.m_textCtrl_region1UserKeyData.Enable( True )
                self.m_textCtrl_region1CounterData.Enable( True )
                self.m_textCtrl_region1FacStart.Enable( True )
                self.m_textCtrl_region1FacLength.Enable( True )
                self.m_choice_region1Lock.Enable( True )
            else:
                self.m_textCtrl_region1UserKeyData.Enable( False )
                self.m_textCtrl_region1CounterData.Enable( False )
                self.m_textCtrl_region1FacStart.Enable( False )
                self.m_textCtrl_region1FacLength.Enable( False )
                self.m_choice_region1Lock.Enable( False )
        elif regionIndex == 2:
            if isRegionEnabled:
                self.m_textCtrl_region2UserKeyData.Enable( True )
                self.m_textCtrl_region2CounterData.Enable( True )
                self.m_textCtrl_region2FacStart.Enable( True )
                self.m_textCtrl_region2FacLength.Enable( True )
                self.m_choice_region2Lock.Enable( True )
            else:
                self.m_textCtrl_region2UserKeyData.Enable( False )
                self.m_textCtrl_region2CounterData.Enable( False )
                self.m_textCtrl_region2FacStart.Enable( False )
                self.m_textCtrl_region2FacLength.Enable( False )
                self.m_choice_region2Lock.Enable( False )
        elif regionIndex == 3:
            if isRegionEnabled:
                self.m_textCtrl_region3UserKeyData.Enable( True )
                self.m_textCtrl_region3CounterData.Enable( True )
                self.m_textCtrl_region3FacStart.Enable( True )
                self.m_textCtrl_region3FacLength.Enable( True )
                self.m_choice_region3Lock.Enable( True )
            else:
                self.m_textCtrl_region3UserKeyData.Enable( False )
                self.m_textCtrl_region3CounterData.Enable( False )
                self.m_textCtrl_region3FacStart.Enable( False )
                self.m_textCtrl_region3FacLength.Enable( False )
                self.m_choice_region3Lock.Enable( False )
        else:
            pass

    def _changeTotalRegions( self ):
        self._getTotalRegions()
        self._updateRegionInfoField(0, False)
        self._updateRegionInfoField(1, False)
        self._updateRegionInfoField(2, False)
        self._updateRegionInfoField(3, False)
        for i in range(self.userKeyCtrlDict['total_regions']):
            self._updateRegionInfoField(i, True)

    def callbackChangeTotalRegions( self, event ):
        self._changeTotalRegions()

    def _genRandomUserKeyData( self ):
        userKey = ''
        for i in range(32):
            userKey += random.choice('0123456789abcdef')
        return userKey

    def callbackGenRandomKek( self, event ):
        self.m_textCtrl_kekData.Clear()
        self.m_textCtrl_kekData.write(self._genRandomUserKeyData())

    def callbackGenRandomUserKey( self, event ):
        if self.userKeyCtrlDict['total_regions'] >= 1:
            self.m_textCtrl_region0UserKeyData.Clear()
            self.m_textCtrl_region0UserKeyData.write(self._genRandomUserKeyData())
        if self.userKeyCtrlDict['total_regions'] >= 2:
            self.m_textCtrl_region1UserKeyData.Clear()
            self.m_textCtrl_region1UserKeyData.write(self._genRandomUserKeyData())
        if self.userKeyCtrlDict['total_regions'] >= 3:
            self.m_textCtrl_region2UserKeyData.Clear()
            self.m_textCtrl_region2UserKeyData.write(self._genRandomUserKeyData())
        if self.userKeyCtrlDict['total_regions'] >= 4:
            self.m_textCtrl_region3UserKeyData.Clear()
            self.m_textCtrl_region3UserKeyData.write(self._genRandomUserKeyData())

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def callbackOk( self, event ):
        self._getTotalRegions()
        for i in range(self.userKeyCtrlDict['total_regions']):
            if not self._getRegionInfo(i):
                return
        self._getXipBaseAddr()
        self._getKekSource()
        if not self._getKekData():
            return
        if not self._getScrambleArg():
            return
        self.userKeyCtrlDict['hw_eng'] = 'otfad'
        #print 'base_addr=' + self.userKeyCmdDict['base_addr']
        #print 'kek=' + self.userKeyCmdDict['kek']
        #print 'otfad_arg=' + self.userKeyCmdDict['otfad_arg']
        #print 'scramble_arg=' + self.userKeyCmdDict['scramble_arg']
        #print 'otfad_ctx_lock=' + self.userKeyCmdDict['otfad_ctx_lock']
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
