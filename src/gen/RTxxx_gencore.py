#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import json
import subprocess
import bincopy
import gendef
import RTxxx_gendef
sys.path.append(os.path.abspath(".."))
from ui import RTxxx_uicore
from ui import RTxxx_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from run import RTxxx_rundef
from utils import elf

class secBootRTxxxGen(RTxxx_uicore.secBootRTxxxUi):

    def __init__(self, parent):
        RTxxx_uicore.secBootRTxxxUi.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initGen()

    def RTxxx_initGen( self ):
        self.srcAppFilename = None
        self.destAppFilename = os.path.join(self.exeTopRoot, 'gen', 'bootable_image', 'bt_application.bin')
        self.appJsonFilename = os.path.join(self.exeTopRoot, 'gen', 'json_file', 'imx_application_gen.json')
        self.elftosbPath = os.path.join(self.exeTopRoot, 'tools', 'elftosb5', 'win', 'elftosb.exe')
        self.appJsonBatFilename = os.path.join(self.exeTopRoot, 'gen', 'json_file', 'imx_application_gen.bat')

        self.isConvertedAppUsed = False

        self.destAppVectorAddress = 0
        self.destAppVectorOffset = None
        self.destAppBinaryBytes = 0
        self.isXipApp = False

    def _RTxxx_generatePlainImageBinary( self, binaryArray, appName, startAddress, lengthInByte ):
        destBinAppFilename = os.path.join(self.userFileFolder, appName + gendef.kAppImageFileExtensionList_Bin[0])
        self.srcAppFilename = destBinAppFilename
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgType] = RTxxx_gendef.kBootImageTypeVal_PlainUnsigned
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgType + 1] = (RTxxx_gendef.kBootImageTypeVal_PlainUnsigned >> 8) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgType + 2] = (RTxxx_gendef.kBootImageTypeVal_PlainUnsigned >> 16) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgType + 3] = (RTxxx_gendef.kBootImageTypeVal_PlainUnsigned >> 24) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLen] = lengthInByte & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLen + 1] = (lengthInByte >> 8) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLen + 2] = (lengthInByte >> 16) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLen + 3] = (lengthInByte >> 24) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLoadAddr] = startAddress & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLoadAddr + 1] = (startAddress >> 8) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLoadAddr + 2] = (startAddress >> 16) & 0xff
        binaryArray[RTxxx_gendef.kBootHeaderOffset_ImgLoadAddr + 3] = (startAddress >> 24) & 0xff
        with open(self.srcAppFilename, 'wb') as fileObj:
            fileObj.write(binaryArray)
            fileObj.close()
        self.isConvertedAppUsed = True

    def _RTxxx_getImageInfo( self, srcAppFilename ):
        startAddress = None
        entryPointAddress = None
        lengthInByte = 0
        if os.path.isfile(srcAppFilename):
            appPath, appFilename = os.path.split(srcAppFilename)
            appName, appType = os.path.splitext(appFilename)
            srcAppFilename, appType = self.convertImageFormatToSrec(srcAppFilename, appName, appType)
            isConvSuccessed = False
            if appType.lower() in gendef.kAppImageFileExtensionList_S19:
                try:
                    srecObj = bincopy.BinFile(str(srcAppFilename))
                    startAddress = srecObj.minimum_address
                    entryPointAddress = self.getVal32FromByteArray(srecObj.as_binary(startAddress + 0x4, startAddress  + 0x8))
                    lengthInByte = len(srecObj.as_binary())
                    self._RTxxx_generatePlainImageBinary(srecObj.as_binary(), appName, startAddress, lengthInByte)
                    isConvSuccessed = True
                except:
                    pass
            else:
                pass
            if not isConvSuccessed:
                startAddress = None
                entryPointAddress = None
                lengthInByte = 0
                self.popupMsgBox(uilang.kMsgLanguageContentDict['genImgError_formatNotValid'][self.languageIndex] + srcAppFilename.encode('utf-8'))
        return startAddress, entryPointAddress, lengthInByte

    def _adjustDestAppFilenameForJson( self ):
        srcAppName = os.path.splitext(os.path.split(self.srcAppFilename)[1])[0]
        destAppPath, destAppFile = os.path.split(self.destAppFilename)
        destAppName, destAppType = os.path.splitext(destAppFile)
        destAppName ='bt_' + srcAppName
        if self.secureBootType == RTxxx_uidef.kSecureBootType_PlainUnsigned:
            destAppName += '_unsigned'
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_PlainSigned:
            destAppName += '_signed'
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_PlainCrc:
            destAppName += '_crc'
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_CryptoSigned:
            destAppName += '_signed_encrypted'
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_PlainSignedKeyStore:
            destAppName += '_signed_keystore'
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_CryptoSignedKeyStore:
            destAppName += '_signed_encrypted_keystore'
        else:
            pass
        self.destAppFilename = os.path.join(destAppPath, destAppName + destAppType)

    def _updateJsonfileContent( self, secureBootType, bootDevice, vectorAddress, entryPointAddress):
        self._adjustDestAppFilenameForJson()
        if secureBootType != RTxxx_uidef.kSecureBootType_PlainUnsigned:
            with open(self.appJsonFilename, 'w') as fileObj:
                jsonDict = {
                    "family": None,
                    "inputImageFile": None,
                    "imageLinkAddress": None,
                    "imageLinkAdressFromImage": False,
                    "outputImageExecutionTarget": None,
                    "outputImageAuthenticationType": None,
                    "outputImageEncryptionKeyFile": "",
                    "enableTrustZone": False,
                    "trustZonePresetFile": "",
                    "useKeyStore": False,
                    "keyStoreFile": "",
                    "rootCertificate0File": "",
                    "rootCertificate1File": "",
                    "rootCertificate2File": "",
                    "rootCertificate3File": "",
                    "mainCertChainId": 0,
                    "mainCertPrivateKeyFile": "",
                    "masterBootOutputFile": None,

                    "enableHwUserModeKeys": False,
                }
                ########################################################################
                if self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT500 or \
                   self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT500S:
                    jsonDict["family"] = RTxxx_gendef.kMcuDeviceFamily_RT500
                elif self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT600 or \
                     self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT600S:
                    jsonDict["family"] = RTxxx_gendef.kMcuDeviceFamily_RT600
                else:
                    pass
                jsonDict["inputImageFile"] = self.srcAppFilename
                jsonDict["imageLinkAddress"] = self.convertLongIntHexText(str(hex(vectorAddress)))
                if self.isXipApp:
                    jsonDict["outputImageExecutionTarget"] = RTxxx_gendef.kBootImageExecTarget_XipFlash
                else:
                    jsonDict["outputImageExecutionTarget"] = RTxxx_gendef.kBootImageExecTarget_Ram
                if secureBootType == RTxxx_uidef.kSecureBootType_PlainCrc:
                    jsonDict["outputImageAuthenticationType"] = RTxxx_gendef.kBootImageAuthType_Crc
                elif secureBootType == RTxxx_uidef.kSecureBootType_PlainSigned or \
                     secureBootType == RTxxx_uidef.kSecureBootType_PlainSignedKeyStore:
                    jsonDict["outputImageAuthenticationType"] = RTxxx_gendef.kBootImageAuthType_Signed
                elif secureBootType == RTxxx_uidef.kSecureBootType_CryptoSigned or \
                     secureBootType == RTxxx_uidef.kSecureBootType_CryptoSignedKeyStore:
                    jsonDict["outputImageAuthenticationType"] = RTxxx_gendef.kBootImageAuthType_CryptoSigned
                else:
                    pass
                jsonDict["masterBootOutputFile"] = self.destAppFilename
                ########################################################################

                json.dump(jsonDict, fileObj, indent=1)
                fileObj.close()

        return True

    def _RTxxx_isValidNonXipAppImage( self, imageStartAddr ):
        if self.isInTheRangeOfSram(imageStartAddr, 1):
            return True
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_invalidNonXipRange'][self.languageIndex])
            return False

    def _RTxxx_isValidAppImage( self, imageStartAddr ):
        if self.isXipApp:
            return True
        else:
            return self._RTxxx_isValidNonXipAppImage(imageStartAddr)

    def createMatchedAppJsonfile( self ):
        self.srcAppFilename = self.getUserAppFilePath()
        imageStartAddr, imageEntryAddr, imageLength = self._RTxxx_getImageInfo(self.srcAppFilename)
        if imageStartAddr == None or imageEntryAddr == None:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_notFound'][self.languageIndex])
            return False
        self.isXipApp = False
        self.destAppVectorAddress = imageStartAddr
        if self.bootDevice == RTxxx_uidef.kBootDevice_FlexspiNor:
            if ((imageStartAddr >= self.tgt.flexspiNorMemBase) and (imageStartAddr < self.tgt.flexspiNorMemBase + RTxxx_rundef.kBootDeviceMemXipSize_FlexspiNor)):
                if (imageStartAddr + imageLength <= self.tgt.flexspiNorMemBase + RTxxx_rundef.kBootDeviceMemXipSize_FlexspiNor):
                    self.isXipApp = True
                    self.destAppVectorOffset = imageStartAddr - self.tgt.flexspiNorMemBase
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_xipSizeTooLarge'][self.languageIndex] + u"0x%s !" %(RTxxx_rundef.kBootDeviceMemXipSize_FlexspiNor))
                    return False
            else:
                #self.destAppVectorOffset = RT10yy_gendef.kInitialLoadSize_NOR
                pass
        elif self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
            if ((imageStartAddr >= self.tgt.quadspiNorMemBase) and (imageStartAddr < self.tgt.quadspiNorMemBase + RTxxx_rundef.kBootDeviceMemXipSize_QuadspiNor)):
                if (imageStartAddr + imageLength <= self.tgt.quadspiNorMemBase + RTxxx_rundef.kBootDeviceMemXipSize_QuadspiNor):
                    self.isXipApp = True
                    self.destAppVectorOffset = imageStartAddr - self.tgt.quadspiNorMemBase
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_xipSizeTooLarge'][self.languageIndex] + u"0x%s !" %(RTxxx_rundef.kBootDeviceMemXipSize_QuadspiNor))
                    return False
            else:
                #self.destAppVectorOffset = RT10yy_gendef.kInitialLoadSize_NOR
                pass
        else:
            pass
        if not self._RTxxx_isValidAppImage(imageStartAddr):
            return False
        self.destAppBinaryBytes = imageLength
        return self._updateJsonfileContent(self.secureBootType, self.bootDevice, imageStartAddr, imageEntryAddr)

    def _updateJsonBatfileContent( self ):
        batContent = "\"" + self.elftosbPath + "\""
        familyStr = ''
        if self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT500 or \
           self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT500S:
            familyStr = RTxxx_gendef.kMcuDeviceFamily_RT500
        elif self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT600 or \
             self.mcuDevice == RTxxx_uidef.kMcuDevice_iMXRT600S:
            familyStr = RTxxx_gendef.kMcuDeviceFamily_RT600
        else:
            pass
        batContent += " -J " + "\"" + self.appJsonFilename + "\"" + ' -f ' + familyStr
        with open(self.appJsonBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def _RTxxx_parseBootableImageGenerationResult( self, output ):
        # elftosb ouput template:
        # (All)        Parsing configuration file: xx.json.
        # (All)            Success.
        # (All)        Starting processing image....
        # (All)            Success. (xx image file: xx.bin created)
        status = False
        info1 = 'Parsing configuration file'
        info2 = 'Starting processing image'
        loc1 = output.find(info1)
        loc2 = output.find(info2)
        if loc1 != -1 and loc1 < loc2:
            info = 'Success'
            loc = output.find(info, loc2)
            if loc != -1:
                status = True
        if status:
            self.printLog('Bootable image is generated: ' + self.destAppFilename)
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_failToGen'][self.languageIndex])
        return status

    def RTxxx_genBootableImage( self ):
        if self.secureBootType != RTxxx_uidef.kSecureBootType_PlainUnsigned:
            self._updateJsonBatfileContent()
            # We have to change system dir to the path of elftosb.exe, or elftosb.exe may not be ran successfully
            curdir = os.getcwd()
            os.chdir(os.path.split(self.elftosbPath)[0])
            process = subprocess.Popen(self.appJsonBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            os.chdir(curdir)
            commandOutput = process.communicate()[0]
            print commandOutput
            if self._RTxxx_parseBootableImageGenerationResult(commandOutput):
                return True
            else:
                return False
        else:
            shutil.copy(self.srcAppFilename, self.destAppFilename)
            return True
