#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import boot
import RTxxx_memdef
sys.path.append(os.path.abspath(".."))
from run import RTxxx_runcore
from gen import RTxxx_gendef
from ui import RTxxx_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from utils import misc

class secBootRTxxxMem(RTxxx_runcore.secBootRTxxxRun):

    def __init__(self, parent):
        RTxxx_runcore.secBootRTxxxRun.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initMem()

    def RTxxx_initMem( self ):

        self.needToShowCfgIntr = None
        self.needToShowImageIntr = None
        self._RTxxx_initShowIntr()

    def _RTxxx_initShowIntr( self ):
        self.needToShowCfgIntr = True
        self.needToShowImageIntr = True

    def RTxxx_readProgrammedMemoryAndShow( self ):
        if not os.path.isfile(self.destAppFilename):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operImgError_hasnotProgImage'][self.languageIndex])
            return
        self.clearMem()

        imageMemBase = 0
        readoutMemLen = 0
        imageFileLen = os.path.getsize(self.destAppFilename)
        if self.bootDevice == RTxxx_uidef.kBootDevice_FlexspiNor or \
           self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
            imageMemBase = self.bootDeviceMemBase
        else:
            pass
        readoutMemLen += imageFileLen + RTxxx_gendef.kBootImageOffset_NOR_SD_EEPROM

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
                if addr <= imageMemBase + RTxxx_memdef.kMemBlockOffset_FDCB:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + RTxxx_memdef.kMemBlockOffset_FDCB + RTxxx_memdef.kMemBlockSize_FDCB:
                    if self.bootDevice == RTxxx_uidef.kBootDevice_FlexspiNor or \
                       self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
                        if self.needToShowCfgIntr:
                            self.printMem('------------------------------------FDCB----------------------------------------------', RTxxx_uidef.kMemBlockColor_FDCB)
                            self.needToShowCfgIntr = False
                        self.printMem(contentToShow, RTxxx_uidef.kMemBlockColor_FDCB)
                    else:
                        self.printMem(contentToShow)
                elif addr <= imageMemBase + RTxxx_gendef.kBootImageOffset_NOR_SD_EEPROM:
                    self.printMem(contentToShow)
                elif addr <= imageMemBase + RTxxx_gendef.kBootImageOffset_NOR_SD_EEPROM + self.destAppBinaryBytes:
                    if self.needToShowImageIntr:
                        self.printMem('-----------------------------------Image----------------------------------------------', RTxxx_uidef.kMemBlockColor_Image)
                        self.needToShowImageIntr = False
                    self.printMem(contentToShow, RTxxx_uidef.kMemBlockColor_Image)
                else:
                    pass
            fileObj.close()
        self._RTxxx_initShowIntr()
        self.tryToSaveImageDataFile(memFilepath)
