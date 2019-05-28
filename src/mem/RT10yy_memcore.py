#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import boot
import memdef
sys.path.append(os.path.abspath(".."))
from fuse import fusecore
from run import rundef
from ui import uidef
from ui import uivar
from ui import uilang
from utils import misc

s_visibleAsciiStart = ' '
s_visibleAsciiEnd = '~'

class secBootMem(fusecore.secBootFuse):

    def __init__(self, parent):
        fusecore.secBootFuse.__init__(self, parent)

        self.userFolder = os.path.join(self.exeTopRoot, 'gen', 'user_file')
        self.userFilename = os.path.join(self.exeTopRoot, 'gen', 'user_file', 'user.dat')

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
        self.destAppCsfAddress = self.getVal32FromBinFile(self.destAppFilename, self.destAppIvtOffset + memdef.kMemberOffsetInIvt_Csf)

    def _getInfoFromIvt( self ):
        self._getCsfBlockInfo()

    def _getDcdInfo( self ):
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            self.destAppDcdLength = os.path.getsize(self.dcdBinFilename)
        else:
            self.destAppDcdLength = 0

    def _getOneLineContentToShow( self, addr, memLeft, fileObj ):
        memContent = ''
        padBytesBefore= addr % 16
        contentToShow = self.getFormattedHexValue(addr - padBytesBefore) + '    '
        if (padBytesBefore + memLeft) > 16:
            memContent = fileObj.read(16 - padBytesBefore)
        else:
            memContent = fileObj.read(memLeft)
        visibleContent = ''
        for i in range(16):
            if i >= padBytesBefore and \
               i < padBytesBefore + len(memContent):
                halfbyteStr = str(hex((ord(memContent[i-padBytesBefore]) & 0xF0)>> 4))
                contentToShow += halfbyteStr[2]
                halfbyteStr = str(hex((ord(memContent[i-padBytesBefore]) & 0x0F)>> 0))
                contentToShow += halfbyteStr[2] + ' '
                if memContent[i-padBytesBefore] >= s_visibleAsciiStart and \
                   memContent[i-padBytesBefore] <= s_visibleAsciiEnd:
                    visibleContent += memContent[i-padBytesBefore]
                else:
                    visibleContent += '.'
            else:
                contentToShow += '-- '
                visibleContent += '-'
        contentToShow += '        ' + visibleContent
        return contentToShow, memContent

    def _showSemcNandFcb( self ):
        memFilename = 'semcNandFcb.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        nfcbAddr = self.bootDeviceMemBase
        dbbtAddr = 0
        status, results, cmdStr = self.blhost.readMemory(nfcbAddr, memdef.kMemBlockSize_NFCB, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False, 0
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self._getOneLineContentToShow(nfcbAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                nfcbAddr += len(memContent)
                if self.needToShowNfcbIntr:
                    self.printMem('------------------------------------NFCB----------------------------------------------', uidef.kMemBlockColor_NFCB)
                    self.needToShowNfcbIntr = False
                self.printMem(contentToShow, uidef.kMemBlockColor_NFCB)
        fingerprint = self.getVal32FromBinFile(memFilepath, rundef.kSemcNandFcbOffset_Fingerprint)
        semcTag = self.getVal32FromBinFile(memFilepath, rundef.kSemcNandFcbOffset_SemcTag)
        if fingerprint == rundef.kSemcNandFcbTag_Fingerprint and semcTag == rundef.kSemcNandFcbTag_Semc:
            dbbtStartPage = self.getVal32FromBinFile(memFilepath, rundef.kSemcNandFcbOffset_DBBTSerachAreaStartPage)
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
        status, results, cmdStr = self.blhost.readMemory(dbbtAddr, memdef.kMemBlockSize_DBBT, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self._getOneLineContentToShow(dbbtAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                dbbtAddr += len(memContent)
                if self.needToShowDbbtIntr:
                    self.printMem('------------------------------------DBBT----------------------------------------------', uidef.kMemBlockColor_DBBT)
                    self.needToShowDbbtIntr = False
                self.printMem(contentToShow, uidef.kMemBlockColor_DBBT)
        try:
            os.remove(memFilepath)
        except:
            pass
        return True

    def _showUsdhcSdMmcMbrdpt( self ):
        memFilename = 'usdhcSdMmcMbrdpt.dat'
        memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
        mbrdptAddr = self.bootDeviceMemBase
        status, results, cmdStr = self.blhost.readMemory(mbrdptAddr, memdef.kMemBlockSize_MBRDPT, memFilename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        readoutMemLen = os.path.getsize(memFilepath)
        memLeft = readoutMemLen
        with open(memFilepath, 'rb') as fileObj:
            while memLeft > 0:
                contentToShow, memContent = self._getOneLineContentToShow(mbrdptAddr, memLeft, fileObj)
                memLeft -= len(memContent)
                mbrdptAddr += len(memContent)
                if self.needToShowMbrdptIntr:
                    self.printMem('----------------------------------MBR&DPT---------------------------------------------', uidef.kMemBlockColor_MBRDPT)
                    self.needToShowMbrdptIntr = False
                self.printMem(contentToShow, uidef.kMemBlockColor_MBRDPT)
        try:
            os.remove(memFilepath)
        except:
            pass
        return True

    def _tryToSaveImageDataFile( self, readbackFilename ):
        if self.needToSaveReadbackImageData():
            savedBinFile = self.getImageDataFileToSave()
            if os.path.isfile(savedBinFile):
                if readbackFilename != savedBinFile:
                    shutil.copy(readbackFilename, savedBinFile)
            else:
                finalBinFile = os.path.join(self.userFolder, os.path.split(readbackFilename)[1])
                shutil.copy(readbackFilename, finalBinFile)
                self.setImageDataFilePath(finalBinFile)
        try:
            os.remove(readbackFilename)
        except:
            pass

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
        if self.bootDevice == uidef.kBootDevice_SemcNand:
            semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(self.bootDevice)
            status, dbbtAddr = self._showSemcNandFcb()
            if status:
                self._showSemcNandDbbt(dbbtAddr)
            # Only Readout first image
            imageMemBase = self.bootDeviceMemBase + (semcNandImageInfoList[0] >> 16) * self.semcNandBlockSize
        elif self.bootDevice == uidef.kBootDevice_FlexspiNor or \
             self.bootDevice == uidef.kBootDevice_LpspiNor:
            imageMemBase = self.bootDeviceMemBase
        elif self.bootDevice == uidef.kBootDevice_UsdhcSd or \
             self.bootDevice == uidef.kBootDevice_UsdhcMmc:
            self._showUsdhcSdMmcMbrdpt()
            imageMemBase = self.bootDeviceMemBase
        else:
            pass
        if self.habDekDataOffset != None and (self.habDekDataOffset + memdef.kMemBlockSize_KeyBlob > imageFileLen):
            readoutMemLen += self.habDekDataOffset + memdef.kMemBlockSize_KeyBlob
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
                contentToShow, memContent = self._getOneLineContentToShow(addr, memLeft, fileObj)
                memLeft -= len(memContent)
                addr += len(memContent)
                if addr <= imageMemBase + memdef.kMemBlockSize_FDCB:
                    if not self.isSdmmcCard:
                        if self.needToShowCfgIntr:
                            self.printMem('------------------------------------FDCB----------------------------------------------', uidef.kMemBlockColor_FDCB)
                            self.needToShowCfgIntr = False
                        self.printMem(contentToShow, uidef.kMemBlockColor_FDCB)
                    else:
                        if addr >= self.bootDeviceMemBase + memdef.kMemBlockSize_MBRDPT:
                            self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset:
                    if self.secureBootType == uidef.kSecureBootType_BeeCrypto:
                        ekib0Start = imageMemBase + memdef.kMemBlockOffset_EKIB0
                        eprdb0Start = imageMemBase + memdef.kMemBlockOffset_EPRDB0
                        ekib1Start = imageMemBase + memdef.kMemBlockOffset_EKIB1
                        eprdb1Start = imageMemBase + memdef.kMemBlockOffset_EPRDB1
                        if addr > ekib0Start and addr <= ekib0Start + memdef.kMemBlockSize_EKIB:
                            if self.needToShowEkib0Intr:
                                self.printMem('-----------------------------------EKIB0----------------------------------------------', uidef.kMemBlockColor_EKIB)
                                self.needToShowEkib0Intr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_EKIB)
                        elif addr > eprdb0Start and addr <= eprdb0Start + memdef.kMemBlockSize_EPRDB:
                            if self.needToShowEprdb0Intr:
                                self.printMem('-----------------------------------EPRDB0---------------------------------------------', uidef.kMemBlockColor_EPRDB)
                                self.needToShowEprdb0Intr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_EPRDB)
                        elif addr > ekib1Start and addr <= ekib1Start + memdef.kMemBlockSize_EKIB:
                            if self.needToShowEkib1Intr:
                                self.printMem('-----------------------------------EKIB1----------------------------------------------', uidef.kMemBlockColor_EKIB)
                                self.needToShowEkib1Intr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_EKIB)
                        elif addr > eprdb1Start and addr <= eprdb1Start + memdef.kMemBlockSize_EPRDB:
                            if self.needToShowEprdb1Intr:
                                self.printMem('-----------------------------------EPRDB1---------------------------------------------', uidef.kMemBlockColor_EPRDB)
                                self.needToShowEprdb1Intr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_EPRDB)
                        else:
                            self.printMem(contentToShow)
                    else:
                        self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset + memdef.kMemBlockSize_IVT:
                    if self.needToShowIvtIntr:
                        self.printMem('------------------------------------IVT-----------------------------------------------', uidef.kMemBlockColor_IVT)
                        self.needToShowIvtIntr = False
                    self.printMem(contentToShow, uidef.kMemBlockColor_IVT)
                elif addr <= imageMemBase + self.destAppIvtOffset + memdef.kMemBlockSize_IVT + memdef.kMemBlockSize_BootData:
                    if self.needToShowBootDataIntr:
                        self.printMem('---------------------------------Boot Data--------------------------------------------', uidef.kMemBlockColor_BootData)
                        self.needToShowBootDataIntr = False
                    self.printMem(contentToShow, uidef.kMemBlockColor_BootData)
                elif addr <= imageMemBase + self.destAppIvtOffset + memdef.kMemBlockOffsetToIvt_DCD:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppIvtOffset + memdef.kMemBlockOffsetToIvt_DCD + self.destAppDcdLength:
                    if self.needToShowDcdIntr:
                        self.printMem('------------------------------------DCD-----------------------------------------------', uidef.kMemBlockColor_DCD)
                        self.needToShowDcdIntr = False
                    self.printMem(contentToShow, uidef.kMemBlockColor_DCD)
                elif addr <= imageMemBase + self.destAppVectorOffset:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + self.destAppVectorOffset + self.destAppBinaryBytes:
                    if self.needToShowImageIntr:
                        self.printMem('-----------------------------------Image----------------------------------------------', uidef.kMemBlockColor_Image)
                        self.needToShowImageIntr = False
                    self.printMem(contentToShow, uidef.kMemBlockColor_Image)
                else:
                    hasShowed = False
                    if self.secureBootType == uidef.kSecureBootType_HabAuth or self.secureBootType == uidef.kSecureBootType_HabCrypto or \
                       (self.secureBootType == uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
                        csfStart = imageMemBase + (self.destAppCsfAddress - self.destAppVectorAddress) + self.destAppInitialLoadSize
                        if addr > csfStart and addr <= csfStart + memdef.kMemBlockSize_CSF:
                            if self.needToShowCsfIntr:
                                self.printMem('------------------------------------CSF-----------------------------------------------', uidef.kMemBlockColor_CSF)
                                self.needToShowCsfIntr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_CSF)
                            hasShowed = True
                    if self.secureBootType == uidef.kSecureBootType_HabCrypto and self.habDekDataOffset != None:
                        keyBlobStart = imageMemBase + (self.destAppVectorOffset - self.destAppInitialLoadSize) + self.habDekDataOffset
                        if addr > keyBlobStart and addr <= keyBlobStart + memdef.kMemBlockSize_KeyBlob:
                            if self.needToShowKeyBlobIntr:
                                self.printMem('--------------------------------DEK KeyBlob-------------------------------------------', uidef.kMemBlockColor_KeyBlob)
                                self.needToShowKeyBlobIntr = False
                            self.printMem(contentToShow, uidef.kMemBlockColor_KeyBlob)
                            hasShowed = True
                    if not hasShowed:
                        if not self.isSdmmcCard:
                            self.printMem(contentToShow)
                        else:
                            if addr >= self.bootDeviceMemBase + memdef.kMemBlockSize_MBRDPT:
                                self.printMem(contentToShow)
            fileObj.close()
        self._initShowIntr()
        self._tryToSaveImageDataFile(memFilepath)

    def _getUserComMemParameters( self, isMemWrite=False ):
        status = False
        memStart = 0
        memLength = 0
        memBinFile = None
        memFlexibleArg = None
        status, memStart = self.getComMemStartAddress()
        if status:
            if isMemWrite:
                memBinFile = self.getComMemBinFile()
                if not os.path.isfile(memBinFile):
                    status = False
                else:
                    memFlexibleArg = memBinFile
            else:
                status, memLength = self.getComMemByteLength()
                if status:
                    memFlexibleArg = memLength
        return status, memStart, memFlexibleArg

    def _convertComMemStart( self, memStart ):
        if memStart < self.bootDeviceMemBase:
            memStart += self.bootDeviceMemBase
        return memStart

    def readBootDeviceMemory( self ):
        status, memStart, memLength = self._getUserComMemParameters(False)
        if status:
            memStart = self._convertComMemStart(memStart)
            alignedMemStart = misc.align_down(memStart, self.comMemReadUnit)
            alignedMemLength = misc.align_up(memLength, self.comMemReadUnit) + self.comMemReadUnit
            if memLength + memStart > alignedMemStart + self.comMemReadUnit:
                alignedMemLength += self.comMemReadUnit
            memFilename = 'commonDataFromBootDevice.dat'
            memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
            status, results, cmdStr = self.blhost.readMemory(alignedMemStart, alignedMemLength, memFilename, self.bootDeviceMemId)
            self.printLog(cmdStr)
            if status == boot.status.kStatus_Success:
                self.clearMem()
                memLeft = memLength
                addr = memStart
                with open(memFilepath, 'rb') as fileObj:
                    fileObj.seek(memStart - alignedMemStart)
                    while memLeft > 0:
                        contentToShow, memContent = self._getOneLineContentToShow(addr, memLeft, fileObj)
                        memLeft -= len(memContent)
                        addr += len(memContent)
                        self.printMem(contentToShow)
                self._tryToSaveImageDataFile(memFilepath)
            else:
                if self.languageIndex == uilang.kLanguageIndex_English:
                    self.popupMsgBox('Failed to read boot device, error code is %d !' %(status))
                elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                    self.popupMsgBox(u"读取启动设备失败，错误的代码是 %d ！" %(status))
                else:
                    pass

    def eraseBootDeviceMemory( self ):
        status, memStart, memLength = self._getUserComMemParameters(False)
        if status:
            memStart = self._convertComMemStart(memStart)
            alignedMemStart = misc.align_down(memStart, self.comMemEraseUnit)
            alignedMemLength = misc.align_up(memLength, self.comMemEraseUnit)
            if memLength + memStart > alignedMemStart + self.comMemEraseUnit:
                alignedMemLength += self.comMemEraseUnit
            status, results, cmdStr = self.blhost.flashEraseRegion(alignedMemStart, alignedMemLength, self.bootDeviceMemId)
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                if self.languageIndex == uilang.kLanguageIndex_English:
                    self.popupMsgBox('Failed to erase boot device, error code is %d !' %(status))
                elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                    self.popupMsgBox(u"擦除启动设备失败，错误的代码是 %d ！" %(status))
                else:
                    pass

    def writeBootDeviceMemory( self ):
        status, memStart, memBinFile = self._getUserComMemParameters(True)
        if status:
            memStart = self._convertComMemStart(memStart)
            if memStart % self.comMemWriteUnit:
                if self.languageIndex == uilang.kLanguageIndex_English:
                    self.popupMsgBox('Start Address should be aligned with 0x%x !' %(self.comMemWriteUnit))
                elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                    self.popupMsgBox(u"起始地址应该以 0x%x 对齐！" %(self.comMemWriteUnit))
                else:
                    pass
                return
            eraseMemStart = misc.align_down(memStart, self.comMemEraseUnit)
            eraseMemEnd = misc.align_up(memStart + os.path.getsize(memBinFile), self.comMemEraseUnit)
            status, results, cmdStr = self.blhost.flashEraseRegion(eraseMemStart, eraseMemEnd - eraseMemStart, self.bootDeviceMemId)
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                if self.languageIndex == uilang.kLanguageIndex_English:
                    self.popupMsgBox('Failed to erase boot device, error code is %d !' %(status))
                elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                    self.popupMsgBox(u"擦除启动设备失败，错误的代码是 %d ！" %(status))
                else:
                    pass
                return
            shutil.copy(memBinFile, self.userFilename)
            status, results, cmdStr = self.blhost.writeMemory(memStart, self.userFilename, self.bootDeviceMemId)
            try:
                os.remove(self.userFilename)
            except:
                pass
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                if self.languageIndex == uilang.kLanguageIndex_English:
                    self.popupMsgBox('Failed to write boot device, error code is %d, You may forget to erase boot device first!' %(status))
                elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                    self.popupMsgBox(u"写入启动设备失败，错误的代码是 %d ，请确认是否先擦除了启动设备！" %(status))
                else:
                    pass

    def readFlexramMemory( self ):
        status, memStart, memLength = self._getUserComMemParameters(False)
        if status:
            if self.isInTheRangeOfFlexram(memStart, memLength):
                alignedMemStart = misc.align_down(memStart, 0x10)
                alignedMemLength = misc.align_up(memLength, 0x10) + 0x10
                if memLength + memStart > alignedMemStart + 0x10:
                    alignedMemLength += 0x10
                memFilename = 'commonDataFromFlexram.dat'
                memFilepath = os.path.join(self.blhostVectorsDir, memFilename)
                status, results, cmdStr = self.blhost.readMemory(alignedMemStart, alignedMemLength, memFilename)
                self.printLog(cmdStr)
                if status == boot.status.kStatus_Success:
                    self.clearMem()
                    memLeft = memLength
                    addr = memStart
                    with open(memFilepath, 'rb') as fileObj:
                        fileObj.seek(memStart - alignedMemStart)
                        while memLeft > 0:
                            contentToShow, memContent = self._getOneLineContentToShow(addr, memLeft, fileObj)
                            memLeft -= len(memContent)
                            addr += len(memContent)
                            self.printMem(contentToShow)
                    self._tryToSaveImageDataFile(memFilepath)
                else:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to read FlexRAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"读取FlexRAM失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInFlexram'][self.languageIndex])

    def writeFlexramMemory( self ):
        status, memStart, memBinFile = self._getUserComMemParameters(True)
        if status:
            memLength = os.path.getsize(memBinFile)
            if self.isInTheRangeOfFlexram(memStart, memLength):
                shutil.copy(memBinFile, self.userFilename)
                status, results, cmdStr = self.blhost.writeMemory(memStart, self.userFilename)
                try:
                    os.remove(self.userFilename)
                except:
                    pass
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to write FlexRAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"写入FlexRAM失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInFlexram'][self.languageIndex])

    def executeAppInFlexram( self ):
        status, memStart, memBinFile = self._getUserComMemParameters(False)
        if status:
            if self.isInTheRangeOfFlexram(memStart, 1):
                vectorFilename = 'vectorDataFromFlexram.dat'
                vectorFilepath = os.path.join(self.blhostVectorsDir, vectorFilename)
                status, results, cmdStr = self.blhost.readMemory(memStart, 8, vectorFilename)
                if status == boot.status.kStatus_Success:
                    programCounter = self.getVal32FromBinFile(vectorFilepath, 4)
                    stackPoint = self.getVal32FromBinFile(vectorFilepath, 0)
                    status, results, cmdStr = self.blhost.execute(programCounter, 0, stackPoint)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        if self.languageIndex == uilang.kLanguageIndex_English:
                            self.popupMsgBox('Failed to execute app in FlexRAM, error code is %d .' %(status))
                        elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                            self.popupMsgBox(u"执行FlexRAM中应用程序失败，错误的代码是 %d 。" %(status))
                        else:
                            pass
                else:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to read PC, SP of app from FlexRAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"读取FlexRAM中应用程序PC,SP失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInFlexram'][self.languageIndex])
