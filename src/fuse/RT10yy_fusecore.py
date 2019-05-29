#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import time
import RT10yy_fusedef
sys.path.append(os.path.abspath(".."))
from run import RT10yy_runcore
from run import RT10yy_rundef
from ui import RT10yy_uidef
from ui import uidef
from ui import uivar
from ui import uilang

class secBootRT10yyFuse(RT10yy_runcore.secBootRT10yyRun):

    def __init__(self, parent):
        RT10yy_runcore.secBootRT10yyRun.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.RT10yy_initFuse()

    def RT10yy_initFuse( self ):
        self.needToScanFuse = None
        self.scannedFuseList = [None] * RT10yy_fusedef.kMaxEfuseWords
        self.toBeBurnnedFuseList = [None] * RT10yy_fusedef.kMaxEfuseWords
        self.runModeFuseFlagList = [None] * RT10yy_fusedef.kMaxEfuseWords
        self.toBeRefreshedFuseList = [False] * RT10yy_fusedef.kMaxEfuseWords
        self.isRunModeFuseFlagRemapped = False

        self.applyFuseOperToRunMode()

    def _initEntryModeFuseFlag( self ):
        if self.isToolRunAsEntryMode:
            for i in range(RT10yy_fusedef.kMaxEfuseWords):
                if (i >= RT10yy_fusedef.kEfuseEntryModeRegion0IndexStart and i <= RT10yy_fusedef.kEfuseEntryModeRegion0IndexEnd) or \
                   (i >= RT10yy_fusedef.kEfuseEntryModeRegion1IndexStart and i <= RT10yy_fusedef.kEfuseEntryModeRegion1IndexEnd) or \
                   (i >= RT10yy_fusedef.kEfuseEntryModeRegion2IndexStart and i <= RT10yy_fusedef.kEfuseEntryModeRegion2IndexEnd) or \
                   (i >= RT10yy_fusedef.kEfuseEntryModeRegion3IndexStart and i <= RT10yy_fusedef.kEfuseEntryModeRegion3IndexEnd) or \
                   (i >= RT10yy_fusedef.kEfuseEntryModeRegion4IndexStart and i <= RT10yy_fusedef.kEfuseEntryModeRegion4IndexEnd):
                    self.runModeFuseFlagList[i] = True
                else:
                    self.runModeFuseFlagList[i] = False
        else:
            for i in range(RT10yy_fusedef.kMaxEfuseWords):
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
            for i in range(RT10yy_fusedef.kEfuseRemapLen):
                self.runModeFuseFlagList[RT10yy_fusedef.kEfuseRemapIndex_Src + i], self.runModeFuseFlagList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.runModeFuseFlagList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i], self.runModeFuseFlagList[RT10yy_fusedef.kEfuseRemapIndex_Src + i]
            self.isRunModeFuseFlagRemapped = True
        else:
            pass

    def _swapRemappedScannedFuseIfAppliable( self ):
        if self.tgt.hasRemappedFuse:
            for i in range(RT10yy_fusedef.kEfuseRemapLen):
                self.scannedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Src + i], self.scannedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.scannedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i], self.scannedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Src + i]
        else:
            pass

    def scanAllFuseRegions( self, needSwapAndShow=True, isRefreshOpt=False ):
        self.needToScanFuse = False
        hasRefreshFuse = False
        self._remapRunModeFuseFlagList()
        for i in range(RT10yy_fusedef.kMaxEfuseWords):
            if self.runModeFuseFlagList[i]:
                if not isRefreshOpt:
                    self.scannedFuseList[i] = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_START + i, '', False)
                elif self.toBeRefreshedFuseList[i]:
                    self.scannedFuseList[i] = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_START + i, '', False)
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
            for i in range(RT10yy_fusedef.kEfuseRemapLen):
                self.toBeBurnnedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Src + i], self.toBeBurnnedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i] = \
                self.toBeBurnnedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Dest + i], self.toBeBurnnedFuseList[RT10yy_fusedef.kEfuseRemapIndex_Src + i]
        else:
            pass

    def _burnFuseLockRegion( self, srcFuseValue, destFuseValue ):
        destFuseValue = destFuseValue | srcFuseValue
        # High-4bits cannot be burned along with low-28bits for fuse lock region, this is design limitation
        srcLock = srcFuseValue & RT10yy_fusedef.kEfuseMask_LockLow
        destLock = destFuseValue & RT10yy_fusedef.kEfuseMask_LockLow
        if srcLock != destLock:
            # Don't allow to lock Fuse SRK because SRK will be OP+RP+WP if lock bit is set and then ROM cannot get SRK
            if ((srcLock & RT10yy_fusedef.kEfuseMask_LockSrk) == 0) and \
               ((destLock & RT10yy_fusedef.kEfuseMask_LockSrk) != 0):
                destLock = destLock & (~RT10yy_fusedef.kEfuseMask_LockSrk)
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_cannotBurnSrkLock'][self.languageIndex])
            self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, destLock, RT10yy_rundef.kActionFrom_BurnFuse)
        srcLock = srcFuseValue & RT10yy_fusedef.kEfuseMask_LockHigh
        destLock = destFuseValue & RT10yy_fusedef.kEfuseMask_LockHigh
        if srcLock != destLock:
            self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, destLock, RT10yy_rundef.kActionFrom_BurnFuse)

    def burnAllFuseRegions( self ):
        self.toBeBurnnedFuseList = self.getUserFuses()
        self._swapRemappedToBeBurnFuseIfAppliable()
        self._remapRunModeFuseFlagList()
        if self.needToScanFuse:
            self.scanAllFuseRegions(False)
        else:
            self._swapRemappedScannedFuseIfAppliable()
        for i in range(RT10yy_fusedef.kMaxEfuseWords):
            if self.runModeFuseFlagList[i]:
                if self.toBeBurnnedFuseList[i] != self.scannedFuseList[i] and \
                   self.toBeBurnnedFuseList[i] != None and \
                   self.scannedFuseList[i] != None:
                    if i == RT10yy_fusedef.kEfuseIndex_LOCK:
                        self._burnFuseLockRegion(self.scannedFuseList[i], self.toBeBurnnedFuseList[i])
                    else:
                        fuseValue = self.toBeBurnnedFuseList[i] | self.scannedFuseList[i]
                        self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_START + i, fuseValue, RT10yy_rundef.kActionFrom_BurnFuse)
                    self.toBeRefreshedFuseList[i] = True
        self.scanAllFuseRegions(True, True)

    def task_doShowSettedEfuse( self ):
        while True:
            efuseDict = uivar.getEfuseSettings()
            if self.toBeBurnnedFuseList[0] != None and efuseDict['0x400_lock'] != self.toBeBurnnedFuseList[0]:
                self.toBeBurnnedFuseList[0] = efuseDict['0x400_lock']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_LOCK, efuseDict['0x400_lock'])
            if self.toBeBurnnedFuseList[5] != None and efuseDict['0x450_bootCfg0'] != self.toBeBurnnedFuseList[5]:
                self.toBeBurnnedFuseList[5] = efuseDict['0x450_bootCfg0']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_BOOT_CFG0, efuseDict['0x450_bootCfg0'])
            if self.toBeBurnnedFuseList[6] != None and efuseDict['0x460_bootCfg1'] != self.toBeBurnnedFuseList[6]:
                self.toBeBurnnedFuseList[6] = efuseDict['0x460_bootCfg1']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_BOOT_CFG1, efuseDict['0x460_bootCfg1'])
            if self.toBeBurnnedFuseList[7] != None and efuseDict['0x470_bootCfg2'] != self.toBeBurnnedFuseList[7]:
                self.toBeBurnnedFuseList[7] = efuseDict['0x470_bootCfg2']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_BOOT_CFG2, efuseDict['0x470_bootCfg2'])
            if self.toBeBurnnedFuseList[45] != None and efuseDict['0x6d0_miscConf0'] != self.toBeBurnnedFuseList[45]:
                self.toBeBurnnedFuseList[45] = efuseDict['0x6d0_miscConf0']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_MISC_CONF0, efuseDict['0x6d0_miscConf0'])
            if self.toBeBurnnedFuseList[46] != None and efuseDict['0x6e0_miscConf1'] != self.toBeBurnnedFuseList[46]:
                self.toBeBurnnedFuseList[46] = efuseDict['0x6e0_miscConf1']
                self.showSettedEfuse(RT10yy_fusedef.kEfuseIndex_MISC_CONF1, efuseDict['0x6e0_miscConf1'])
            time.sleep(0.5)
