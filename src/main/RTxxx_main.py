#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
sys.path.append(os.path.abspath(".."))
from mem import RTxxx_memcore
from ui import RTxxx_uidef
from ui import uidef
from ui import uivar
from ui import uilang

kRetryPingTimes = 5

class secBootRTxxxMain(RTxxx_memcore.secBootRTxxxMem):

    def __init__(self, parent):
        RTxxx_memcore.secBootRTxxxMem.__init__(self, parent)
        self.RTxxx_isAllInOneActionTaskPending = False
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self._RTxxx_initMain()

    def _RTxxx_initMain( self ):
        self.connectStage = uidef.kConnectStage_Rom
        self.isBootableAppAllowedToView = False
        self.lastTime = None
        self.isAccessMemTaskPending = False
        self.accessMemType = ''
        self.isThereBoardConnection = False

    def _RTxxx_startGaugeTimer( self ):
        if not self.RTxxx_isAllInOneActionTaskPending:
            self.lastTime = time.time()
            self.initGauge()

    def _RTxxx_stopGaugeTimer( self ):
        if not self.RTxxx_isAllInOneActionTaskPending:
            self.deinitGauge()
            self.updateCostTime()

    def RTxxx_callbackSetMcuSeries( self ):
        self.RTxxx_initUi()
        self.RTxxx_initGen()
        self.RTxxx_initRun()
        self._RTxxx_initMain()
        self.RTxxx_setTargetSetupValue()

    def RTxxx_callbackSetMcuDevice( self ):
        self.RTxxx_setTargetSetupValue()
        needToPlaySound = False
        self.RTxxx_setSecureBootSeqColor(needToPlaySound)

    def RTxxx_callbackSetBootDevice( self ):
        self.RTxxx_setTargetSetupValue()
        needToPlaySound = False
        self.RTxxx_setSecureBootSeqColor(needToPlaySound)

    def _RTxxx_retryToPingBootloader( self ):
        pingStatus = False
        pingCnt = kRetryPingTimes
        while (not pingStatus) and pingCnt > 0:
            pingStatus = self.RTxxx_pingRom()
            if pingStatus:
                break
            pingCnt = pingCnt - 1
            if self.isUsbhidPortSelected:
                time.sleep(2)
        return pingStatus

    def _RTxxx_connectFailureHandler( self ):
        self.connectStage = uidef.kConnectStage_Rom
        self.updateConnectStatus('red')
        usbIdList = self.RTxxx_getUsbid()
        self.setPortSetupValue(self.connectStage, usbIdList, False, False)
        self.isBootableAppAllowedToView = False

    def _RTxxx_connectStateMachine( self, showError=True ):
        connectSteps = RTxxx_uidef.kConnectStep_Normal
        self.getOneStepConnectMode()
        retryToDetectUsb = False
        if self.isOneStepConnectMode:
            if self.connectStage == uidef.kConnectStage_Reset or self.connectStage == uidef.kConnectStage_ExternalMemory:
                connectSteps = RTxxx_uidef.kConnectStep_Fast - 1
            elif self.connectStage == uidef.kConnectStage_Rom:
                connectSteps = RTxxx_uidef.kConnectStep_Fast
                retryToDetectUsb = True
            else:
                pass
        while connectSteps:
            if not self.updatePortSetupValue(retryToDetectUsb, showError):
                self._RTxxx_connectFailureHandler()
                return
            if self.connectStage == uidef.kConnectStage_Rom:
                self.RTxxx_connectToDevice(self.connectStage)
                if self._RTxxx_retryToPingBootloader():
                    self.RTxxx_getMcuDeviceInfoViaRom()
                    self.updateConnectStatus('green')
                    self.connectStage = uidef.kConnectStage_ExternalMemory
                else:
                    self.updateConnectStatus('red')
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_doubleCheckBmod'][self.languageIndex])
                    return
            elif self.connectStage == uidef.kConnectStage_ExternalMemory:
                if self.RTxxx_configureBootDevice():
                    self.RTxxx_getBootDeviceInfoViaRom()
                    self.connectStage = uidef.kConnectStage_Reset
                    self.updateConnectStatus('blue')
                else:
                    if showError:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_failToCfgBootDevice'][self.languageIndex])
                    self._RTxxx_connectFailureHandler()
                    return
            elif self.connectStage == uidef.kConnectStage_Reset:
                self.RTxxx_resetMcuDevice()
                self.isBootableAppAllowedToView = False
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
                usbIdList = self.RTxxx_getUsbid()
                self.setPortSetupValue(self.connectStage, usbIdList, True, True)
                self.RTxxx_connectToDevice(self.connectStage)
            else:
                pass
            connectSteps -= 1

    def RTxxx_callbackConnectToDevice( self ):
        self._RTxxx_startGaugeTimer()
        self.printLog("'Connect to xxx' button is clicked")
        if not self.isSbFileEnabledToGen:
            self._RTxxx_connectStateMachine(True)
        else:
            if not self.isThereBoardConnection:
                if self.connectStage == uidef.kConnectStage_Rom:
                    self.initSbAppBdfilesContent()
                else:
                    # It means there is board connection
                    self.isThereBoardConnection = True
                self._RTxxx_connectStateMachine(False)
                if not self.isThereBoardConnection:
                    if self.connectStage == uidef.kConnectStage_Rom:
                        # It means there is no board connection, but we need to set it as True for SB generation
                        self.isThereBoardConnection = True
                        self.RTxxx_isDeviceEnabledToOperate = False
                        self.RTxxx_configureBootDevice()
                        self.connectStage = uidef.kConnectStage_Reset
                        self.updateConnectStatus('blue')
                else:
                    self.isThereBoardConnection = False
            else:
                self.isThereBoardConnection = False
                self.RTxxx_isDeviceEnabledToOperate = True
                self.connectStage = uidef.kConnectStage_Rom
                self.updateConnectStatus('black')
        self._RTxxx_stopGaugeTimer()

    def RTxxx_callbackSetSecureBootType( self ):
        self.setCostTime(0)
        self.RTxxx_setSecureBootSeqColor()

    def RTxxx_task_doAllInOneAction( self ):
        while True:
            if self.RTxxx_isAllInOneActionTaskPending:
                self._RTxxx_doAllInOneAction()
                self.RTxxx_isAllInOneActionTaskPending = False
                self._RTxxx_stopGaugeTimer()
            time.sleep(1)

    def _RTxxx_doAllInOneAction( self ):
        allInOneSeqCnt = 1
        status = False
        while allInOneSeqCnt:
            status = self._RTxxx_doGenImage()
            if not status:
                break
            status = self._RTxxx_doFlashImage()
            if not status:
                break
            allInOneSeqCnt -= 1
        if status and self.isAutomaticImageReadback:
            self.showPageInMainBootSeqWin(uidef.kPageIndex_BootDeviceMemory)
            self._RTxxx_doViewMem()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_AllInOne, status)

    def RTxxx_callbackAllInOneAction( self ):
        self._RTxxx_startGaugeTimer()
        self.RTxxx_isAllInOneActionTaskPending = True

    def _RTxxx_doGenImage( self ):
        status = False
        self._RTxxx_startGaugeTimer()
        self.printLog("'Generate Bootable Image' button is clicked")
        if self.createMatchedAppJsonfile():
            if self.RTxxx_genBootableImage():
                status = True
        self._RTxxx_stopGaugeTimer()
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_GenImage, status)
        return status

    def RTxxx_callbackGenImage( self ):
        if not self.isToolRunAsEntryMode:
            self._RTxxx_doGenImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _RTxxx_doFlashImage( self ):
        status = False
        if self.connectStage == uidef.kConnectStage_Reset:
            self._RTxxx_startGaugeTimer()
            self.printLog("'Load Bootable Image' button is clicked")
            if not self.RTxxx_flashBootableImage():
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_failToFlashImage'][self.languageIndex])
            else:
                self.isBootableAppAllowedToView = True
                status = True
            self._RTxxx_stopGaugeTimer()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])
        self.invalidateStepButtonColor(uidef.kSecureBootSeqStep_FlashImage, status)
        return status

    def RTxxx_callbackFlashImage( self ):
        if not self.isToolRunAsEntryMode:
            self._RTxxx_doFlashImage()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['separActnError_notAvailUnderEntry'][self.languageIndex])

    def _RTxxx_doViewMem( self ):
        if self.connectStage == uidef.kConnectStage_Reset:
            if self.isBootableAppAllowedToView:
                self._RTxxx_startGaugeTimer()
                self.RTxxx_readProgrammedMemoryAndShow()
                self._RTxxx_stopGaugeTimer()
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotFlashImage'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])

    def RTxxx_callbackViewMem( self ):
        self._RTxxx_doViewMem()

    def RTxxx_switchToolRunMode( self ):
        pass

