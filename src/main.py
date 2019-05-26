#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import threading
import inspect
import ctypes
from mem import memcore
from ui import uidef
from ui import uivar
from ui import uilang
from fuse import fusedef
from ui import ui_cfg_flexspinor
from ui import ui_cfg_flexspinand
from ui import ui_cfg_semcnor
from ui import ui_cfg_semcnand
from ui import ui_cfg_usdhcsd
from ui import ui_cfg_usdhcmmc
from ui import ui_cfg_lpspinor
from ui import ui_cfg_dcd
from ui import ui_settings_cert
from ui import ui_settings_fixed_otpmk_key
from ui import ui_settings_flexible_user_keys
from ui import ui_efuse_lock
from ui import ui_efuse_bootcfg0_flexspinor_10bits
from ui import ui_efuse_bootcfg0_flexspinor_12bits
from ui import ui_efuse_bootcfg1
from ui import ui_efuse_bootcfg2
from ui import ui_efuse_miscconf0
from ui import ui_efuse_miscconf1_flexspinor

g_main_win = None
g_task_detectUsbhid = None
g_task_playSound = None
g_task_allInOneAction = None
g_task_accessMem = None
g_task_increaseGauge = None
g_task_showSettedEfuse = None

kRetryPingTimes = 5

kBootloaderType_Rom         = 0
kBootloaderType_Flashloader = 1

