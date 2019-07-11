#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
sys.path.append(os.path.abspath(".."))
from mem import RTyyyy_memcore
from ui import RTyyyy_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from fuse import RTyyyy_fusedef
from ui import ui_cfg_dcd
from ui import ui_settings_cert
from ui import ui_settings_fixed_otpmk_key
from ui import ui_settings_flexible_user_keys
from ui import RT10yy_ui_efuse_lock
from ui import RT10yy_ui_efuse_bootcfg0_flexspinor_3bits
from ui import RT10yy_ui_efuse_bootcfg0_flexspinor_10bits
from ui import RT10yy_ui_efuse_bootcfg0_flexspinor_12bits
from ui import RT10yy_ui_efuse_bootcfg1
from ui import RT10yy_ui_efuse_bootcfg2
from ui import RT10yy_ui_efuse_miscconf0
from ui import RT10yy_ui_efuse_miscconf1_flexspinor

kRetryPingTimes = 5

kBootloaderType_Rom         = 0
kBootloaderType_Flashloader = 1

class secBootRTyyyyMain(RTyyyy_memcore.secBootRTyyyyMem):

    def __init__(self, parent):
        RTyyyy_memcore.secBootRTyyyyMem.__init__(self, parent)
        self.RTyyyy_isAllInOneActionTaskPending = False
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self._RTyyyy_initMain()

    def _RTyyyy_initMain( self ):
        self.connectStage = uidef.kConnectStage_Rom
        self.isBootableAppAllowedToView = False
        self.lastTime = None
        self.isThereBoardConnection = False

    def _RTyyyy_startGaugeTimer( self ):
        if not self.RTyyyy_isAllInOneActionTaskPending:
            self.lastTime = time.time()
            self.initGauge()

    def _RTyyyy_stopGaugeTimer( self ):
        if not self.RTyyyy_isAllInOneActionTaskPending:
            self.deinitGauge()
            self.updateCostTime()

    def RTyyyy_callbackSetMcuSeries( self ):
        self.RTyyyy_initUi()
        self.RTyyyy_initGen()
        self.RTyyyy_initRun()
        self.RTyyyy_initFuse()
        self.RTyyyy_initMem()
        self._RTyyyy_initMain()
        self.RTyyyy_setTargetSetupValue()

    def RTyyyy_callbackSetMcuDevice( self ):
        self.RTyyyy_setTargetSetupValue()
        self.applyFuseOperToRunMode()
        needToPlaySound = False
        self.RTyyyy_setSecureBootSeqColor(needToPlaySound)

    def RTyyyy_callbackSetBootDevice( self ):
        self.RTyyyy_setTargetSetupValue()
        needToPlaySound = False
        self.RTyyyy_setSecureBootSeqColor(needToPlaySound)

    def callbackDeviceConfigurationData( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        dcdFrame = ui_cfg_dcd.secBootUiCfgDcd(None)
        dcdFrame.SetTitle(uilang.kSubLanguageContentDict['dcd_title'][self.languageIndex])
        dcdFrame.setNecessaryInfo(self.dcdBinFilename, self.dcdCfgFilename, self.dcdModelFolder)
        dcdFrame.Show(True)

    def _RTyyyy_retryToPingBootloader( self, bootType ):
        pingStatus = False
        pingCnt = kRetryPingTimes
        while (not pingStatus) and pingCnt > 0:
            if bootType == kBootloaderType_Rom:
                pingStatus = self.RTyyyy_pingRom()
            elif bootType == kBootloaderType_Flashloader:
                pingStatus = self.RTyyyy_pingFlashloader()
            else:
                pass
            if pingStatus:
                break
            pingCnt = pingCnt - 1
            if self.isUsbhidPortSelected:
                time.sleep(2)
        return pingStatus

    def _RTyyyy_connectFailureHandler( self ):
        self.connectStage = uidef.kConnectStage_Rom
        self.updateConnectStatus('red')
        usbIdList = self.RTyyyy_getUsbid()
        self.setPortSetupValue(self.connectStage, usbIdList, False, False)
        self.isBootableAppAllowedToView = False

    def _RTyyyy_connectStateMachine( self, showError=True ):
        connectSteps = RTyyyy_uidef.kConnectStep_Normal
        self.getOneStepConnectMode()
        retryToDetectUsb = False
        if self.isOneStepConnectMode:
            if self.connectStage == uidef.kConnectStage_Reset or self.connectStage == uidef.kConnectStage_ExternalMemory:
                connectSteps = RTyyyy_uidef.kConnectStep_Fast - 2
            elif self.connectStage == uidef.kConnectStage_Flashloader:
                connectSteps = RTyyyy_uidef.kConnectStep_Fast - 1
                retryToDetectUsb = True
            elif self.connectStage == uidef.kConnectStage_Rom:
                connectSteps = RTyyyy_uidef.kConnectStep_Fast
                retryToDetectUsb = True
            else:
                pass
        while connectSteps:
            if not self.updatePortSetupValue(retryToDetectUsb, showError):
                if self.connectStage == uidef.kConnectStage_Rom:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_doubleCheckBmod'][self.languageIndex])
                self._RTyyyy_connectFailureHandler()
                return
            if self.connectStage == uidef.kConnectStage_Rom:
                self.RTyyyy_connectToDevice(self.connectStage)
                if self._RTyyyy_retryToPingBootloader(kBootloaderType_Rom):
                    self.RTyyyy_getMcuDeviceInfoViaRom()
                    self.getMcuDeviceHabStatus()
                    if self.RTyyyy_jumpToFlashloader():
                        self.connectStage = uidef.kConnectStage_Flashloader
                        self.updateConnectStatus('yellow')
                        usbIdList = self.RTyyyy_getUsbid()
                        self.setPortSetupValue(self.connectStage, usbIdList, True, True)
                    else:
                        self.updateConnectStatus('red')
                        if showError:
                            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToJumpToFl'][self.languageIndex])
                        return
                else:
                    self.updateConnectStatus('red')
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_doubleCheckBmod'][self.languageIndex])
                    return
            elif self.connectStage == uidef.kConnectStage_Flashloader:
                self.RTyyyy_connectToDevice(self.connectStage)
                if self._RTyyyy_retryToPingBootloader(kBootloaderType_Flashloader):
                    self.getMcuDeviceInfoViaFlashloader()
                    self.getMcuDeviceBtFuseSel()
                    self.getFlexramInfoViaFlashloader()
                    self.updateConnectStatus('green')
                    self.connectStage = uidef.kConnectStage_ExternalMemory
                else:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToPingFl'][self.languageIndex])
                    self._RTyyyy_connectFailureHandler()
                    return
            elif self.connectStage == uidef.kConnectStage_ExternalMemory:
                if self.RTyyyy_configureBootDevice():
                    self.getBootDeviceInfoViaFlashloader()
                    self.connectStage = uidef.kConnectStage_Reset
                    self.updateConnectStatus('blue')
                else:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToCfgBootDevice'][self.languageIndex])
                    self._RTyyyy_connectFailureHandler()
                    return
            elif self.connectStage == uidef.kConnectStage_Reset:
                self.RTyyyy_resetMcuDevice()
                self.isBootableAppAllowedToView = False
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
                usbIdList = self.RTyyyy_getUsbid()
                self.setPortSetupValue(self.connectStage, usbIdList, True, True)
                self.RTyyyy_connectToDevice(self.connectStage)
            else:
                pass
            connectSteps -= 1

    def RTyyyy_callbackConnectToDevice( self ):
        self._RTyyyy_startGaugeTimer()
        self.printLog("'Connect to xxx' button is clicked")
        if not self.isSbFileEnabledToGen:
            self._RTyyyy_connectStateMachine(True)
        else:
            if not self.isThereBoardConnection:
                if self.connectStage == uidef.kConnectStage_Rom:
                    self.initSbAppBdfilesContent()
                else:
                    # It means there is board connection
                    self.isThereBoardConnection = True
                self._RTyyyy_connectStateMachine(False)
                if not self.isThereBoardConnection:
                    if self.connectStage == uidef.kConnectStage_Rom:
                        # It means there is no board connection, but we need to set it as True for SB generation
                        self.isThereBoardConnection = True
                        self.RTyyyy_connectToDevice(uidef.kConnectStage_Flashloader)
                        self.RTyyyy_isDeviceEnabledToOperate = False
                        self.configureBootDevice()
                        self.connectStage = uidef.kConnectStage_Reset
                        self.updateConnectStatus('blue')
                else:
                    self.isThereBoardConnection = False
            else:
                self.isThereBoardConnection = False
                self.RTyyyy_isDeviceEnabledToOperate = True
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
        self._RTyyyy_stopGaugeTimer()

    def RTyyyy_callbackSetSecureBootType( self ):
        self.setCostTime(0)
        self.RTyyyy_setSecureBootSeqColor()

    def RTyyyy_task_doAllInOneAction( self ):
        while True:
            if self.RTyyyy_isAllInOneActionTaskPending:
                self._RTyyyy_doAllInOneAction()
                self.RTyyyy_isAllInOneActionTaskPending = False
                self._RTyyyy_stopGaugeTimer()
            time.sleep(1)

    def _RTyyyy_doAllInOneAction( self ):
        allInOneSeqCnt = 1
        directReuseCert = False
        status = False
        while allInOneSeqCnt:
            if self.secureBootType == RTyyyy_uidef.kSecureBootType_HabAuth or \
               self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto or \
               ((self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor and self.isCertEnabledForHwCrypto):
                status = self._doGenCert(directReuseCert)
                if not status:
                    break
                status = self._doProgramSrk()
                if not status:
                    break
            status = self._RTyyyy_doGenImage()
            if not status:
                break
            if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
                status = self._doHwEncryption()
                if not status:
                    break
                if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                    status = self._doProgramHwCryptoDek()
                    if not status:
                        break
                elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                    if self.isCertEnabledForHwCrypto:
                        # If HAB is not closed here, we need to close HAB and re-do All-In-One Action
                        if self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed0 and \
                           self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed1:
                           if not self.isSbFileEnabledToGen:
                                self.enableHab()
                                self._RTyyyy_connectStateMachine()
                                while self.connectStage != uidef.kConnectStage_Reset:
                                    self._RTyyyy_connectStateMachine()
                                directReuseCert = True
                                allInOneSeqCnt += 1
                else:
                    pass
            status = self._RTyyyy_doFlashImage()
            if not status:
                break
            if self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto:
                status = self._doFlashHabDek()
                if not status:
                    break
            allInOneSeqCnt -= 1
        if self.isSbFileEnabledToGen:
            status = self.genSbAppImages()
        else:
            if status and self.isAutomaticImageReadback:
                self.showPageInMainBootSeqWin(uidef.kPageIndex_BootDeviceMemory)
                self._RTyyyy_doViewMem()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_AllInOne, status)

    def RTyyyy_callbackAllInOneAction( self ):
        self._RTyyyy_startGaugeTimer()
        self.RTyyyy_isAllInOneActionTaskPending = True

    def callbackAdvCertSettings( self, event ):
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != RTyyyy_uidef.kSecureBootType_Development:
            if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and (not self.isCertEnabledForHwCrypto):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForHwCrypto'][self.languageIndex])
            else:
                if self.checkIfSubWinHasBeenOpened():
                    return
                certSettingsFrame = ui_settings_cert.secBootUiSettingsCert(None)
                certSettingsFrame.SetTitle(uilang.kSubLanguageContentDict['cert_title'][self.languageIndex])
                certSettingsFrame.Show(True)
                self.updateAllCstPathToCorrectVersion()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_noNeedToSetForUnsigned'][self.languageIndex])

    def _wantToReuseAvailableCert( self, directReuseCert ):
        certAnswer = wx.NO
        if self.isCertificateGenerated(self.secureBootType):
            if not directReuseCert:
                msgText = ((uilang.kMsgLanguageContentDict['certGenInfo_reuseOldCert'][self.languageIndex]))
                certAnswer = wx.MessageBox(msgText, "Certificate Question", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
                if certAnswer == wx.CANCEL:
                    return None
                elif certAnswer == wx.NO:
                    msgText = ((uilang.kMsgLanguageContentDict['certGenInfo_haveNewCert'][self.languageIndex]))
                    certAnswer = wx.MessageBox(msgText, "Certificate Question", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
                    if certAnswer == wx.CANCEL:
                        return None
                    elif certAnswer == wx.YES:
                        certAnswer = wx.NO
                    else:
                        certAnswer = wx.YES
            else:
                certAnswer = wx.YES
        return (certAnswer == wx.YES)

    def _doGenCert( self, directReuseCert=False ):
        status = False
        reuseCert = None
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != RTyyyy_uidef.kSecureBootType_Development:
            if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and (not self.isCertEnabledForHwCrypto):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForHwCrypto'][self.languageIndex])
            else:
                self._RTyyyy_startGaugeTimer()
                self.printLog("'Generate Certificate' button is clicked")
                self.updateAllCstPathToCorrectVersion()
                reuseCert = self._wantToReuseAvailableCert(directReuseCert)
                if reuseCert == None:
                    pass
                elif not reuseCert:
                    self.cleanUpCertificate()
                    if self.createSerialAndKeypassfile():
                        self.RTyyyy_setSecureBootButtonColor()
                        self.genCertificate()
                        self.genSuperRootKeys()
                        self.showSuperRootKeys()
                        self.backUpCertificate()
                        status = True
                else:
                    status = True
                self._RTyyyy_stopGaugeTimer()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_noNeedToGenForUnsigned'][self.languageIndex])
        if reuseCert != None:
            self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_GenCert, status)
        return status

    def callbackGenCert( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doGenCert()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _RTyyyy_doGenImage( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        else:
            self._RTyyyy_startGaugeTimer()
            self.printLog("'Generate Bootable Image' button is clicked")
            if self.createMatchedAppBdfile():
                # Need to update image picture for DCD
                needToPlaySound = False
                self.RTyyyy_setSecureBootSeqColor(needToPlaySound)
                if self.RTyyyy_genBootableImage():
                    self.showHabDekIfApplicable()
                    status = True
            self._RTyyyy_stopGaugeTimer()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_GenImage, status)
        return status

    def RTyyyy_callbackGenImage( self ):
        if not self.isToolRunAsEntryMode:
            self._RTyyyy_doGenImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def callbackSetCertForHwCrypto( self, event ):
        if self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto:
            self.setHwCryptoCertColor()

    def callbackSetKeyStorageRegion( self, event ):
        if self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto:
            self.setKeyStorageRegionColor()

    def callbackAdvKeySettings( self, event ):
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            if self.checkIfSubWinHasBeenOpened():
                return
            if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                otpmkKeySettingsFrame = ui_settings_fixed_otpmk_key.secBootUiSettingsFixedOtpmkKey(None)
                otpmkKeySettingsFrame.SetTitle(uilang.kSubLanguageContentDict['otpmkKey_title'][self.languageIndex])
                otpmkKeySettingsFrame.Show(True)
            elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                userKeySettingsFrame = ui_settings_flexible_user_keys.secBootUiSettingsFlexibleUserKeys(None)
                userKeySettingsFrame.SetTitle(uilang.kSubLanguageContentDict['userKey_title'][self.languageIndex])
                userKeySettingsFrame.setNecessaryInfo(self.mcuDevice, self.tgt.flexspiNorMemBase)
                userKeySettingsFrame.Show(True)
            else:
                pass
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['keyGenError_onlyForHwCrypto'][self.languageIndex])

    def _doHwEncryption( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            self._RTyyyy_startGaugeTimer()
            if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FixedOtpmkKey:
                if self.connectStage == uidef.kConnectStage_Reset:
                    if not self.prepareForFixedOtpmkEncryption():
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_failToPrepareForSnvs'][self.languageIndex])
                    else:
                        status = True
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
            elif self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                self.encrypteImageUsingFlexibleUserKeys()
                status = True
            else:
                pass
            self._RTyyyy_stopGaugeTimer()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForHwCrypto'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_PrepHwCrypto, status)
        return status

    def callbackDoHwEncryption( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doHwEncryption()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doProgramSrk( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != RTyyyy_uidef.kSecureBootType_Development:
            if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and (not self.isCertEnabledForHwCrypto):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForHwCrypto'][self.languageIndex])
            else:
                if self.connectStage == uidef.kConnectStage_ExternalMemory or \
                   self.connectStage == uidef.kConnectStage_Reset:
                    self._RTyyyy_startGaugeTimer()
                    self.printLog("'Load SRK data' button is clicked")
                    if self.burnSrkData():
                        status = True
                    self._RTyyyy_stopGaugeTimer()
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operKeyError_srkNotForUnsigned'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_ProgSrk, status)
        return status

    def callbackProgramSrk( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doProgramSrk()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doProgramHwCryptoDek( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            if self.keyStorageRegion == RTyyyy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                if self.connectStage == uidef.kConnectStage_ExternalMemory or \
                   self.connectStage == uidef.kConnectStage_Reset:
                    self._RTyyyy_startGaugeTimer()
                    if self.burnBeeDekData():
                        status = True
                    self._RTyyyy_stopGaugeTimer()
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operKeyError_dekNotForSnvs'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operKeyError_dekOnlyForHwCrypto'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_OperHwCrypto, status)
        return status

    def callbackProgramHwCryptoDek( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doProgramHwCryptoDek()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _RTyyyy_doFlashImage( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        else:
            if self.connectStage == uidef.kConnectStage_Reset:
                self._RTyyyy_startGaugeTimer()
                self.printLog("'Load Bootable Image' button is clicked")
                if not self.RTyyyy_flashBootableImage():
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_failToFlashImage'][self.languageIndex])
                else:
                    self.isBootableAppAllowedToView = True
                    if self.burnBootDeviceFuses():
                        if (self.secureBootType == RTyyyy_uidef.kSecureBootType_HabAuth) or \
                           (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto and self.isCertEnabledForHwCrypto):
                            if self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed0 and \
                               self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed1:
                                self.enableHab()
                        if self.secureBootType == RTyyyy_uidef.kSecureBootType_BeeCrypto and self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
                            if self.burnBeeKeySel():
                                status = True
                        else:
                            status = True
                self._RTyyyy_stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_FlashImage, status)
        return status

    def RTyyyy_callbackFlashImage( self ):
        if not self.isToolRunAsEntryMode:
            self._RTyyyy_doFlashImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doFlashHabDek( self ):
        status = False
        if (self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto) and self.bootDevice != RTyyyy_uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHwCryptoError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType == RTyyyy_uidef.kSecureBootType_HabCrypto:
            if self.connectStage == uidef.kConnectStage_Reset:
                self._RTyyyy_startGaugeTimer()
                self.printLog("'Load KeyBlob Data' button is clicked")
                if self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed0 and \
                   self.mcuDeviceHabStatus != RTyyyy_fusedef.kHabStatus_Closed1:
                    if not self.isSbFileEnabledToGen:
                        self.enableHab()
                        self._RTyyyy_connectStateMachine()
                        while self.connectStage != uidef.kConnectStage_Reset:
                            self._RTyyyy_connectStateMachine()
                self.flashHabDekToGenerateKeyBlob()
                self.isBootableAppAllowedToView = True
                status = True
                self._RTyyyy_stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_keyBlobOnlyForHab'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_ProgDek, status)
        return status

    def callbackFlashHabDek( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doFlashHabDek()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def callbackSetEfuseLock( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseLockFrame = RT10yy_ui_efuse_lock.secBootUiEfuseLock(None)
        efuseLockFrame.SetTitle("eFuse 0x400 Lock")
        efuseLockFrame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseLockFrame.Show(True)

    def callbackEnterEfuseLock( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_LOCK)

    def callbackSetEfuseBootCfg0( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg0Frame = None
        if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            if self.tgt.flexspiNorEfuseBootCfg0Bits == 3:
                efuseBootCfg0Frame = RT10yy_ui_efuse_bootcfg0_flexspinor_3bits.secBootUiEfuseBootCfg0FlexspiNor3bits(None)
            elif self.tgt.flexspiNorEfuseBootCfg0Bits == 10:
                efuseBootCfg0Frame = RT10yy_ui_efuse_bootcfg0_flexspinor_10bits.secBootUiEfuseBootCfg0FlexspiNor10bits(None)
            elif self.tgt.flexspiNorEfuseBootCfg0Bits == 12:
                efuseBootCfg0Frame = RT10yy_ui_efuse_bootcfg0_flexspinor_12bits.secBootUiEfuseBootCfg0FlexspiNor12bits(None)
            else:
                pass
            efuseBootCfg0Frame.SetTitle("eFuse 0x450 Boot Cfg0 - FlexSPI NOR")
        else:
            uivar.setRuntimeSettings(False)
            return
        efuseBootCfg0Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg0Frame.Show(True)

    def callbackEnterEfuseBootCfg0( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_BOOT_CFG0)

    def callbackSetEfuseBootCfg1( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg1Frame = RT10yy_ui_efuse_bootcfg1.secBootUiEfuseBootCfg1(None)
        efuseBootCfg1Frame.SetTitle("eFuse 0x460 Boot Cfg1")
        efuseBootCfg1Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg1Frame.Show(True)

    def callbackEnterEfuseBootCfg1( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_BOOT_CFG1)

    def callbackSetEfuseBootCfg2( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg2Frame = RT10yy_ui_efuse_bootcfg2.secBootUiEfuseBootCfg2(None)
        efuseBootCfg2Frame.SetTitle("eFuse 0x470 Boot Cfg2")
        efuseBootCfg2Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg2Frame.Show(True)

    def callbackEnterEfuseBootCfg2( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_BOOT_CFG2)

    def callbackSetEfuseMiscConf0( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseMiscConf0Frame = RT10yy_ui_efuse_miscconf0.secBootUiEfuseMiscConf0(None)
        efuseMiscConf0Frame.SetTitle("eFuse 0x6d0 Misc Conf0")
        efuseMiscConf0Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseMiscConf0Frame.Show(True)

    def callbackEnterEfuseMiscConf0( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_MISC_CONF0)

    def callbackSetEfuseMiscConf1( self, event ):
        if self.checkIfSubWinHasBeenOpened():
            return
        efuseMiscConf1Frame = None
        if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor:
            efuseMiscConf1Frame = RT10yy_ui_efuse_miscconf1_flexspinor.secBootUiEfuseMiscConf1FlexspiNor(None)
            efuseMiscConf1Frame.SetTitle("eFuse 0x6e0 Misc Conf1 - FlexSPI NOR")
        else:
            uivar.setRuntimeSettings(False)
            return
        efuseMiscConf1Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseMiscConf1Frame.Show(True)

    def callbackEnterEfuseMiscConf1( self, event ):
        self.enterSettableEfuse(RTyyyy_fusedef.kEfuseIndex_MISC_CONF1)

    def _RTyyyy_doViewMem( self ):
        if self.connectStage == uidef.kConnectStage_Reset:
            if self.isBootableAppAllowedToView:
                self._RTyyyy_startGaugeTimer()
                self.RTyyyy_readProgrammedMemoryAndShow()
                self._RTyyyy_stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotFlashImage'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])

    def RTyyyy_callbackViewMem( self ):
        self._RTyyyy_doViewMem()

    def RTyyyy_switchToolRunMode( self ):
        self.applyFuseOperToRunMode()
        self.RTyyyy_setSecureBootButtonColor()
