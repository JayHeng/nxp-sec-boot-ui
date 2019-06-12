#!/usr/bin/env python

# Copyright (c) 2014 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys, os
sys.path.append(os.path.abspath(".."))
from boot.memoryrange import MemoryRange
from ui import RTyyyy_uidef
from ui import RTyyyy_uidef_efuse
from ui import uidef

cpu = 'MIMXRT1052'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x0130'
hasSdpReadRegisterCmd = True
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = 0x20000000
flashloaderJumpAddr = 0x20000400
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = [RTyyyy_uidef.kSecureBootType_Development,
                            RTyyyy_uidef.kSecureBootType_HabAuth,
                            RTyyyy_uidef.kSecureBootType_HabCrypto,
                            RTyyyy_uidef.kSecureBootType_BeeCrypto]
hasRemappedFuse = False
availableBootDevices = RTyyyy_uidef.kBootDevice_Latest
flexspiNorDevice = uidef.kFlexspiNorDevice_ISSI_IS26KS512S
flexspiNorMemBase = 0x60000000
xspiNorCfgInfoOffset = 0x1000
flexspiNorEfuseBootCfg0Bits = 12
isSipFlexspiNorDevice = False
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isEccTypeSetInFuseMiscConf = False

quadspiNorDevice = None
quadspiNorMemBase = None

efuse_0x400_bit14    = {'SRK':                     ['0 - Unlock', '1 - W,0,RP']}
efuse_0x400_bit15    = {'OTPMK_MSB':               ['0 - Unlock', '1 - W,0,RP']}
efuse_0x450_bit3_2   = {'Hold_Time':               ['00 - 500us', '01 - 1ms', '10 - 3ms', '11 - 10ms']}
efuse_0x450_bit7_4   = {'Boot_Device_Selection':   ['0000 - FlexSPI NOR',
                                                    '0001 - SEMC NOR',
                                                    '0010 - SEMC NAND',
                                                    '0011 - SEMC NAND',
                                                    '0100 - uSDHC SD',
                                                    '0101 - uSDHC SD',
                                                    '0110 - uSDHC SD',
                                                    '0111 - uSDHC SD',
                                                    '1000 - uSDHC (e)MMC',
                                                    '1001 - uSDHC (e)MMC',
                                                    '1010 - uSDHC (e)MMC',
                                                    '1011 - uSDHC (e)MMC',
                                                    '1100 - FlexSPI NAND',
                                                    '1101 - FlexSPI NAND',
                                                    '1110 - FlexSPI NAND',
                                                    '1111 - FlexSPI NAND',
                                                    ]}
