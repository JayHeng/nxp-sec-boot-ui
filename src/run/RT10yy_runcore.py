#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import math
import RT10yy_rundef
import rundef
import boot
sys.path.append(os.path.abspath(".."))
from gen import RT10yy_gencore
from gen import RT10yy_gendef
from fuse import RT10yy_fusedef
from ui import RT10yy_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from mem import RT10yy_memdef
from boot import bltest
from boot import target
from utils import misc

def RT10yy_createTarget(device, exeBinRoot):
    # Build path to target directory and config file.
    cpu = "MIMXRT1052"
    if device == uidef.kMcuDevice_iMXRT1015:
        cpu = "MIMXRT1015"
    elif device == uidef.kMcuDevice_iMXRT102x:
        cpu = "MIMXRT1021"
    elif device == uidef.kMcuDevice_iMXRT105x:
        cpu = "MIMXRT1052"
    elif device == uidef.kMcuDevice_iMXRT106x:
        cpu = "MIMXRT1062"
    elif device == uidef.kMcuDevice_iMXRT1064:
        cpu = "MIMXRT1064"
    else:
        pass
    targetBaseDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets', cpu)

    # Check for existing target directory.
    if not os.path.isdir(targetBaseDir):
        targetBaseDir = os.path.join(os.path.dirname(exeBinRoot), 'src', 'targets', cpu)
        if not os.path.isdir(targetBaseDir):
            raise ValueError("Missing target directory at path %s" % targetBaseDir)

    targetConfigFile = os.path.join(targetBaseDir, 'bltargetconfig.py')

    # Check for config file existence.
    if not os.path.isfile(targetConfigFile):
        raise RuntimeError("Missing target config file at path %s" % targetConfigFile)

    # Build locals dict by copying our locals and adjusting file path and name.
    targetConfig = locals().copy()
    targetConfig['__file__'] = targetConfigFile
    targetConfig['__name__'] = 'bltargetconfig'

    # Execute the target config script.
    execfile(targetConfigFile, globals(), targetConfig)

    # Create the target object.
    tgt = target.Target(**targetConfig)

    return tgt, targetBaseDir

