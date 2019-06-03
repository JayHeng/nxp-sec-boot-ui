#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import boot
sys.path.append(os.path.abspath(".."))
from run import runcore
from ui import uidef
from ui import uivar
from ui import uilang
from utils import misc

s_visibleAsciiStart = ' '
s_visibleAsciiEnd = '~'

class secBootMem(runcore.secBootRun):

    def __init__(self, parent):
        runcore.secBootRun.__init__(self, parent)

        self.userFolder = os.path.join(self.exeTopRoot, 'gen', 'user_file')
        self.userFilename = os.path.join(self.exeTopRoot, 'gen', 'user_file', 'user.dat')

    def tryToSaveImageDataFile( self, readbackFilename ):
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

    def getOneLineContentToShow( self, addr, memLeft, fileObj ):
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
                        contentToShow, memContent = self.getOneLineContentToShow(addr, memLeft, fileObj)
                        memLeft -= len(memContent)
                        addr += len(memContent)
                        self.printMem(contentToShow)
                self.tryToSaveImageDataFile(memFilepath)
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

    def readRamMemory( self ):
        status, memStart, memLength = self._getUserComMemParameters(False)
        if status:
            if (self.mcuSeries == uidef.kMcuSeries_iMXRT10yy and self.isInTheRangeOfFlexram(memStart, memLength)) or \
               (self.mcuSeries == uidef.kMcuSeries_iMXRTxxx and self.isInTheRangeOfSram(memStart, memLength)):
                alignedMemStart = misc.align_down(memStart, 0x10)
                alignedMemLength = misc.align_up(memLength, 0x10) + 0x10
                if memLength + memStart > alignedMemStart + 0x10:
                    alignedMemLength += 0x10
                memFilename = 'commonDataFromRam.dat'
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
                            contentToShow, memContent = self.getOneLineContentToShow(addr, memLeft, fileObj)
                            memLeft -= len(memContent)
                            addr += len(memContent)
                            self.printMem(contentToShow)
                    self.tryToSaveImageDataFile(memFilepath)
                else:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to read RAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"读取FlexRAM失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInRam'][self.languageIndex])

    def writeRamMemory( self ):
        status, memStart, memBinFile = self._getUserComMemParameters(True)
        if status:
            memLength = os.path.getsize(memBinFile)
            if (self.mcuSeries == uidef.kMcuSeries_iMXRT10yy and self.isInTheRangeOfFlexram(memStart, memLength)) or \
               (self.mcuSeries == uidef.kMcuSeries_iMXRTxxx and self.isInTheRangeOfSram(memStart, memLength)):
                shutil.copy(memBinFile, self.userFilename)
                status, results, cmdStr = self.blhost.writeMemory(memStart, self.userFilename)
                try:
                    os.remove(self.userFilename)
                except:
                    pass
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to write RAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"写入FlexRAM失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInRam'][self.languageIndex])

    def executeAppInRam( self ):
        status, memStart, memBinFile = self._getUserComMemParameters(False)
        if status:
            if (self.mcuSeries == uidef.kMcuSeries_iMXRT10yy and self.isInTheRangeOfFlexram(memStart, 1)) or \
               (self.mcuSeries == uidef.kMcuSeries_iMXRTxxx and self.isInTheRangeOfSram(memStart, 1)):
                vectorFilename = 'vectorDataFromRam.dat'
                vectorFilepath = os.path.join(self.blhostVectorsDir, vectorFilename)
                status, results, cmdStr = self.blhost.readMemory(memStart, 8, vectorFilename)
                if status == boot.status.kStatus_Success:
                    programCounter = self.getVal32FromBinFile(vectorFilepath, 4)
                    stackPoint = self.getVal32FromBinFile(vectorFilepath, 0)
                    status, results, cmdStr = self.blhost.execute(programCounter, 0, stackPoint)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        if self.languageIndex == uilang.kLanguageIndex_English:
                            self.popupMsgBox('Failed to execute app in RAM, error code is %d .' %(status))
                        elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                            self.popupMsgBox(u"执行FlexRAM中应用程序失败，错误的代码是 %d 。" %(status))
                        else:
                            pass
                else:
                    if self.languageIndex == uilang.kLanguageIndex_English:
                        self.popupMsgBox('Failed to read PC, SP of app from RAM, error code is %d .' %(status))
                    elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                        self.popupMsgBox(u"读取FlexRAM中应用程序PC,SP失败，错误的代码是 %d 。" %(status))
                    else:
                        pass
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_notInRam'][self.languageIndex])