efuse_0x460_bit13_12 = {'BEE_KEY0_SEL':            ['00 - From Register', '01 - Reserved', '10 - From OTPMK[255:128]', '11 - From SW-GP2']}
efuse_0x460_bit15_14 = {'BEE_KEY1_SEL':            ['00 - From Register', '01 - Reserved', '10 - From OTPMK[255:128]', '11 - From SW-GP2']}
efuse_0x460_bit24    = {'SD_BT_DLL':               ['0 - Disabled', '1 - Enabled']}
efuse_0x460_bit29    = {'PWR_STA_SEL':             ['0 - 5ms', '1 - 2.5ms']}
efuse_0x460_bit31_30 = {'SD_BT_Power_Cycle_SEL':   ['00 - 20ms', '01 - 10ms', '10 - 5ms', '11 - 2.5ms']}
efuse_0x470_bit0     = {'BT_SD_Pad':               ['0 - Normal', '1 - Overridden']}
efuse_0x470_bit3     = {'BT_SDMMC':                ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit5     = {'BT_SD2_Volt':             ['0 - 3.3V', '1 - 1.8V']}
efuse_0x470_bit6     = {'BT_SD1_Polar':            ['0 - Low Active', '1 - High Active']}
efuse_0x470_bit7     = {'SD_BT_DLL_M':             ['0 - Slave', '1 - Override']}
efuse_0x470_bit8     = {'BT_uSDHC_SRE':            ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit9     = {'BT_uSDHC_SION':           ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit11    = {'BT_eMMC_Pullup':          ['0 - 47K', '1 - 22K']}
efuse_0x470_bit12    = {'BT_uSDHC_Pulldown':       ['0 - No Action', '1 - Pull Down']}
efuse_0x470_bit13    = {'BT_uSDHC_HYS':            ['0', '1']}
efuse_0x470_bit14    = {'BT_eMMC4.4':              ['0', '1']}
efuse_0x470_bit15    = {'BT_SD2_Polar':            ['0 - Low Active', '1 - High Active']}
efuse_0x470_bit30_24 = {'BT_eMMC4.4_DLL_Delayline':['N/A']}
efuse_0x470_bit31    = {'BT_NAND_Pad':             ['0 - Normal', '1 - Overridden']}
efuse_0x6d0_bit11_8  = {'BT_Read_Retry_Sequence':  ['0000 - Don\'t use read retry(RR) sequence',
                                                    '0001 - Micron 20nm RR sequence',
                                                    '0010 - Toshiba A19nm RR sequence',
                                                    '0011 - Toshiba 19nm RR sequence',
                                                    '0100 - SanDisk 19nm RR sequence',
                                                    '0101 - SanDisk 1ynmRR sequence',
                                                    '0110 - Reserved',
                                                    '0111 - Reserved',
                                                    '1000 - Reserved',
                                                    '1001 - Reserved',
                                                    '1010 - Reserved',
                                                    '1011 - Reserved',
                                                    '1100 - Reserved',
                                                    '1101 - Reserved',
                                                    '1110 - Reserved',
                                                    '1111 - Reserved',
                                                    ]}
efuse_0x6d0_bit24    = {'Recovery_BT':             ['0 - Disabled', '1 - Enabled']}
efuse_0x6d0_bit26_25 = {'BT_LPSPI_Port':           ['00 - LPSPI1', '01 - LPSPI2','10 - LPSPI3','11 - LPSPI4']}
efuse_0x6d0_bit27    = {'BT_LPSPI_Addr':           ['0 - 3bytes(24-bit)', '1 - 2bytes(16-bit)']}
efuse_0x6d0_bit29_28 = {'BT_LPSPI_Speed':          ['00 - 20MHz', '01 - 10MHz', '10 - 5MHz', '11 - 2MHz']}
efuse_0x6d0_bit31_30 = {'SD_Calibration_Step':     ['00 - 1', '01 - Reserved', '10 - Reserved', '11 - Reserved']}

efuseDescDiffDict = {'0x400_lock_bit7' :        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit14':        efuse_0x400_bit14,
                     '0x400_lock_bit15':        efuse_0x400_bit15,
                     '0x400_lock_bit17':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit20':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit25_24':     RTyyyy_uidef_efuse.efuse_temp_reserved2,

                     '0x450_bootcfg0_bit0':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x450_bootcfg0_bit3_2':   efuse_0x450_bit3_2,
                     '0x450_bootcfg0_bit7_4':   efuse_0x450_bit7_4,

                     '0x460_bootcfg1_bit6'    : RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x460_bootcfg1_bit13_12': efuse_0x460_bit13_12,
                     '0x460_bootcfg1_bit15_14': efuse_0x460_bit15_14,
                     '0x460_bootcfg1_bit24'   : efuse_0x460_bit24,
                     '0x460_bootcfg1_bit29'   : efuse_0x460_bit29,
                     '0x460_bootcfg1_bit31_30': efuse_0x460_bit31_30,

                     '0x470_bootcfg2_bit0':     efuse_0x470_bit0,
                     '0x470_bootcfg2_bit3':     efuse_0x470_bit3,
                     '0x470_bootcfg2_bit5':     efuse_0x470_bit5,
                     '0x470_bootcfg2_bit6':     efuse_0x470_bit6,
                     '0x470_bootcfg2_bit7':     efuse_0x470_bit7,
                     '0x470_bootcfg2_bit8':     efuse_0x470_bit8,
                     '0x470_bootcfg2_bit9':     efuse_0x470_bit9,
                     '0x470_bootcfg2_bit11':    efuse_0x470_bit11,
                     '0x470_bootcfg2_bit12':    efuse_0x470_bit12,
                     '0x470_bootcfg2_bit13':    efuse_0x470_bit13,
                     '0x470_bootcfg2_bit14':    efuse_0x470_bit14,
                     '0x470_bootcfg2_bit15':    efuse_0x470_bit15,
                     '0x470_bootcfg2_bit30_24': efuse_0x470_bit30_24,
                     '0x470_bootcfg2_bit31':    efuse_0x470_bit31,

                     '0x6d0_miscconf0_bit11_8': efuse_0x6d0_bit11_8,
                     '0x6d0_miscconf0_bit19_16':RTyyyy_uidef_efuse.efuse_0x6d0_flexramPartion512KB,
                     '0x6d0_miscconf0_bit24':   efuse_0x6d0_bit24,
                     '0x6d0_miscconf0_bit26_25':efuse_0x6d0_bit26_25,
                     '0x6d0_miscconf0_bit27':   efuse_0x6d0_bit27,
                     '0x6d0_miscconf0_bit29_28':efuse_0x6d0_bit29_28,
                     '0x6d0_miscconf0_bit31_30':efuse_0x6d0_bit31_30,

                     '0x6e0_miscconf1_bit0':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit3_1':  RTyyyy_uidef_efuse.efuse_temp_reserved3,
                     '0x6e0_miscconf1_bit5_4':  RTyyyy_uidef_efuse.efuse_temp_reserved2,
                     '0x6e0_miscconf1_bit6':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit11_8': RTyyyy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit15_12':RTyyyy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit23_16':RTyyyy_uidef_efuse.efuse_temp_reserved8,
                     '0x6e0_miscconf1_bit31_24':RTyyyy_uidef_efuse.efuse_temp_reserved8,
                    }

# memory map
memoryRange = {
    # ITCM, 512KByte
    'itcm' : MemoryRange(0x00000000, 0x80000, 'state_mem0.dat'),
    # DTCM, 512KByte
    'dtcm' : MemoryRange(0x20000000, 0x80000, 'state_mem1.dat'),
    # OCRAM, 512KByte
    'ocram' : MemoryRange(0x20200000, 0x80000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {
    # OCRAM, 512KB
    'ram' : [0x20203800, 0x20207EF8]
}
