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
from ui import RT10yy_uidef
from ui import RT10yy_uidef_efuse
from ui import uidef

cpu = 'MIMXRT1062'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x0135'
hasSdpReadRegisterCmd = True
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = 0x20000000
flashloaderJumpAddr = 0x20000400
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = [RT10yy_uidef.kSecureBootType_Development,
                            RT10yy_uidef.kSecureBootType_HabAuth,
                            RT10yy_uidef.kSecureBootType_HabCrypto,
                            RT10yy_uidef.kSecureBootType_BeeCrypto]
hasRemappedFuse = True
availableBootDevices = RT10yy_uidef.kBootDevice_Latest
flexspiNorDevice = uidef.kFlexspiNorDevice_ISSI_IS25LP064A
flexspiNorMemBase = 0x60000000
xspiNorCfgInfoOffset = 0x1000
flexspiNorEfuseBootCfg0Bits = 12
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isSipFlexspiNorDevice = False
isEccTypeSetInFuseMiscConf = True

quadspiNorDevice = None
quadspiNorMemBase = None

efuse_0x400_bit7     = {'GP4_R':                   ['0 - Unlock', '1 - RP']}
efuse_0x400_bit15    = {'ROM_PATCH':               ['0 - Unlock', '1 - W,0P']}
efuse_0x400_bit17    = {'OTPMK':                   ['0 - Unlock', '1 - W,0,RP']}
efuse_0x400_bit20    = {'OTPMK_CRC':               ['0 - Unlock', '1 - W,0P']}
efuse_0x400_bit25_24 = {'GP4':                     ['00 - Unlock', '01 - WP', '10 - OP', '01 - W,OP']}
efuse_0x450_bit0     = {'Auto_Probe':              ['0 - Disabled', '1 - Enabled']}
efuse_0x450_bit3_2   = {'Flash_Probe_Type':        ['00 - QuadSPI NOR', '01 - Macronix Octal FLASH', '10 - Micron Octal FLASH', '11 - Adesto Octal FLASH']}
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
efuse_0x460_bit13_12 = {'BEE_KEY0_SEL':            ['00 - From Register', '01 - GP4[127:0]', '10 - From OTPMK[255:128]', '11 - From SW-GP2']}
efuse_0x460_bit15_14 = {'BEE_KEY1_SEL':            ['00 - From Register', '01 - GP4[127:0]', '10 - From OTPMK[255:128]', '11 - From SW-GP2']}
efuse_0x460_bit31_30 = {'SD_BT_Power_Cycle_SEL':   ['00 - 20ms', '01 - 10ms', '10 - 5ms', '11 - 2.5ms']}
efuse_0x470_bit0     = {'BT_SD_Pad':               ['0 - Normal', '1 - Overridden']}
efuse_0x470_bit3     = {'BT_SDMMC':                ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit5     = {'BT_SD2_Volt':             ['0 - 3.3V', '1 - 1.8V']}
efuse_0x470_bit6     = {'BT_SD1_Polar':            ['0 - Low Active', '1 - High Active']}
efuse_0x470_bit8     = {'BT_uSDHC_SRE':            ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit9     = {'BT_uSDHC_SION':           ['0 - Enabled', '1 - Disabled']}
efuse_0x470_bit11    = {'BT_eMMC_Pullup':          ['0 - 47K', '1 - 22K']}
efuse_0x470_bit12    = {'BT_uSDHC_Pulldown':       ['0 - No Action', '1 - Pull Down']}
efuse_0x470_bit13    = {'BT_uSDHC_HYS':            ['0', '1']}
efuse_0x470_bit14    = {'BT_eMMC4.4':              ['0', '1']}
efuse_0x470_bit15    = {'BT_SD2_Polar':            ['0 - Low Active', '1 - High Active']}
efuse_0x470_bit30_24 = {'BT_eMMC4.4_DLL_Delayline':['N/A']}
efuse_0x6e0_bit0     = {'SIP_Test':                ['0 - Disabled', '1 - Enabled']}
efuse_0x6e0_bit3_1   = {'xSPI_Flash_BT_Frequency': ['000 - 100MHz', '001 - 120MHz', '010 - 133MHz', '011 - 166MHz', '100 - Reserved', '101 - 80MHz', '110 - 60MHz', '111 - Reserved']}
efuse_0x6e0_bit5_4   = {'xSPI_Flash_Hold_Time':    ['00 - 500us', '01 - 1ms', '10 - 3ms', '11 - 10ms']}
efuse_0x6e0_bit6     = {'JEDEC_Hw_RST':            ['0 - Disabled', '1 - Enabled']}
efuse_0x6e0_bit11_8  = {'xSPI_Flash_Dummy_Cycle':  ['N/A']}
efuse_0x6e0_bit15_12 = {'xSPI_Flash_Image_Size':   ['0000 - 256KB * FlexSPI_NOR_Secondary_Image_Offset',
                                                    '0001 - 1MB',
                                                    '0010 - 2MB',
                                                    '0011 - 3MB',
                                                    '0100 - 4MB',
                                                    '0101 - 5MB',
                                                    '0110 - 6MB',
                                                    '0111 - 7MB',
                                                    '1000 - 8MB',
                                                    '1001 - 9MB',
                                                    '1010 - 10MB',
                                                    '1011 - 11MB',
                                                    '1100 - 12MB',
                                                    '1101 - 256KB',
                                                    '1110 - 512KB',
                                                    '1111 - 768KB',
                                                   ]}
efuse_0x6e0_bit23_16 = {'FlexSPI_NOR_Secondary_Image_Offset (256KB * fuse value)':['N/A']}
efuse_0x6e0_bit31_24 = {'BT_Pin_SEL':              ['N/A']}

efuseDescDiffDict = {'0x400_lock_bit7' :        efuse_0x400_bit7,
                     '0x400_lock_bit14':        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit15':        efuse_0x400_bit15,
                     '0x400_lock_bit17':        efuse_0x400_bit17,
                     '0x400_lock_bit20':        efuse_0x400_bit20,
                     '0x400_lock_bit25_24':     efuse_0x400_bit25_24,

                     '0x450_bootcfg0_bit0':     efuse_0x450_bit0,
                     '0x450_bootcfg0_bit3_2':   efuse_0x450_bit3_2,
                     '0x450_bootcfg0_bit7_4':   efuse_0x450_bit7_4,

                     '0x460_bootcfg1_bit13_12': efuse_0x460_bit13_12,
                     '0x460_bootcfg1_bit15_14': efuse_0x460_bit15_14,
                     '0x460_bootcfg1_bit31_30': efuse_0x460_bit31_30,

                     '0x470_bootcfg2_bit0':     efuse_0x470_bit0,
                     '0x470_bootcfg2_bit3':     efuse_0x470_bit3,
                     '0x470_bootcfg2_bit5':     efuse_0x470_bit5,
                     '0x470_bootcfg2_bit6':     efuse_0x470_bit6,
                     '0x470_bootcfg2_bit8':     efuse_0x470_bit8,
                     '0x470_bootcfg2_bit9':     efuse_0x470_bit9,
                     '0x470_bootcfg2_bit11':    efuse_0x470_bit11,
                     '0x470_bootcfg2_bit12':    efuse_0x470_bit12,
                     '0x470_bootcfg2_bit13':    efuse_0x470_bit13,
                     '0x470_bootcfg2_bit14':    efuse_0x470_bit14,
                     '0x470_bootcfg2_bit15':    efuse_0x470_bit15,
                     '0x470_bootcfg2_bit30_24': efuse_0x470_bit30_24,

                     '0x6d0_miscconf0_bit19_16':RT10yy_uidef_efuse.efuse_0x6d0_flexramPartion512KB,

                     '0x6e0_miscconf1_bit0':    efuse_0x6e0_bit0,
                     '0x6e0_miscconf1_bit3_1':  efuse_0x6e0_bit3_1,
                     '0x6e0_miscconf1_bit5_4':  efuse_0x6e0_bit5_4,
                     '0x6e0_miscconf1_bit6':    efuse_0x6e0_bit6,
                     '0x6e0_miscconf1_bit11_8': efuse_0x6e0_bit11_8,
                     '0x6e0_miscconf1_bit15_12':efuse_0x6e0_bit15_12,
                     '0x6e0_miscconf1_bit23_16':efuse_0x6e0_bit23_16,
                     '0x6e0_miscconf1_bit31_24':efuse_0x6e0_bit31_24,
                    }

# memory map
memoryRange = {
    # ITCM, 512KByte
    'itcm' : MemoryRange(0x00000000, 0x80000, 'state_mem0.dat'),
    # DTCM, 512KByte
    'dtcm' : MemoryRange(0x20000000, 0x80000, 'state_mem1.dat'),
    # OCRAM, 1MByte
    'ocram' : MemoryRange(0x20200000, 0x100000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 1MB
    'ram' : [0x20203800, 0x20207F58]
}