##
# @brief
class secBootRT10yyRun(RT10yy_gencore.secBootRT10yyGen):

    def __init__(self, parent):
        RT10yy_gencore.secBootRT10yyGen.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.RT10yy_initRun()

    def RT10yy_initRun( self ):
        self.blhost = None
        self.sdphost = None
        self.tgt = None
        self.cpuDir = None
        self.sdphostVectorsDir = os.path.join(self.exeTopRoot, 'tools', 'sdphost', 'win', 'vectors')
        self.blhostVectorsDir = os.path.join(self.exeTopRoot, 'tools', 'blhost', 'win', 'vectors')

        self.RT10yy_isDeviceEnabledToOperate = True
        self.bootDeviceMemId = None
        self.bootDeviceMemBase = None
        self.semcNandImageCopies = None
        self.semcNandBlockSize = None
        self.isFlexspiNorErasedForImage = False

        self.mcuDeviceHabStatus = None
        self.mcuDeviceBtFuseSel = None
        self.mcuDeviceBeeKey0Sel = None
        self.mcuDeviceBeeKey1Sel = None

        self.comMemWriteUnit = 0x1
        self.comMemEraseUnit = 0x1
        self.comMemReadUnit = 0x1

        self.sbLastSharedFuseBootCfg1 = RT10yy_fusedef.kEfuseValue_Invalid

        self.RT10yy_createMcuTarget()

    def RT10yy_createMcuTarget( self ):
        self.tgt, self.cpuDir = RT10yy_createTarget(self.mcuDevice, self.exeBinRoot)

    def RT10yy_getUsbid( self ):
        self.RT10yy_createMcuTarget()
        return [self.tgt.romUsbVid, self.tgt.romUsbPid, self.tgt.flashloaderUsbVid, self.tgt.flashloaderUsbPid]

    def RT10yy_connectToDevice( self , connectStage):
        if connectStage == uidef.kConnectStage_Rom:
            # Create the target object.
            self.RT10yy_createMcuTarget()
            if self.isUartPortSelected:
                sdpPeripheral = 'sdp_uart'
                uartComPort = self.uartComPort
                uartBaudrate = int(self.uartBaudrate)
                usbVid = ''
                usbPid = ''
            elif self.isUsbhidPortSelected:
                sdpPeripheral = 'sdp_usb'
                uartComPort = ''
                uartBaudrate = ''
                usbVid = self.tgt.romUsbVid
                usbPid = self.tgt.romUsbPid
            else:
                pass
            self.sdphost = bltest.createBootloader(self.tgt,
                                                   self.sdphostVectorsDir,
                                                   sdpPeripheral,
                                                   uartBaudrate, uartComPort,
                                                   usbVid, usbPid)
        elif connectStage == uidef.kConnectStage_Flashloader:
            if self.isUartPortSelected:
                blPeripheral = 'uart'
                uartComPort = self.uartComPort
                uartBaudrate = int(self.uartBaudrate)
                usbVid = ''
                usbPid = ''
            elif self.isUsbhidPortSelected:
                blPeripheral = 'usb'
                uartComPort = ''
                uartBaudrate = ''
                usbVid = self.tgt.flashloaderUsbVid
                usbPid = self.tgt.flashloaderUsbPid
            else:
                pass
            self.blhost = bltest.createBootloader(self.tgt,
                                                  self.blhostVectorsDir,
                                                  blPeripheral,
                                                  uartBaudrate, uartComPort,
                                                  usbVid, usbPid,
                                                  True)
        elif connectStage == uidef.kConnectStage_Reset:
            self.tgt = None
        else:
            pass

    def RT10yy_pingRom( self ):
        status, results, cmdStr = self.sdphost.errorStatus()
        self.printLog(cmdStr)
        return (status == boot.status.kSDP_Status_HabEnabled or status == boot.status.kSDP_Status_HabDisabled)

    def _getDeviceRegisterBySdphost( self, regAddr, regName, needToShow=True):
        filename = 'readReg.dat'
        filepath = os.path.join(self.sdphostVectorsDir, filename)
        status, results, cmdStr = self.sdphost.readRegister(regAddr, 32, 4, filename)
        self.printLog(cmdStr)
        if (status == boot.status.kSDP_Status_HabEnabled or status == boot.status.kSDP_Status_HabDisabled):
            regVal = self.getVal32FromBinFile(filepath)
            if needToShow:
                self.printDeviceStatus(regName + " = " + self.convertLongIntHexText(str(hex(regVal))))
            return regVal
        else:
            if needToShow:
                self.printDeviceStatus(regName + " = --------")
            return None
        try:
            os.remove(filepath)
        except:
            pass

    def _readMcuDeviceRegisterUuid( self ):
        self._getDeviceRegisterBySdphost( RT10yy_rundef.kRegisterAddr_UUID1, 'OCOTP->B0W1 UUID[31:00]')
        self._getDeviceRegisterBySdphost( RT10yy_rundef.kRegisterAddr_UUID2, 'OCOTP->B0W2 UUID[63:32]')

    def _readMcuDeviceRegisterSrcSmbr( self ):
        self._getDeviceRegisterBySdphost( RT10yy_rundef.kRegisterAddr_SRC_SBMR1, 'SRC->SMBR1')
        self._getDeviceRegisterBySdphost( RT10yy_rundef.kRegisterAddr_SRC_SBMR2, 'SRC->SMBR2')

    def RT10yy_getMcuDeviceInfoViaRom( self ):
        self.printDeviceStatus("--------MCU device Register----------")
        self._readMcuDeviceRegisterUuid()
        self._readMcuDeviceRegisterSrcSmbr()

    def getMcuDeviceHabStatus( self ):
        secConfig = self._getDeviceRegisterBySdphost( RT10yy_rundef.kRegisterAddr_SRC_SBMR2, '', False)
        if secConfig != None:
            self.mcuDeviceHabStatus = ((secConfig & RT10yy_rundef.kRegisterMask_SecConfig) >> RT10yy_rundef.kRegisterShift_SecConfig)
            if self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_FAB:
                self.printDeviceStatus('HAB status = FAB')
            elif self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Open:
                self.printDeviceStatus('HAB status = Open')
            elif self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Closed0 or self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Closed1:
                self.printDeviceStatus('HAB status = Closed')
            else:
                pass

    def jumpToFlashloader( self ):
        flashloaderBinFile = None
        if self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Closed0 or self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Closed1:
            flashloaderSrecFile = os.path.join(self.cpuDir, 'flashloader.srec')
            flashloaderBinFile = self.genSignedFlashloader(flashloaderSrecFile)
            if flashloaderBinFile == None:
                return False
        elif self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_FAB or self.mcuDeviceHabStatus == RT10yy_fusedef.kHabStatus_Open:
            flashloaderBinFile = os.path.join(self.cpuDir, 'ivt_flashloader.bin')
        else:
            pass
        status, results, cmdStr = self.sdphost.writeFile(self.tgt.flashloaderLoadAddr, flashloaderBinFile)
        self.printLog(cmdStr)
        if status != boot.status.kSDP_Status_HabEnabled and status != boot.status.kSDP_Status_HabDisabled:
            return False
        status, results, cmdStr = self.sdphost.jumpAddress(self.tgt.flashloaderJumpAddr)
        self.printLog(cmdStr)
        if status != boot.status.kSDP_Status_HabEnabled and status != boot.status.kSDP_Status_HabDisabled:
            return False
        return True

    def pingFlashloader( self ):
        status, results, cmdStr = self.blhost.getProperty(boot.properties.kPropertyTag_CurrentVersion)
        self.printLog(cmdStr)
        return (status == boot.status.kStatus_Success)

    def readMcuDeviceFuseByBlhost( self, fuseIndex, fuseName, needToShow=True):
        if not self.RT10yy_isDeviceEnabledToOperate and self.isSbFileEnabledToGen:
            return RT10yy_fusedef.kEfuseValue_Blank
        status, results, cmdStr = self.blhost.efuseReadOnce(fuseIndex)
        self.printLog(cmdStr)
        if (status == boot.status.kStatus_Success):
            if needToShow:
                self.printDeviceStatus(fuseName + " = " + self.convertLongIntHexText(str(hex(results[1]))))
            if self.isSbFileEnabledToGen:
                if fuseIndex == RT10yy_fusedef.kEfuseIndex_BOOT_CFG1 and self.sbLastSharedFuseBootCfg1 == RT10yy_fusedef.kEfuseValue_Invalid:
                    self.sbLastSharedFuseBootCfg1 = results[1]
            return results[1]
        else:
            if needToShow:
                self.printDeviceStatus(fuseName + " = --------")
            return None

    def _readMcuDeviceFuseTester( self ):
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_TESTER0, '(0x410) TESTER0')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_TESTER1, '(0x420) TESTER1')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_TESTER2, '(0x430) TESTER2')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_TESTER3, '(0x440) TESTER3')

    def _readMcuDeviceFuseBootCfg( self ):
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_BOOT_CFG0, '(0x450) BOOT_CFG0')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_BOOT_CFG1, '(0x460) BOOT_CFG1')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_BOOT_CFG2, '(0x470) BOOT_CFG2')

    def _genOtpmkDekFile( self, otpmk4, otpmk5, otpmk6, otpmk7 ):
        try:
            os.remove(self.otpmkDekFilename)
        except:
            pass
        self.fillVal32IntoBinFile(self.otpmkDekFilename, otpmk4)
        self.fillVal32IntoBinFile(self.otpmkDekFilename, otpmk5)
        self.fillVal32IntoBinFile(self.otpmkDekFilename, otpmk6)
        self.fillVal32IntoBinFile(self.otpmkDekFilename, otpmk7)

    def _readMcuDeviceFuseOtpmkDek( self ):
        otpmk4 = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_OTPMK4, '', False)
        otpmk5 = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_OTPMK5, '', False)
        otpmk6 = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_OTPMK6, '', False)
        otpmk7 = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_OTPMK7, '', False)
        if otpmk4 != None and otpmk5 != None and otpmk6 != None and otpmk7 != None:
            self._genOtpmkDekFile(otpmk4, otpmk5, otpmk6, otpmk7)

    def _readMcuDeviceFuseSrk( self ):
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK0, '(0x580) SRK0')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK1, '(0x590) SRK1')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK2, '(0x5A0) SRK2')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK3, '(0x5B0) SRK3')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK4, '(0x5C0) SRK4')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK5, '(0x5D0) SRK5')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK6, '(0x5E0) SRK6')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK7, '(0x5F0) SRK7')

    def _readMcuDeviceFuseSwGp2( self ):
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_0, '(0x690) SW_GP2_0')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_1, '(0x6A0) SW_GP2_1')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_2, '(0x6B0) SW_GP2_2')
        self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_3, '(0x6C0) SW_GP2_3')

    def getMcuDeviceInfoViaFlashloader( self ):
        self.printDeviceStatus("--------MCU device eFusemap--------")
        #self._readMcuDeviceFuseTester()
        self._readMcuDeviceFuseBootCfg()
        #self._readMcuDeviceFuseOtpmkDek()
        #self._readMcuDeviceFuseSrk()
        #self._readMcuDeviceFuseSwGp2()

    def getMcuDeviceBtFuseSel( self ):
        btFuseSel = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_BtFuseSel, '', False)
        if btFuseSel != None:
            self.mcuDeviceBtFuseSel = ((btFuseSel & RT10yy_fusedef.kEfuseMask_BtFuseSel) >> RT10yy_fusedef.kEfuseShift_BtFuseSel)
            if self.mcuDeviceBtFuseSel == 0:
                self.printDeviceStatus('BT_FUSE_SEL = 1\'b0')
                self.printDeviceStatus('  When BMOD[1:0] = 2\'b00 (Boot From Fuses), It means there is no application in boot device, MCU will enter serial downloader mode directly')
                self.printDeviceStatus('  When BMOD[1:0] = 2\'b10 (Internal Boot), It means MCU will boot application according to both BOOT_CFGx pins and Fuse BOOT_CFGx')
            elif self.mcuDeviceBtFuseSel == 1:
                self.printDeviceStatus('BT_FUSE_SEL = 1\'b1')
                self.printDeviceStatus('  When BMOD[1:0] = 2\'b00 (Boot From Fuses), It means there is application in boot device, MCU will boot application according to Fuse BOOT_CFGx')
                self.printDeviceStatus('  When BMOD[1:0] = 2\'b10 (Internal Boot), It means MCU will boot application according to Fuse BOOT_CFGx only')
            else:
                pass

    def _RT10yy_prepareForBootDeviceOperation ( self ):
        if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_FlexspiNor
            self.bootDeviceMemBase = self.tgt.flexspiNorMemBase
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNand:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_FlexspiNand
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_FlexspiNand
        elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNor:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_SemcNor
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_SemcNor
        elif self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_SemcNand
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_SemcNand
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_UsdhcSd
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_UsdhcSd
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_UsdhcMmc
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_UsdhcMmc
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            self.bootDeviceMemId = rundef.kBootDeviceMemId_SpiNor
            self.bootDeviceMemBase = RT10yy_rundef.kBootDeviceMemBase_LpspiNor
        else:
            pass

    def _getSemcNandDeviceInfo ( self ):
        filename = 'semcNandFcb.dat'
        filepath = os.path.join(self.blhostVectorsDir, filename)
        status, results, cmdStr = self.blhost.readMemory(self.bootDeviceMemBase + RT10yy_rundef.kSemcNandFcbInfo_StartAddr, RT10yy_rundef.kSemcNandFcbInfo_Length, filename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        fingerprint = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_Fingerprint)
        semcTag = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_SemcTag)
        if fingerprint == RT10yy_rundef.kSemcNandFcbTag_Fingerprint and semcTag == RT10yy_rundef.kSemcNandFcbTag_Semc:
            firmwareCopies = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_FirmwareCopies)
            pageByteSize = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_PageByteSize)
            pagesInBlock = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_PagesInBlock)
            blocksInPlane = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_BlocksInPlane)
            planesInDevice = self.getVal32FromBinFile(filepath, RT10yy_rundef.kSemcNandFcbOffset_PlanesInDevice)
            self.printDeviceStatus("Page Size         = " + self.showAsOptimalMemoryUnit(pageByteSize))
            self.printDeviceStatus("Pages In Block    = " + str(pagesInBlock))
            self.printDeviceStatus("Blocks In Plane   = " + str(blocksInPlane))
            self.printDeviceStatus("Planes In Device  = " + str(planesInDevice))
            self.semcNandImageCopies = firmwareCopies
            self.semcNandBlockSize = pageByteSize * pagesInBlock
            self.comMemWriteUnit = pageByteSize
            self.comMemEraseUnit = pageByteSize * pagesInBlock
            self.comMemReadUnit = pageByteSize
        else:
            self.printDeviceStatus("Page Size         = --------")
            self.printDeviceStatus("Pages In Block    = --------")
            self.printDeviceStatus("Blocks In Plane   = --------")
            self.printDeviceStatus("Planes In Device  = --------")
            return False
        try:
            os.remove(filepath)
        except:
            pass
        return True

    def _getFlexspiNorDeviceInfo ( self ):
        if not self.RT10yy_isDeviceEnabledToOperate and self.isSbFileEnabledToGen:
            return True
        filename = 'flexspiNorCfg.dat'
        filepath = os.path.join(self.blhostVectorsDir, filename)
        status, results, cmdStr = self.blhost.readMemory(self.bootDeviceMemBase + rundef.kFlexspiNorCfgInfo_StartAddr, rundef.kFlexspiNorCfgInfo_Length, filename, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if status != boot.status.kStatus_Success:
            return False
        flexspiTag = self.getVal32FromBinFile(filepath, rundef.kFlexspiNorCfgOffset_FlexspiTag)
        if flexspiTag == rundef.kFlexspiNorCfgTag_Flexspi:
            pageByteSize = self.getVal32FromBinFile(filepath, rundef.kFlexspiNorCfgOffset_PageByteSize)
            sectorByteSize = self.getVal32FromBinFile(filepath, rundef.kFlexspiNorCfgOffset_SectorByteSize)
            blockByteSize = self.getVal32FromBinFile(filepath, rundef.kFlexspiNorCfgOffset_BlockByteSize)
            self.printDeviceStatus("Page Size   = " + self.showAsOptimalMemoryUnit(pageByteSize))
            self.printDeviceStatus("Sector Size = " + self.showAsOptimalMemoryUnit(sectorByteSize))
            self.printDeviceStatus("Block Size  = " + self.showAsOptimalMemoryUnit(blockByteSize))
            self.comMemWriteUnit = pageByteSize
            self.comMemEraseUnit = sectorByteSize
            self.comMemReadUnit = pageByteSize
        else:
            self.printDeviceStatus("Page Size   = --------")
            self.printDeviceStatus("Sector Size = --------")
            self.printDeviceStatus("Block Size  = --------")
            return False
        try:
            os.remove(filepath)
        except:
            pass
        return True

    def _getLpspiNorDeviceInfo ( self ):
        pageByteSize = 0
        sectorByteSize = 0
        totalByteSize = 0
        lpspiNorOpt0, lpspiNorOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
        val = (lpspiNorOpt0 & 0x0000000F) >> 0
        if val <= 2:
            pageByteSize = int(math.pow(2, val + 8))
        else:
            pageByteSize = int(math.pow(2, val + 2))
        val = (lpspiNorOpt0 & 0x000000F0) >> 4
        if val <= 1:
            sectorByteSize = int(math.pow(2, val + 12))
        else:
            sectorByteSize = int(math.pow(2, val + 13))
        val = (lpspiNorOpt0 & 0x00000F00) >> 8
        if val <= 11:
            totalByteSize = int(math.pow(2, val + 19))
        else:
            totalByteSize = int(math.pow(2, val + 3))
        self.printDeviceStatus("Page Size   = " + self.showAsOptimalMemoryUnit(pageByteSize))
        self.printDeviceStatus("Sector Size = " + self.showAsOptimalMemoryUnit(sectorByteSize))
        self.printDeviceStatus("Total Size  = " + self.showAsOptimalMemoryUnit(totalByteSize))
        self.comMemWriteUnit = pageByteSize
        self.comMemEraseUnit = sectorByteSize
        self.comMemReadUnit = pageByteSize
        return True

    def _getUsdhcSdMmcDeviceInfo ( self ):
        status, results, cmdStr = self.blhost.getProperty(boot.properties.kPropertyTag_ExternalMemoryAttribles, self.bootDeviceMemId)
        self.printLog(cmdStr)
        if (status == boot.status.kStatus_Success):
            #typedef struct
            #{
            #    uint32_t availableAttributesFlag; //!< Available Atrributes, bit map
            #    uint32_t startAddress;            //!< start Address of external memory
            #    uint32_t flashSizeInKB;           //!< flash size of external memory
            #    uint32_t pageSize;                //!< page size of external memory
            #    uint32_t sectorSize;              //!< sector size of external memory
            #    uint32_t blockSize;               //!< block size of external memory
            #} external_memory_property_store_t;
            blockByteSize = results[5]
            totalSizeKB = results[2]
            self.printDeviceStatus("Block Size  = " + self.showAsOptimalMemoryUnit(blockByteSize))
            strTotalSizeGB = ("%.2f" % (totalSizeKB / 1024.0 / 1024))
            self.printDeviceStatus("Total Size  = " + self.convertLongIntHexText(strTotalSizeGB)) + ' GB'
            self.comMemWriteUnit = blockByteSize
            self.comMemEraseUnit = blockByteSize
            self.comMemReadUnit = blockByteSize
        else:
            self.printDeviceStatus("Block Size  = --------")
            self.printDeviceStatus("Total Size  = --------")
            return False
        return True

    def getBootDeviceInfoViaFlashloader ( self ):
        if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            self.printDeviceStatus("--------SEMC NAND memory----------")
            self._getSemcNandDeviceInfo()
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            self.printDeviceStatus("--------FlexSPI NOR memory--------")
            if not self._getFlexspiNorDeviceInfo():
                if not self._eraseFlexspiNorForConfigBlockLoading():
                    return False
                if not self._programFlexspiNorConfigBlock():
                    return False
                self._getFlexspiNorDeviceInfo()
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            self.printDeviceStatus("--------LPSPI NOR/EEPROM memory---")
            self._getLpspiNorDeviceInfo()
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
            self.printDeviceStatus("--------uSDHC SD Card info--------")
            self._getUsdhcSdMmcDeviceInfo()
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            self.printDeviceStatus("--------uSDHC (e)MMC Card info----")
            self._getUsdhcSdMmcDeviceInfo()
        else:
            pass

    def _addFlashActionIntoSbAppBdContent(self, actionContent ):
        self.sbAppBdContent += actionContent
        self.sbAppFlashBdContent += actionContent

    def _eraseFlexspiNorForConfigBlockLoading( self ):
        status = boot.status.kStatus_Success
        if self.RT10yy_isDeviceEnabledToOperate:
            status, results, cmdStr = self.blhost.flashEraseRegion(self.tgt.flexspiNorMemBase, rundef.kFlexspiNorCfgInfo_Length, rundef.kBootDeviceMemId_FlexspiNor)
            self.printLog(cmdStr)
        if self.isSbFileEnabledToGen:
            self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(self.tgt.flexspiNorMemBase))) + ".." + self.convertLongIntHexText(str(hex(self.tgt.flexspiNorMemBase + rundef.kFlexspiNorCfgInfo_Length))) + ";\n")
        return (status == boot.status.kStatus_Success)

    def _programFlexspiNorConfigBlock ( self ):
        #if not self.tgt.isSipFlexspiNorDevice:
        if True:
            status = boot.status.kStatus_Success
            # 0xf000000f is the tag to notify Flashloader to program FlexSPI NOR config block to the start of device
            if self.RT10yy_isDeviceEnabledToOperate:
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadCfgBlock, 0x4, rundef.kFlexspiNorCfgInfo_Notify)
                self.printLog(cmdStr)
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(rundef.kFlexspiNorCfgInfo_Notify))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadCfgBlock))) + ";\n")
            if status != boot.status.kStatus_Success:
                return False
            if self.RT10yy_isDeviceEnabledToOperate:
                status, results, cmdStr = self.blhost.configureMemory(self.bootDeviceMemId, RT10yy_rundef.kRamFreeSpaceStart_LoadCfgBlock)
                self.printLog(cmdStr)
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    enable " + self.sbEnableBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadCfgBlock))) + ";\n")
            if self.isSbFileEnabledToGen:
                return True
            else:
                return (status == boot.status.kStatus_Success)
        else:
            status, results, cmdStr = self.blhost.writeMemory(self.bootDeviceMemBase, os.path.join(self.cpuDir, 'sip_flash_config.bin'), self.bootDeviceMemId)
            self.printLog(cmdStr)
            return (status == boot.status.kStatus_Success)

    def RT10yy_configureBootDevice ( self ):
        self._RT10yy_prepareForBootDeviceOperation()
        configOptList = []
        if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(self.bootDevice)
            configOptList.extend([semcNandOpt, semcNandFcbOpt])
            for i in range(len(semcNandImageInfoList)):
                if semcNandImageInfoList[i] != None:
                    configOptList.extend([semcNandImageInfoList[i]])
                else:
                    break
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            flexspiNorOpt0, flexspiNorOpt1, flexspiNorDeviceModel = uivar.getBootDeviceConfiguration(uidef.kBootDevice_XspiNor)
            configOptList.extend([flexspiNorOpt0, flexspiNorOpt1])
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            lpspiNorOpt0, lpspiNorOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
            configOptList.extend([lpspiNorOpt0, lpspiNorOpt1])
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
            usdhcSdOpt = uivar.getBootDeviceConfiguration(self.bootDevice)
            configOptList.extend([usdhcSdOpt])
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            usdhcMmcOpt0, usdhcMmcOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
            configOptList.extend([usdhcMmcOpt0, usdhcMmcOpt1])
        else:
            pass
        status = boot.status.kStatus_Success
        for i in range(len(configOptList)):
            if self.RT10yy_isDeviceEnabledToOperate:
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadCommOpt + 4 * i, 0x4, configOptList[i])
                self.printLog(cmdStr)
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(configOptList[i]))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadCommOpt + 4 * i))) + ";\n")
            if status != boot.status.kStatus_Success:
                return False
        if self.RT10yy_isDeviceEnabledToOperate:
            status, results, cmdStr = self.blhost.configureMemory(self.bootDeviceMemId, RT10yy_rundef.kRamFreeSpaceStart_LoadCommOpt)
            self.printLog(cmdStr)
        if self.isSbFileEnabledToGen:
            self._addFlashActionIntoSbAppBdContent("    enable " + self.sbEnableBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadCommOpt))) + ";\n")
        if status != boot.status.kStatus_Success:
            return False
        return True

    def _showOtpmkDek( self ):
        if os.path.isfile(self.otpmkDekFilename):
            self.clearOtpmkDekData()
            keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
            for i in range(keyWords):
                val32 = self.getVal32FromBinFile(self.otpmkDekFilename, (i * 4))
                self.printOtpmkDekData(self.getFormattedHexValue(val32))

    def _eraseFlexspiNorForImageLoading( self ):
        imageLen = os.path.getsize(self.destAppFilename)
        memEraseLen = misc.align_up(imageLen, self.comMemEraseUnit)
        if self.isSbFileEnabledToGen:
            self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(self.tgt.flexspiNorMemBase))) + ".." + self.convertLongIntHexText(str(hex(self.tgt.flexspiNorMemBase + memEraseLen))) + ";\n")
        else:
            status, results, cmdStr = self.blhost.flashEraseRegion(self.tgt.flexspiNorMemBase, memEraseLen, rundef.kBootDeviceMemId_FlexspiNor)
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                return False
        self.isFlexspiNorErasedForImage = True
        return True

    def prepareForFixedOtpmkEncryption( self ):
        self._RT10yy_prepareForBootDeviceOperation()
        #self._showOtpmkDek()
        if not self._eraseFlexspiNorForImageLoading():
            return False
        otpmkKeyOpt, otpmkEncryptedRegionStartListList, otpmkEncryptedRegionLengthList = uivar.getAdvancedSettings(RT10yy_uidef.kAdvancedSettings_OtpmkKey)
        # Prepare PRDB options
        #---------------------------------------------------------------------------
        # 0xe0120000 is an option for PRDB contruction and image encryption
        # bit[31:28] tag, fixed to 0x0E
        # bit[27:24] Key source, fixed to 0 for A0 silicon
        # bit[23:20] AES mode: 1 - CTR mode
        # bit[19:16] Encrypted region count
        # bit[15:00] reserved in A0
        #---------------------------------------------------------------------------
        encryptedRegionCnt = (otpmkKeyOpt & 0x000F0000) >> 16
        if encryptedRegionCnt == 0:
            otpmkKeyOpt = (otpmkKeyOpt & 0xFFF0FFFF) | (0x1 << 16)
            encryptedRegionCnt = 1
            otpmkEncryptedRegionStartListList[0] = self.tgt.flexspiNorMemBase + RT10yy_gendef.kIvtOffset_NOR
            otpmkEncryptedRegionLengthList[0] = misc.align_up(os.path.getsize(self.destAppFilename), RT10yy_gendef.kSecFacRegionAlignedUnit) - RT10yy_gendef.kIvtOffset_NOR
        else:
            pass
        if self.isSbFileEnabledToGen:
            self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(otpmkKeyOpt))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt))) + ";\n")
        else:
            status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt, 0x4, otpmkKeyOpt)
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                return False
        for i in range(encryptedRegionCnt):
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(otpmkEncryptedRegionStartListList[i]))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt + i * 8 + 4))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(otpmkEncryptedRegionLengthList[i]))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt + i * 8 + 8))) + ";\n")
            else:
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt + i * 8 + 4, 0x4, otpmkEncryptedRegionStartListList[i])
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt + i * 8 + 8, 0x4, otpmkEncryptedRegionLengthList[i])
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
        if self.isSbFileEnabledToGen:
            self._addFlashActionIntoSbAppBdContent("    enable " + self.sbEnableBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt))) + ";\n")
        else:
            status, results, cmdStr = self.blhost.configureMemory(self.bootDeviceMemId, RT10yy_rundef.kRamFreeSpaceStart_LoadPrdbOpt)
            self.printLog(cmdStr)
            if status != boot.status.kStatus_Success:
                return False
        if not self._programFlexspiNorConfigBlock():
            return False
        return True

    def _isDeviceFuseSrkRegionReadyForBurn( self, srkFuseFilename ):
        isReady = True
        isBlank = True
        keyWords = RT10yy_gendef.kSecKeyLengthInBits_SRK / 32
        for i in range(keyWords):
            srk = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK0 + i, '(' + str(hex(0x580 + i * 0x10)) + ') ' + 'SRK' + str(i), False)
            if srk == None:
                isReady = False
                break
            elif srk != 0:
                isBlank = False
                val32 = self.getVal32FromBinFile(srkFuseFilename, (i * 4))
                if srk != val32:
                    isReady = False
                    break
        return isReady, isBlank

    def burnMcuDeviceFuseByBlhost( self, fuseIndex, fuseValue, actionFrom=RT10yy_rundef.kActionFrom_AllInOne):
        status = boot.status.kStatus_Success
        if self.isSbFileEnabledToGen:
            if actionFrom == RT10yy_rundef.kActionFrom_AllInOne:
                if fuseIndex == RT10yy_fusedef.kEfuseIndex_BOOT_CFG1:
                    fuseValue = fuseValue | self.sbLastSharedFuseBootCfg1
                    self.sbLastSharedFuseBootCfg1 = fuseValue
                sbAppBdContent = "    load fuse 0x" + self.getFormattedFuseValue(fuseValue) + " > " + self.convertLongIntHexText(str(hex(fuseIndex))) + ";\n"
                self.sbAppBdContent += sbAppBdContent
                self.sbAppEfuseBdContent += sbAppBdContent
                self.isEfuseOperationInSbApp = True
            elif actionFrom == RT10yy_rundef.kActionFrom_BurnFuse:
                self.sbUserEfuseBdContent += "    load fuse 0x" + self.getFormattedFuseValue(fuseValue) + " > " + self.convertLongIntHexText(str(hex(fuseIndex))) + ";\n"
            else:
                pass
        else:
            status, results, cmdStr = self.blhost.efuseProgramOnce(fuseIndex, self.getFormattedFuseValue(fuseValue))
            self.printLog(cmdStr)
        return (status == boot.status.kStatus_Success)

    def burnSrkData ( self ):
        if os.path.isfile(self.srkFuseFilename):
            isReady, isBlank = self._isDeviceFuseSrkRegionReadyForBurn(self.srkFuseFilename)
            if isReady:
                if isBlank:
                    keyWords = RT10yy_gendef.kSecKeyLengthInBits_SRK / 32
                    for i in range(keyWords):
                        val32 = self.getVal32FromBinFile(self.srkFuseFilename, (i * 4))
                        burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SRK0 + i, val32)
                        if not burnResult:
                            self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnSrk'][self.languageIndex])
                            return False
                return True
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_srkHasBeenBurned'][self.languageIndex])
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_srkNotGen'][self.languageIndex])
        return False

    def _isDeviceFuseSwGp2RegionReadyForBurn( self, swgp2DekFilename ):
        isReady = True
        isBlank = True
        keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
        for i in range(keyWords):
            dek = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_0 + i, '(' + str(hex(0x690 + i * 0x10)) + ') ' + 'SW_GP2_' + str(i), False)
            if dek == None:
                isReady = False
                break
            elif dek != 0:
                isBlank = False
                val32 = self.getVal32FromBinFile(swgp2DekFilename, (i * 4))
                if dek != val32:
                    isReady = False
                    break
        return isReady, isBlank

    def _isDeviceFuseGp4RegionReadyForBurn( self, gp4DekFilename ):
        isReady = True
        isBlank = True
        keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
        for i in range(keyWords):
            dek = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_GP4_0 + i, '(' + str(hex(0x8C0 + i * 0x10)) + ') ' + 'GP4_' + str(i), False)
            if dek == None:
                isReady = False
                break
            elif dek != 0:
                isBlank = False
                val32 = self.getVal32FromBinFile(gp4DekFilename, (i * 4))
                if dek != val32:
                    isReady = False
                    break
        return isReady, isBlank

    def _lockFuseSwGp2( self ):
        lock = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, '', False)
        if lock != None:
            lock = (lock | (RT10yy_fusedef.kEfuseMask_WLockSwGp2 | RT10yy_fusedef.kEfuseMask_RLockSwGp2)) & (~RT10yy_fusedef.kEfuseMask_LockHigh)
            burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, lock)
            if not burnResult:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnSwgp2Lock'][self.languageIndex])
                return False
        return True

    def _lockFuseGp4( self ):
        lock = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, '', False)
        if lock != None:
            lock = (lock | (RT10yy_fusedef.kEfuseMask_WLockGp4 | RT10yy_fusedef.kEfuseMask_RLockGp4)) & (~RT10yy_fusedef.kEfuseMask_LockHigh)
            burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_LOCK, lock)
            if not burnResult:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnGp4Lock'][self.languageIndex])
                return False

    def burnBeeDekData ( self ):
        needToBurnSwGp2 = False
        needToBurnGp4 = False
        swgp2DekFilename = None
        gp4DekFilename = None
        userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(RT10yy_uidef.kAdvancedSettings_UserKeys)
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            if userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                needToBurnSwGp2 = True
                swgp2DekFilename = self.beeDek1Filename
            elif userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                needToBurnGp4 = True
                gp4DekFilename = self.beeDek1Filename
            else:
                pass
        if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
            if userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                needToBurnSwGp2 = True
                swgp2DekFilename = self.beeDek0Filename
            elif userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                needToBurnGp4 = True
                gp4DekFilename = self.beeDek0Filename
            else:
                pass
        keyWords = RT10yy_gendef.kSecKeyLengthInBits_DEK / 32
        if needToBurnSwGp2:
            isReady, isBlank = self._isDeviceFuseSwGp2RegionReadyForBurn(swgp2DekFilename)
            if isReady:
                if isBlank:
                    for i in range(keyWords):
                        val32 = self.getVal32FromBinFile(swgp2DekFilename, (i * 4))
                        burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_SW_GP2_0 + i, val32)
                        if not burnResult:
                            self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnSwgp2'][self.languageIndex])
                            return False
                    if not self._lockFuseSwGp2():
                        return False
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_swgp2HasBeenBurned'][self.languageIndex])
        else:
            pass
        if needToBurnGp4:
            isReady, isBlank = self._isDeviceFuseGp4RegionReadyForBurn(gp4DekFilename)
            if isReady:
                if isBlank:
                    for i in range(keyWords):
                        val32 = self.getVal32FromBinFile(gp4DekFilename, (i * 4))
                        burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseIndex_GP4_0 + i, val32)
                        if not burnResult:
                            self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnGp4'][self.languageIndex])
                            return False
                    if not self._lockFuseGp4():
                        return False
            else:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_gp4HasBeenBurned'][self.languageIndex])
        else:
            pass
        return True

    def _genDestEncAppFileWithoutCfgBlock( self ):
        destEncAppPath, destEncAppFile = os.path.split(self.destEncAppFilename)
        destEncAppName, destEncAppType = os.path.splitext(destEncAppFile)
        destEncAppName += '_nocfgblock'
        self.destEncAppNoCfgBlockFilename = os.path.join(destEncAppPath, destEncAppName + destEncAppType)
        imageLen = os.path.getsize(self.destEncAppFilename)
        imageData = None
        with open(self.destEncAppFilename, 'rb') as fileObj:
            imageData = fileObj.read(imageLen)
            if len(imageData) > rundef.kFlexspiNorCfgInfo_Length:
                imageData = imageData[rundef.kFlexspiNorCfgInfo_Length:len(imageData)]
            fileObj.close()
        with open(self.destEncAppNoCfgBlockFilename, 'wb') as fileObj:
            fileObj.write(imageData)
            fileObj.close()

    def RT10yy_flashBootableImage ( self ):
        self._RT10yy_prepareForBootDeviceOperation()
        imageLen = os.path.getsize(self.destAppFilename)
        if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(self.bootDevice)
            memEraseLen = misc.align_up(imageLen, self.comMemEraseUnit)
            for i in range(self.semcNandImageCopies):
                imageLoadAddr = self.bootDeviceMemBase + (semcNandImageInfoList[i] >> 16) * self.semcNandBlockSize
                if self.isSbFileEnabledToGen:
                    self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ".." + self.convertLongIntHexText(str(hex(imageLoadAddr + memEraseLen))) + ";\n")
                    self._addFlashActionIntoSbAppBdContent("    load " + self.sbAccessBootDeviceMagic + " myBinFile > " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ";\n")
                else:
                    status, results, cmdStr = self.blhost.flashEraseRegion(imageLoadAddr, memEraseLen, self.bootDeviceMemId)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        return False
                    status, results, cmdStr = self.blhost.writeMemory(imageLoadAddr, self.destAppFilename, self.bootDeviceMemId)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        return False
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            if not self.isFlexspiNorErasedForImage:
                if not self._eraseFlexspiNorForImageLoading():
                    return False
                if self.secureBootType == RT10yy_uidef.kSecureBootType_Development or \
                   self.secureBootType == RT10yy_uidef.kSecureBootType_HabAuth or \
                   (self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys):
                    if not self._programFlexspiNorConfigBlock():
                        self.isFlexspiNorErasedForImage = False
                        return False
            if self.secureBootType == RT10yy_uidef.kSecureBootType_BeeCrypto and self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
                self._genDestEncAppFileWithoutCfgBlock()
                imageLoadAddr = self.bootDeviceMemBase + rundef.kFlexspiNorCfgInfo_Length
                if self.isSbFileEnabledToGen:
                    self._addFlashActionIntoSbAppBdContent("    load " + self.sbAccessBootDeviceMagic + " myBinFile > " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ";\n")
                    status = boot.status.kStatus_Success
                else:
                    status, results, cmdStr = self.blhost.writeMemory(imageLoadAddr, self.destEncAppNoCfgBlockFilename, self.bootDeviceMemId)
                    self.printLog(cmdStr)
            else:
                imageLoadAddr = self.bootDeviceMemBase + RT10yy_gendef.kIvtOffset_NOR
                if self.isSbFileEnabledToGen:
                    self._addFlashActionIntoSbAppBdContent("    load " + self.sbAccessBootDeviceMagic + " myBinFile > " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ";\n")
                    status = boot.status.kStatus_Success
                else:
                    status, results, cmdStr = self.blhost.writeMemory(imageLoadAddr, self.destAppNoPaddingFilename, self.bootDeviceMemId)
                    self.printLog(cmdStr)
            self.isFlexspiNorErasedForImage = False
            if status != boot.status.kStatus_Success:
                return False
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            memEraseLen = misc.align_up(imageLen, self.comMemEraseUnit)
            imageLoadAddr = self.bootDeviceMemBase
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ".." + self.convertLongIntHexText(str(hex(imageLoadAddr + memEraseLen))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.sbAccessBootDeviceMagic + " myBinFile > " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ";\n")
            else:
                status, results, cmdStr = self.blhost.flashEraseRegion(imageLoadAddr, memEraseLen, self.bootDeviceMemId)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.writeMemory(imageLoadAddr, self.destAppFilename, self.bootDeviceMemId)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
             self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            memEraseLen = misc.align_up(imageLen, self.comMemEraseUnit)
            imageLoadAddr = self.bootDeviceMemBase + RT10yy_gendef.kIvtOffset_NAND_SD_EEPROM
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ".." + self.convertLongIntHexText(str(hex(imageLoadAddr + memEraseLen))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.sbAccessBootDeviceMagic + " myBinFile > " + self.convertLongIntHexText(str(hex(imageLoadAddr))) + ";\n")
            else:
                status, results, cmdStr = self.blhost.flashEraseRegion(imageLoadAddr, memEraseLen, self.bootDeviceMemId)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.writeMemory(imageLoadAddr, self.destAppNoPaddingFilename, self.bootDeviceMemId)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
        else:
            pass
        if self.isConvertedAppUsed:
            try:
                os.remove(self.srcAppFilename)
            except:
                pass
            self.isConvertedAppUsed = False
        return True

    def _getMcuDeviceSemcNandCfg( self ):
        semcNandCfg = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_SemcNandCfg, '', False)
        return semcNandCfg

    def _getMcuDeviceLpspiCfg( self ):
        lpspiCfg = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_LpspiCfg, '', False)
        return lpspiCfg

    def burnBootDeviceFuses( self ):
        if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
            setSemcNandCfg = 0
            semcNandOpt, semcNandFcbOpt, imageInfo = uivar.getBootDeviceConfiguration(self.bootDevice)
            # Set Device Ecc Status
            eccStatus = (semcNandOpt & 0x00020000) >> 17
            setSemcNandCfg = (setSemcNandCfg & (~RT10yy_fusedef.kEfuseMask_RawNandEccStatus) | (eccStatus << RT10yy_fusedef.kEfuseShift_RawNandEccStatus))
            # Set I/O Port Size
            portSize = (semcNandOpt & 0x00000300) >> 8
            if portSize <= 1:
                portSize = 0
            else:
                portSize = 1
            setSemcNandCfg = (setSemcNandCfg & (~RT10yy_fusedef.kEfuseMask_RawNandPortSize) | (portSize << RT10yy_fusedef.kEfuseShift_RawNandPortSize))
            if self.tgt.isEccTypeSetInFuseMiscConf:
                # Set ECC Check Type
                eccType = (semcNandOpt & 0x00010000) >> 16
                eccType = (eccType + 1) % 2
                setSemcNandCfg = (setSemcNandCfg & (~RT10yy_fusedef.kEfuseMask_RawNandEccEdoSet) | (eccType << RT10yy_fusedef.kEfuseShift_RawNandEccEdoSet))
            else:
                # Set EDO mode
                edoMode = (semcNandOpt & 0x00000008) >> 3
                setSemcNandCfg = (setSemcNandCfg & (~RT10yy_fusedef.kEfuseMask_RawNandEccEdoSet) | (edoMode << RT10yy_fusedef.kEfuseShift_RawNandEccEdoSet))
            getSemcNandCfg = self._getMcuDeviceSemcNandCfg()
            if getSemcNandCfg != None:
                getSemcNandCfg = getSemcNandCfg | setSemcNandCfg
                if (getSemcNandCfg & (RT10yy_fusedef.kEfuseMask_RawNandEccStatus | RT10yy_fusedef.kEfuseMask_RawNandPortSize | RT10yy_fusedef.kEfuseMask_RawNandEccEdoSet)) != setSemcNandCfg:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_miscConf1HasBeenBurned'][self.languageIndex])
                    return False
                else:
                    burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_SemcNandCfg, getSemcNandCfg)
                    if not burnResult:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnMiscConf1'][self.languageIndex])
                        return False
        elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
            pass
        elif self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor:
            setLpspiCfg = 0
            # Set EEPROM enable
            setLpspiCfg = setLpspiCfg | RT10yy_fusedef.kEfuseMask_EepromEnable
            lpspiNorOpt0, lpspiNorOpt1 = uivar.getBootDeviceConfiguration(self.bootDevice)
            # Set Spi Index
            spiIndex = ((lpspiNorOpt0 & 0x00F00000) >> 20) - 1
            setLpspiCfg = (setLpspiCfg & (~RT10yy_fusedef.kEfuseMask_LpspiIndex) | (spiIndex << RT10yy_fusedef.kEfuseShift_LpspiIndex))
            # Set Spi Speed
            spiSpeed = (lpspiNorOpt1 & 0x0000000F) >> 0
            setLpspiCfg = (setLpspiCfg & (~RT10yy_fusedef.kEfuseMask_LpspiSpeed) | (spiSpeed << RT10yy_fusedef.kEfuseShift_LpspiSpeed))
            # Set Spi Addressing
            spiAddressing = 0
            val = (lpspiNorOpt0 & 0x00000F00) >> 8
            totalByteSize = 0
            if val <= 11:
                totalByteSize = int(math.pow(2, val + 19))
            else:
                totalByteSize = int(math.pow(2, val + 3))
            if totalByteSize > (64 * 1024):
                spiAddressing = RT10yy_fusedef.kSpiAddressing_3Bytes
            else:
                spiAddressing = RT10yy_fusedef.kSpiAddressing_2Bytes
            setLpspiCfg = (setLpspiCfg & (~RT10yy_fusedef.kEfuseMask_SpiAddressing) | (spiAddressing << RT10yy_fusedef.kEfuseShift_SpiAddressing))
            getLpspiCfg = self._getMcuDeviceLpspiCfg()
            if getLpspiCfg != None:
                getLpspiCfg = getLpspiCfg | setLpspiCfg
                if (getLpspiCfg & (RT10yy_fusedef.kEfuseMask_EepromEnable | RT10yy_fusedef.kEfuseMask_LpspiIndex | RT10yy_fusedef.kEfuseMask_SpiAddressing | RT10yy_fusedef.kEfuseMask_LpspiSpeed)) != setLpspiCfg:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_miscConf0HasBeenBurned'][self.languageIndex])
                    return False
                else:
                    burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_LpspiCfg, getLpspiCfg)
                    if not burnResult:
                        self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnMiscConf0'][self.languageIndex])
                        return False
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd:
            pass
        elif self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
            pass
        else:
            pass
        return True

    def _getMcuDeviceBeeKeySel( self ):
        beeKeySel = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_BeeKeySel, '', False)
        if beeKeySel != None:
            self.mcuDeviceBeeKey0Sel = ((beeKeySel & RT10yy_fusedef.kEfuseMask_BeeKey0Sel) >> RT10yy_fusedef.kEfuseShift_BeeKey0Sel)
            self.mcuDeviceBeeKey1Sel = ((beeKeySel & RT10yy_fusedef.kEfuseMask_BeeKey1Sel) >> RT10yy_fusedef.kEfuseShift_BeeKey1Sel)
        return beeKeySel

    def burnBeeKeySel( self ):
        setBeeKey0Sel = None
        setBeeKey1Sel = None
        if self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FixedOtpmkKey:
            otpmkKeyOpt, otpmkEncryptedRegionStartListList, otpmkEncryptedRegionLengthList = uivar.getAdvancedSettings(RT10yy_uidef.kAdvancedSettings_OtpmkKey)
            encryptedRegionCnt = (otpmkKeyOpt & 0x000F0000) >> 16
            # One PRDB means one BEE_KEY, no matter how many FAC regions it has
            if encryptedRegionCnt >= 0:
                setBeeKey0Sel = RT10yy_fusedef.kBeeKeySel_FromOtpmk
            #if encryptedRegionCnt > 1:
            #    setBeeKey1Sel = RT10yy_fusedef.kBeeKeySel_FromOtpmk
        elif self.keyStorageRegion == RT10yy_uidef.kKeyStorageRegion_FlexibleUserKeys:
            userKeyCtrlDict, userKeyCmdDict = uivar.getAdvancedSettings(RT10yy_uidef.kAdvancedSettings_UserKeys)
            if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine0 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                if userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_OTPMK:
                    setBeeKey0Sel = RT10yy_fusedef.kBeeKeySel_FromOtpmk
                elif userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                    setBeeKey0Sel = RT10yy_fusedef.kBeeKeySel_FromSwGp2
                elif userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                    setBeeKey0Sel = RT10yy_fusedef.kBeeKeySel_FromGp4
                else:
                    pass
            if userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_Engine1 or userKeyCtrlDict['engine_sel'] == RT10yy_uidef.kUserEngineSel_BothEngines:
                if userKeyCtrlDict['engine0_key_src'] == RT10yy_uidef.kUserKeySource_OTPMK:
                    setBeeKey1Sel = RT10yy_fusedef.kBeeKeySel_FromOtpmk
                elif userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_SW_GP2:
                    setBeeKey1Sel = RT10yy_fusedef.kBeeKeySel_FromSwGp2
                elif userKeyCtrlDict['engine1_key_src'] == RT10yy_uidef.kUserKeySource_GP4:
                    setBeeKey1Sel = RT10yy_fusedef.kBeeKeySel_FromGp4
                else:
                    pass
        else:
            pass
        getBeeKeySel = self._getMcuDeviceBeeKeySel()
        if getBeeKeySel != None:
            if setBeeKey0Sel != None:
                getBeeKeySel = getBeeKeySel | (setBeeKey0Sel << RT10yy_fusedef.kEfuseShift_BeeKey0Sel)
                if ((getBeeKeySel & RT10yy_fusedef.kEfuseMask_BeeKey0Sel) >> RT10yy_fusedef.kEfuseShift_BeeKey0Sel) != setBeeKey0Sel:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_beeKey0SelHasBeenBurned'][self.languageIndex])
                    return False
            if setBeeKey1Sel != None:
                getBeeKeySel = getBeeKeySel | (setBeeKey1Sel << RT10yy_fusedef.kEfuseShift_BeeKey1Sel)
                if ((getBeeKeySel & RT10yy_fusedef.kEfuseMask_BeeKey1Sel) >> RT10yy_fusedef.kEfuseShift_BeeKey1Sel) != setBeeKey1Sel:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_beeKey1SelHasBeenBurned'][self.languageIndex])
                    return False
            burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_BeeKeySel, getBeeKeySel)
            if not burnResult:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnBeeKeyxSel'][self.languageIndex])
                return False
        return True

    def flashHabDekToGenerateKeyBlob ( self ):
        if os.path.isfile(self.habDekFilename) and self.habDekDataOffset != None:
            self._RT10yy_prepareForBootDeviceOperation()
            imageLen = os.path.getsize(self.destAppFilename)
            imageCopies = 0x1
            if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
                imageCopies = self.semcNandImageCopies
            else:
                pass
            # Construct KeyBlob Option
            #---------------------------------------------------------------------------
            # bit [31:28] tag, fixed to 0x0b
            # bit [27:24] type, 0 - Update KeyBlob context, 1 Program Keyblob to SPI NAND
            # bit [23:20] keyblob option block size, must equal to 3 if type =0,
            #             reserved if type = 1
            # bit [19:08] Reserved
            # bit [07:04] DEK size, 0-128bit 1-192bit 2-256 bit, only applicable if type=0
            # bit [03:00] Firmware Index, only applicable if type = 1
            # if type = 0, next words indicate the address that holds dek
            #              the 3rd word
            #----------------------------------------------------------------------------
            keyBlobContextOpt = 0xb0300000
            keyBlobDataOpt = 0xb1000000
            if self.isSbFileEnabledToGen:
                self._addFlashActionIntoSbAppBdContent("    load dekFile > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadDekData))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(keyBlobContextOpt))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadDekData))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext + 4))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(self.habDekDataOffset))) + " > " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext + 8))) + ";\n")
                self._addFlashActionIntoSbAppBdContent("    enable " + self.sbEnableBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext))) + ";\n")
            else:
                status, results, cmdStr = self.blhost.writeMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadDekData, self.habDekFilename)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext, 0x4, keyBlobContextOpt)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext + 4, 0x4, RT10yy_rundef.kRamFreeSpaceStart_LoadDekData)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.fillMemory(RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext + 8, 0x4, self.habDekDataOffset)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
                status, results, cmdStr = self.blhost.configureMemory(self.bootDeviceMemId, RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobContext)
                self.printLog(cmdStr)
                if status != boot.status.kStatus_Success:
                    return False
            for i in range(imageCopies):
                ramFreeSpace = RT10yy_rundef.kRamFreeSpaceStart_LoadKeyBlobData + (RT10yy_rundef.kRamFreeSpaceStep_LoadKeyBlobData * i)
                if self.isSbFileEnabledToGen:
                    self._addFlashActionIntoSbAppBdContent("    load " + self.convertLongIntHexText(str(hex(keyBlobDataOpt + i))) + " > " + self.convertLongIntHexText(str(hex(ramFreeSpace))) + ";\n")
                else:
                    status, results, cmdStr = self.blhost.fillMemory(ramFreeSpace, 0x4, keyBlobDataOpt + i)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        return False
                ########################################################################
                # Flashloader will not erase keyblob region automatically, so we need to handle it here manually
                imageLoadAddr = 0x0
                if self.bootDevice == RT10yy_uidef.kBootDevice_SemcNand:
                    semcNandOpt, semcNandFcbOpt, imageInfo = uivar.getBootDeviceConfiguration(self.bootDevice)
                    imageLoadAddr = self.bootDeviceMemBase + (imageInfo[i] >> 16) * self.semcNandBlockSize
                elif self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor or \
                     self.bootDevice == RT10yy_uidef.kBootDevice_LpspiNor or \
                     self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcSd or \
                     self.bootDevice == RT10yy_uidef.kBootDevice_UsdhcMmc:
                    imageLoadAddr = self.bootDeviceMemBase
                else:
                    pass
                alignedErasedSize = misc.align_up(imageLen, self.comMemEraseUnit)
                needToBeErasedSize = misc.align_up(self.habDekDataOffset + RT10yy_memdef.kMemBlockSize_KeyBlob, self.comMemEraseUnit)
                if alignedErasedSize < needToBeErasedSize:
                    memEraseLen = needToBeErasedSize - alignedErasedSize
                    alignedMemEraseAddr = imageLoadAddr + alignedErasedSize
                    if self.isSbFileEnabledToGen:
                        self._addFlashActionIntoSbAppBdContent("    erase " + self.sbAccessBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(alignedMemEraseAddr))) + ".." + self.convertLongIntHexText(str(hex(alignedMemEraseAddr + memEraseLen))) + ";\n")
                    else:
                        status, results, cmdStr = self.blhost.flashEraseRegion(alignedMemEraseAddr, memEraseLen, self.bootDeviceMemId)
                        self.printLog(cmdStr)
                        if status != boot.status.kStatus_Success:
                            return False
                ########################################################################
                if self.isSbFileEnabledToGen:
                    self._addFlashActionIntoSbAppBdContent("    enable " + self.sbEnableBootDeviceMagic + " " + self.convertLongIntHexText(str(hex(ramFreeSpace))) + ";\n")
                else:
                    status, results, cmdStr = self.blhost.configureMemory(self.bootDeviceMemId, ramFreeSpace)
                    self.printLog(cmdStr)
                    if status != boot.status.kStatus_Success:
                        return False
            if self.bootDevice == RT10yy_uidef.kBootDevice_FlexspiNor:
                if not self._eraseFlexspiNorForConfigBlockLoading():
                    return False
                if not self._programFlexspiNorConfigBlock():
                    return False
            self.updateImgPictureAfterFlashDek()
            return True
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['certGenError_dekNotGen'][self.languageIndex])
            return False

    def enableHab( self ):
        if self.mcuDeviceHabStatus != RT10yy_fusedef.kHabStatus_Closed0 and \
           self.mcuDeviceHabStatus != RT10yy_fusedef.kHabStatus_Closed1:
            secConfig1 = self.readMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_SecConfig1, '', False)
            if secConfig1 != None:
                secConfig1 = secConfig1 | RT10yy_fusedef.kEfuseMask_SecConfig1
                burnResult = self.burnMcuDeviceFuseByBlhost(RT10yy_fusedef.kEfuseLocation_SecConfig1, secConfig1)
                if not burnResult:
                    self.popupMsgBox(uilang.kMsgLanguageContentDict['burnFuseError_failToBurnSecConfig1'][self.languageIndex])
                    return False
        return True

    def RT10yy_resetMcuDevice( self ):
        status, results, cmdStr = self.blhost.reset()
        self.printLog(cmdStr)
        return (status == boot.status.kStatus_Success)
