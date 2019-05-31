#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import RT10yy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from gen import gencore
from run import RT10yy_rundef
from run import rundef
from fuse import RT10yy_fusedef

class secBootRT10yyUi(gencore.secBootGen):

    def __init__(self, parent):
        gencore.secBootGen.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.RT10yy_initUi()

    def RT10yy_initUi( self ):
        self.isNandDevice = False
        self.isSdmmcCard = False
        self.sbEnableBootDeviceMagic = None
        self.sbAccessBootDeviceMagic = None
        self._RT10yy_initTargetSetupValue()
        self.RT10yy_setTargetSetupValue()

        self.secureBootType = None
        self.keyStorageRegion = None
        self.isCertEnabledForBee = None
        self._RT10yy_initSecureBootSeqValue()
        self._RT10yy_initSecureBootSeqColor()

        self.RT10yy_setLanguage()

    def _RT10yy_initTargetSetupValue( self ):
        self.m_choice_mcuDevice.Clear()
        self.m_choice_bootDevice.Clear()
        self.m_choice_mcuDevice.SetItems(RT10yy_uidef.kMcuDevice_Latest)
        self.m_choice_bootDevice.SetItems(RT10yy_uidef.kBootDevice_Latest)
        totalSel = self.m_choice_mcuDevice.GetCount()
        if self.toolCommDict['mcuDevice'] < totalSel:
            self.m_choice_mcuDevice.SetSelection(self.toolCommDict['mcuDevice'])
        else:
            self.m_choice_mcuDevice.SetSelection(0)
        totalSel = self.m_choice_bootDevice.GetCount()
        if self.toolCommDict['bootDevice'] < totalSel:
            self.m_choice_bootDevice.SetSelection(self.toolCommDict['bootDevice'])
        else:
            self.m_choice_bootDevice.SetSelection(0)

    def _setFlexspiNorDeviceForEvkBoard( self ):
        try:
            flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_ISSI_IS25LP064A
            flexspiNorOpt1 = 0x0
            flexspiDeviceModel = self.tgt.flexspiNorDevice
            if flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_ISSI_IS25LP064A:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_ISSI_IS25LP064A
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_ISSI_IS26KS512S:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_ISSI_IS26KS512S
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_MXIC_MX25UM51245G:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_MXIC_MX25UM51245G
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_MXIC_MX25UM51345G:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_MXIC_MX25UM51345G
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_Micron_MT35X:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_Micron_MT35X
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_Adesto_AT25SF128A:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_Adesto_AT25SF128A
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_Adesto_ATXP032:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_Adesto_ATXP032
            elif flexspiDeviceModel == RT10yy_uidef.kFlexspiNorDevice_Cypress_S26KS512S:
                flexspiNorOpt0 = RT10yy_uidef.kFlexspiNorOpt0_Cypress_S26KS512S
            else:
                pass
            uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_FlexspiNor, flexspiNorOpt0, flexspiNorOpt1, flexspiDeviceModel)
        except:
            pass

    def _RT10yy_refreshBootDeviceList( self ):
        if self.tgt.availableBootDevices != None:
            self.m_choice_bootDevice.Clear()
            self.m_choice_bootDevice.SetItems(self.tgt.availableBootDevices)
            retSel = self.m_choice_bootDevice.FindString(self.bootDevice)
            if retSel != wx.NOT_FOUND:
                self.m_choice_bootDevice.SetSelection(retSel)
            else:
                self.m_choice_bootDevice.SetSelection(0)

    def RT10yy_setTargetSetupValue( self ):
        self.showPageInMainBootSeqWin(RT10yy_uidef.kPageIndex_ImageGenerationSequence)
        self.mcuDevice = self.m_choice_mcuDevice.GetString(self.m_choice_mcuDevice.GetSelection())
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['mcuDevice'] = self.m_choice_mcuDevice.GetSelection()
        self.RT10yy_createMcuTarget()
        self._RT10yy_refreshBootDeviceList()
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['bootDevice'] = self.m_choice_bootDevice.GetSelection()
        if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'flexspinor'
            self.sbAccessBootDeviceMagic = ''
            self._setFlexspiNorDeviceForEvkBoard()
        elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'semcnor'
            self.sbAccessBootDeviceMagic = ''
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            self.isNandDevice = False
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'spieeprom'
            self.sbAccessBootDeviceMagic = 'spieeprom'
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNand:
            self.isNandDevice = True
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'flexspinand'
            self.sbAccessBootDeviceMagic = 'flexspinand'
        elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            self.isNandDevice = True
            self.isSdmmcCard = False
            self.sbEnableBootDeviceMagic = 'semcnand'
            self.sbAccessBootDeviceMagic = 'semcnand'
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
            self.isNandDevice = True
            self.isSdmmcCard = True
            self.sbEnableBootDeviceMagic = 'sdcard'
            self.sbAccessBootDeviceMagic = 'sdcard'
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            self.isNandDevice = True
            self.isSdmmcCard = True
            self.sbEnableBootDeviceMagic = 'mmccard'
            self.sbAccessBootDeviceMagic = 'mmccard'
        else:
            pass

    def _RT10yy_initSecureBootSeqValue( self ):
        self.m_choice_secureBootType.Clear()
        self.m_choice_secureBootType.SetItems(RT10yy_uidef.kSecureBootType_Latest)
        totalSel = self.m_choice_secureBootType.GetCount()
        if self.toolCommDict['secBootType'] < totalSel:
            self.m_choice_secureBootType.SetSelection(self.toolCommDict['secBootType'])
        else:
            self.m_choice_secureBootType.SetSelection(0)
        self.m_textCtrl_serial.Clear()
        self.m_textCtrl_serial.write(self.toolCommDict['certSerial'])
        self.m_textCtrl_keyPass.Clear()
        self.m_textCtrl_keyPass.write(self.toolCommDict['certKeyPass'])
        if self.toolCommDict['appFilename'] != None:
            self.m_filePicker_appPath.SetPath(self.toolCommDict['appFilename'])
        self.m_choice_appFormat.SetSelection(self.toolCommDict['appFormat'])
        self._setUserBinaryBaseField()
        self.m_textCtrl_appBaseAddr.Clear()
        self.m_textCtrl_appBaseAddr.write(self.toolCommDict['appBinBaseAddr'])
        self.m_choice_keyStorageRegion.SetSelection(self.toolCommDict['keyStoreRegion'])
        self.m_choice_enableCertForBee.SetSelection(self.toolCommDict['certOptForBee'])

    def _RT10yy_initSecureBootSeqColor ( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
        self.RT10yy_setSecureBootSeqColor()

    def invalidateStepButtonColor( self, stepName, excuteResult ):
        invalidColor = None
        allInOneSoundEffect = None
        stepSoundEffect = None
        if excuteResult:
            invalidColor = uidef.kBootSeqColor_Invalid
            allInOneSoundEffect = uidef.kSoundEffectFilename_Success
            stepSoundEffect = uidef.kSoundEffectFilename_Progress
        else:
            invalidColor = uidef.kBootSeqColor_Failed
            allInOneSoundEffect = uidef.kSoundEffectFilename_Failure
        if stepName == RT10yy_uidef.kSecureBootSeqStep_AllInOne:
            self.m_button_allInOneAction.SetBackgroundColour( invalidColor )
            self.soundEffectFilenameForTask = allInOneSoundEffect
        else:
            if stepName == RT10yy_uidef.kSecureBootSeqStep_GenCert:
                self.m_button_genCert.SetBackgroundColour( invalidColor )
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_GenImage:
                self.m_button_genImage.SetBackgroundColour( invalidColor )
                if excuteResult and self.secureBootType != RT10yy_uidef.kSecureBootType_BeeCrypto:
                    self.showPageInMainBootSeqWin(RT10yy_uidef.kPageIndex_ImageLoadingSequence)
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_PrepBee:
                self.m_button_prepBee.SetBackgroundColour( invalidColor )
                if excuteResult:
                    self.showPageInMainBootSeqWin(RT10yy_uidef.kPageIndex_ImageLoadingSequence)
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_ProgSrk:
                self.m_button_progSrk.SetBackgroundColour( invalidColor )
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_OperBee:
                self.m_button_operBee.SetBackgroundColour( invalidColor )
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_FlashImage:
                self.m_button_flashImage.SetBackgroundColour( invalidColor )
            elif stepName == RT10yy_uidef.kSecureBootSeqStep_ProgDek:
                self.m_button_progDek.SetBackgroundColour( invalidColor )
            else:
                pass
            if stepSoundEffect != None:
                self.playSoundEffect(stepSoundEffect)
        self.Refresh()

    def RT10yy_setSecureBootButtonColor( self, needToPlaySound=True ):
        activeColor = None
        optionalColor = None
        setEnable = None
        if self.isToolRunAsEntryMode:
            activeColor = uidef.kBootSeqColor_Invalid
            optionalColor = uidef.kBootSeqColor_Invalid
        else:
            activeColor = uidef.kBootSeqColor_Active
            optionalColor = uidef.kBootSeqColor_Optional
        setEnable = not self.isToolRunAsEntryMode
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        if self.secureBootType == RT10yy_uidef.kSecureBootType_Development:
            self.m_button_genImage.Enable( setEnable )
            self.m_button_genImage.SetBackgroundColour( activeColor )
            self.m_button_flashImage.Enable( setEnable )
            self.m_button_flashImage.SetBackgroundColour( activeColor )
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
            self.m_button_genCert.Enable( setEnable )
            self.m_button_genCert.SetBackgroundColour( activeColor )
            self.m_button_genImage.Enable( setEnable )
            self.m_button_genImage.SetBackgroundColour( activeColor )
            self.m_button_progSrk.Enable( setEnable )
            self.m_button_progSrk.SetBackgroundColour( activeColor )
            self.m_button_flashImage.Enable( setEnable )
            self.m_button_flashImage.SetBackgroundColour( activeColor )
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
            if (self.bootDevice != RT10yy_uidef.kBootDevice_FlexspiNor and self.bootDevice != RT10yy_uidef.kBootDevice_SemcNor) or \
               self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab:
                self.m_button_genCert.Enable( setEnable )
                self.m_button_genCert.SetBackgroundColour( activeColor )
                self.m_button_genImage.Enable( setEnable )
                self.m_button_genImage.SetBackgroundColour( activeColor )
                self.m_button_progSrk.Enable( setEnable )
                self.m_button_progSrk.SetBackgroundColour( activeColor )
                self.m_button_flashImage.Enable( setEnable )
                self.m_button_flashImage.SetBackgroundColour( activeColor )
                self.m_button_progDek.Enable( setEnable )
                self.m_button_progDek.SetBackgroundColour( activeColor )
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
            if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
                if self.isCertEnabledForBee:
                    self.m_button_genCert.Enable( setEnable )
                    self.m_button_genCert.SetBackgroundColour( optionalColor )
                    self.m_button_progSrk.Enable( setEnable )
                    self.m_button_progSrk.SetBackgroundColour( optionalColor )
                if self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                    self.m_button_prepBee.Enable( setEnable )
                    self.m_button_prepBee.SetBackgroundColour( activeColor )
                elif self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                    self.m_button_prepBee.Enable( setEnable )
                    self.m_button_prepBee.SetBackgroundColour( activeColor )
                    self.m_button_operBee.Enable( setEnable )
                    self.m_button_operBee.SetBackgroundColour( activeColor )
                else:
                    pass
                self.m_button_genImage.Enable( setEnable )
                self.m_button_genImage.SetBackgroundColour( activeColor )
                self.m_button_flashImage.Enable( setEnable )
                self.m_button_flashImage.SetBackgroundColour( activeColor )
        else:
            pass
        self.m_button_allInOneAction.Enable( True )
        self.m_button_allInOneAction.SetBackgroundColour( uidef.kBootSeqColor_Active )
        self.Refresh()
        if needToPlaySound:
            self.soundEffectFilenameForTask = uidef.kSoundEffectFilename_Restart

    def _getImgName( self ):
        memType = ''
        hasDcd = ''
        if self.isNandDevice:
            if self.isSdmmcCard:
                memType = 'sdmmc_'
            else:
                memType = 'nand_'
        else:
            memType = 'nor_'
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            hasDcd = 'dcd_'
        return memType, hasDcd

    def showPageInMainBootSeqWin(self, pageIndex ):
        if pageIndex != self.m_notebook_imageSeq.GetSelection():
            self.m_notebook_imageSeq.SetSelection(pageIndex)

    def RT10yy_setSecureBootSeqColor( self , needToPlaySound=True ):
        self.hasDynamicLableBeenInit = True
        self.showPageInMainBootSeqWin(RT10yy_uidef.kPageIndex_ImageGenerationSequence)
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.toolCommDict['secBootType'] = self.m_choice_secureBootType.GetSelection()
        self.resetSecureBootSeqColor()
        self.m_button_genCert.SetLabel(uilang.kMainLanguageContentDict['button_genCert'][self.languageIndex])
        self.m_button_progSrk.SetLabel(uilang.kMainLanguageContentDict['button_progSrk'][self.languageIndex])
        self.m_button_operBee.SetLabel(uilang.kMainLanguageContentDict['button_operBee'][self.languageIndex])
        self.m_button_progDek.SetLabel(uilang.kMainLanguageContentDict['button_progDek'][self.languageIndex])
        if self.secureBootType == RT10yy_uidef.kSecureBootType_Development:
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_u'][self.languageIndex])
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType, strHasDcd = self._getImgName()
            imgPath = "../img/" + strMemType + "image_" + strHasDcd + "unsigned.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_u'][self.languageIndex])
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
            self.m_panel_doAuth1_certInput.Enable( True )
            self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_panel_doAuth2_certFmt.Enable( True )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_s'][self.languageIndex])
            self.m_panel_progSrk1_showSrk.Enable( True )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType, strHasDcd = self._getImgName()
            imgPath = "../img/" + strMemType + "image_" + strHasDcd + "signed.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_s'][self.languageIndex])
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
            if (self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor) and \
               (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
                self.resetSecureBootSeqColor()
            else:
                self.m_panel_doAuth1_certInput.Enable( True )
                self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
                self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
                self.m_panel_doAuth2_certFmt.Enable( True )
                self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage1_browseApp.Enable( True )
                self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage2_habCryptoAlgo.Enable( True )
                self.m_panel_genImage2_habCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_se'][self.languageIndex])
                self.m_panel_progSrk1_showSrk.Enable( True )
                self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_flashImage1_showImage.Enable( True )
                self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
                strMemType, strHasDcd = self._getImgName()
                imgPath = "../img/" + strMemType + "image_" + strHasDcd + "signed_hab_encrypted_nodek.png"
                self.showImageLayout(imgPath.encode('utf-8'))
                self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_e'][self.languageIndex])
                self.m_panel_progDek1_showHabDek.Enable( True )
                self.m_panel_progDek1_showHabDek.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
            if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
                self.m_panel_genImage1_browseApp.Enable( True )
                self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_genImage3_enableCertForBee.Enable( True )
                self.m_panel_genImage3_enableCertForBee.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.setKeyStorageRegionColor()
                self.setBeeCertColor()
                self.m_panel_flashImage1_showImage.Enable( True )
                self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            else:
                self.resetSecureBootSeqColor()
        else:
            pass
        self.RT10yy_setSecureBootButtonColor(needToPlaySound)
        self.Refresh()

    def updateImgPictureAfterFlashDek( self ):
        strMemType, strHasDcd = self._getImgName()
        imgPath = "../img/" + strMemType + "image_" + strHasDcd + "signed_hab_encrypted.png"
        self.showImageLayout(imgPath.encode('utf-8'))

    def getSerialAndKeypassContent( self ):
        serialContent = self.m_textCtrl_serial.GetLineText(0)
        keypassContent = self.m_textCtrl_keyPass.GetLineText(0)
        self.toolCommDict['certSerial'] = serialContent
        self.toolCommDict['certKeyPass'] = keypassContent
        return serialContent, keypassContent

    def setBeeCertColor( self ):
        txt = self.m_choice_enableCertForBee.GetString(self.m_choice_enableCertForBee.GetSelection())
        self.toolCommDict['certOptForBee'] = self.m_choice_enableCertForBee.GetSelection()
        strMemType, strHasDcd = self._getImgName()
        imgPath = ""
        if txt == 'No':
            self.isCertEnabledForBee = False
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_u'][self.languageIndex])
            imgPath = "../img/nor_image_" + strHasDcd + "unsigned_bee_encrypted.png"
        elif txt == 'Yes':
            self.isCertEnabledForBee = True
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_s'][self.languageIndex])
            imgPath = "../img/nor_image_" + strHasDcd + "signed_bee_encrypted.png"
        else:
            pass
        self.showImageLayout(imgPath.encode('utf-8'))
        self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_e'][self.languageIndex])
        self.resetCertificateColor()
        if self.isCertEnabledForBee:
            activeColor = None
            if self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                activeColor = uidef.kBootSeqColor_Active
            elif self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                activeColor = uidef.kBootSeqColor_Optional
            else:
                pass
            self.m_panel_doAuth1_certInput.Enable( True )
            self.m_panel_doAuth1_certInput.SetBackgroundColour( activeColor )
            self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
            self.m_panel_doAuth2_certFmt.Enable( True )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( activeColor )
            self.m_button_genCert.Enable( True )
            self.m_button_genCert.SetBackgroundColour( activeColor )
            self.m_panel_progSrk1_showSrk.Enable( True )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( activeColor )
            self.m_button_progSrk.Enable( True )
            self.m_button_progSrk.SetBackgroundColour( activeColor )
        self.Refresh()

    def setKeyStorageRegionColor( self ):
        self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
        self.toolCommDict['keyStoreRegion'] = self.m_choice_keyStorageRegion.GetSelection()
        self.resetKeyStorageRegionColor()
        self.m_panel_prepBee1_beeKeyRegion.Enable( True )
        self.m_panel_prepBee1_beeKeyRegion.SetBackgroundColour( uidef.kBootSeqColor_Active )
        self.m_panel_prepBee2_beeCryptoAlgo.Enable( True )
        self.m_panel_prepBee2_beeCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
        if self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FixedOtpmkKey:
            self.m_choice_enableCertForBee.Clear()
            self.m_choice_enableCertForBee.SetItems(['Yes'])
            self.m_choice_enableCertForBee.SetSelection(0)
            self.setBeeCertColor()
            self.m_choice_availBeeEngines.Clear()
            self.m_choice_availBeeEngines.SetItems(['1'])
            self.m_choice_availBeeEngines.SetSelection(0)
            self.m_button_prepBee.Enable( True )
            self.m_button_prepBee.SetLabel(uilang.kMainLanguageContentDict['button_prepBee_p'][self.languageIndex])
            self.m_button_prepBee.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
            enableCertForBeeTxt = self.m_choice_enableCertForBee.GetString(self.m_choice_enableCertForBee.GetSelection())
            self.m_choice_enableCertForBee.Clear()
            self.m_choice_enableCertForBee.SetItems(['No', 'Yes'])
            self.m_choice_enableCertForBee.SetSelection(self.m_choice_enableCertForBee.FindString(enableCertForBeeTxt))
            self.setBeeCertColor()
            self.m_choice_availBeeEngines.Clear()
            self.m_choice_availBeeEngines.SetItems(['2'])
            self.m_choice_availBeeEngines.SetSelection(0)
            self.m_button_prepBee.Enable( True )
            self.m_button_prepBee.SetLabel(uilang.kMainLanguageContentDict['button_prepBee_e'][self.languageIndex])
            self.m_button_prepBee.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operBee1_beeKeyInfo.Enable( True )
            self.m_panel_operBee1_beeKeyInfo.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operBee2_showGp4Dek.Enable( True )
            self.m_panel_operBee2_showGp4Dek.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_operBee3_showSwgp2Dek.Enable( True )
            self.m_panel_operBee3_showSwgp2Dek.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_operBee.Enable( True )
            self.m_button_operBee.SetBackgroundColour( uidef.kBootSeqColor_Active )
        else:
            pass
        self.Refresh()

    def printSrkData( self, srkStr ):
        self.m_textCtrl_srk256bit.write(srkStr + "\n")

    def clearSrkData( self ):
        self.m_textCtrl_srk256bit.Clear()

    def printHabDekData( self, dekStr ):
        self.m_textCtrl_habDek128bit.write(dekStr + "\n")

    def clearHabDekData( self ):
        self.m_textCtrl_habDek128bit.Clear()

    def printOtpmkDekData( self, dekStr ):
        #self.m_textCtrl_otpmkDek128bit.write(dekStr + "\n")
        pass

    def clearOtpmkDekData( self ):
        #self.m_textCtrl_otpmkDek128bit.Clear()
        pass

    def printGp4DekData( self, dekStr ):
        self.m_textCtrl_gp4Dek128bit.write(dekStr + "\n")

    def clearGp4DekData( self ):
        self.m_textCtrl_gp4Dek128bit.Clear()

    def printSwGp2DekData( self, dekStr ):
        self.m_textCtrl_swgp2Dek128bit.write(dekStr + "\n")

    def clearSwGp2DekData( self ):
        self.m_textCtrl_swgp2Dek128bit.Clear()

    def getComMemStartAddress( self ):
        return self.getVal32FromHexText(self.m_textCtrl_memStart.GetLineText(0))

    def getComMemByteLength( self ):
        return self.getVal32FromHexText(self.m_textCtrl_memLength.GetLineText(0))

    def getComMemBinFile( self ):
        memBinFile = self.m_filePicker_memBinFile.GetPath()
        return memBinFile.encode('utf-8').encode("gbk")

    def needToSaveReadbackImageData( self ):
        return self.m_checkBox_saveImageData.GetValue()

    def getImageDataFileToSave( self ):
        savedBinFile = self.m_filePicker_savedBinFile.GetPath()
        return savedBinFile.encode('utf-8').encode("gbk")

    def setImageDataFilePath( self, filePath ):
        self.m_filePicker_savedBinFile.SetPath(filePath)

    def printMem( self , memStr, strColor=RT10yy_uidef.kMemBlockColor_Padding ):
        self.m_textCtrl_bootDeviceMem.SetDefaultStyle(wx.TextAttr(strColor, RT10yy_uidef.kMemBlockColor_Background))
        self.m_textCtrl_bootDeviceMem.AppendText(memStr + "\n")

    def clearMem( self ):
        self.m_textCtrl_bootDeviceMem.Clear()

    def showImageLayout( self , imgPath ):
        self.m_bitmap_bootableImage.SetBitmap(wx.Bitmap( imgPath, wx.BITMAP_TYPE_ANY ))

    def updateFuseRegionField( self ):
        color = None
        if self.isToolRunAsEntryMode:
            color = wx.SYS_COLOUR_GRAYTEXT
        else:
            color = wx.SYS_COLOUR_WINDOW
        self.m_textCtrl_fuse400.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

        self.m_textCtrl_fuse430.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse440.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

        self.m_textCtrl_fuse480.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse490.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse4f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse500.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse510.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse520.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse530.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse540.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse550.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse560.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse570.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

        self.m_textCtrl_fuse600.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse610.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse620.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse630.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse640.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse650.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse660.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse670.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse680.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )

        self.m_textCtrl_fuse6f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse700.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse710.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse720.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse730.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse740.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse750.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse760.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse770.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse780.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse790.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7c0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7d0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7e0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse7f0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse800.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse810.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse820.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse830.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse840.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse850.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse860.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse870.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse880.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse890.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse8a0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.m_textCtrl_fuse8b0.SetBackgroundColour( wx.SystemSettings.GetColour( color ) )
        self.Refresh()

    def getFormattedFuseValue( self, fuseValue, direction='LSB'):
        formattedVal32 = ''
        for i in range(8):
            loc = 0
            if direction =='LSB':
                loc = 32 - (i + 1) * 4
            elif direction =='MSB':
                loc = i * 4
            else:
                pass
            halfbyteStr = str(hex((fuseValue & (0xF << loc))>> loc))
            formattedVal32 += halfbyteStr[2]
        return formattedVal32

    def getFormattedHexValue( self, val32 ):
        return ('0x' + self.getFormattedFuseValue(val32))

    def _parseReadFuseValue( self, fuseValue ):
        if fuseValue != None:
            return self.getFormattedHexValue(fuseValue)
        else:
            return '--------'

    def showScannedFuses( self , scannedFuseList ):
        efuseDict = uivar.getEfuseSettings()

        self.m_textCtrl_fuse400.Clear()
        self.m_textCtrl_fuse400.write(self._parseReadFuseValue(scannedFuseList[0]))
        efuseDict['0x400_lock'] = scannedFuseList[0]
        self.m_textCtrl_fuse410.Clear()
        self.m_textCtrl_fuse410.write(self._parseReadFuseValue(scannedFuseList[1]))
        self.m_textCtrl_fuse420.Clear()
        self.m_textCtrl_fuse420.write(self._parseReadFuseValue(scannedFuseList[2]))
        self.m_textCtrl_fuse430.Clear()
        self.m_textCtrl_fuse430.write(self._parseReadFuseValue(scannedFuseList[3]))
        self.m_textCtrl_fuse440.Clear()
        self.m_textCtrl_fuse440.write(self._parseReadFuseValue(scannedFuseList[4]))
        self.m_textCtrl_fuse450.Clear()
        self.m_textCtrl_fuse450.write(self._parseReadFuseValue(scannedFuseList[5]))
        efuseDict['0x450_bootCfg0'] = scannedFuseList[5]
        self.m_textCtrl_fuse460.Clear()
        self.m_textCtrl_fuse460.write(self._parseReadFuseValue(scannedFuseList[6]))
        efuseDict['0x460_bootCfg1'] = scannedFuseList[6]
        self.m_textCtrl_fuse470.Clear()
        self.m_textCtrl_fuse470.write(self._parseReadFuseValue(scannedFuseList[7]))
        efuseDict['0x470_bootCfg2'] = scannedFuseList[7]
        self.m_textCtrl_fuse480.Clear()
        self.m_textCtrl_fuse480.write(self._parseReadFuseValue(scannedFuseList[8]))
        self.m_textCtrl_fuse490.Clear()
        self.m_textCtrl_fuse490.write(self._parseReadFuseValue(scannedFuseList[9]))
        self.m_textCtrl_fuse4a0.Clear()
        self.m_textCtrl_fuse4a0.write(self._parseReadFuseValue(scannedFuseList[10]))
        self.m_textCtrl_fuse4b0.Clear()
        self.m_textCtrl_fuse4b0.write(self._parseReadFuseValue(scannedFuseList[11]))
        self.m_textCtrl_fuse4c0.Clear()
        self.m_textCtrl_fuse4c0.write(self._parseReadFuseValue(scannedFuseList[12]))
        self.m_textCtrl_fuse4d0.Clear()
        self.m_textCtrl_fuse4d0.write(self._parseReadFuseValue(scannedFuseList[13]))
        self.m_textCtrl_fuse4e0.Clear()
        self.m_textCtrl_fuse4e0.write(self._parseReadFuseValue(scannedFuseList[14]))
        self.m_textCtrl_fuse4f0.Clear()
        self.m_textCtrl_fuse4f0.write(self._parseReadFuseValue(scannedFuseList[15]))

        self.m_textCtrl_fuse500.Clear()
        self.m_textCtrl_fuse500.write(self._parseReadFuseValue(scannedFuseList[16]))
        self.m_textCtrl_fuse510.Clear()
        self.m_textCtrl_fuse510.write(self._parseReadFuseValue(scannedFuseList[17]))
        self.m_textCtrl_fuse520.Clear()
        self.m_textCtrl_fuse520.write(self._parseReadFuseValue(scannedFuseList[18]))
        self.m_textCtrl_fuse530.Clear()
        self.m_textCtrl_fuse530.write(self._parseReadFuseValue(scannedFuseList[19]))
        self.m_textCtrl_fuse540.Clear()
        self.m_textCtrl_fuse540.write(self._parseReadFuseValue(scannedFuseList[20]))
        self.m_textCtrl_fuse550.Clear()
        self.m_textCtrl_fuse550.write(self._parseReadFuseValue(scannedFuseList[21]))
        self.m_textCtrl_fuse560.Clear()
        self.m_textCtrl_fuse560.write(self._parseReadFuseValue(scannedFuseList[22]))
        self.m_textCtrl_fuse570.Clear()
        self.m_textCtrl_fuse570.write(self._parseReadFuseValue(scannedFuseList[23]))
        self.m_textCtrl_fuse580.Clear()
        self.m_textCtrl_fuse580.write(self._parseReadFuseValue(scannedFuseList[24]))
        self.m_textCtrl_fuse590.Clear()
        self.m_textCtrl_fuse590.write(self._parseReadFuseValue(scannedFuseList[25]))
        self.m_textCtrl_fuse5a0.Clear()
        self.m_textCtrl_fuse5a0.write(self._parseReadFuseValue(scannedFuseList[26]))
        self.m_textCtrl_fuse5b0.Clear()
        self.m_textCtrl_fuse5b0.write(self._parseReadFuseValue(scannedFuseList[27]))
        self.m_textCtrl_fuse5c0.Clear()
        self.m_textCtrl_fuse5c0.write(self._parseReadFuseValue(scannedFuseList[28]))
        self.m_textCtrl_fuse5d0.Clear()
        self.m_textCtrl_fuse5d0.write(self._parseReadFuseValue(scannedFuseList[29]))
        self.m_textCtrl_fuse5e0.Clear()
        self.m_textCtrl_fuse5e0.write(self._parseReadFuseValue(scannedFuseList[30]))
        self.m_textCtrl_fuse5f0.Clear()
        self.m_textCtrl_fuse5f0.write(self._parseReadFuseValue(scannedFuseList[31]))

        self.m_textCtrl_fuse600.Clear()
        self.m_textCtrl_fuse600.write(self._parseReadFuseValue(scannedFuseList[32]))
        self.m_textCtrl_fuse610.Clear()
        self.m_textCtrl_fuse610.write(self._parseReadFuseValue(scannedFuseList[33]))
        self.m_textCtrl_fuse620.Clear()
        self.m_textCtrl_fuse620.write(self._parseReadFuseValue(scannedFuseList[34]))
        self.m_textCtrl_fuse630.Clear()
        self.m_textCtrl_fuse630.write(self._parseReadFuseValue(scannedFuseList[35]))
        self.m_textCtrl_fuse640.Clear()
        self.m_textCtrl_fuse640.write(self._parseReadFuseValue(scannedFuseList[36]))
        self.m_textCtrl_fuse650.Clear()
        self.m_textCtrl_fuse650.write(self._parseReadFuseValue(scannedFuseList[37]))
        self.m_textCtrl_fuse660.Clear()
        self.m_textCtrl_fuse660.write(self._parseReadFuseValue(scannedFuseList[38]))
        self.m_textCtrl_fuse670.Clear()
        self.m_textCtrl_fuse670.write(self._parseReadFuseValue(scannedFuseList[39]))
        self.m_textCtrl_fuse680.Clear()
        self.m_textCtrl_fuse680.write(self._parseReadFuseValue(scannedFuseList[40]))
        self.m_textCtrl_fuse690.Clear()
        self.m_textCtrl_fuse690.write(self._parseReadFuseValue(scannedFuseList[41]))
        self.m_textCtrl_fuse6a0.Clear()
        self.m_textCtrl_fuse6a0.write(self._parseReadFuseValue(scannedFuseList[42]))
        self.m_textCtrl_fuse6b0.Clear()
        self.m_textCtrl_fuse6b0.write(self._parseReadFuseValue(scannedFuseList[43]))
        self.m_textCtrl_fuse6c0.Clear()
        self.m_textCtrl_fuse6c0.write(self._parseReadFuseValue(scannedFuseList[44]))
        self.m_textCtrl_fuse6d0.Clear()
        self.m_textCtrl_fuse6d0.write(self._parseReadFuseValue(scannedFuseList[45]))
        efuseDict['0x6d0_miscConf0'] = scannedFuseList[45]
        self.m_textCtrl_fuse6e0.Clear()
        self.m_textCtrl_fuse6e0.write(self._parseReadFuseValue(scannedFuseList[46]))
        efuseDict['0x6e0_miscConf1'] = scannedFuseList[46]
        self.m_textCtrl_fuse6f0.Clear()
        self.m_textCtrl_fuse6f0.write(self._parseReadFuseValue(scannedFuseList[47]))

        self.m_textCtrl_fuse700.Clear()
        self.m_textCtrl_fuse700.write(self._parseReadFuseValue(scannedFuseList[48]))
        self.m_textCtrl_fuse710.Clear()
        self.m_textCtrl_fuse710.write(self._parseReadFuseValue(scannedFuseList[49]))
        self.m_textCtrl_fuse720.Clear()
        self.m_textCtrl_fuse720.write(self._parseReadFuseValue(scannedFuseList[50]))
        self.m_textCtrl_fuse730.Clear()
        self.m_textCtrl_fuse730.write(self._parseReadFuseValue(scannedFuseList[51]))
        self.m_textCtrl_fuse740.Clear()
        self.m_textCtrl_fuse740.write(self._parseReadFuseValue(scannedFuseList[52]))
        self.m_textCtrl_fuse750.Clear()
        self.m_textCtrl_fuse750.write(self._parseReadFuseValue(scannedFuseList[53]))
        self.m_textCtrl_fuse760.Clear()
        self.m_textCtrl_fuse760.write(self._parseReadFuseValue(scannedFuseList[54]))
        self.m_textCtrl_fuse770.Clear()
        self.m_textCtrl_fuse770.write(self._parseReadFuseValue(scannedFuseList[55]))
        self.m_textCtrl_fuse780.Clear()
        self.m_textCtrl_fuse780.write(self._parseReadFuseValue(scannedFuseList[56]))
        self.m_textCtrl_fuse790.Clear()
        self.m_textCtrl_fuse790.write(self._parseReadFuseValue(scannedFuseList[57]))
        self.m_textCtrl_fuse7a0.Clear()
        self.m_textCtrl_fuse7a0.write(self._parseReadFuseValue(scannedFuseList[58]))
        self.m_textCtrl_fuse7b0.Clear()
        self.m_textCtrl_fuse7b0.write(self._parseReadFuseValue(scannedFuseList[59]))
        self.m_textCtrl_fuse7c0.Clear()
        self.m_textCtrl_fuse7c0.write(self._parseReadFuseValue(scannedFuseList[60]))
        self.m_textCtrl_fuse7d0.Clear()
        self.m_textCtrl_fuse7d0.write(self._parseReadFuseValue(scannedFuseList[61]))
        self.m_textCtrl_fuse7e0.Clear()
        self.m_textCtrl_fuse7e0.write(self._parseReadFuseValue(scannedFuseList[62]))
        self.m_textCtrl_fuse7f0.Clear()
        self.m_textCtrl_fuse7f0.write(self._parseReadFuseValue(scannedFuseList[63]))

        self.m_textCtrl_fuse800.Clear()
        self.m_textCtrl_fuse800.write(self._parseReadFuseValue(scannedFuseList[64]))
        self.m_textCtrl_fuse810.Clear()
        self.m_textCtrl_fuse810.write(self._parseReadFuseValue(scannedFuseList[65]))
        self.m_textCtrl_fuse820.Clear()
        self.m_textCtrl_fuse820.write(self._parseReadFuseValue(scannedFuseList[66]))
        self.m_textCtrl_fuse830.Clear()
        self.m_textCtrl_fuse830.write(self._parseReadFuseValue(scannedFuseList[67]))
        self.m_textCtrl_fuse840.Clear()
        self.m_textCtrl_fuse840.write(self._parseReadFuseValue(scannedFuseList[68]))
        self.m_textCtrl_fuse850.Clear()
        self.m_textCtrl_fuse850.write(self._parseReadFuseValue(scannedFuseList[69]))
        self.m_textCtrl_fuse860.Clear()
        self.m_textCtrl_fuse860.write(self._parseReadFuseValue(scannedFuseList[70]))
        self.m_textCtrl_fuse870.Clear()
        self.m_textCtrl_fuse870.write(self._parseReadFuseValue(scannedFuseList[71]))
        self.m_textCtrl_fuse880.Clear()
        self.m_textCtrl_fuse880.write(self._parseReadFuseValue(scannedFuseList[72]))
        self.m_textCtrl_fuse890.Clear()
        self.m_textCtrl_fuse890.write(self._parseReadFuseValue(scannedFuseList[73]))
        self.m_textCtrl_fuse8a0.Clear()
        self.m_textCtrl_fuse8a0.write(self._parseReadFuseValue(scannedFuseList[74]))
        self.m_textCtrl_fuse8b0.Clear()
        self.m_textCtrl_fuse8b0.write(self._parseReadFuseValue(scannedFuseList[75]))
        self.m_textCtrl_fuse8c0.Clear()
        self.m_textCtrl_fuse8c0.write(self._parseReadFuseValue(scannedFuseList[76]))
        self.m_textCtrl_fuse8d0.Clear()
        self.m_textCtrl_fuse8d0.write(self._parseReadFuseValue(scannedFuseList[77]))
        self.m_textCtrl_fuse8e0.Clear()
        self.m_textCtrl_fuse8e0.write(self._parseReadFuseValue(scannedFuseList[78]))
        self.m_textCtrl_fuse8f0.Clear()
        self.m_textCtrl_fuse8f0.write(self._parseReadFuseValue(scannedFuseList[79]))

        uivar.setEfuseSettings(efuseDict)

    def _parseUserFuseValue( self, fuseText ):
        if len(fuseText) >= 3 and fuseText[0:2] == '0x':
            return int(fuseText[2:len(fuseText)], 16)
        else:
            return None

    def getUserFuses( self ):
        userFuseList = [None] * RT10yy_fusedef.kMaxEfuseWords
        userFuseList[0] = self._parseUserFuseValue(self.m_textCtrl_fuse400.GetLineText(0))
        userFuseList[1] = self._parseUserFuseValue(self.m_textCtrl_fuse410.GetLineText(0))
        userFuseList[2] = self._parseUserFuseValue(self.m_textCtrl_fuse420.GetLineText(0))
        userFuseList[3] = self._parseUserFuseValue(self.m_textCtrl_fuse430.GetLineText(0))
        userFuseList[4] = self._parseUserFuseValue(self.m_textCtrl_fuse440.GetLineText(0))
        userFuseList[5] = self._parseUserFuseValue(self.m_textCtrl_fuse450.GetLineText(0))
        userFuseList[6] = self._parseUserFuseValue(self.m_textCtrl_fuse460.GetLineText(0))
        userFuseList[7] = self._parseUserFuseValue(self.m_textCtrl_fuse470.GetLineText(0))
        userFuseList[8] = self._parseUserFuseValue(self.m_textCtrl_fuse480.GetLineText(0))
        userFuseList[9] = self._parseUserFuseValue(self.m_textCtrl_fuse490.GetLineText(0))
        userFuseList[10] = self._parseUserFuseValue(self.m_textCtrl_fuse4a0.GetLineText(0))
        userFuseList[11] = self._parseUserFuseValue(self.m_textCtrl_fuse4b0.GetLineText(0))
        userFuseList[12] = self._parseUserFuseValue(self.m_textCtrl_fuse4c0.GetLineText(0))
        userFuseList[13] = self._parseUserFuseValue(self.m_textCtrl_fuse4d0.GetLineText(0))
        userFuseList[14] = self._parseUserFuseValue(self.m_textCtrl_fuse4e0.GetLineText(0))
        userFuseList[15] = self._parseUserFuseValue(self.m_textCtrl_fuse4f0.GetLineText(0))

        userFuseList[16] = self._parseUserFuseValue(self.m_textCtrl_fuse500.GetLineText(0))
        userFuseList[17] = self._parseUserFuseValue(self.m_textCtrl_fuse510.GetLineText(0))
        userFuseList[18] = self._parseUserFuseValue(self.m_textCtrl_fuse520.GetLineText(0))
        userFuseList[19] = self._parseUserFuseValue(self.m_textCtrl_fuse530.GetLineText(0))
        userFuseList[20] = self._parseUserFuseValue(self.m_textCtrl_fuse540.GetLineText(0))
        userFuseList[21] = self._parseUserFuseValue(self.m_textCtrl_fuse550.GetLineText(0))
        userFuseList[22] = self._parseUserFuseValue(self.m_textCtrl_fuse560.GetLineText(0))
        userFuseList[23] = self._parseUserFuseValue(self.m_textCtrl_fuse570.GetLineText(0))
        userFuseList[24] = self._parseUserFuseValue(self.m_textCtrl_fuse580.GetLineText(0))
        userFuseList[25] = self._parseUserFuseValue(self.m_textCtrl_fuse590.GetLineText(0))
        userFuseList[26] = self._parseUserFuseValue(self.m_textCtrl_fuse5a0.GetLineText(0))
        userFuseList[27] = self._parseUserFuseValue(self.m_textCtrl_fuse5b0.GetLineText(0))
        userFuseList[28] = self._parseUserFuseValue(self.m_textCtrl_fuse5c0.GetLineText(0))
        userFuseList[29] = self._parseUserFuseValue(self.m_textCtrl_fuse5d0.GetLineText(0))
        userFuseList[30] = self._parseUserFuseValue(self.m_textCtrl_fuse5e0.GetLineText(0))
        userFuseList[31] = self._parseUserFuseValue(self.m_textCtrl_fuse5f0.GetLineText(0))

        userFuseList[32] = self._parseUserFuseValue(self.m_textCtrl_fuse600.GetLineText(0))
        userFuseList[33] = self._parseUserFuseValue(self.m_textCtrl_fuse610.GetLineText(0))
        userFuseList[34] = self._parseUserFuseValue(self.m_textCtrl_fuse620.GetLineText(0))
        userFuseList[35] = self._parseUserFuseValue(self.m_textCtrl_fuse630.GetLineText(0))
        userFuseList[36] = self._parseUserFuseValue(self.m_textCtrl_fuse640.GetLineText(0))
        userFuseList[37] = self._parseUserFuseValue(self.m_textCtrl_fuse650.GetLineText(0))
        userFuseList[38] = self._parseUserFuseValue(self.m_textCtrl_fuse660.GetLineText(0))
        userFuseList[39] = self._parseUserFuseValue(self.m_textCtrl_fuse670.GetLineText(0))
        userFuseList[40] = self._parseUserFuseValue(self.m_textCtrl_fuse680.GetLineText(0))
        userFuseList[41] = self._parseUserFuseValue(self.m_textCtrl_fuse690.GetLineText(0))
        userFuseList[42] = self._parseUserFuseValue(self.m_textCtrl_fuse6a0.GetLineText(0))
        userFuseList[43] = self._parseUserFuseValue(self.m_textCtrl_fuse6b0.GetLineText(0))
        userFuseList[44] = self._parseUserFuseValue(self.m_textCtrl_fuse6c0.GetLineText(0))
        userFuseList[45] = self._parseUserFuseValue(self.m_textCtrl_fuse6d0.GetLineText(0))
        userFuseList[46] = self._parseUserFuseValue(self.m_textCtrl_fuse6e0.GetLineText(0))
        userFuseList[47] = self._parseUserFuseValue(self.m_textCtrl_fuse6f0.GetLineText(0))

        userFuseList[48] = self._parseUserFuseValue(self.m_textCtrl_fuse700.GetLineText(0))
        userFuseList[49] = self._parseUserFuseValue(self.m_textCtrl_fuse710.GetLineText(0))
        userFuseList[50] = self._parseUserFuseValue(self.m_textCtrl_fuse720.GetLineText(0))
        userFuseList[51] = self._parseUserFuseValue(self.m_textCtrl_fuse730.GetLineText(0))
        userFuseList[52] = self._parseUserFuseValue(self.m_textCtrl_fuse730.GetLineText(0))
        userFuseList[53] = self._parseUserFuseValue(self.m_textCtrl_fuse750.GetLineText(0))
        userFuseList[54] = self._parseUserFuseValue(self.m_textCtrl_fuse760.GetLineText(0))
        userFuseList[55] = self._parseUserFuseValue(self.m_textCtrl_fuse770.GetLineText(0))
        userFuseList[56] = self._parseUserFuseValue(self.m_textCtrl_fuse780.GetLineText(0))
        userFuseList[57] = self._parseUserFuseValue(self.m_textCtrl_fuse790.GetLineText(0))
        userFuseList[58] = self._parseUserFuseValue(self.m_textCtrl_fuse7a0.GetLineText(0))
        userFuseList[59] = self._parseUserFuseValue(self.m_textCtrl_fuse7b0.GetLineText(0))
        userFuseList[60] = self._parseUserFuseValue(self.m_textCtrl_fuse7c0.GetLineText(0))
        userFuseList[61] = self._parseUserFuseValue(self.m_textCtrl_fuse7d0.GetLineText(0))
        userFuseList[62] = self._parseUserFuseValue(self.m_textCtrl_fuse7e0.GetLineText(0))
        userFuseList[63] = self._parseUserFuseValue(self.m_textCtrl_fuse7f0.GetLineText(0))

        userFuseList[64] = self._parseUserFuseValue(self.m_textCtrl_fuse800.GetLineText(0))
        userFuseList[65] = self._parseUserFuseValue(self.m_textCtrl_fuse810.GetLineText(0))
        userFuseList[66] = self._parseUserFuseValue(self.m_textCtrl_fuse820.GetLineText(0))
        userFuseList[67] = self._parseUserFuseValue(self.m_textCtrl_fuse830.GetLineText(0))
        userFuseList[68] = self._parseUserFuseValue(self.m_textCtrl_fuse840.GetLineText(0))
        userFuseList[69] = self._parseUserFuseValue(self.m_textCtrl_fuse850.GetLineText(0))
        userFuseList[70] = self._parseUserFuseValue(self.m_textCtrl_fuse860.GetLineText(0))
        userFuseList[71] = self._parseUserFuseValue(self.m_textCtrl_fuse870.GetLineText(0))
        userFuseList[72] = self._parseUserFuseValue(self.m_textCtrl_fuse880.GetLineText(0))
        userFuseList[73] = self._parseUserFuseValue(self.m_textCtrl_fuse890.GetLineText(0))
        userFuseList[74] = self._parseUserFuseValue(self.m_textCtrl_fuse8a0.GetLineText(0))
        userFuseList[75] = self._parseUserFuseValue(self.m_textCtrl_fuse8b0.GetLineText(0))
        userFuseList[76] = self._parseUserFuseValue(self.m_textCtrl_fuse8c0.GetLineText(0))
        userFuseList[77] = self._parseUserFuseValue(self.m_textCtrl_fuse8d0.GetLineText(0))
        userFuseList[78] = self._parseUserFuseValue(self.m_textCtrl_fuse8e0.GetLineText(0))
        userFuseList[79] = self._parseUserFuseValue(self.m_textCtrl_fuse8f0.GetLineText(0))

        return userFuseList

    def showSettedEfuse( self , fuseIndex, fuseValue ):
        if fuseIndex == RT10yy_fusedef.kEfuseIndex_LOCK:
            self.m_textCtrl_fuse400.Clear()
            self.m_textCtrl_fuse400.write(self._parseReadFuseValue(fuseValue))
        elif fuseIndex == RT10yy_fusedef.kEfuseIndex_BOOT_CFG0:
            self.m_textCtrl_fuse450.Clear()
            self.m_textCtrl_fuse450.write(self._parseReadFuseValue(fuseValue))
        elif fuseIndex == RT10yy_fusedef.kEfuseIndex_BOOT_CFG1:
            self.m_textCtrl_fuse460.Clear()
            self.m_textCtrl_fuse460.write(self._parseReadFuseValue(fuseValue))
        elif fuseIndex == RT10yy_fusedef.kEfuseIndex_BOOT_CFG2:
            self.m_textCtrl_fuse470.Clear()
            self.m_textCtrl_fuse470.write(self._parseReadFuseValue(fuseValue))
        elif fuseIndex == RT10yy_fusedef.kEfuseIndex_MISC_CONF0:
            self.m_textCtrl_fuse6d0.Clear()
            self.m_textCtrl_fuse6d0.write(self._parseReadFuseValue(fuseValue))
        elif fuseIndex == RT10yy_fusedef.kEfuseIndex_MISC_CONF1:
            self.m_textCtrl_fuse6e0.Clear()
            self.m_textCtrl_fuse6e0.write(self._parseReadFuseValue(fuseValue))
        else:
            pass

    def RT10yy_setLanguage( self ):
        langIndex = self.languageIndex
        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_GenSeq, uilang.kMainLanguageContentDict['panel_genSeq'][langIndex])
        self.m_staticText_serial.SetLabel(uilang.kMainLanguageContentDict['sText_serial'][langIndex])
        self.m_staticText_keyPass.SetLabel(uilang.kMainLanguageContentDict['sText_keyPass'][langIndex])
        self.m_button_advCertSettings.SetLabel(uilang.kMainLanguageContentDict['button_advCertSettings'][langIndex])
        self.m_staticText_certFmt.SetLabel(uilang.kMainLanguageContentDict['sText_certFmt'][langIndex])
        self.m_staticText_hashAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_hashAlgo'][langIndex])
        self.m_staticText_appPath.SetLabel(uilang.kMainLanguageContentDict['sText_appPath'][langIndex])
        self.m_staticText_appBaseAddr.SetLabel(uilang.kMainLanguageContentDict['sText_appBaseAddr'][langIndex])
        self.m_staticText_habCryptoAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_habCryptoAlgo'][langIndex])
        self.m_staticText_enableCertForBee.SetLabel(uilang.kMainLanguageContentDict['sText_enableCertForBee'][langIndex])
        self.m_staticText_keyStorageRegion.SetLabel(uilang.kMainLanguageContentDict['sText_keyStorageRegion'][langIndex])
        self.m_staticText_availBeeEngines.SetLabel(uilang.kMainLanguageContentDict['sText_availBeeEngines'][langIndex])
        self.m_button_advKeySettings.SetLabel(uilang.kMainLanguageContentDict['button_advKeySettings'][langIndex])
        self.m_staticText_beeCryptoAlgo.SetLabel(uilang.kMainLanguageContentDict['sText_beeCryptoAlgo'][langIndex])
        self.m_staticText_maxFacCnt.SetLabel(uilang.kMainLanguageContentDict['sText_maxFacCnt'][langIndex])

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_LoadSeq, uilang.kMainLanguageContentDict['panel_loadSeq'][langIndex])
        self.m_staticText_srk256bit.SetLabel(uilang.kMainLanguageContentDict['sText_srk256bit'][langIndex])
        self.m_staticText_beeKeyInfo.SetLabel(uilang.kMainLanguageContentDict['sText_beeKeyInfo'][langIndex])
        self.m_staticText_showImage.SetLabel(uilang.kMainLanguageContentDict['sText_showImage'][langIndex])
        self.m_staticText_habDek128bit.SetLabel(uilang.kMainLanguageContentDict['sText_habDek128bit'][langIndex])

        if self.hasDynamicLableBeenInit:
            self.RT10yy_setSecureBootSeqColor(False)
            if self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                self.m_button_prepBee.SetLabel(uilang.kMainLanguageContentDict['button_prepBee_p'][self.languageIndex])
            elif self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                self.m_button_prepBee.SetLabel(uilang.kMainLanguageContentDict['button_prepBee_e'][self.languageIndex])
            else:
                pass

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_fuseUtil, uilang.kMainLanguageContentDict['panel_fuseUtil'][langIndex])
        self.m_button_scan.SetLabel(uilang.kMainLanguageContentDict['button_scan'][langIndex])
        self.m_button_burn.SetLabel(uilang.kMainLanguageContentDict['button_burn'][langIndex])

        self.m_notebook_imageSeq.SetPageText(uilang.kPanelIndex_memView, uilang.kMainLanguageContentDict['panel_memView'][langIndex])
        self.m_staticText_memStart.SetLabel(uilang.kMainLanguageContentDict['sText_memStart'][langIndex])
        self.m_staticText_memLength.SetLabel(uilang.kMainLanguageContentDict['sText_memLength'][langIndex])
        self.m_staticText_memBinFile.SetLabel(uilang.kMainLanguageContentDict['sText_memBinFile'][langIndex])
        self.m_button_readMem.SetLabel(uilang.kMainLanguageContentDict['button_readMem'][langIndex])
        self.m_button_eraseMem.SetLabel(uilang.kMainLanguageContentDict['button_eraseMem'][langIndex])
        self.m_button_writeMem.SetLabel(uilang.kMainLanguageContentDict['button_writeMem'][langIndex])
        self.m_button_executeApp.SetLabel(uilang.kMainLanguageContentDict['button_executeApp'][langIndex])
        self.m_button_viewMem.SetLabel(uilang.kMainLanguageContentDict['button_viewMem'][langIndex])
        self.m_button_clearMem.SetLabel(uilang.kMainLanguageContentDict['button_clearMem'][langIndex])
        self.m_checkBox_saveImageData.SetLabel(uilang.kMainLanguageContentDict['checkBox_saveImageData'][langIndex])
