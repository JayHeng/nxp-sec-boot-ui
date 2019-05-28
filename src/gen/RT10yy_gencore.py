#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
import array
import shutil
import subprocess
import bincopy
import RT10yy_gendef
sys.path.append(os.path.abspath(".."))
from ui import RT10yy_uicore
from ui import RT10yy_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from run import RT10yy_rundef
from mem import RT10yy_memdef
from utils import elf

class secBootRT10yyGen(RT10yy_uicore.secBootRT10yyUi):

    def __init__(self, parent):
        RT10yy_uicore.secBootRT10yyUi.__init__(self, parent)
        self.serialFilename = os.path.join(self.exeTopRoot, 'gen', 'hab_cert', 'serial')
        self.keypassFilename = os.path.join(self.exeTopRoot, 'gen', 'hab_cert', 'key_pass.txt')
        self.cstBinFolder = os.path.join(self.exeTopRoot, 'tools', 'cst', 'mingw32', 'bin')
        self.cstKeysFolder = os.path.join(self.exeTopRoot, 'tools', 'cst', 'keys')
        self.cstCrtsFolder = os.path.join(self.exeTopRoot, 'tools', 'cst', 'crts')
        self.hab4PkiTreePath = os.path.join(self.exeTopRoot, 'tools', 'cst', 'keys')
        self.hab4PkiTreeName = 'hab4_pki_tree.bat'
        self.certBatFilename = os.path.join(self.exeTopRoot, 'gen', 'hab_cert', 'imx_cert_gen.bat')
        self.srktoolPath = os.path.join(self.exeTopRoot, 'tools', 'cst', 'mingw32', 'bin', 'srktool.exe')
        self.srkFolder = os.path.join(self.exeTopRoot, 'gen', 'hab_cert')
        self.srkTableFilename = None
        self.srkFuseFilename = None
        self.crtSrkCaPemFileList = [None] * 4
        self.crtCsfUsrPemFileList = [None] * 4
        self.crtImgUsrPemFileList = [None] * 4
        self.certBackupFolder = os.path.join(self.exeTopRoot, 'gen', 'hab_cert', 'backup')
        self.srkBatFilename = os.path.join(self.exeTopRoot, 'gen', 'hab_cert', 'imx_srk_gen.bat')
        self.cstBinToElftosbPath = '../../cst/mingw32/bin'
        self.cstCrtsToElftosbPath = '../../cst/crts/'
        self.genCertToElftosbPath = '../../../gen/hab_cert/'
        self.genCryptoToElftosbPath = '../../../gen/hab_crypto/'
        self.lastCstVersion = RT10yy_uidef.kCstVersion_v3_0_1
        self.opensslBinFolder = os.path.join(self.exeTopRoot, 'tools', 'openssl', '1.1.0j', 'win32')
        self.habDekFilename = os.path.join(self.exeTopRoot, 'gen', 'hab_crypto', 'hab_dek.bin')
        self.habDekDataOffset = None

        self.dcdFolder = os.path.join(self.exeTopRoot, 'gen', 'dcd_file')
        self.dcdBinFilename = os.path.join(self.exeTopRoot, 'gen', 'dcd_file', RT10yy_gendef.kStdDcdFilename_Bin)
        self.dcdCfgFilename = os.path.join(self.exeTopRoot, 'gen', 'dcd_file', RT10yy_gendef.kStdDcdFilename_Cfg)
        self.imgutilPath = os.path.join(self.exeTopRoot, 'tools', 'imgutil', 'win', 'imgutil.exe')
        self.dcdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'dcd_file', 'imx_dcd_gen.bat')
        self.dcdModelFolder = os.path.join(self.exeTopRoot, 'src', 'targets', 'dcd_model')
        self.dcdSdramBaseAddress = None
        self.isDcdFromSrcApp = False

        self.srcAppFilename = None
        self.destAppFilename = os.path.join(self.exeTopRoot, 'gen', 'bootable_image', 'ivt_application.bin')
        self.destAppNoPaddingFilename = os.path.join(self.exeTopRoot, 'gen', 'bootable_image', 'ivt_application_nopadding.bin')
        self.appBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_application_gen.bd')
        self.elftosbPath = os.path.join(self.exeTopRoot, 'tools', 'elftosb4', 'win', 'elftosb.exe')
        self.appBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_application_gen.bat')
        self.destSbAppFilename = os.path.join(self.exeTopRoot, 'gen', 'sb_image', 'application_device.sb')
        self.sbAppBdContent = ''
        self.sbAppBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_application_sb_gen.bd')
        self.sbAppBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_application_sb_gen.bat')
        self.destSbAppFlashFilename = os.path.join(self.exeTopRoot, 'gen', 'sb_image', 'application_device_flash.sb')
        self.sbAppFlashBdContent = ''
        self.sbAppFlashBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_app_flash_sb_gen.bd')
        self.sbAppFlashBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_app_flash_sb_gen.bat')
        self.isEfuseOperationInSbApp = False
        self.destSbAppEfuseFilename = os.path.join(self.exeTopRoot, 'gen', 'sb_image', 'application_device_efuse.sb')
        self.sbAppEfuseBdContent = ''
        self.sbAppEfuseBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_app_efuse_sb_gen.bd')
        self.sbAppEfuseBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_app_efuse_sb_gen.bat')
        self.destSbUserEfuseFilename = os.path.join(self.exeTopRoot, 'gen', 'sb_image', 'burn_efuse.sb')
        self.sbUserEfuseBdContent = ''
        self.sbUserEfuseBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_user_efuse_sb_gen.bd')
        self.sbUserEfuseBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_user_efuse_sb_gen.bat')
        self.updateAllCstPathToCorrectVersion()
        self.imageEncPath = os.path.join(self.exeTopRoot, 'tools', 'image_enc', 'win', 'image_enc.exe')
        self.beeDek0Filename = os.path.join(self.exeTopRoot, 'gen', 'bee_crypto', 'bee_dek0.bin')
        self.beeDek1Filename = os.path.join(self.exeTopRoot, 'gen', 'bee_crypto', 'bee_dek1.bin')
        self.encBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bee_crypto', 'imx_application_enc.bat')
        self.otpmkDekFilename = os.path.join(self.exeTopRoot, 'gen', 'bee_crypto', 'otpmk_dek.bin')
        self.destEncAppFilename = None
        self.destEncAppNoCfgBlockFilename = None

        self.flBdFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_flashloader_gen.bd')
        self.flBdBatFilename = os.path.join(self.exeTopRoot, 'gen', 'bd_file', 'imx_flashloader_gen.bat')
        self.destFlFilename = os.path.join(self.exeTopRoot, 'gen', 'bootable_image', 'ivt_flashloader_signed.bin')

        self.userFileFolder = os.path.join(self.exeTopRoot, 'gen', 'user_file')
        self.mdkAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'keil_mdk', 'fromelf.exe')
        self.iarElfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'iar_ewarm', 'ielftool.exe')
        self.mcuxAxfConvToolPath = os.path.join(self.exeTopRoot, 'tools', 'ide_utils', 'mcuxpresso', 'arm-none-eabi-objcopy.exe')
        self.appFmtBatFilename = os.path.join(self.exeTopRoot, 'gen', 'user_file', 'imx_format_conv.bat')
        self.isConvertedAppUsed = False

        self.destAppIvtOffset = None
        self.destAppInitialLoadSize = 0
        self.destAppVectorAddress = 0
        self.destAppVectorOffset = None
        self.destAppBinaryBytes = 0
        self.destAppCsfAddress = None
        self.isXipApp = False

    def _copyCstBinToElftosbFolder( self ):
        shutil.copy(self.cstBinFolder + '\\cst.exe', os.path.split(self.elftosbPath)[0])

    def _copyOpensslBinToCstFolder( self ):
        shutil.copy(self.opensslBinFolder + '\\openssl.exe', self.hab4PkiTreePath)
        shutil.copy(self.opensslBinFolder + '\\libcrypto-1_1.dll', self.hab4PkiTreePath)
        shutil.copy(self.opensslBinFolder + '\\libssl-1_1.dll', self.hab4PkiTreePath)
        shutil.copy(self.opensslBinFolder + '\\libcrypto-1_1.dll', self.cstBinFolder)
        shutil.copy(self.opensslBinFolder + '\\libssl-1_1.dll', self.cstBinFolder)

    def updateAllCstPathToCorrectVersion( self ):
        try:
            certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
            if self.lastCstVersion != certSettingsDict['cstVersion']:
                self.cstBinFolder = self.cstBinFolder.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.cstKeysFolder = self.cstKeysFolder.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.cstCrtsFolder = self.cstCrtsFolder.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.hab4PkiTreePath = self.hab4PkiTreePath.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.srktoolPath = self.srktoolPath.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.cstBinToElftosbPath = self.cstBinToElftosbPath.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.cstCrtsToElftosbPath = self.cstCrtsToElftosbPath.replace(self.lastCstVersion, certSettingsDict['cstVersion'])
                self.lastCstVersion = certSettingsDict['cstVersion']
            self._copyCstBinToElftosbFolder()
            self._copyOpensslBinToCstFolder()
        except:
            pass

    def _copySerialAndKeypassfileToCstFolder( self ):
        shutil.copy(self.serialFilename, self.cstKeysFolder)
        shutil.copy(self.keypassFilename, self.cstKeysFolder)
        self.printLog('serial and key_pass.txt are copied to: ' + self.cstKeysFolder)

    def createSerialAndKeypassfile( self ):
        serialContent, keypassContent = self.getSerialAndKeypassContent()
        # The 8 digits in serial are the source that Openssl use to generate certificate serial number.
        if (not serialContent.isdigit()) or len(serialContent) != 8:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['inputError_serial'][self.languageIndex])
            return False
        if len(keypassContent) == 0:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['inputError_keyPass'][self.languageIndex])
            return False
        with open(self.serialFilename, 'wb') as fileObj:
            fileObj.write(serialContent)
            fileObj.close()
        with open(self.keypassFilename, 'wb') as fileObj:
            # The 2 lines string need to be the same in key_pass.txt, which is the pass phase that used for protecting private key during code signing.
            fileObj.write(keypassContent + '\n' + keypassContent)
            fileObj.close()
        self.printLog('serial is generated: ' + self.serialFilename)
        self.printLog('key_pass.txt is generated: ' + self.keypassFilename)
        self._copySerialAndKeypassfileToCstFolder()
        return True

    def _updateCertBatfileContent( self ):
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        batArg = ''
        batArg += ' ' + certSettingsDict['useExistingCaKey']
        if certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_1_0:
            batArg += ' ' + certSettingsDict['useEllipticCurveCrypto']
            if certSettingsDict['useEllipticCurveCrypto'] == 'y':
                batArg += ' ' + certSettingsDict['pkiTreeKeyLen']
            elif certSettingsDict['useEllipticCurveCrypto'] == 'n':
                batArg += ' ' + str(certSettingsDict['pkiTreeKeyLen'])
            else:
                pass
        elif certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v2_3_3 or certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_0_1:
            batArg += ' ' + str(certSettingsDict['pkiTreeKeyLen'])
        else:
            pass
        batArg += ' ' + str(certSettingsDict['pkiTreeDuration'])
        batArg += ' ' + str(certSettingsDict['SRKs'])
        if certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_0_1 or certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_1_0:
            batArg += ' ' + certSettingsDict['caFlagSet']
        elif certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v2_3_3:
            pass
        else:
            pass

        batContent = "\"" + os.path.join(self.hab4PkiTreePath, self.hab4PkiTreeName) + "\""
        batContent += batArg
        with open(self.certBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def genCertificate( self ):
        self.updateAllCstPathToCorrectVersion()
        self._updateCertBatfileContent()
        # We have to change system dir to the path of hab4_pki_tree.bat, or hab4_pki_tree.bat will not be ran successfully
        curdir = os.getcwd()
        os.chdir(self.hab4PkiTreePath)
        os.system(self.certBatFilename)
        os.chdir(curdir)
        self.printLog('Certificates are generated into these folders: ' + self.cstKeysFolder + ' , ' + self.cstCrtsFolder)

    def _setSrkFilenames( self ):
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        srkTableName = 'SRK'
        srkFuseName = 'SRK'
        for i in range(certSettingsDict['SRKs']):
            srkTableName += '_' + str(i + 1)
            srkFuseName += '_' + str(i + 1)
        srkTableName += '_table.bin'
        srkFuseName += '_fuse.bin'
        self.srkTableFilename = os.path.join(self.srkFolder, srkTableName)
        self.srkFuseFilename = os.path.join(self.srkFolder, srkFuseName)

    def _getCrtSrkCaPemFilenames( self ):
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        for i in range(certSettingsDict['SRKs']):
            self.crtSrkCaPemFileList[i] = self.cstCrtsFolder + '\\'
            self.crtSrkCaPemFileList[i] += 'SRK' + str(i + 1) + '_sha256'
            if certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_1_0 and certSettingsDict['useEllipticCurveCrypto'] == 'y':
                self.crtSrkCaPemFileList[i] += '_' + certSettingsDict['pkiTreeKeyCn']
                self.crtSrkCaPemFileList[i] += '_v3_ca_crt.pem'
            else:
                self.crtSrkCaPemFileList[i] += '_' + str(certSettingsDict['pkiTreeKeyLen'])
                self.crtSrkCaPemFileList[i] += '_65537_v3_ca_crt.pem'

    def _getCrtCsfImgUsrPemFilenames( self ):
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        for i in range(certSettingsDict['SRKs']):
            self.crtCsfUsrPemFileList[i] = self.cstCrtsFolder + '\\'
            self.crtCsfUsrPemFileList[i] += 'CSF' + str(i + 1) + '_1_sha256'
            if certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_1_0 and certSettingsDict['useEllipticCurveCrypto'] == 'y':
                self.crtSrkCaPemFileList[i] += '_' + certSettingsDict['pkiTreeKeyCn']
                self.crtSrkCaPemFileList[i] += '_v3_usr_crt.pem'
            else:
                self.crtCsfUsrPemFileList[i] += '_' + str(certSettingsDict['pkiTreeKeyLen'])
                self.crtCsfUsrPemFileList[i] += '_65537_v3_usr_crt.pem'
            self.crtImgUsrPemFileList[i] = self.cstCrtsFolder + '\\'
            self.crtImgUsrPemFileList[i] += 'IMG' + str(i + 1) + '_1_sha256'
            if certSettingsDict['cstVersion'] == RT10yy_uidef.kCstVersion_v3_1_0 and certSettingsDict['useEllipticCurveCrypto'] == 'y':
                self.crtSrkCaPemFileList[i] += '_' + certSettingsDict['pkiTreeKeyCn']
                self.crtSrkCaPemFileList[i] += '_v3_usr_crt.pem'
            else:
                self.crtImgUsrPemFileList[i] += '_' + str(certSettingsDict['pkiTreeKeyLen'])
                self.crtImgUsrPemFileList[i] += '_65537_v3_usr_crt.pem'

    def _updateSrkBatfileContent( self ):
        self._setSrkFilenames()
        self._getCrtSrkCaPemFilenames()
        self._getCrtCsfImgUsrPemFilenames()
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        batContent = "\"" + self.srktoolPath + "\""
        batContent += " -h 4"
        batContent += " -t " + "\"" + self.srkTableFilename + "\""
        batContent += " -e " + "\"" + self.srkFuseFilename + "\""
        batContent += " -d sha256"
        batContent += " -c "
        for i in range(certSettingsDict['SRKs']):
            if i != 0:
                batContent += ','
            batContent += "\"" + self.crtSrkCaPemFileList[i] + "\""
        batContent += " -f 1"
        with open(self.srkBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def genSuperRootKeys( self ):
        self._updateSrkBatfileContent()
        #os.system(self.srkBatFilename)
        process = subprocess.Popen(self.srkBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.printLog('Public SuperRootKey files are generated successfully')

    def showSuperRootKeys( self ):
        self.clearSrkData()
        keyWords = RT10yy_gendef.kSecKeyLengthInBits_SRK / 32
        for i in range(keyWords):
            val32 = self.getVal32FromBinFile(self.srkFuseFilename, (i * 4))
            self.printSrkData(self.getFormattedHexValue(val32))

    def cleanUpCertificate( self ):
        for root, dirs, files in os.walk(self.cstCrtsFolder):
            for file in files:
                if os.path.split(file)[1] not in RT10yy_uidef.kCstCrtsFileList:
                    os.remove(os.path.join(root, file))
        for root, dirs, files in os.walk(self.cstKeysFolder):
            for file in files:
                if (os.path.split(file)[1] not in RT10yy_uidef.kCstKeysFileList) and \
                   (os.path.split(file)[1] not in RT10yy_uidef.kCstKeysToolFileList) :
                    os.remove(os.path.join(root, file))

    def backUpCertificate( self ):
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        backupFoldername = os.path.join(self.certBackupFolder, time.strftime('%Y-%m-%d_%Hh%Mm%Ss ',time.localtime(time.time())) + \
                                                               '(' + str(certSettingsDict['SRKs']) + 'srk_' + str(certSettingsDict['pkiTreeKeyLen']) + 'bits_' + str(certSettingsDict['pkiTreeDuration']) + 'years)')
        os.mkdir(backupFoldername)
        shutil.copytree(self.cstKeysFolder, os.path.join(backupFoldername, 'keys'))
        shutil.copytree(self.cstCrtsFolder, os.path.join(backupFoldername, 'crts'))
        shutil.copy(self.srkTableFilename, backupFoldername)
        shutil.copy(self.srkFuseFilename, backupFoldername)
        shutil.make_archive(backupFoldername, 'zip', root_dir=backupFoldername)
        shutil.rmtree(backupFoldername)

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
        if appFormat == RT10yy_uidef.kAppImageFormat_ElfFromIar or appFormat == RT10yy_uidef.kAppImageFormat_AxfFromMdk:
            batContent = "\"" + self.iarElfConvToolPath + "\" --srec-s3only \"" + appFilename +"\" \"" + destSrecAppFilename + "\""
        elif appFormat == RT10yy_uidef.kAppImageFormat_AxfFromMcux or appFormat == RT10yy_uidef.kAppImageFormat_ElfFromGcc:
            batContent = "\"" + self.mcuxAxfConvToolPath + "\" -O srec \"" + appFilename +"\" \"" + destSrecAppFilename + "\""
        #elif appFormat == RT10yy_uidef.kAppImageFormat_AxfFromMdk:
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
            appType = RT10yy_gendef.kAppImageFileExtensionList_S19[0]
            self.isConvertedAppUsed = True
            self.printLog('User image file has been converted to S-Records successfully')
            return self.srcAppFilename, appType
        else:
            appType = RT10yy_gendef.kAppImageFileExtensionList_Elf[0]
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
        if appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_Hex:
            fmtObj = bincopy.BinFile(str(appFilename))
        elif appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_Bin:
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
            appType = RT10yy_gendef.kAppImageFileExtensionList_S19[0]
            self.isConvertedAppUsed = True
        return appFilename, appType

    def _convertImageFormatToSrec( self, appFilename, appName, appType):
        appFormat = self.getUserAppFileFormat()
        destSrecAppFilename = os.path.join(self.userFileFolder, appName + RT10yy_gendef.kAppImageFileExtensionList_S19[0])
        if appFormat == RT10yy_uidef.kAppImageFormat_AutoDetect:
            if appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_S19:
                return appFilename, appType
            elif (appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_Hex) or (appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_Bin):
                return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, appType)
            else:
                appFilename, appType = self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, RT10yy_uidef.kAppImageFormat_ElfFromIar)
                if appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_S19:
                    return appFilename, appType
                appFilename, appType = self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, RT10yy_uidef.kAppImageFormat_AxfFromMcux)
                if appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_S19:
                    return appFilename, appType
                return self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, RT10yy_uidef.kAppImageFormat_AxfFromMdk)
        elif appFormat == RT10yy_uidef.kAppImageFormat_AxfFromMdk or \
             appFormat == RT10yy_uidef.kAppImageFormat_ElfFromIar or \
             appFormat == RT10yy_uidef.kAppImageFormat_AxfFromMcux or \
             appFormat == RT10yy_uidef.kAppImageFormat_ElfFromGcc:
            return self._convertElfOrAxfToSrec(appFilename, destSrecAppFilename, appFormat)
        elif appFormat == RT10yy_uidef.kAppImageFormat_IntelHex:
            return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, RT10yy_gendef.kAppImageFileExtensionList_Hex[0])
        elif appFormat == RT10yy_uidef.kAppImageFormat_RawBinary:
            return self._convertHexOrBinToSrec(appFilename, destSrecAppFilename, RT10yy_gendef.kAppImageFileExtensionList_Bin[0])
        elif appFormat == RT10yy_uidef.kAppImageFormat_MotoSrec:
            return appFilename, RT10yy_gendef.kAppImageFileExtensionList_S19[0]
        else:
            pass

    def _getIvtInfoFromIvtBlockBytes( self, ivtBlockBytes ):
        ivtEntry= self.getVal32FromByteArray(ivtBlockBytes[RT10yy_memdef.kMemberOffsetInIvt_Entry:RT10yy_memdef.kMemberOffsetInIvt_Entry + 4])
        ivtDcd= self.getVal32FromByteArray(ivtBlockBytes[RT10yy_memdef.kMemberOffsetInIvt_Dcd:RT10yy_memdef.kMemberOffsetInIvt_Dcd + 4])
        ivtBd= self.getVal32FromByteArray(ivtBlockBytes[RT10yy_memdef.kMemberOffsetInIvt_BootData:RT10yy_memdef.kMemberOffsetInIvt_BootData + 4])
        ivtSelf= self.getVal32FromByteArray(ivtBlockBytes[RT10yy_memdef.kMemberOffsetInIvt_Self:RT10yy_memdef.kMemberOffsetInIvt_Self + 4])
        return ivtEntry, ivtDcd, ivtBd, ivtSelf

    def _extractDcdDataFromSrcApp(self, initialLoadAppBytes ):
        ivtEntry, ivtDcd, ivtBd, ivtSelf = self._getIvtInfoFromIvtBlockBytes(initialLoadAppBytes[self.destAppIvtOffset:self.destAppIvtOffset + RT10yy_memdef.kMemBlockSize_IVT])
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        if ivtDcd != 0 and ivtDcd < ivtEntry and (not dcdCtrlDict['isDcdEnabled']):
            dcdDataOffset = self.destAppIvtOffset + ivtDcd - ivtSelf
            # Note: We cannot specify dcd offset when generating bootable image by elftosb, dcd offset is always kMemBlockOffsetToIvt_DCD
            #       but dcd offset can be set arbitrarily in src app image as it is generated by IDE
            dcdHoleBytes = 0x0
            if ivtDcd - ivtSelf < RT10yy_memdef.kMemBlockOffsetToIvt_DCD:
                dcdHoleBytes = RT10yy_memdef.kMemBlockOffsetToIvt_DCD - (ivtDcd - ivtSelf)
            dcdDataBytes = initialLoadAppBytes[dcdDataOffset:len(initialLoadAppBytes) - dcdHoleBytes]
            dcdDataTag = dcdDataBytes[RT10yy_memdef.kMemberOffsetInDcd_Tag]
            if dcdDataTag == RT10yy_memdef.kBootHeaderTag_DCD:
                with open(self.dcdBinFilename, 'wb') as fileObj:
                    fileObj.write(dcdDataBytes)
                    fileObj.close()
                self._enableDcdBecauseOfSrcApp()
                self.isDcdFromSrcApp = True

    def _extractImageDataFromSrcApp(self, wholeSrcAppBytes, appName ):
        ivtEntry, ivtDcd, ivtBd, ivtSelf = self._getIvtInfoFromIvtBlockBytes(wholeSrcAppBytes[self.destAppIvtOffset:self.destAppIvtOffset + RT10yy_memdef.kMemBlockSize_IVT])
        imageDataOffset = self.destAppIvtOffset + ivtEntry - ivtSelf
        imageDataBytes = wholeSrcAppBytes[imageDataOffset:len(wholeSrcAppBytes)]
        imageEntryPoint = self.getVal32FromByteArray(wholeSrcAppBytes[imageDataOffset + 0x4:imageDataOffset + 0x8])
        fmtObj = bincopy.BinFile()
        fmtObj.add_binary(imageDataBytes, ivtEntry)
        self.srcAppFilename = os.path.join(self.userFileFolder, appName + '_extracted' + RT10yy_gendef.kAppImageFileExtensionList_S19[0])
        with open(self.srcAppFilename, 'wb') as fileObj:
            fileObj.write(self._getSrecDataWithoutS6Frame(fmtObj.as_srec(16, 32)))
            fileObj.close()
        self.isConvertedAppUsed = True
        return ivtEntry, imageEntryPoint, len(imageDataBytes)

    def _isSrcAppBootableImage( self, initialLoadAppBytes ):
        ivtTag = initialLoadAppBytes[self.destAppIvtOffset + RT10yy_memdef.kMemberOffsetInIvt_Tag]
        ivtLen = initialLoadAppBytes[self.destAppIvtOffset + RT10yy_memdef.kMemberOffsetInIvt_Len]
        if ivtTag != RT10yy_memdef.kBootHeaderTag_IVT or ivtLen != RT10yy_memdef.kMemBlockSize_IVT:
            return False
        ivtEntry, ivtDcd, ivtBd, ivtSelf = self._getIvtInfoFromIvtBlockBytes(initialLoadAppBytes[self.destAppIvtOffset:self.destAppIvtOffset + RT10yy_memdef.kMemBlockSize_IVT])
        if (ivtBd <= ivtSelf) or (ivtBd - ivtSelf != RT10yy_memdef.kMemBlockSize_IVT):
            return False
        self.printLog('Origianl image file is a bootable image file')
        return True

    def _getImageInfo( self, srcAppFilename ):
        startAddress = None
        entryPointAddress = None
        lengthInByte = 0
        if os.path.isfile(srcAppFilename):
            appPath, appFilename = os.path.split(srcAppFilename)
            appName, appType = os.path.splitext(appFilename)
            srcAppFilename, appType = self._convertImageFormatToSrec(srcAppFilename, appName, appType)
            isConvSuccessed = False
            if appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_Elf:
                try:
                    elfObj = None
                    with open(srcAppFilename, 'rb') as f:
                        e = elf.ELFObject()
                        e.fromFile(f)
                        elfObj = e
                    #for symbol in RT10yy_gendef.kToolchainSymbolList_VectorAddr:
                    #    try:
                    #        startAddress = elfObj.getSymbol(symbol).st_value
                    #        break
                    #    except:
                    #        startAddress = None
                    #if startAddress == None:
                    #    self.popupMsgBox('Cannot get vectorAddr symbol from image file: ' + srcAppFilename)
                    #entryPointAddress = elfObj.e_entry
                    #for symbol in RT10yy_gendef.kToolchainSymbolList_EntryAddr:
                    #    try:
                    #        entryPointAddress = elfObj.getSymbol(symbol).st_value
                    #        break
                    #    except:
                    #        entryPointAddress = None
                    #if entryPointAddress == None:
                    #    self.popupMsgBox('Cannot get entryAddr symbol from image file: ' + srcAppFilename)
                    startAddress = elfObj.programmheaders[0].p_paddr
                    entryPointAddress = self.getVal32FromBinFile(srcAppFilename, elfObj.programmheaders[0].p_offset + 4)
                    for i in range(elfObj.e_phnum):
                        lengthInByte += elfObj.programmheaders[i].p_memsz
                    isConvSuccessed = True
                except:
                    pass
            elif appType.lower() in RT10yy_gendef.kAppImageFileExtensionList_S19:
                try:
                    srecObj = bincopy.BinFile(str(srcAppFilename))
                    startAddress = srecObj.minimum_address
                    initialLoadAppBytes = srecObj.as_binary(startAddress, startAddress + self.destAppInitialLoadSize)
                    if self._isSrcAppBootableImage(initialLoadAppBytes):
                        self._extractDcdDataFromSrcApp(initialLoadAppBytes)
                        startAddress, entryPointAddress, lengthInByte = self._extractImageDataFromSrcApp(srecObj.as_binary(), appName)
                    else:
                        #entryPointAddress = srecObj.execution_start_address
                        entryPointAddress = self.getVal32FromByteArray(srecObj.as_binary(startAddress + 0x4, startAddress  + 0x8))
                        lengthInByte = len(srecObj.as_binary())
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
        #print ('Image Vector address is 0x%x' %(startAddress))
        #print ('Image Entry address is 0x%x' %(entryPointAddress))
        #print ('Image length is 0x%x' %(lengthInByte))
        return startAddress, entryPointAddress, lengthInByte

    def _verifyAppVectorAddressForBd( self, vectorAddr, initialLoadSize ):
        executeBase = 0
        if ((vectorAddr >= self.tgt.memoryRange['itcm'].start) and (vectorAddr < self.tgt.memoryRange['itcm'].start + self.tgt.memoryRange['itcm'].length)):
             executeBase = self.tgt.memoryRange['itcm'].start
        elif ((vectorAddr >= self.tgt.memoryRange['dtcm'].start) and (vectorAddr < self.tgt.memoryRange['dtcm'].start + self.tgt.memoryRange['dtcm'].length)):
             executeBase = self.tgt.memoryRange['dtcm'].start
        elif ((vectorAddr >= self.tgt.memoryRange['ocram'].start) and (vectorAddr < self.tgt.memoryRange['ocram'].start + self.tgt.memoryRange['ocram'].length)):
             executeBase = self.tgt.memoryRange['ocram'].start
        elif ((vectorAddr >= self.tgt.flexspiNorMemBase) and (vectorAddr < self.tgt.flexspiNorMemBase + RT10yy_rundef.kBootDeviceMemXipSize_FlexspiNor)):
             executeBase = self.tgt.flexspiNorMemBase
        elif ((vectorAddr >= RT10yy_rundef.kBootDeviceMemBase_SemcNor) and (vectorAddr < RT10yy_rundef.kBootDeviceMemBase_SemcNor + RT10yy_rundef.kBootDeviceMemXipSize_SemcNor)):
             executeBase = RT10yy_rundef.kBootDeviceMemBase_SemcNor
        elif ((self.dcdSdramBaseAddress != None) and ((vectorAddr >= self.dcdSdramBaseAddress) and (vectorAddr < RT10yy_rundef.kBootDeviceMemBase_SemcSdram + RT10yy_rundef.kBootDeviceMemMaxSize_SemcSdram))):
             executeBase = self.dcdSdramBaseAddress
        else:
            pass
        if (vectorAddr - executeBase) >= initialLoadSize:
            return True
        else:
            return False

    def _updateDcdBatfileContent( self ):
        batContent = "\"" + self.imgutilPath + "\""
        batContent += " --dcd_gen"
        batContent += " dcd_desc_file=" + "\"" + self.dcdCfgFilename + "\""
        batContent += " ofile=" + "\"" + self.dcdBinFilename + "\""
        with open(self.dcdBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def _parseDcdGenerationResult( self, output ):
        # imgutil ouput template:
        # DCD binary file is generated successfully
        info = 'DCD binary file is generated successfully'
        if output.find(info) != -1:
            self.printLog('DCD binary is generated: ' + self.dcdBinFilename)
            return True
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['genDcdError_failToGen'][self.languageIndex])
            return False

    def _genDcdBinFileAccordingToCfgFile( self ):
        curdir = os.getcwd()
        os.chdir(os.path.split(self.imgutilPath)[0])
        process = subprocess.Popen(self.dcdBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.chdir(curdir)
        commandOutput = process.communicate()[0]
        print commandOutput
        if self._parseDcdGenerationResult(commandOutput):
            return True
        else:
            return False

    def _enableDcdBecauseOfSrcApp( self ):
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        dcdCtrlDict['isDcdEnabled'] = True
        dcdCtrlDict['dcdFileType'] = RT10yy_gendef.kUserDcdFileType_Bin
        dcdSettingsDict['sdramBase'] = '0x80000000'
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd, dcdCtrlDict, dcdSettingsDict)

    def _recoverDcdBecauseOfSrcApp( self ):
        if self.isDcdFromSrcApp:
            dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
            dcdCtrlDict['isDcdEnabled'] = False
            uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd, dcdCtrlDict, dcdSettingsDict)
            self.isDcdFromSrcApp = False

    def _addDcdContentIfAppliable( self ):
        dcdConvResult = True
        dcdContent = ''
        self.dcdSdramBaseAddress = None
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            if dcdCtrlDict['dcdFileType'] == RT10yy_gendef.kUserDcdFileType_Bin:
                pass
            elif dcdCtrlDict['dcdFileType'] == RT10yy_gendef.kUserDcdFileType_Cfg:
                self._updateDcdBatfileContent()
                dcdConvResult = self._genDcdBinFileAccordingToCfgFile()
            else:
                pass
            if dcdConvResult:
                shutil.copy(self.dcdBinFilename, os.path.join(os.path.split(self.elftosbPath)[0], RT10yy_gendef.kStdDcdFilename_Bin))
                dcdContent += "    DCDFilePath = \"" + RT10yy_gendef.kStdDcdFilename_Bin + "\";\n"
                if dcdSettingsDict['sdramBase'] != None:
                    self.dcdSdramBaseAddress = self._getVal32FromHexText(dcdSettingsDict['sdramBase'])
        return dcdConvResult, dcdContent

    def _setDestAppInitialBootHeaderInfo( self, bootDevice ):
        if bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or \
           bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
            self.destAppIvtOffset = RT10yy_gendef.kIvtOffset_NOR
            self.destAppInitialLoadSize = RT10yy_gendef.kInitialLoadSize_NOR
        elif bootDevice == RT10yy_uidef.kBootDevice_FlexspiNand or \
             bootDevice == RT10yy_uidef.kBootDevice_SemcNand or \
             bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
             bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc or \
             bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            self.destAppIvtOffset = RT10yy_gendef.kIvtOffset_NAND_SD_EEPROM
            self.destAppInitialLoadSize = RT10yy_gendef.kInitialLoadSize_NAND_SD_EEPROM
        elif bootDevice == RT10yy_uidef.kBootDevice_RamFlashloader:
            self.destAppIvtOffset = RT10yy_gendef.kIvtOffset_RAM_FLASHLOADER
            self.destAppInitialLoadSize = RT10yy_gendef.kInitialLoadSize_RAM_FLASHLOADER
        else:
            pass

    def _setDestAppFinalBootHeaderInfo( self, bootDevice ):
        self._setDestAppInitialBootHeaderInfo(bootDevice)
        if bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or \
           bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
            if self.isXipApp:
                self.destAppInitialLoadSize = self.destAppVectorOffset
            else:
                self.destAppInitialLoadSize = RT10yy_gendef.kInitialLoadSize_NOR
        elif bootDevice == RT10yy_uidef.kBootDevice_FlexspiNand or \
             bootDevice == RT10yy_uidef.kBootDevice_SemcNand or \
             bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
             bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc or \
             bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            self.isXipApp = False
            self.destAppVectorOffset = self.destAppInitialLoadSize
        else:
            pass

    def _updateBdfileContent( self, secureBootType, bootDevice, vectorAddress, entryPointAddress):
        bdContent = ""
        ############################################################################
        bdContent += "options {\n"
        if secureBootType == RT10yy_uidef.kSecureBootType_Development:
            flags = RT10yy_gendef.kBootImageTypeFlag_Unsigned
        elif secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
            flags = RT10yy_gendef.kBootImageTypeFlag_Signed
        elif secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
            flags = RT10yy_gendef.kBootImageTypeFlag_Encrypted
        elif secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
            if self.isCertEnabledForBee:
                flags = RT10yy_gendef.kBootImageTypeFlag_Signed
            else:
                flags = RT10yy_gendef.kBootImageTypeFlag_Unsigned
        else:
            pass
        bdContent += "    flags = " + flags + ";\n"
        startAddress = 0x0
        self._setDestAppFinalBootHeaderInfo(bootDevice)
        if not self._verifyAppVectorAddressForBd(vectorAddress, self.destAppInitialLoadSize):
            if bootDevice != RT10yy_uidef.kBootDevice_RamFlashloader:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_invalidVector'][self.languageIndex] + self.srcAppFilename)
            return False
        else:
            startAddress = vectorAddress - self.destAppInitialLoadSize
        bdContent += "    startAddress = " + self.convertLongIntHexText(str(hex(startAddress))) + ";\n"
        bdContent += "    ivtOffset = " + self.convertLongIntHexText(str(hex(self.destAppIvtOffset))) + ";\n"
        bdContent += "    initialLoadSize = " + self.convertLongIntHexText(str(hex(self.destAppInitialLoadSize))) + ";\n"
        dcdConvResult, dcdContent = self._addDcdContentIfAppliable()
        if dcdConvResult:
            bdContent += dcdContent
        else:
            return False
        if secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
            #bdContent += "    cstFolderPath = \"" + self.cstBinFolder + "\";\n"
            #bdContent += "    cstFolderPath = \"" + self.cstBinToElftosbPath + "\";\n"
            pass
        else:
            pass
        bdContent += "    entryPointAddress = " + self.convertLongIntHexText(str(hex(entryPointAddress))) + ";\n"
        bdContent += "}\n"
        ############################################################################
        bdContent += "\nsources {\n"
        bdContent += "    elfFile = extern(0);\n"
        bdContent += "}\n"
        ############################################################################
        if secureBootType == RT10yy_uidef.kSecureBootType_Development or \
           (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and (not self.isCertEnabledForBee)):
            bdContent += "\nsection (0) {\n"
            bdContent += "}\n"
        elif secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or \
             secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto or \
             (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
            ########################################################################
            bdContent += "\nconstants {\n"
            bdContent += "    SEC_CSF_HEADER              = 20;\n"
            bdContent += "    SEC_CSF_INSTALL_SRK         = 21;\n"
            bdContent += "    SEC_CSF_INSTALL_CSFK        = 22;\n"
            bdContent += "    SEC_CSF_INSTALL_NOCAK       = 23;\n"
            bdContent += "    SEC_CSF_AUTHENTICATE_CSF    = 24;\n"
            bdContent += "    SEC_CSF_INSTALL_KEY         = 25;\n"
            bdContent += "    SEC_CSF_AUTHENTICATE_DATA   = 26;\n"
            bdContent += "    SEC_CSF_INSTALL_SECRET_KEY  = 27;\n"
            bdContent += "    SEC_CSF_DECRYPT_DATA        = 28;\n"
            bdContent += "    SEC_NOP                     = 29;\n"
            bdContent += "    SEC_SET_MID                 = 30;\n"
            bdContent += "    SEC_SET_ENGINE              = 31;\n"
            bdContent += "    SEC_INIT                    = 32;\n"
            bdContent += "    SEC_UNLOCK                  = 33;\n"
            bdContent += "}\n"
            ########################################################################
            bdContent += "\nsection (SEC_CSF_HEADER;\n"
            if secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or \
               (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
                headerVersion = RT10yy_gendef.kBootImageCsfHeaderVersion_Signed
            elif secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                headerVersion = RT10yy_gendef.kBootImageCsfHeaderVersion_Encrypted
            else:
                pass
            bdContent += "    Header_Version=\"" + headerVersion + "\",\n"
            bdContent += "    Header_HashAlgorithm=\"sha256\",\n"
            bdContent += "    Header_Engine=\"DCP\",\n"
            bdContent += "    Header_EngineConfiguration=0,\n"
            bdContent += "    Header_CertificateFormat=\"x509\",\n"
            bdContent += "    Header_SignatureFormat=\"CMS\"\n"
            bdContent += "    )\n"
            bdContent += "{\n"
            bdContent += "}\n"
            ########################################################################
            bdContent += "\nsection (SEC_CSF_INSTALL_SRK;\n"
            #bdContent += "    InstallSRK_Table=\"" + self.srkTableFilename + "\",\n"
            bdContent += "    InstallSRK_Table=\"" + self.genCertToElftosbPath + os.path.split(self.srkTableFilename)[1] + "\",\n"
            bdContent += "    InstallSRK_SourceIndex=0\n"
            bdContent += "    )\n"
            bdContent += "{\n"
            bdContent += "}\n"
            bdContent += "\nsection (SEC_CSF_INSTALL_CSFK;\n"
            #bdContent += "    InstallCSFK_File=\"" + self.crtCsfUsrPemFileList[0] + "\",\n"
            bdContent += "    InstallCSFK_File=\"" + self.cstCrtsToElftosbPath + os.path.split(self.crtCsfUsrPemFileList[0])[1] + "\",\n"
            bdContent += "    InstallCSFK_CertificateFormat=\"x509\"\n"
            bdContent += "    )\n"
            bdContent += "{\n"
            bdContent += "}\n"
            bdContent += "\nsection (SEC_CSF_AUTHENTICATE_CSF)\n"
            bdContent += "{\n"
            bdContent += "}\n"
            bdContent += "\nsection (SEC_CSF_INSTALL_KEY;\n"
            #bdContent += "    InstallKey_File=\"" + self.crtImgUsrPemFileList[0] + "\",\n"
            bdContent += "    InstallKey_File=\"" + self.cstCrtsToElftosbPath + os.path.split(self.crtImgUsrPemFileList[0])[1] + "\",\n"
            bdContent += "    InstallKey_VerificationIndex=0,\n"
            bdContent += "    InstallKey_TargetIndex=2)\n"
            bdContent += "{\n"
            bdContent += "}\n"
            bdContent += "\nsection (SEC_CSF_AUTHENTICATE_DATA;\n"
            bdContent += "    AuthenticateData_VerificationIndex=2,\n"
            bdContent += "    AuthenticateData_Engine=\"DCP\",\n"
            bdContent += "    AuthenticateData_EngineConfiguration=0)\n"
            bdContent += "{\n"
            bdContent += "}\n"
            ########################################################################
            if secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or \
               (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
                bdContent += "\nsection (SEC_SET_ENGINE;\n"
                bdContent += "    SetEngine_HashAlgorithm = \"sha256\",\n"
                bdContent += "    SetEngine_Engine = \"DCP\",\n"
                bdContent += "    SetEngine_EngineConfiguration = \"0\")\n"
                bdContent += "{\n"
                bdContent += "}\n"
                bdContent += "\nsection (SEC_UNLOCK;\n"
                bdContent += "    Unlock_Engine = \"SNVS\",\n"
                bdContent += "    Unlock_features = \"ZMK WRITE\"\n"
                bdContent += "    )\n"
                bdContent += "{\n"
                bdContent += "}\n"
            elif secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                bdContent += "section (SEC_CSF_INSTALL_SECRET_KEY;\n"
                bdContent += "    SecretKey_Name=\"" + self.genCryptoToElftosbPath + os.path.split(self.habDekFilename)[1] + "\",\n"
                bdContent += "    SecretKey_Length=128,\n"
                bdContent += "    SecretKey_VerifyIndex=0,\n"
                bdContent += "    SecretKey_TargetIndex=0)\n"
                bdContent += "{\n"
                bdContent += "}\n"
                bdContent += "section (SEC_CSF_DECRYPT_DATA;\n"
                bdContent += "    Decrypt_Engine=\"DCP\",\n"
                bdContent += "    Decrypt_EngineConfiguration=\"0\",\n"
                bdContent += "    Decrypt_VerifyIndex=0,\n"
                bdContent += "    Decrypt_MacBytes=16)\n"
                bdContent += "{\n"
                bdContent += "}\n"
            else:
                pass
            ########################################################################
        else:
            pass

        if bootDevice == RT10yy_uidef.kBootDevice_RamFlashloader:
            with open(self.flBdFilename, 'wb') as fileObj:
                fileObj.write(bdContent)
                fileObj.close()
        else:
            with open(self.appBdFilename, 'wb') as fileObj:
                fileObj.write(bdContent)
                fileObj.close()

        return True

    def _tryToReuseExistingCert( self ):
        self._setSrkFilenames()
        self._getCrtSrkCaPemFilenames()
        self._getCrtCsfImgUsrPemFilenames()

    def isCertificateGenerated( self, secureBootType ):
        if secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or \
           secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto or \
           (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.isCertEnabledForBee):
            self._tryToReuseExistingCert()
            if (os.path.isfile(self.srkTableFilename) and \
                os.path.isfile(self.srkFuseFilename) and \
                os.path.isfile(self.crtSrkCaPemFileList[0]) and \
                os.path.isfile(self.crtCsfUsrPemFileList[0]) and \
                os.path.isfile(self.crtImgUsrPemFileList[0])):
                self.showSuperRootKeys()
                return True
            else:
                return False
        elif secureBootType == RT10yy_uidef.kSecureBootType_Development or \
             (secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and (not self.isCertEnabledForBee)):
            return True
        else:
            pass

    def isInTheRangeOfFlexram( self, start, length ):
        if ((start >= self.tgt.memoryRange['itcm'].start) and (start + length <= self.tgt.memoryRange['itcm'].start + self.tgt.memoryRange['itcm'].length)) or \
           ((start >= self.tgt.memoryRange['dtcm'].start) and (start + length <= self.tgt.memoryRange['dtcm'].start + self.tgt.memoryRange['dtcm'].length)) or \
           ((start >= self.tgt.memoryRange['ocram'].start) and (start + length <= self.tgt.memoryRange['ocram'].start + self.tgt.memoryRange['ocram'].length)):
            return True
        else:
            return False

    def _isValidNonXipAppImage( self, imageStartAddr ):
        if self.isInTheRangeOfFlexram(imageStartAddr, 1):
            return True
        elif ((imageStartAddr >= RT10yy_rundef.kBootDeviceMemBase_SemcSdram) and (imageStartAddr < RT10yy_rundef.kBootDeviceMemBase_SemcSdram + RT10yy_rundef.kBootDeviceMemMaxSize_SemcSdram)):
            return True
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_invalidNonXipRange'][self.languageIndex])
            return False

    def _isValidAppImage( self, imageStartAddr ):
        if self.isXipApp:
            if self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_xipNotForHabCrypto'][self.languageIndex])
                return False
            else:
                return True
        else:
            #if self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
            #    self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_nonXipNotForBeeCrypto'][self.languageIndex])
            #    return False
            #else:
            if (self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth) and \
               (self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor) and \
               (not self.tgt.isNonXipImageAppliableForXipableDeviceUnderClosedHab):
               self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_nonXipNotAppliable'][self.languageIndex])
               return False
            return self._isValidNonXipAppImage(imageStartAddr)

    def createMatchedAppBdfile( self ):
        self.srcAppFilename = self.getUserAppFilePath()
        self._setDestAppInitialBootHeaderInfo(self.bootDevice)
        imageStartAddr, imageEntryAddr, imageLength = self._getImageInfo(self.srcAppFilename)
        if imageStartAddr == None or imageEntryAddr == None:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_notFound'][self.languageIndex])
            return False
        self.isXipApp = False
        self.destAppVectorAddress = imageStartAddr
        if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            if ((imageStartAddr >= self.tgt.flexspiNorMemBase) and (imageStartAddr < self.tgt.flexspiNorMemBase + RT10yy_rundef.kBootDeviceMemXipSize_FlexspiNor)):
                if (imageStartAddr + imageLength <= self.tgt.flexspiNorMemBase + RT10yy_rundef.kBootDeviceMemXipSize_FlexspiNor):
                    self.isXipApp = True
                    self.destAppVectorOffset = imageStartAddr - self.tgt.flexspiNorMemBase
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_xipSizeTooLarge'][self.languageIndex] + u"0x%s !" %(RT10yy_rundef.kBootDeviceMemXipSize_FlexspiNor))
                    return False
            else:
                self.destAppVectorOffset = RT10yy_gendef.kInitialLoadSize_NOR
        elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
            if ((imageStartAddr >= RT10yy_rundef.kBootDeviceMemBase_SemcNor) and (imageStartAddr < RT10yy_rundef.kBootDeviceMemBase_SemcNor + RT10yy_rundef.kBootDeviceMemXipSize_SemcNor)):
                if (imageStartAddr + imageLength <= RT10yy_rundef.kBootDeviceMemBase_SemcNor + RT10yy_rundef.kBootDeviceMemXipSize_SemcNor):
                    self.isXipApp = True
                    self.destAppVectorOffset = imageStartAddr - RT10yy_rundef.kBootDeviceMemBase_SemcNor
                else:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_xipSizeTooLarge'][self.languageIndex] + u"0x%s !" %(RT10yy_rundef.kBootDeviceMemXipSize_SemcNor))
                    return False
            else:
                self.destAppVectorOffset = RT10yy_gendef.kInitialLoadSize_NOR
        else:
            pass
        if not self._isValidAppImage(imageStartAddr):
            return False
        self.destAppBinaryBytes = imageLength
        if not self.isCertificateGenerated(self.secureBootType):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operCertError_notGen'][self.languageIndex])
            return False
        return self._updateBdfileContent(self.secureBootType, self.bootDevice, imageStartAddr, imageEntryAddr)

    def _adjustDestAppFilenameForBd( self ):
        srcAppName = os.path.splitext(os.path.split(self.srcAppFilename)[1])[0]
        destAppPath, destAppFile = os.path.split(self.destAppFilename)
        destAppName, destAppType = os.path.splitext(destAppFile)
        destAppName ='ivt_' + srcAppName
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_Dcd)
        if dcdCtrlDict['isDcdEnabled']:
            destAppName += '_dcd'
        if self.secureBootType == RT10yy_uidef.kSecureBootType_Development:
            destAppName += '_unsigned'
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
            destAppName += '_signed'
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
            destAppName += '_signed_hab_encrypted'
        elif self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
            if self.isCertEnabledForBee:
                destAppName += '_signed'
            else:
                destAppName += '_unsigned'
        else:
            pass
        self.destAppFilename = os.path.join(destAppPath, destAppName + destAppType)
        self.destAppNoPaddingFilename = os.path.join(destAppPath, destAppName + '_nopadding' + destAppType)

    def _updateBdBatfileContent( self ):
        self._adjustDestAppFilenameForBd()
        batContent = "\"" + self.elftosbPath + "\""
        batContent += " -f imx -V -c " + "\"" + self.appBdFilename + "\"" + ' -o ' + "\"" + self.destAppFilename + "\"" + ' ' + "\"" + self.srcAppFilename + "\""
        with open(self.appBdBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def _parseBootableImageGenerationResult( self, output ):
        # elftosb ouput template:
        # (Signed)     CSF Processed successfully and signed data available in csf.bin
        # (All)                Section: xxx
        # (All)                ...
        # (All)        iMX bootable image generated successfully
        # (Encrypted)  Key Blob Address is 0xe000.
        # (Encrypted)  Key Blob data should be placed at Offset :0x6000 in the image
        info = 'iMX bootable image generated successfully'
        if output.find(info) != -1:
            self.printLog('Bootable image is generated: ' + self.destAppFilename)
            info1 = 'Key Blob data should be placed at Offset :0x'
            info2 = ' in the image'
            loc1 = output.find(info1)
            loc2 = output.find(info2)
            if loc1 != -1 and loc1 < loc2:
                loc1 += len(info1)
                self.habDekDataOffset = int(output[loc1:loc2], 16)
            else:
                self.habDekDataOffset = None
            return True
        else:
            self.habDekDataOffset = None
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_failToGen'][self.languageIndex])
            return False

    def genBootableImage( self ):
        self._updateBdBatfileContent()
        # We have to change system dir to the path of elftosb.exe, or elftosb.exe may not be ran successfully
        curdir = os.getcwd()
        os.chdir(os.path.split(self.elftosbPath)[0])
        process = subprocess.Popen(self.appBdBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.chdir(curdir)
        commandOutput = process.communicate()[0]
        print commandOutput
        self._recoverDcdBecauseOfSrcApp()
        if self._parseBootableImageGenerationResult(commandOutput):
            return True
        else:
            return False

    def showHabDekIfApplicable( self ):
        if self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto and self.habDekDataOffset != None:
            if os.path.isfile(self.habDekFilename):
                self.clearHabDekData()
                keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
                for i in range(keyWords):
                    val32 = self.getVal32FromBinFile(self.habDekFilename, (i * 4))
                    self.printHabDekData(self.getFormattedHexValue(val32))

    def _setDestAppFilenameForBee( self ):
        destAppPath, destAppFile = os.path.split(self.destAppFilename)
        destAppName, destAppType = os.path.splitext(destAppFile)
        destAppName += '_bee_encrypted'
        self.destEncAppFilename = os.path.join(destAppPath, destAppName + destAppType)

    def _genBeeDekFile( self, engineIndex, keyContent ):
        if engineIndex == 0:
            #print 'beeDek0Filename content: ' + keyContent
            self.fillDek128ContentIntoBinFile(self.beeDek0Filename, keyContent)
        elif engineIndex == 1:
            #print 'beeDek1Filename content: ' + keyContent
            self.fillDek128ContentIntoBinFile(self.beeDek1Filename, keyContent)
        else:
            pass

    def _showBeeDekForGp4( self, dekFilename ):
        if os.path.isfile(dekFilename):
            self.clearGp4DekData()
            keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
            for i in range(keyWords):
                val32 = self.getVal32FromBinFile(dekFilename, (i * 4))
                self.printGp4DekData(self.getFormattedHexValue(val32))

    def _showBeeDekForSwGp2( self, dekFilename ):
        if os.path.isfile(dekFilename):
            self.clearSwGp2DekData()
            keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
            for i in range(keyWords):
                val32 = self.getVal32FromBinFile(dekFilename, (i * 4))
                self.printSwGp2DekData(self.getFormattedHexValue(val32))

    def _genBeeDekFilesAndShow( self, userKeyCtrlDict, userKeyCmdDict ):
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self._genBeeDekFile(0, userKeyCmdDict['engine0_key'])
            if userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                self._showBeeDekForSwGp2(self.beeDek0Filename)
            elif userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                self._showBeeDekForGp4(self.beeDek0Filename)
            else:
                pass
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            self._genBeeDekFile(1, userKeyCmdDict['engine1_key'])
            if userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                self._showBeeDekForSwGp2(self.beeDek1Filename)
            elif userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                self._showBeeDekForGp4(self.beeDek1Filename)
            else:
                pass

    def _updateEncBatfileContent( self, userKeyCtrlDict, userKeyCmdDict ):
        batContent = "\"" + self.imageEncPath + "\""
        batContent += " ifile=" + "\"" + self.destAppFilename + "\""
        batContent += " ofile=" + "\"" + self.destEncAppFilename + "\""
        batContent += " base_addr=" + userKeyCmdDict['base_addr']
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            batContent += " region0_key=" + userKeyCmdDict['engine0_key']
            batContent += " region0_arg=" + userKeyCmdDict['engine0_arg']
            batContent += " region0_lock=" + userKeyCmdDict['engine0_lock']
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            batContent += " region1_key=" + userKeyCmdDict['engine1_key']
            batContent += " region1_arg=" + userKeyCmdDict['engine1_arg']
            batContent += " region1_lock=" + userKeyCmdDict['engine1_lock']
        batContent += " use_zero_key=" + userKeyCmdDict['use_zero_key']
        batContent += " is_boot_image=" + userKeyCmdDict['is_boot_image']
        with open(self.encBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def _encrypteBootableImage( self ):
        curdir = os.getcwd()
        os.chdir(os.path.split(self.imageEncPath)[0])
        process = subprocess.Popen(self.encBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.chdir(curdir)
        commandOutput = process.communicate()[0]
        print commandOutput

    def encrypteImageUsingFlexibleUserKeys( self ):
        userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_UserKeys)
        if userKeyCmdDict['is_boot_image'] == '1':
            self._setDestAppFilenameForBee()
            self._updateEncBatfileContent(userKeyCtrlDict, userKeyCmdDict)
            self._encrypteBootableImage()
            self._genBeeDekFilesAndShow(userKeyCtrlDict, userKeyCmdDict)
        elif userKeyCmdDict['is_boot_image'] == '0':
            pass

    def _createSignedFlBdfile( self, srcFlFilename):
        self._setDestAppInitialBootHeaderInfo(RT10yy_uidef.kBootDevice_RamFlashloader)
        imageStartAddr, imageEntryAddr, imageLength = self._getImageInfo(srcFlFilename)
        if imageStartAddr == None or imageEntryAddr == None:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_invalidFl'][self.languageIndex])
            return False
        if not self.isCertificateGenerated(RT10yy_uidef.kSecureBootType_HabAuth):
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operCertError_notGen1'][self.languageIndex])
            return False
        return self._updateBdfileContent(RT10yy_uidef.kSecureBootType_HabAuth, RT10yy_uidef.kBootDevice_RamFlashloader, imageStartAddr, imageEntryAddr)

    def _updateFlBdBatfileContent( self, srcFlFilename ):
        batContent = "\"" + self.elftosbPath + "\""
        batContent += " -f imx -V -c " + "\"" + self.flBdFilename + "\"" + ' -o ' + "\"" + self.destFlFilename + "\"" + ' ' + "\"" + srcFlFilename + "\""
        with open(self.flBdBatFilename, 'wb') as fileObj:
            fileObj.write(batContent)
            fileObj.close()

    def genSignedFlashloader( self, srcFlFilename ):
        if self._createSignedFlBdfile(srcFlFilename):
            self._updateFlBdBatfileContent(srcFlFilename)
            curdir = os.getcwd()
            os.chdir(os.path.split(self.elftosbPath)[0])
            process = subprocess.Popen(self.flBdBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            os.chdir(curdir)
            commandOutput = process.communicate()[0]
            print commandOutput
            return self.destFlFilename
        else:
            return None

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

    def getDek128ContentFromBinFile( self, filename ):
        if os.path.isfile(filename):
            dek128Content = ''
            with open(filename, 'rb') as fileObj:
                var8Value = fileObj.read(16)
                for i in range(16):
                    temp = str(hex(ord(var8Value[15 - i]) & 0xFF))
                    if len(temp) >= 4 and temp[0:2] == '0x':
                        dek128Content += temp[2:4]
                    else:
                        return None
                fileObj.close()
            return dek128Content
        else:
            return None

    def fillDek128ContentIntoBinFile( self, filename, dekContent ):
        with open(filename, 'wb') as fileObj:
            halfbyteStr = ''
            for i in range(16):
                locEnd = 32 - i * 2
                locStart = locEnd - 2
                halfbyteStr = chr(int(dekContent[locStart:locEnd], 16) & 0xFF)
                fileObj.write(halfbyteStr)
            fileObj.close()

    def _initSbAppBdfileContent( self, sbType=RT10yy_gendef.kSbFileType_All ):
        bdContent = ""
        ############################################################################
        bdContent += "sources {\n"
        if sbType == RT10yy_gendef.kSbFileType_All or sbType == RT10yy_gendef.kSbFileType_Flash:
            bdContent += "    myBinFile = extern (0);\n"
            if self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                bdContent += "    dekFile = extern (1);\n"
        else:
            pass
        bdContent += "}\n"
        ############################################################################
        bdContent += "\nsection (0) {\n"
        ############################################################################
        if sbType == RT10yy_gendef.kSbFileType_All:
            self.sbAppBdContent = bdContent
        elif sbType == RT10yy_gendef.kSbFileType_Flash:
            self.sbAppFlashBdContent = bdContent
        elif sbType == RT10yy_gendef.kSbFileType_Efuse:
            self.sbAppEfuseBdContent = bdContent
        else:
            pass

    def initSbAppBdfilesContent( self ):
        self._initSbAppBdfileContent(RT10yy_gendef.kSbFileType_All)
        self._initSbAppBdfileContent(RT10yy_gendef.kSbFileType_Flash)
        self._initSbAppBdfileContent(RT10yy_gendef.kSbFileType_Efuse)
        self.isEfuseOperationInSbApp = False

    def _doneSbAppBdfileContent( self, sbType=RT10yy_gendef.kSbFileType_All ):
        bdContent = ""
        bdFilename = None
        if sbType == RT10yy_gendef.kSbFileType_All:
            self.sbAppBdContent += "}\n"
            bdContent = self.sbAppBdContent
            bdFilename = self.sbAppBdFilename
        elif sbType == RT10yy_gendef.kSbFileType_Flash:
            self.sbAppFlashBdContent += "}\n"
            bdContent = self.sbAppFlashBdContent
            bdFilename = self.sbAppFlashBdFilename
        elif sbType == RT10yy_gendef.kSbFileType_Efuse:
            self.sbAppEfuseBdContent += "}\n"
            bdContent = self.sbAppEfuseBdContent
            bdFilename = self.sbAppEfuseBdFilename
        else:
            pass
        with open(bdFilename, 'wb') as fileObj:
            fileObj.write(bdContent)
            fileObj.close()

    def _adjustDestSbAppFilenameForBd( self, sbType=RT10yy_gendef.kSbFileType_All ):
        if sbType == RT10yy_gendef.kSbFileType_All:
            srcAppName = os.path.splitext(os.path.split(self.srcAppFilename)[1])[0]
            destSbAppPath, destSbAppFile = os.path.split(self.destSbAppFilename)
            destSbAppName, destSbAppType = os.path.splitext(destSbAppFile)
            destSbAppName = srcAppName
            if self.secureBootType == RT10yy_uidef.kSecureBootType_Development:
                destSbAppName += '_unsigned'
            elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth:
                destSbAppName += '_signed'
            elif self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                destSbAppName += '_signed_hab_encrypted'
            elif self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto:
                if self.isCertEnabledForBee:
                    destSbAppName += '_signed_bee_encrypted'
                else:
                    destSbAppName += '_unsigned_bee_encrypted'
            else:
                pass
            destSbAppName += '_' + self.sbEnableBootDeviceMagic
            if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
                flexspiNorOpt0, flexspiNorOpt1, flexspiNorDeviceModel = uivar.getBootDeviceConfiguration(self.bootDevice)
                if flexspiNorDeviceModel == 'No':
                    destSbAppName += '_' + self.convertLongIntHexText(str(hex(flexspiNorOpt0))) + '_' + self.convertLongIntHexText(str(hex(flexspiNorOpt1)))
                else:
                    destSbAppName += '_' + flexspiNorDeviceModel
            elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
                semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(self.bootDevice)
                destSbAppName += '_' + self.convertLongIntHexText(str(hex(semcNandOpt))) + '_' + self.convertLongIntHexText(str(hex(semcNandFcbOpt)))
            elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
                lpspiNorOpt0, lpspiNorOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
                destSbAppName += '_' + self.convertLongIntHexText(str(hex(lpspiNorOpt0))) + '_' + self.convertLongIntHexText(str(hex(lpspiNorOpt1)))
            elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
                pass
            elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNand:
                pass
            elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
                usdhcSdOpt = uivar.getBootDeviceConfiguration(self.bootDevice)
                destSbAppName += '_' + self.convertLongIntHexText(str(hex(usdhcSdOpt)))
            elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
                usdhcMmcOpt0, usdhcMmcOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
                destSbAppName += '_' + self.convertLongIntHexText(str(hex(usdhcMmcOpt0))) + '_' + self.convertLongIntHexText(str(hex(usdhcMmcOpt1)))
            else:
                pass
            self.destSbAppFilename = os.path.join(destSbAppPath, destSbAppName + destSbAppType)
        elif sbType == RT10yy_gendef.kSbFileType_Flash:
            destSbAppPath, destSbAppFile = os.path.split(self.destSbAppFilename)
            destSbAppName, destSbAppType = os.path.splitext(destSbAppFile)
            self.destSbAppFlashFilename = os.path.join(destSbAppPath, destSbAppName + '_flash' + destSbAppType)
        elif sbType == RT10yy_gendef.kSbFileType_Efuse:
            destSbAppPath, destSbAppFile = os.path.split(self.destSbAppFilename)
            destSbAppName, destSbAppType = os.path.splitext(destSbAppFile)
            self.destSbAppEfuseFilename = os.path.join(destSbAppPath, destSbAppName + '_efuse' + destSbAppType)
        else:
            pass

    def _updateSbAppBdBatfileContent( self, sbType=RT10yy_gendef.kSbFileType_All ):
        destAppFilename = None
        sbAppBdFilename = None
        destSbAppFilename = None
        sbAppBdBatFilename = None
        self._adjustDestSbAppFilenameForBd(sbType)
        if sbType == RT10yy_gendef.kSbFileType_All:
            sbAppBdFilename = self.sbAppBdFilename
            destSbAppFilename = self.destSbAppFilename
            sbAppBdBatFilename = self.sbAppBdBatFilename
        elif sbType == RT10yy_gendef.kSbFileType_Flash:
            sbAppBdFilename = self.sbAppFlashBdFilename
            destSbAppFilename = self.destSbAppFlashFilename
            sbAppBdBatFilename = self.sbAppFlashBdBatFilename
        elif sbType == RT10yy_gendef.kSbFileType_Efuse:
            sbAppBdFilename = self.sbAppEfuseBdFilename
            destSbAppFilename = self.destSbAppEfuseFilename
            sbAppBdBatFilename = self.sbAppEfuseBdBatFilename
        else:
            pass
        if sbType == RT10yy_gendef.kSbFileType_All or sbType == RT10yy_gendef.kSbFileType_Flash:
            if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
                if self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                    destAppFilename = self.destEncAppNoCfgBlockFilename
                else:
                    destAppFilename = self.destAppNoPaddingFilename
            elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand or \
                 self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
                destAppFilename = self.destAppFilename
            elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
                 self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
                destAppFilename = self.destAppNoPaddingFilename
            else:
                pass
            destAppFilename = ' ' + "\"" + destAppFilename + "\""
        else:
            destAppFilename = ''
        sbBatContent = "\"" + self.elftosbPath + "\""
        sbBatContent += " -f kinetis -V -c " + "\"" + sbAppBdFilename + "\"" + ' -o ' + "\"" + destSbAppFilename + "\"" + destAppFilename
        if sbType == RT10yy_gendef.kSbFileType_All or sbType == RT10yy_gendef.kSbFileType_Flash:
            if self.secureBootType == RT10yy_uidef.kSecureBootType_HabCrypto:
                sbBatContent += ' ' + "\"" + self.habDekFilename + "\""
        with open(sbAppBdBatFilename, 'wb') as fileObj:
            fileObj.write(sbBatContent)
            fileObj.close()

    def _parseSbImageGenerationResult( self, output ):
        # elftosb ouput template:
        #Boot Section 0x00000000:
        #  FILL | adr=0x00002000 | len=0x00000004 | ptn=0xc0233007
        #  FILL | adr=0x00002004 | len=0x00000004 | ptn=0x00000000
        #  ENA  | adr=0x00002000 | cnt=0x00000004 | flg=0x0900
        #  ERAS | adr=0x60000000 | cnt=0x00040000 | flg=0x0000
        #  FILL | adr=0x00003000 | len=0x00000004 | ptn=0xf000000f
        #  ENA  | adr=0x00003000 | cnt=0x00000004 | flg=0x0900
        #  LOAD | adr=0x60001000 | len=0x00002b34 | crc=0x0388f030 | flg=0x0000
        info = 'Boot Section'
        if output.find(info) != -1:
            self.printLog('.sb image is generated: ' + self.destSbAppFilename)
            return True
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['srcImgError_failToGenSb'][self.languageIndex])
            return False

    def _genSbAppImage( self, sbType=RT10yy_gendef.kSbFileType_All ):
        self._doneSbAppBdfileContent(sbType)
        self._updateSbAppBdBatfileContent(sbType)
        # We have to change system dir to the path of elftosb.exe, or elftosb.exe may not be ran successfully
        curdir = os.getcwd()
        os.chdir(os.path.split(self.elftosbPath)[0])
        sbAppBdBatFilename = None
        if sbType == RT10yy_gendef.kSbFileType_All:
            sbAppBdBatFilename = self.sbAppBdBatFilename
        elif sbType == RT10yy_gendef.kSbFileType_Flash:
            sbAppBdBatFilename = self.sbAppFlashBdBatFilename
        elif sbType == RT10yy_gendef.kSbFileType_Efuse:
            sbAppBdBatFilename = self.sbAppEfuseBdBatFilename
        else:
            pass
        process = subprocess.Popen(sbAppBdBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.chdir(curdir)
        commandOutput = process.communicate()[0]
        print commandOutput
        if self._parseSbImageGenerationResult(commandOutput):
            return True
        else:
            return False

    def genSbAppImages( self ):
        if not self._genSbAppImage(RT10yy_gendef.kSbFileType_All):
            return False
        if self.isEfuseOperationInSbApp:
            if not self._genSbAppImage(RT10yy_gendef.kSbFileType_Flash):
                return False
            if not self._genSbAppImage(RT10yy_gendef.kSbFileType_Efuse):
                return False
        return True

    def initSbEfuseBdfileContent( self ):
        self.sbUserEfuseBdContent = ""
        ############################################################################
        self.sbUserEfuseBdContent += "sources {\n"
        self.sbUserEfuseBdContent += "}\n"
        ############################################################################
        self.sbUserEfuseBdContent += "\nsection (0) {\n"
        ############################################################################

    def _doneSbEfuseBdfileContent( self ):
        ############################################################################
        self.sbUserEfuseBdContent += "}\n"
        ############################################################################
        with open(self.sbUserEfuseBdFilename, 'wb') as fileObj:
            fileObj.write(self.sbUserEfuseBdContent)
            fileObj.close()

    def _updateSbEfuseBdBatfileContent( self ):
        sbBatContent = "\"" + self.elftosbPath + "\""
        sbBatContent += " -f kinetis -V -c " + "\"" + self.sbUserEfuseBdFilename + "\"" + ' -o ' + "\"" + self.destSbUserEfuseFilename + "\""
        with open(self.sbUserEfuseBdBatFilename, 'wb') as fileObj:
            fileObj.write(sbBatContent)
            fileObj.close()

    def genSbEfuseImage( self ):
        self._doneSbEfuseBdfileContent()
        self._updateSbEfuseBdBatfileContent()
        # We have to change system dir to the path of elftosb.exe, or elftosb.exe may not be ran successfully
        curdir = os.getcwd()
        os.chdir(os.path.split(self.elftosbPath)[0])
        process = subprocess.Popen(self.sbUserEfuseBdBatFilename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.chdir(curdir)
        commandOutput = process.communicate()[0]
        print commandOutput
        if self._parseSbImageGenerationResult(commandOutput):
            return True
        else:
            return False