def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class secBootMain(memcore.secBootMem):

    def __init__(self, parent):
        memcore.secBootMem.__init__(self, parent)
        self.connectStage = uidef.kConnectStage_Rom
        self.isBootableAppAllowedToView = False
        self.lastTime = None
        self.isAllInOneActionTaskPending = False
        self.isAccessMemTaskPending = False
        self.accessMemType = ''
        self.isThereBoardConnection = False

    def _startGaugeTimer( self ):
        if not self.isAllInOneActionTaskPending:
            self.lastTime = time.time()
            self.initGauge()

    def _stopGaugeTimer( self ):
        if not self.isAllInOneActionTaskPending:
            self.deinitGauge()
            self.updateCostTime()

    def callbackSetMcuSeries( self, event ):
        self.setTargetSetupValue()

    def callbackSetMcuDevice( self, event ):
        self.setTargetSetupValue()
        self._setUartUsbPort()
        self.applyFuseOperToRunMode()
        needToPlaySound = False
        self.setSecureBootSeqColor(needToPlaySound)

    def callbackSetBootDevice( self, event ):
        self.setTargetSetupValue()
        needToPlaySound = False
        self.setSecureBootSeqColor(needToPlaySound)

    def _checkIfSubWinHasBeenOpened( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        if not runtimeSettings[0]:
            uivar.setRuntimeSettings(True)
            return False
        else:
            return True

    def callbackBootDeviceConfiguration( self, event ):
        if self.bootDevice == uidef.kBootDevice_FlexspiNor:
            if self.tgt.isSipFlexspiNorDevice:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['bootDeviceInfo_hasOnchipSerialNor'][self.languageIndex])
                return
        if self._checkIfSubWinHasBeenOpened():
            return
        if self.bootDevice == uidef.kBootDevice_FlexspiNor:
            flexspiNorFrame = ui_cfg_flexspinor.secBootUiCfgFlexspiNor(None)
            flexspiNorFrame.SetTitle(uilang.kSubLanguageContentDict['flexspinor_title'][self.languageIndex])
            flexspiNorFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_FlexspiNand:
            flexspiNandFrame = ui_cfg_flexspinand.secBootUiFlexspiNand(None)
            flexspiNandFrame.SetTitle(u"FlexSPI NAND Device Configuration")
            flexspiNandFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_SemcNor:
            semcNorFrame = ui_cfg_semcnor.secBootUiSemcNor(None)
            semcNorFrame.SetTitle(u"SEMC NOR Device Configuration")
            semcNorFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_SemcNand:
            semcNandFrame = ui_cfg_semcnand.secBootUiCfgSemcNand(None)
            semcNandFrame.SetTitle(uilang.kSubLanguageContentDict['semcnand_title'][self.languageIndex])
            semcNandFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_UsdhcSd:
            usdhcSdFrame = ui_cfg_usdhcsd.secBootUiUsdhcSd(None)
            usdhcSdFrame.SetTitle(uilang.kSubLanguageContentDict['usdhcsd_title'][self.languageIndex])
            usdhcSdFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_UsdhcMmc:
            usdhcMmcFrame = ui_cfg_usdhcmmc.secBootUiUsdhcMmc(None)
            usdhcMmcFrame.SetTitle(uilang.kSubLanguageContentDict['usdhcmmc_title'][self.languageIndex])
            usdhcMmcFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_LpspiNor:
            lpspiNorFrame = ui_cfg_lpspinor.secBootUiCfgLpspiNor(None)
            lpspiNorFrame.SetTitle(uilang.kSubLanguageContentDict['lpspinor_title'][self.languageIndex])
            lpspiNorFrame.Show(True)
        else:
            pass

    def callbackDeviceConfigurationData( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        dcdFrame = ui_cfg_dcd.secBootUiCfgDcd(None)
        dcdFrame.SetTitle(uilang.kSubLanguageContentDict['dcd_title'][self.languageIndex])
        dcdFrame.setNecessaryInfo(self.dcdBinFilename, self.dcdCfgFilename, self.dcdModelFolder)
        dcdFrame.Show(True)

    def _setUartUsbPort( self ):
        usbIdList = self.getUsbid()
        retryToDetectUsb = False
        showError = True
        self.setPortSetupValue(self.connectStage, usbIdList, retryToDetectUsb, showError)

    def callbackSetUartPort( self, event ):
        self._setUartUsbPort()

    def callbackSetUsbhidPort( self, event ):
        self._setUartUsbPort()

    def callbackSetOneStep( self, event ):
        if not self.isToolRunAsEntryMode:
            self.getOneStepConnectMode()
        else:
            self.initOneStepConnectMode()
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_cannotSetOneStep'][self.languageIndex])

    def _retryToPingBootloader( self, bootType ):
        pingStatus = False
        pingCnt = kRetryPingTimes
        while (not pingStatus) and pingCnt > 0:
            if bootType == kBootloaderType_Rom:
                pingStatus = self.pingRom()
            elif bootType == kBootloaderType_Flashloader:
                pingStatus = self.pingFlashloader()
            else:
                pass
            if pingStatus:
                break
            pingCnt = pingCnt - 1
            if self.isUsbhidPortSelected:
                time.sleep(2)
        return pingStatus

    def _connectFailureHandler( self ):
        self.connectStage = uidef.kConnectStage_Rom
        self.updateConnectStatus('red')
        usbIdList = self.getUsbid()
        self.setPortSetupValue(self.connectStage, usbIdList, False, False)
        self.isBootableAppAllowedToView = False

    def _connectStateMachine( self, showError=True ):
        connectSteps = uidef.kConnectStep_Normal
        self.getOneStepConnectMode()
        retryToDetectUsb = False
        if self.isOneStepConnectMode:
            if self.connectStage == uidef.kConnectStage_Reset or self.connectStage == uidef.kConnectStage_ExternalMemory:
                connectSteps = uidef.kConnectStep_Fast - 2
            elif self.connectStage == uidef.kConnectStage_Flashloader:
                connectSteps = uidef.kConnectStep_Fast - 1
                retryToDetectUsb = True
            elif self.connectStage == uidef.kConnectStage_Rom:
                connectSteps = uidef.kConnectStep_Fast
                retryToDetectUsb = True
            else:
                pass
        while connectSteps:
            if not self.updatePortSetupValue(retryToDetectUsb, showError):
                self._connectFailureHandler()
                return
            if self.connectStage == uidef.kConnectStage_Rom:
                self.connectToDevice(self.connectStage)
                if self._retryToPingBootloader(kBootloaderType_Rom):
                    self.getMcuDeviceInfoViaRom()
                    self.getMcuDeviceHabStatus()
                    if self.jumpToFlashloader():
                        self.connectStage = uidef.kConnectStage_Flashloader
                        self.updateConnectStatus('yellow')
                        usbIdList = self.getUsbid()
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
                self.connectToDevice(self.connectStage)
                if self._retryToPingBootloader(kBootloaderType_Flashloader):
                    self.getMcuDeviceInfoViaFlashloader()
                    self.getMcuDeviceBtFuseSel()
                    self.updateConnectStatus('green')
                    self.connectStage = uidef.kConnectStage_ExternalMemory
                else:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToPingFl'][self.languageIndex])
                    self._connectFailureHandler()
                    return
            elif self.connectStage == uidef.kConnectStage_ExternalMemory:
                if self.configureBootDevice():
                    self.getBootDeviceInfoViaFlashloader()
                    self.connectStage = uidef.kConnectStage_Reset
                    self.updateConnectStatus('blue')
                else:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToCfgBootDevice'][self.languageIndex])
                    self._connectFailureHandler()
                    return
            elif self.connectStage == uidef.kConnectStage_Reset:
                self.resetMcuDevice()
                self.isBootableAppAllowedToView = False
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
                usbIdList = self.getUsbid()
                self.setPortSetupValue(self.connectStage, usbIdList, True, True)
                self.connectToDevice(self.connectStage)
            else:
                pass
            connectSteps -= 1

    def callbackConnectToDevice( self, event ):
        self._startGaugeTimer()
        self.printLog("'Connect to xxx' button is clicked")
        if not self.isSbFileEnabledToGen:
            self._connectStateMachine(True)
        else:
            if not self.isThereBoardConnection:
                if self.connectStage == uidef.kConnectStage_Rom:
                    self.initSbAppBdfilesContent()
                else:
                    # It means there is board connection
                    self.isThereBoardConnection = True
                self._connectStateMachine(False)
                if not self.isThereBoardConnection:
                    if self.connectStage == uidef.kConnectStage_Rom:
                        # It means there is no board connection, but we need to set it as True for SB generation
                        self.isThereBoardConnection = True
                        self.connectToDevice(uidef.kConnectStage_Flashloader)
                        self.isDeviceEnabledToOperate = False
                        self.configureBootDevice()
                        self.connectStage = uidef.kConnectStage_Reset
                        self.updateConnectStatus('blue')
                else:
                    self.isThereBoardConnection = False
            else:
                self.isThereBoardConnection = False
                self.isDeviceEnabledToOperate = True
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
        self._stopGaugeTimer()

    def callbackSetSecureBootType( self, event ):
        self.setCostTime(0)
        self.setSecureBootSeqColor()

    def task_doAllInOneAction( self ):
        while True:
            if self.isAllInOneActionTaskPending:
                self._doAllInOneAction()
                self.isAllInOneActionTaskPending = False
                self._stopGaugeTimer()
            time.sleep(1)

    def _doAllInOneAction( self ):
        allInOneSeqCnt = 1
        directReuseCert = False
        status = False
        while allInOneSeqCnt:
            if self.secureBootType == uidef.kSecureBootType_HabAuth or \
               self.secureBootType == uidef.kSecureBootType_HabCrypto or \
               (self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor and self.isCertEnabledForBee):
                status = self._doGenCert(directReuseCert)
                if not status:
                    break
                status = self._doProgramSrk()
                if not status:
                    break
            status = self._doGenImage()
            if not status:
                break
            if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor:
                status = self._doBeeEncryption()
                if not status:
                    break
                if self.keyStorageRegion == uidef.kKeyStorageRegion_FlexibleUserKeys:
                    status = self._doProgramBeeDek()
                    if not status:
                        break
                elif self.keyStorageRegion == uidef.kKeyStorageRegion_FixedOtpmkKey:
                    if self.isCertEnabledForBee:
                        # If HAB is not closed here, we need to close HAB and re-do All-In-One Action
                        if self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed0 and \
                           self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed1:
                           if not self.isSbFileEnabledToGen:
                                self.enableHab()
                                self._connectStateMachine()
                                while self.connectStage != uidef.kConnectStage_Reset:
                                    self._connectStateMachine()
                                directReuseCert = True
                                allInOneSeqCnt += 1
                else:
                    pass
            status = self._doFlashImage()
            if not status:
                break
            if self.secureBootType == uidef.kSecureBootType_HabCrypto:
                status = self._doFlashHabDek()
                if not status:
                    break
            allInOneSeqCnt -= 1
        if self.isSbFileEnabledToGen:
            status = self.genSbAppImages()
        else:
            if status and self.isAutomaticImageReadback:
                self.showPageInMainBootSeqWin(uidef.kPageIndex_BootDeviceMemory)
                self._doViewMem()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_AllInOne, status)

    def callbackAllInOneAction( self, event ):
        self._startGaugeTimer()
        self.isAllInOneActionTaskPending = True

    def callbackAdvCertSettings( self, event ):
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != uidef.kSecureBootType_Development:
            if self.secureBootType == uidef.kSecureBootType_BeeCrypto and (not self.isCertEnabledForBee):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForBee'][self.languageIndex])
            else:
                if self._checkIfSubWinHasBeenOpened():
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
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != uidef.kSecureBootType_Development:
            if self.secureBootType == uidef.kSecureBootType_BeeCrypto and (not self.isCertEnabledForBee):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForBee'][self.languageIndex])
            else:
                self._startGaugeTimer()
                self.printLog("'Generate Certificate' button is clicked")
                self.updateAllCstPathToCorrectVersion()
                reuseCert = self._wantToReuseAvailableCert(directReuseCert)
                if reuseCert == None:
                    pass
                elif not reuseCert:
                    self.cleanUpCertificate()
                    if self.createSerialAndKeypassfile():
                        self.setSecureBootButtonColor()
                        self.genCertificate()
                        self.genSuperRootKeys()
                        self.showSuperRootKeys()
                        self.backUpCertificate()
                        status = True
                else:
                    status = True
                self._stopGaugeTimer()
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

    def callbackChangedAppFile( self, event ):
        self.getUserAppFilePath()
        self.setCostTime(0)
        self.setSecureBootButtonColor()

    def callbackSetAppFormat( self, event ):
        self.getUserAppFileFormat()

    def _doGenImage( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        else:
            self._startGaugeTimer()
            self.printLog("'Generate Bootable Image' button is clicked")
            if self.createMatchedAppBdfile():
                # Need to update image picture for DCD
                needToPlaySound = False
                self.setSecureBootSeqColor(needToPlaySound)
                if self.genBootableImage():
                    self.showHabDekIfApplicable()
                    status = True
            self._stopGaugeTimer()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_GenImage, status)
        return status

    def callbackGenImage( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doGenImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def callbackSetCertForBee( self, event ):
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto:
            self.setBeeCertColor()

    def callbackSetKeyStorageRegion( self, event ):
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto:
            self.setKeyStorageRegionColor()

    def callbackAdvKeySettings( self, event ):
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor:
            if self._checkIfSubWinHasBeenOpened():
                return
            if self.keyStorageRegion == uidef.kKeyStorageRegion_FixedOtpmkKey:
                otpmkKeySettingsFrame = ui_settings_fixed_otpmk_key.secBootUiSettingsFixedOtpmkKey(None)
                otpmkKeySettingsFrame.SetTitle(uilang.kSubLanguageContentDict['otpmkKey_title'][self.languageIndex])
                otpmkKeySettingsFrame.Show(True)
            elif self.keyStorageRegion == uidef.kKeyStorageRegion_FlexibleUserKeys:
                userKeySettingsFrame = ui_settings_flexible_user_keys.secBootUiSettingsFlexibleUserKeys(None)
                userKeySettingsFrame.SetTitle(uilang.kSubLanguageContentDict['userKey_title'][self.languageIndex])
                userKeySettingsFrame.setNecessaryInfo(self.mcuDevice, self.tgt.flexspiNorMemBase)
                userKeySettingsFrame.Show(True)
            else:
                pass
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['keyGenError_onlyForBee'][self.languageIndex])

    def _doBeeEncryption( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor:
            self._startGaugeTimer()
            if self.keyStorageRegion == uidef.kKeyStorageRegion_FixedOtpmkKey:
                if self.connectStage == uidef.kConnectStage_Reset:
                    if not self.prepareForFixedOtpmkEncryption():
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_failToPrepareForSnvs'][self.languageIndex])
                    else:
                        status = True
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
            elif self.keyStorageRegion == uidef.kKeyStorageRegion_FlexibleUserKeys:
                self.encrypteImageUsingFlexibleUserKeys()
                status = True
            else:
                pass
            self._stopGaugeTimer()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForBee'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_PrepBee, status)
        return status

    def callbackDoBeeEncryption( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doBeeEncryption()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doProgramSrk( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType != uidef.kSecureBootType_Development:
            if self.secureBootType == uidef.kSecureBootType_BeeCrypto and (not self.isCertEnabledForBee):
                self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_notEnabledForBee'][self.languageIndex])
            else:
                if self.connectStage == uidef.kConnectStage_ExternalMemory or \
                   self.connectStage == uidef.kConnectStage_Reset:
                    self._startGaugeTimer()
                    self.printLog("'Load SRK data' button is clicked")
                    if self.burnSrkData():
                        status = True
                    self._stopGaugeTimer()
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

    def _doProgramBeeDek( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor:
            if self.keyStorageRegion == uidef.kKeyStorageRegion_FlexibleUserKeys:
                if self.connectStage == uidef.kConnectStage_ExternalMemory or \
                   self.connectStage == uidef.kConnectStage_Reset:
                    self._startGaugeTimer()
                    if self.burnBeeDekData():
                        status = True
                    self._stopGaugeTimer()
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operKeyError_dekNotForSnvs'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operKeyError_dekOnlyForBee'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_OperBee, status)
        return status

    def callbackProgramBeeDek( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doProgramBeeDek()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doFlashImage( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        else:
            if self.connectStage == uidef.kConnectStage_Reset:
                self._startGaugeTimer()
                self.printLog("'Load Bootable Image' button is clicked")
                if not self.flashBootableImage():
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_failToFlashImage'][self.languageIndex])
                else:
                    self.isBootableAppAllowedToView = True
                    if self.burnBootDeviceFuses():
                        if (self.secureBootType == uidef.kSecureBootType_HabAuth) or \
                           (self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
                            if self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed0 and \
                               self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed1:
                                self.enableHab()
                        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice == uidef.kBootDevice_FlexspiNor:
                            if self.burnBeeKeySel():
                                status = True
                        else:
                            status = True
                self._stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_FlashImage, status)
        return status

    def callbackFlashImage( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doFlashImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _doFlashHabDek( self ):
        status = False
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.bootDevice != uidef.kBootDevice_FlexspiNor:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operBeeError_onlyForFlexspiNor'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto and \
             (self.bootDevice == uidef.kBootDevice_FlexspiNor or self.bootDevice == uidef.kBootDevice_SemcNor) and \
             (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operHabError_notAppliableDevice'][self.languageIndex])
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto:
            if self.connectStage == uidef.kConnectStage_Reset:
                self._startGaugeTimer()
                self.printLog("'Load KeyBlob Data' button is clicked")
                if self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed0 and \
                   self.mcuDeviceHabStatus != fusedef.kHabStatus_Closed1:
                    if not self.isSbFileEnabledToGen:
                        self.enableHab()
                        self._connectStateMachine()
                        while self.connectStage != uidef.kConnectStage_Reset:
                            self._connectStateMachine()
                self.flashHabDekToGenerateKeyBlob()
                self.isBootableAppAllowedToView = True
                status = True
                self._stopGaugeTimer()
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
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseLockFrame = ui_efuse_lock.secBootUiEfuseLock(None)
        efuseLockFrame.SetTitle("eFuse 0x400 Lock")
        efuseLockFrame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseLockFrame.Show(True)

    def callbackSetEfuseBootCfg0( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg0Frame = None
        if self.bootDevice == uidef.kBootDevice_FlexspiNor:
            if self.tgt.flexspiNorEfuseBootCfg0Bits == 10:
                efuseBootCfg0Frame = ui_efuse_bootcfg0_flexspinor_10bits.secBootUiEfuseBootCfg0FlexspiNor10bits(None)
            elif self.tgt.flexspiNorEfuseBootCfg0Bits == 12:
                efuseBootCfg0Frame = ui_efuse_bootcfg0_flexspinor_12bits.secBootUiEfuseBootCfg0FlexspiNor12bits(None)
            else:
                pass
            efuseBootCfg0Frame.SetTitle("eFuse 0x450 Boot Cfg0 - FlexSPI NOR")
        else:
            uivar.setRuntimeSettings(False)
            return
        efuseBootCfg0Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg0Frame.Show(True)

    def callbackSetEfuseBootCfg1( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg1Frame = ui_efuse_bootcfg1.secBootUiEfuseBootCfg1(None)
        efuseBootCfg1Frame.SetTitle("eFuse 0x460 Boot Cfg1")
        efuseBootCfg1Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg1Frame.Show(True)

    def callbackSetEfuseBootCfg2( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseBootCfg2Frame = ui_efuse_bootcfg2.secBootUiEfuseBootCfg2(None)
        efuseBootCfg2Frame.SetTitle("eFuse 0x470 Boot Cfg2")
        efuseBootCfg2Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseBootCfg2Frame.Show(True)

    def callbackSetEfuseMiscConf0( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseMiscConf0Frame = ui_efuse_miscconf0.secBootUiEfuseMiscConf0(None)
        efuseMiscConf0Frame.SetTitle("eFuse 0x6d0 Misc Conf0")
        efuseMiscConf0Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseMiscConf0Frame.Show(True)

    def callbackSetEfuseMiscConf1( self, event ):
        if self._checkIfSubWinHasBeenOpened():
            return
        efuseMiscConf1Frame = None
        if self.bootDevice == uidef.kBootDevice_FlexspiNor:
            efuseMiscConf1Frame = ui_efuse_miscconf1_flexspinor.secBootUiEfuseMiscConf1FlexspiNor(None)
            efuseMiscConf1Frame.SetTitle("eFuse 0x6e0 Misc Conf1 - FlexSPI NOR")
        else:
            uivar.setRuntimeSettings(False)
            return
        efuseMiscConf1Frame.setNecessaryInfo(self.tgt.efuseDescDiffDict)
        efuseMiscConf1Frame.Show(True)

    def task_doAccessMem( self ):
        while True:
            if self.isAccessMemTaskPending:
                if self.accessMemType == 'ScanFuse':
                    self.scanAllFuseRegions()
                    if self.isSbFileEnabledToGen:
                        self.initSbEfuseBdfileContent()
                elif self.accessMemType == 'BurnFuse':
                    self.burnAllFuseRegions()
                    if self.isSbFileEnabledToGen:
                        self.genSbEfuseImage()
                elif self.accessMemType == 'ReadMem':
                    if self.connectStage == uidef.kConnectStage_ExternalMemory:
                        self.readFlexramMemory()
                    elif self.connectStage == uidef.kConnectStage_Reset:
                        self.readBootDeviceMemory()
                    else:
                        pass
                elif self.accessMemType == 'EraseMem':
                    self.eraseBootDeviceMemory()
                elif self.accessMemType == 'WriteMem':
                    if self.connectStage == uidef.kConnectStage_ExternalMemory:
                        self.writeFlexramMemory()
                    elif self.connectStage == uidef.kConnectStage_Reset:
                        self.writeBootDeviceMemory()
                    else:
                        pass
                else:
                    pass
                self.isAccessMemTaskPending = False
                self._stopGaugeTimer()
            time.sleep(1)

    def callbackScanFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'ScanFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackBurnFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'BurnFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def _doViewMem( self ):
        if self.connectStage == uidef.kConnectStage_Reset:
            if self.isBootableAppAllowedToView:
                self._startGaugeTimer()
                self.readProgrammedMemoryAndShow()
                self._stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotFlashImage'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])

    def callbackViewMem( self, event ):
        self._doViewMem()

    def callbackClearMem( self, event ):
        self.clearMem()

    def _doReadMem( self ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'ReadMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackReadMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doReadMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def _doEraseMem( self ):
        if self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'EraseMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])

    def callbackEraseMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doEraseMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def _doWriteMem( self ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'WriteMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackWriteMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doWriteMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def callbackExecuteApp( self, event ):
        pass

    def callbackClearLog( self, event ):
        self.clearLog()

    def callbackSaveLog( self, event ):
        self.saveLog()

    def _stopTask( self, thread ):
        _async_raise(thread.ident, SystemExit)

    def _deinitToolToExit( self ):
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Tool, self.toolCommDict)
        uivar.deinitVar()
        #exit(0)
        self._stopTask(g_task_detectUsbhid)
        self._stopTask(g_task_playSound)
        self._stopTask(g_task_allInOneAction)
        self._stopTask(g_task_accessMem)
        self._stopTask(g_task_increaseGauge)
        self._stopTask(g_task_showSettedEfuse)
        global g_main_win
        g_main_win.Show(False)
        try:
            self.Destroy()
        except:
            pass

    def callbackExit( self, event ):
        self._deinitToolToExit()

    def callbackClose( self, event ):
        self._deinitToolToExit()

    def _switchToolRunMode( self ):
        self.applyFuseOperToRunMode()
        self.setSecureBootButtonColor()
        self.enableOneStepForEntryMode()

    def callbackSetRunModeAsEntry( self, event ):
        self.setToolRunMode()
        self._switchToolRunMode()

    def callbackSetRunModeAsMaster( self, event ):
        self.setToolRunMode()
        self._switchToolRunMode()

    def callbackSetUsbDetectionAsDynamic( self, event ):
        self.setUsbDetection()

    def callbackSetUsbDetectionAsStatic( self, event ):
        self.setUsbDetection()

    def callbackSetSoundEffectAsMario( self, event ):
        self.setSoundEffect()

    def callbackSetSoundEffectAsQuiet( self, event ):
        self.setSoundEffect()

    def callbackSetGenSbFileAsYes( self, event ):
        self.setGenSbFile()

    def callbackSetGenSbFileAsNo( self, event ):
        self.setGenSbFile()

    def callbackSetImageReadbackAsAutomatic( self, event ):
        self.setImageReadback()

    def callbackSetImageReadbackAsManual( self, event ):
        self.setImageReadback()

    def callbackSetLanguageAsEnglish( self, event ):
        self.setLanguage()

    def callbackSetLanguageAsChinese( self, event ):
        self.setLanguage()

    def callbackShowHomePage( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['homePage_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['homePage_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowAboutAuthor( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['aboutAuthor_author'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email1'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email2'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_blog'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['aboutAuthor_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowContributors( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['contributors_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['contributors_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowSpecialThanks( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['specialThanks_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['specialThanks_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowRevisionHistory( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['revisionHistory_v1_0_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_1_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_2_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_3_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_4_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_5_0'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['revisionHistory_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()

    g_main_win = secBootMain(None)
    g_main_win.SetTitle(u"NXP MCU Boot Utility v1.5.0")
    g_main_win.Show()

    g_task_detectUsbhid = threading.Thread(target=g_main_win.task_doDetectUsbhid)
    g_task_detectUsbhid.setDaemon(True)
    g_task_detectUsbhid.start()
    g_task_playSound = threading.Thread(target=g_main_win.task_doPlaySound)
    g_task_playSound.setDaemon(True)
    g_task_playSound.start()
    g_task_allInOneAction = threading.Thread(target=g_main_win.task_doAllInOneAction)
    g_task_allInOneAction.setDaemon(True)
    g_task_allInOneAction.start()
    g_task_accessMem = threading.Thread(target=g_main_win.task_doAccessMem)
    g_task_accessMem.setDaemon(True)
    g_task_accessMem.start()
    g_task_increaseGauge = threading.Thread(target=g_main_win.task_doIncreaseGauge)
    g_task_increaseGauge.setDaemon(True)
    g_task_increaseGauge.start()
    g_task_showSettedEfuse = threading.Thread(target=g_main_win.task_doShowSettedEfuse)
    g_task_showSettedEfuse.setDaemon(True)
    g_task_showSettedEfuse.start()

    app.MainLoop()
