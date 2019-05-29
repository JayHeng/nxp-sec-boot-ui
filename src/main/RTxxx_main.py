#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
sys.path.append(os.path.abspath(".."))
from run import RTxxx_runcore
from ui import RTxxx_uidef
from ui import uidef

kRetryPingTimes = 5

class secBootRTxxxMain(RTxxx_runcore.secBootRTxxxRun):

    def __init__(self, parent):
        RTxxx_runcore.secBootRTxxxRun.__init__(self, parent)
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

    def RTxxx_callbackSetBootDevice( self ):
        self.RTxxx_setTargetSetupValue()

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

    def RTxxx_task_doAllInOneAction( self ):
        while True:
            if self.RTxxx_isAllInOneActionTaskPending:
                self._RTxxx_doAllInOneAction()
                self.RTxxx_isAllInOneActionTaskPending = False
                self._RTxxx_stopGaugeTimer()
            time.sleep(1)

    def _RTxxx_doAllInOneAction( self ):
        pass

    def RTxxx_callbackAllInOneAction( self, event ):
        self._RTxxx_startGaugeTimer()
        self.RTxxx_isAllInOneActionTaskPending = True

    def RTxxx_switchToolRunMode( self ):
        pass

