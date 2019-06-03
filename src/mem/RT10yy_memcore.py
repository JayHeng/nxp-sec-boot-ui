#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import boot
import RT10yy_memdef
sys.path.append(os.path.abspath(".."))
from fuse import RT10yy_fusecore
from run import RT10yy_rundef
from ui import RT10yy_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from utils import misc

class secBootRT10yyMem(RT10yy_fusecore.secBootRT10yyFuse):

    def __init__(self, parent):
        RT10yy_fusecore.secBootRT10yyFuse.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.RT10yy_initMem()

    def RT10yy_initMem( self ):

        self.needToShowCfgIntr = None
        self.needToShowEkib0Intr = None
        self.needToShowEprdb0Intr = None
        self.needToShowEkib1Intr = None
        self.needToShowEprdb1Intr = None
        self.needToShowIvtIntr = None
        self.needToShowBootDataIntr = None
        self.needToShowDcdIntr = None
        self.needToShowImageIntr = None
        self.needToShowCsfIntr = None
        self.needToShowKeyBlobIntr = None
        self.needToShowNfcbIntr = None
        self.needToShowDbbtIntr = None
        self.needToShowMbrdptIntr = None
        self._initShowIntr()

    def _initShowIntr( self ):
        self.needToShowCfgIntr = True
        self.needToShowEkib0Intr = True
        self.needToShowEprdb0Intr = True
        self.needToShowEkib1Intr = True
        self.needToShowEprdb1Intr = True
        self.needToShowIvtIntr = True
        self.needToShowBootDataIntr = True
        self.needToShowDcdIntr = True
        self.needToShowImageIntr = True
        self.needToShowCsfIntr = True
        self.needToShowKeyBlobIntr = True
        self.needToShowNfcbIntr = True
        self.needToShowDbbtIntr = True
        self.needToShowMbrdptIntr = True

    def _getCsfBlockInfo( self ):
        self.destAppCsfAddress = self.getVal32FromBinFile(self.destAppFilename, self.destAppIvtOffset + RT10yy_memdef.kMemberOffsetInIvt_Csf)

    def _getInfoFromIvt( self ):
        self._getCsfBlockInfo()

    def _getDcdInfo( self ):
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            self.destAppDcdLength = os.path.getsize(self.dcdBinFilename)
        else:
            self.destAppDcdLength = 0

    def _showSemcNandFcb( self ):
        memFilename = 'semcNandFcb.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        nfcbAddr = self.bootDeviceMemBase
        dbbtAddr = 0
        status, results, cmdStr = self.blhost.readMemory(nfcbAddr, RT10yy_memdef.kMemBlockSize_NFCB, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False, 0
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self.getOneLineContentToShow(nfcbAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                nfcbAddr += len(memContent)
                if self.needToShowNfcbIntr:
                    self.printMem('------------------------------------NFCB----------------------------------------------', RT10yy_uidef.kMemBlockColor_NFCB)
                    self.needToShowNfcbIntr = False
                self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_NFCB)
        fingerprint = self.getVal32FromBinFile(memFilepath, RT10yy_rundef.kSemcNandFcbOffset_Fingerprint)
        semcTag = self.getVal32FromBinFile(memFilepath, RT10yy_rundef.kSemcNandFcbOffset_SemcTag)
        if fingerprint == RT10yy_rundef.kSemcNandFcbTag_Fingerprint and semcTag == RT10yy_rundef.kSemcNandFcbTag_Semc:
            dbbtStartPage = self.getVal32FromBinFile(memFilepath, RT10yy_rundef.kSemcNandFcbOffset_DBBTSerachAreaStartPage)
            dbbtAddr = self.bootDeviceMemBase + dbbtStartPage * self.comMemReadUnit
        else:
            return False, 0
        try:
            os.remove(memFilepath)
        except:
            pass
        return True, dbbtAddr

    def _showSemcNandDbbt( self, dbbtAddr ):
        memFilename = 'semcNandDbbt.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        status, results, cmdStr = self.blhost.readMemory(dbbtAddr, RT10yy_memdef.kMemBlockSize_DBBT, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self.getOneLineContentToShow(dbbtAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                dbbtAddr += len(memContent)
                if self.needToShowDbbtIntr:
                    self.printMem('------------------------------------DBBT----------------------------------------------', RT10yy_uidef.kMemBlockColor_DBBT)
                    self.needToShowDbbtIntr = False
                self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_DBBT)
        try:
            os.remove(memFilepath)
        except:
            pass
        return True

    def _showUsdhcSdMmcMbrdpt( self ):
        memFilename = 'usdhcSdMmcMbrdpt.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        mbrdptAddr = self.bootDeviceMemBase
        status, results, cmdStr = self.blhost.readMemory(mbrdptAddr, RT10yy_memdef.kMemBlockSize_MBRDPT, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self.getOneLineContentToShow(mbrdptAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                mbrdptAddr += len(memContent)
                if self.needToShowMbrdptIntr:
                    self.printMem('----------------------------------MBR&DPT---------------------------------------------', RT10yy_uidef.kMemBlockColor_MBRDPT)
                    self.needToShowMbrdptIntr = False
                self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_MBRDPT)
        try:
            os.remove(memFilepath)
        except:
            pass
        return True

    def readProgrammedMemoryAndShow( self ):
        if not os.path.isfile(self.destAppFilename):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotProgImage'][self.languageIndex])
            return
        self.clearMem()
        self._getInfoFromIvt()
        self._getDcdInfo()

        imageMemBase = 0
        readoutMemLen = 0
        imageFileLen = os.path.getsize(self.destAppFilename)
        if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(self.bootDevice)
            status, dbbtAddr = self._showSemcNandFcb()
            if status:
                self._showSemcNandDbbt(dbbtAddr)
            # Only Readout first image
            imageMemBase = self.bootDeviceMemBase + (semcNandImageInfoList[0] >> 16) * self.semcNandBlockSize
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or \
             self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            imageMemBase = self.bootDeviceMemBase
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
             self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            self._showUsdhcSdMmcMbrdpt()
            imageMemBase = self.bootDeviceMemBase
        else:
            pass
        if self.habDekDataOffset != None and (self.habDekDataOffset + RT10yy_memdef.kMemBlockSize_KeyBlob > imageFileLen):
            readoutMemLen += self.habDekDataOffset + RT10yy_memdef.kMemBlockSize_KeyBlob
        else:
            readoutMemLen += imageFileLen

        memFilename = 'bootableImageFromBootDevice.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        status, results, cmdStr = self.blhost.readMemory(imageMemBase, readoutMemLen, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False

        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        addr = imageMemBase
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self.getOneLineContentToShow(addr, memLeft, fileObj)
                memLeft -= len(memContent)
                addr += len(memContent)
                if addr <= imageMemBase + RT10yy_memdef.kMemBlockSize_FDCB:
                    if not self.isSdmmcCard:
                        if self.needToShowCfgIntr:
                            self.printMem('------------------------------------FDCB----------------------------------------------', RT10yy_uidef.kMemBlockColor_FDCB)
                            self.needToShowCfgIntr = False
                        self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_FDCB)
                    else:
                        if addr >= self.bootDeviceMemBase + RT10yy_memdef.kMemBlockSize_MBRDPT:
                            self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset:
                    if self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
                        ekib0Start = imageMemBase + RT10yy_memdef.kMemBlockOffset_EKIB0
                        eprdb0Start = imageMemBase + RT10yy_memdef.kMemBlockOffset_EPRDB0
                        ekib1Start = imageMemBase + RT10yy_memdef.kMemBlockOffset_EKIB1
                        eprdb1Start = imageMemBase + RT10yy_memdef.kMemBlockOffset_EPRDB1
                        if addr > ekib0Start and addr <= ekib0Start + RT10yy_memdef.kMemBlockSize_EKIB:
                            if self.needToShowEkib0Intr:
                                self.printMem('-----------------------------------EKIB0----------------------------------------------', RT10yy_uidef.kMemBlockColor_EKIB)
                                self.needToShowEkib0Intr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_EKIB)
                        elif addr > eprdb0Start and addr <= eprdb0Start + RT10yy_memdef.kMemBlockSize_EPRDB:
                            if self.needToShowEprdb0Intr:
                                self.printMem('-----------------------------------EPRDB0---------------------------------------------', RT10yy_uidef.kMemBlockColor_EPRDB)
                                self.needToShowEprdb0Intr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_EPRDB)
                        elif addr > ekib1Start and addr <= ekib1Start + RT10yy_memdef.kMemBlockSize_EKIB:
                            if self.needToShowEkib1Intr:
                                self.printMem('-----------------------------------EKIB1----------------------------------------------', RT10yy_uidef.kMemBlockColor_EKIB)
                                self.needToShowEkib1Intr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_EKIB)
                        elif addr > eprdb1Start and addr <= eprdb1Start + RT10yy_memdef.kMemBlockSize_EPRDB:
                            if self.needToShowEprdb1Intr:
                                self.printMem('-----------------------------------EPRDB1---------------------------------------------', RT10yy_uidef.kMemBlockColor_EPRDB)
                                self.needToShowEprdb1Intr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_EPRDB)
                        else:
                            self.printMem(contentToShow)
                    else:
                        self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset + RT10yy_memdef.kMemBlockSize_IVT:
                    if self.needToShowIvtIntr:
                        self.printMem('------------------------------------IVT-----------------------------------------------', RT10yy_uidef.kMemBlockColor_IVT)
                        self.needToShowIvtIntr = False
                    self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_IVT)
                elif addr <= imageMemBase + self.destAppIvtOffset + RT10yy_memdef.kMemBlockSize_IVT + RT10yy_memdef.kMemBlockSize_BootData:
                    if self.needToShowBootDataIntr:
                        self.printMem('---------------------------------Boot Data--------------------------------------------', RT10yy_uidef.kMemBlockColor_BootData)
                        self.needToShowBootDataIntr = False
                    self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_BootData)
                elif addr <= imageMemBase + self.destAppIvtOffset + RT10yy_memdef.kMemBlockOffsetToIvt_DCD:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset + RT10yy_memdef.kMemBlockOffsetToIvt_DCD + self.destAppDcdLength:
                    if self.needToShowDcdIntr:
                        self.printMem('------------------------------------DCD-----------------------------------------------', RT10yy_uidef.kMemBlockColor_DCD)
                        self.needToShowDcdIntr = False
                    self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_DCD)
                elif addr <= imageMemBase + self.destAppVectorOffset:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppVectorOffset + self.destAppBinaryBytes:
                    if self.needToShowImageIntr:
                        self.printMem('-----------------------------------Image----------------------------------------------', RT10yy_uidef.kMemBlockColor_Image)
                        self.needToShowImageIntr = False
                    self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_Image)
                else:
                    hasShowed = False
                    if self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto or \
                       (self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
                        csfStart = imageMemBase + (self.destAppCsfAddress - self.destAppVectorAddress) + self.destAppInitialLoadSize
                        if addr > csfStart and addr <= csfStart + RT10yy_memdef.kMemBlockSize_CSF:
                            if self.needToShowCsfIntr:
                                self.printMem('------------------------------------CSF-----------------------------------------------', RT10yy_uidef.kMemBlockColor_CSF)
                                self.needToShowCsfIntr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_CSF)
                            hasShowed = True
                    if self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto and self.habDekDataOffset != None:
                        keyBlobStart = imageMemBase + (self.destAppVectorOffset - self.destAppInitialLoadSize) + self.habDekDataOffset
                        if addr > keyBlobStart and addr <= keyBlobStart + RT10yy_memdef.kMemBlockSize_KeyBlob:
                            if self.needToShowKeyBlobIntr:
                                self.printMem('--------------------------------DEK KeyBlob-------------------------------------------', RT10yy_uidef.kMemBlockColor_KeyBlob)
                                self.needToShowKeyBlobIntr = False
                            self.printMem(contentToShow, RT10yy_uidef.kMemBlockColor_KeyBlob)
                            hasShowed = True
                    if not hasShowed:
                        if not self.isSdmmcCard:
                            self.printMem(contentToShow)
                        else:
                            if addr >= self.bootDeviceMemBase + RT10yy_memdef.kMemBlockSize_MBRDPT:
                                self.printMem(contentToShow)
            fileObj.close()
        self._initShowIntr()
        self.tryToSaveImageDataFile(memFilepath)
