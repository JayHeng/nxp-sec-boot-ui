#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import json
import sys
import os
import time
import RTyyyy_fusedef
import collections

sys.path.append(os.path.abspath(".."))
from run import RTyyyy_runcore
from run import RTyyyy_rundef
from ui import RTyyyy_uidef
from ui import uicore
from ui import uidef
from ui import uivar
from ui import uilang
from operator import itemgetter

class secBootRTyyyyFuse(RTyyyy_runcore.secBootRTyyyyRun):

    def __init__(self, parent):
        RTyyyy_runcore.secBootRTyyyyRun.__init__(self, parent)
        self.needToScanFuse = None
        self.scannedFuseList = [None] * RTyyyy_fusedef.kMaxEfuseWords
        self.toBeBurnnedFuseList = [None] * RTyyyy_fusedef.kMaxEfuseWords
        self.runModeFuseFlagList = [None] * RTyyyy_fusedef.kMaxEfuseWords
        self.toBeRefreshedFuseList = [False] * RTyyyy_fusedef.kMaxEfuseWords
        self.isRunModeFuseFlagRemapped = False
        self.loadedFuseList = [None] * RTyyyy_fusedef.kMaxEfuseWords
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_initFuse()

    def RTyyyy_initFuse( self ):
        self.applyFuseOperToRunMode()
        self.updateFuseGroupText()

    def _initEntryModeFuseFlag( self ):
        if self.isToolRunAsEntryMode:
            for i in range(RTyyyy_fusedef.kMaxEfuseWords):
                if (i >= RTyyyy_fusedef.kEfuseEntryModeRegion0IndexStart and i <= RTyyyy_fusedef.kEfuseEntryModeRegion0IndexEnd) or \
                   (i >= RTyyyy_fusedef.kEfuseEntryModeRegion1IndexStart and i <= RTyyyy_fusedef.kEfuseEntryModeRegion1IndexEnd) or \
                   (i >= RTyyyy_fusedef.kEfuseEntryModeRegion2IndexStart and i <= RTyyyy_fusedef.kEfuseEntryModeRegion2IndexEnd) or \
                   (i >= RTyyyy_fusedef.kEfuseEntryModeRegion3IndexStart and i <= RTyyyy_fusedef.kEfuseEntryModeRegion3IndexEnd) or \
                   (i >= RTyyyy_fusedef.kEfuseEntryModeRegion4IndexStart and i <= RTyyyy_fusedef.kEfuseEntryModeRegion4IndexEnd):
                    self.runModeFuseFlagList[i] = True
                else:
                    self.runModeFuseFlagList[i] = False
        else:
            for i in range(RTyyyy_fusedef.kMaxEfuseWords):
                self.runModeFuseFlagList[i] = True

    def applyFuseOperToRunMode( self ):
        self._initEntryModeFuseFlag()
        self.updateFuseRegionField()
        self.isRunModeFuseFlagRemapped = False
        self.needToScanFuse = True

    def _remapRunModeFuseFlagList( self ):
        if self.isRunModeFuseFlagRemapped:
            return
        if self.tgt.hasRemappedFuse:
            for i in range(RTyyyy_fusedef.kEfuseRemapLen):
                self.runModeFuseFlagList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i], self.runModeFuseFlagList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.runModeFuseFlagList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i], self.runModeFuseFlagList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i]
            self.isRunModeFuseFlagRemapped = True
        else:
            pass

    def _swapRemappedScannedFuseIfAppliable( self ):
        if self.tgt.hasRemappedFuse:
            for i in range(RTyyyy_fusedef.kEfuseRemapLen):
                self.scannedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i], self.scannedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.scannedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i], self.scannedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i]
        else:
            pass

    def scanAllFuseRegions( self, needSwapAndShow=True, isRefreshOpt=False ):
        self.needToScanFuse = False
        hasRefreshFuse = False
        self._remapRunModeFuseFlagList()
        for i in range(RTyyyy_fusedef.kMaxEfuseWords):
            if self.runModeFuseFlagList[i]:
                if not isRefreshOpt:
                    self.scannedFuseList[i] = self.readMcuDeviceFuseByBlhost(self.tgt.efusemapIndexDict['kEfuseIndex_START'] + i, '', False)
                elif self.toBeRefreshedFuseList[i]:
                    self.scannedFuseList[i] = self.readMcuDeviceFuseByBlhost(self.tgt.efusemapIndexDict['kEfuseIndex_START'] + i, '', False)
                    self.toBeRefreshedFuseList[i] = False
                    hasRefreshFuse = True
            else:
                self.scannedFuseList[i] = None
        if isRefreshOpt and (not hasRefreshFuse):
            return
        if needSwapAndShow:
            self._swapRemappedScannedFuseIfAppliable()
            self.showScannedFuses(self.scannedFuseList)

    def _swapRemappedToBeBurnFuseIfAppliable( self ):
        if self.tgt.hasRemappedFuse:
            for i in range(RTyyyy_fusedef.kEfuseRemapLen):
                self.toBeBurnnedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i], self.toBeBurnnedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.toBeBurnnedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Dest + i], self.toBeBurnnedFuseList[RTyyyy_fusedef.kEfuseRemapIndex_Src + i]
        else:
            pass

    def _burnFuseLockRegion( self, srcFuseValue, destFuseValue ):
        destFuseValue = destFuseValue | srcFuseValue
        # High-4bits cannot be burned along with low-28bits for fuse lock region, this is design limitation
        srcLock = srcFuseValue & RTyyyy_fusedef.kEfuseMask_LockLow
        destLock = destFuseValue & RTyyyy_fusedef.kEfuseMask_LockLow
        if srcLock != destLock:
            # Don't allow to lock Fuse SRK because SRK will be OP+RP+WP if lock bit is set and then ROM cannot get SRK
            if ((srcLock & RTyyyy_fusedef.kEfuseMask_LockSrk) == 0) and \
               ((destLock & RTyyyy_fusedef.kEfuseMask_LockSrk) != 0):
                destLock = destLock & (~RTyyyy_fusedef.kEfuseMask_LockSrk)
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_cannotBurnSrkLock'][self.languageIndex])
            self.burnMcuDeviceFuseByBlhost(self.tgt.efusemapIndexDict['kEfuseIndex_LOCK'], destLock, RTyyyy_rundef.kActionFrom_BurnFuse)
        srcLock = srcFuseValue & RTyyyy_fusedef.kEfuseMask_LockHigh
        destLock = destFuseValue & RTyyyy_fusedef.kEfuseMask_LockHigh
        if srcLock != destLock:
            self.burnMcuDeviceFuseByBlhost(self.tgt.efusemapIndexDict['kEfuseIndex_LOCK'], destLock, RTyyyy_rundef.kActionFrom_BurnFuse)

    def burnAllFuseRegions( self ):
        self.toBeBurnnedFuseList = self.getUserFuses()
        self._swapRemappedToBeBurnFuseIfAppliable()
        self._remapRunModeFuseFlagList()
        if self.needToScanFuse:
            self.scanAllFuseRegions(False)
        else:
            self._swapRemappedScannedFuseIfAppliable()
        for i in range(RTyyyy_fusedef.kMaxEfuseWords):
            if self.runModeFuseFlagList[i]:
                if self.toBeBurnnedFuseList[i] != self.scannedFuseList[i] and \
                   self.toBeBurnnedFuseList[i] != None and \
                   self.scannedFuseList[i] != None:
                    if i == self.tgt.efusemapIndexDict['kEfuseIndex_LOCK']:
                        self._burnFuseLockRegion(self.scannedFuseList[i], self.toBeBurnnedFuseList[i])
                    else:
                        fuseValue = self.toBeBurnnedFuseList[i] | self.scannedFuseList[i]
                        self.burnMcuDeviceFuseByBlhost(self.tgt.efusemapIndexDict['kEfuseIndex_START'] + i, fuseValue, RTyyyy_rundef.kActionFrom_BurnFuse)
                    self.toBeRefreshedFuseList[i] = True
        self.scanAllFuseRegions(True, True)

    def RTyyyy_task_doShowSettedEfuse( self ):
        while True:
            if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
                efuseDict = uivar.getEfuseSettings()
                if efuseDict['0x400_lock'] != self.toBeBurnnedFuseList[0]:
                    self.toBeBurnnedFuseList[0] = efuseDict['0x400_lock']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_LOCK'], efuseDict['0x400_lock'])
                if efuseDict['0x450_bootCfg0'] != self.toBeBurnnedFuseList[5]:
                    self.toBeBurnnedFuseList[5] = efuseDict['0x450_bootCfg0']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG0'], efuseDict['0x450_bootCfg0'])
                if efuseDict['0x460_bootCfg1'] != self.toBeBurnnedFuseList[6]:
                    self.toBeBurnnedFuseList[6] = efuseDict['0x460_bootCfg1']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG1'], efuseDict['0x460_bootCfg1'])
                if efuseDict['0x470_bootCfg2'] != self.toBeBurnnedFuseList[7]:
                    self.toBeBurnnedFuseList[7] = efuseDict['0x470_bootCfg2']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_BOOT_CFG2'], efuseDict['0x470_bootCfg2'])
                if efuseDict['0x6d0_miscConf0'] != self.toBeBurnnedFuseList[45]:
                    self.toBeBurnnedFuseList[45] = efuseDict['0x6d0_miscConf0']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF0'], efuseDict['0x6d0_miscConf0'])
                if efuseDict['0x6e0_miscConf1'] != self.toBeBurnnedFuseList[46]:
                    self.toBeBurnnedFuseList[46] = efuseDict['0x6e0_miscConf1']
                    self.showSettedEfuse(self.tgt.efusemapIndexDict['kEfuseIndex_MISC_CONF1'], efuseDict['0x6e0_miscConf1'])
            time.sleep(0.5)

    def saveFuseRegions( self ):
        if os.path.isfile(self.fuseSettingFilename):
            with open(self.fuseSettingFilename, 'r+') as fileObj:
                FuseMapJson = json.load(fileObj)
                FuseMapDict = FuseMapJson["FuseMAP"][0]
                fileObj.close()
            self.saveFuselist = [None] * RTyyyy_fusedef.kMaxEfuseWords
            self.saveFuselist = self.getUserFuses()
            with open(self.fuseSettingFilename, 'w') as fileObj:
                FuseMapDict = collections.OrderedDict(sorted(FuseMapDict.iteritems(), key=itemgetter(0), reverse=False))
                num = 0
                for key in FuseMapDict:
                    FuseMapDict[key] = self.saveFuselist[num]
                    num = num + 1
                num = 0
                for key in FuseMapDict:
                    if self.saveFuselist[num] == None:
                        FuseMapDict[key] = "None"
                    else:
                        FuseMapDict[key] = (str(hex(self.saveFuselist[num])))[2:10]
                    num = num + 1
                cfgDict = {
                    "FuseMAP": [FuseMapDict]
                }
                json.dump(cfgDict, fileObj, indent=1)
                fileObj.close()

    def loadFuseRegions( self ):
        if os.path.isfile(self.fuseSettingFilename):
            with open(self.fuseSettingFilename, 'r') as fileObj:
                FuseMapJson = json.load(fileObj)
                FuseMapDict = FuseMapJson["FuseMAP"][0]
                fileObj.close()
                FuseMapDict = collections.OrderedDict(sorted(FuseMapDict.iteritems(), key=itemgetter(0), reverse=False))
            num = 0
            for key in FuseMapDict:
                self.loadedFuseList[num] = FuseMapDict[key]
                num = num + 1
            for i in range(RTyyyy_fusedef.kMaxEfuseWords):
                if self.loadedFuseList[i] == "None":
                    self.loadedFuseList[i] = None
                else:
                    self.loadedFuseList[i] = int(self.loadedFuseList[i], 16)
        self.showScannedFuses(self.loadedFuseList)







