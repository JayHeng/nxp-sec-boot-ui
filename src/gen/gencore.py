#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import array
import gendef
sys.path.append(os.path.abspath(".."))
from ui import uicore

class secBootGen(uicore.secBootUi):

    def __init__(self, parent):
        uicore.secBootUi.__init__(self, parent)

        self.userFileFolder = os.path.join(self.exeTopRoot, 'gen', 'user_file')
        self.mdkAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'keil_mdk', 'fromelf.exe')
        self.iarElfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'iar_ewarm', 'ielftool.exe')
        self.mcuxAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'mcuxpresso', 'arm-none-eabi-objcopy.exe')
        self.appFmtBatFilename = os.path.join(self.exeTopRoot, 'gen', 'user_file', 'imx_format_conv.bat')

    def getReg32FromBinFile( self, filename, offset=0):
        return hex(self.getVal32FromBinFile(filename, offset))

    def getVal32FromBinFile( self, filename, offset=0):
        var32Vaule = 0
        if os.path.isfile(filename):
            var32Vaule = array.array('c', [chr(0xff)]) * 4
            with open(filename, 'rb') as fileObj:
                fileObj.seek(offset)
                var32Vaule = fileObj.read(4)
                fileObj.close()
            var32Vaule = (ord(var32Vaule[3])<<24) + (ord(var32Vaule[2])<<16) + (ord(var32Vaule[1])<<8) + ord(var32Vaule[0])
        return var32Vaule

    def getVal32FromByteArray( self, binarray, offset=0):
        val32Vaule = ((binarray[3+offset]<<24) + (binarray[2+offset]<<16) + (binarray[1+offset]<<8) + binarray[0+offset])
        return val32Vaule

    def fillVal32IntoBinFile( self, filename, val32):
        with open(filename, 'ab') as fileObj:
            byteStr = ''
            for i in range(4):
                byteStr = chr((val32 & (0xFF << (i * 8))) >> (i * 8))
                fileObj.write(byteStr)
            fileObj.close()
