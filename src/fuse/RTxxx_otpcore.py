#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import json
import sys
import os
import time
from fuse import RTxxx_otpdef
import collections

sys.path.append(os.path.abspath(".."))
from run import RTxxx_runcore
from run import RTxxx_rundef
from ui import RTxxx_uidef
from ui import uicore
from ui import uidef
from ui import uivar
from ui import uilang
from operator import itemgetter

class secBootRTxxxOtp(RTxxx_runcore.secBootRTxxxRun):

    def __init__(self, parent):
        RTxxx_runcore.secBootRTxxxRun.__init__(self, parent)
        self.needToScanOtp = None
        self.scannedOtpList = [None] * RTxxx_otpdef.kTotalOtpWords
        self.toBeBurnnedOtpList = [None] * RTxxx_otpdef.kTotalOtpWords
        self.runModeOtpFlagList = [None] * RTxxx_otpdef.kTotalOtpWords
        self.toBeRefreshedOtpList = [False] * RTxxx_otpdef.kTotalOtpWords
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initOtp()

    def RTxxx_initOtp( self ):
        self.applyOtpOperToRunMode()
        self.RTxxx_updateOtpGroupText()

    def _initEntryModeOtpFlag( self ):
        if self.isToolRunAsEntryMode:
            for i in range(RTxxx_otpdef.kTotalOtpWords):
                idx = i + self.tgt.otpmapIndexDict['kOtpIndex_START']
                if (idx >= self.tgt.otpmapIndexDict['kOtpEntryModeRegion0IndexStart'] and idx <= self.tgt.otpmapIndexDict['kOtpEntryModeRegion0IndexEnd']) or \
                   (idx >= self.tgt.otpmapIndexDict['kOtpEntryModeRegion1IndexStart'] and idx <= self.tgt.otpmapIndexDict['kOtpEntryModeRegion1IndexEnd']) :
                    self.runModeOtpFlagList[i] = True
                else:
                    self.runModeOtpFlagList[i] = False
        else:
            for i in range(RTxxx_otpdef.kTotalOtpWords):
                self.runModeOtpFlagList[i] = True

    def applyOtpOperToRunMode( self ):
        self._initEntryModeOtpFlag()
        self.RTxxx_updateOtpRegionField()
        self.needToScanOtp = True

    def RTxxx_scanAllOtpRegions( self, needShow=True, isRefreshOpt=False ):
        self.needToScanOtp = False
        hasRefreshOtp = False
        curOtpGroupStartIndex = self.efuseGroupSel * RTxxx_otpdef.kGroupOtpWords
        nxtOtpGroupStartIndex = (self.efuseGroupSel + 1) * RTxxx_otpdef.kGroupOtpWords
        for i in range(RTxxx_otpdef.kGroupOtpWords):
            idx = curOtpGroupStartIndex + i
            if self.runModeOtpFlagList[idx]:
                if not isRefreshOpt:
                    self.scannedOtpList[idx] = self.RTxxx_readMcuDeviceOtpByBlhost(self.tgt.otpmapIndexDict['kOtpIndex_START'] + idx, '', False)
                elif self.toBeRefreshedOtpList[idx]:
                    self.scannedOtpList[idx] = self.RTxxx_readMcuDeviceOtpByBlhost(self.tgt.otpmapIndexDict['kOtpIndex_START'] + idx, '', False)
                    self.toBeRefreshedOtpList[idx] = False
                    hasRefreshOtp = True
            else:
                self.scannedOtpList[idx] = None
        if isRefreshOpt and (not hasRefreshOtp):
            return
        if needShow:
            self.RTxxx_showScannedOtps(self.scannedOtpList[curOtpGroupStartIndex:nxtOtpGroupStartIndex])

    def RTxxx_burnAllOtpRegions( self ):
        curOtpGroupStartIndex = self.efuseGroupSel * RTxxx_otpdef.kGroupOtpWords
        nxtOtpGroupStartIndex = (self.efuseGroupSel + 1) * RTxxx_otpdef.kGroupOtpWords
        self.toBeBurnnedOtpList[curOtpGroupStartIndex:nxtOtpGroupStartIndex] = self.getUserFuses()
        if self.needToScanOtp:
            self.RTxxx_scanAllOtpRegions(False)
        for i in range(RTxxx_otpdef.kGroupOtpWords):
            idx = curOtpGroupStartIndex + i
            if self.runModeOtpFlagList[idx]:
                if self.toBeBurnnedOtpList[idx] != self.scannedOtpList[idx] and \
                   self.toBeBurnnedOtpList[idx] != None and \
                   self.scannedOtpList[idx] != None:
                    otpValue = self.toBeBurnnedOtpList[idx] | self.scannedOtpList[idx]
                    self.RTxxx_burnMcuDeviceOtpByBlhost(self.tgt.otpmapIndexDict['kOtpIndex_START'] + idx, otpValue, RTxxx_rundef.kActionFrom_BurnOtp)
                    self.toBeRefreshedOtpList[idx] = True
        self.RTxxx_scanAllOtpRegions(True, True)

