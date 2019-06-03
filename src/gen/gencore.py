#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import bincopy
import array
import gendef
sys.path.append(os.path.abspath(".."))
from ui import uicore
from ui import uidef
from ui import uivar
from ui import uilang

class secBootGen(uicore.secBootUi):

    def __init__(self, parent):
        uicore.secBootUi.__init__(self, parent)

        self.srcAppFilename = None

        self.userFileFolder = os.path.join(self.exeTopRoot, 'gen', 'user_file')
        self.mdkAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'keil_mdk', 'fromelf.exe')
        self.iarElfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'iar_ewarm', 'ielftool.exe')
        self.mcuxAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'mcuxpresso', 'arm-none-eabi-objcopy.exe')
        self.appFmtBatFilename = os.path.join(self.exeTopRoot, 'gen', 'user_file', 'imx_format_conv.bat')
        self.isConvertedAppUsed = False

    def isInTheRangeOfFlexram( self, start, length ):
        if ((start >= self.tgt.memoryRange['itcm'].start) and (start + length <= self.tgt.memoryRange['itcm'].start + self.tgt.memoryRange['itcm'].length)) or \
           ((start >= self.tgt.memoryRange['dtcm'].start) and (start + length <= self.tgt.memoryRange['dtcm'].start + self.tgt.memoryRange['dtcm'].length)) or \
           ((start >= self.tgt.memoryRange['ocram'].start) and (start + length <= self.tgt.memoryRange['ocram'].start + self.tgt.memoryRange['ocram'].length)):
            return True
        else:
            return False

    def isInTheRangeOfSram( self, start, length ):
        if ((start >= self.tgt.memoryRange['sram'].start) and (start + length <= self.tgt.memoryRange['sram'].start + self.tgt.memoryRange['sram'].length)):
            return True
        else:
            return False

    def _convertElfOrAxfToSrec( self, appFilename, destSrecAppFilename, appFormat):
        batContent = ''
        # below are conv results:
        # ----------------------------------------------------------------
        # |                       |    IAR     |    MDK     |    MCUX    |
        # ----------------------------------------------------------------
        # |      ielftool         |    Yes     |    Yes     |    No      |   // Start address is always 0x0000_0000
        # ----------------------------------------------------------------
        # | arm-none-eabi-objcopy |    Yes     |    No      |    Yes     |   // Error content in last three lines
        # ----------------------------------------------------------------
        # |      fromelf          |    No      |    Yes     |    No      |   // A folder will be generated for IAR, All contents are error for MCUX
        # ----------------------------------------------------------------
        if appFormat == uidef.kAppImageFormat_ElfFromIar or appFormat == uidef.kAppImageFormat_AxfFromMdk:
            batContent = "\"" + self.iarElfConvToolPath + "\" --srec-s3only \"" + appFilename +"\" \"" + destSrecAppFilename + "\""
        elif appFormat == uidef.kAppImageFormat_AxfFromMcux or appFormat == uidef.kAppImageFormat_ElfFromGcc:
            batContent = "\"" + self.mcuxAxfConvToolPath + "\" -O srec \"" + appFilename +"\" \"" + destSrecAppFilename + "\""
        #elif appFormat == uidef.kAppImageFormat_AxfFromMdk:
        #    batContent = "\"" + self.mdkAxfConvToolPath + "\" --m32 \"" + appFilename +"\" --output \"" + destSrecAppFilename + "\""
        else:
            pass
        with open(self.appFmtBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()
        try:
            #os.system(self.appFmtBatFilename)
            process = subprocess.Popen(self.appFmtBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except:
            pass
        if os.path.isfile(destSrecAppFilename):
            self.srcAppFilename = destSrecAppFilename
            appType = gendef.kAppImageFileExtensionList_S19[0]
            self.isConvertedAppUsed = True
            self.printLog('User image file has been converted to S-Records successfully')
            return self.srcAppFilename, appType
        else:
            appType = gendef.kAppImageFileExtensionList_Elf[0]
            return appFilename, appType

    def _getSrecDataWithoutS6Frame( self, srecData ):
        s6FrameStartLoc = srecData.find('S6')
        if s6FrameStartLoc != -1:
            newSrecData = srecData[0:s6FrameStartLoc]
            s6FrameEndLoc = srecData.find('\n', s6FrameStartLoc)
            if s6FrameEndLoc != -1:
                if len(srecData) > s6FrameEndLoc:
                    newSrecData += srecData[s6FrameEndLoc + 1:len(srecData)]
                else:
                    newSrecData += '\n'
            else:
                newSrecData += '\n'
            return newSrecData
        else:
            return srecData

    def _convertHexOrBinToSrec( self, appFilename, destSrecAppFilename, appType):
        status = True
        fmtObj = None
        if appType.lower() in gendef.kAppImageFileExtensionList_Hex:
            fmtObj = bincopy.BinFile(str(appFilename))
        elif appType.lower() in gendef.kAppImageFileExtensionList_Bin:
            fmtObj = bincopy.BinFile()
            status, baseAddr = self.getUserBinaryBaseAddress()
            if status:
                fmtObj.add_binary_file(str(appFilename), baseAddr)
            else:
                appType = None
        if status:
            self.srcAppFilename = destSrecAppFilename
            with open(self.srcAppFilename, 'wb') as fileObj:
                # Prototype: as_srec(number_of_data_bytes=32, address_length_bits=32)
                #    Format the binary file as Motorola S-Records records and return them as a string.
                #    number_of_data_bytes is the number of data bytes in each record.
                #    address_length_bits is the number of address bits in each record.
                fileObj.write(self._getSrecDataWithoutS6Frame(fmtObj.as_srec(16, 32)))
                fileObj.close()
            appFilename = self.srcAppFilename
            appType = gendef.kAppImageFileExtensionList_S19[0]
            self.isConvertedAppUsed = True
        return appFilename, appType

    def convertImageFormatToSrec( self, appFilename, appName, appType):
        appFormat = self.getUserAppFileFormat()
        destSrecAppFilename = os.path.join(self.userFileFolder, appName + gendef.kAppImageFileExtensionList_S19[0])
        if appFormat == uidef.kAppImageFormat_AutoDetect:
            if appType.lower() in gendef.kAppImageFileExtensionList_S19:
                return appFilename, appType
            elif (appType.lower() in gendef.kAppImageFileExtensionList_Hex) or (appType.lower() in gendef.kAppImageFileExtensionList_Bin):
                return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, appType)
            else:
                appFilename, appType = self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, uidef.kAppImageFormat_ElfFromIar)
                if appType.lower() in gendef.kAppImageFileExtensionList_S19:
                    return appFilename, appType
                appFilename, appType = self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, uidef.kAppImageFormat_AxfFromMcux)
                if appType.lower() in gendef.kAppImageFileExtensionList_S19:
                    return appFilename, appType
                return self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, uidef.kAppImageFormat_AxfFromMdk)
        elif appFormat == uidef.kAppImageFormat_AxfFromMdk or \
             appFormat == uidef.kAppImageFormat_ElfFromIar or \
             appFormat == uidef.kAppImageFormat_AxfFromMcux or \
             appFormat == uidef.kAppImageFormat_ElfFromGcc:
            return self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, appFormat)
        elif appFormat == uidef.kAppImageFormat_IntelHex:
            return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, gendef.kAppImageFileExtensionList_Hex[0])
        elif appFormat == uidef.kAppImageFormat_RawBinary:
            return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, gendef.kAppImageFileExtensionList_Bin[0])
        elif appFormat == uidef.kAppImageFormat_MotoSrec:
            return appFilename, gendef.kAppImageFileExtensionList_S19[0]
        else:
            pass

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
