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

cpu = 'MIMXRT1011'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x0145'
hasSdpReadRegisterCmd = False
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = 0x20205c00
flashloaderJumpAddr = 0x20205c00
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = [RT10yy_uidef.kSecureBootType_Development,
                            RT10yy_uidef.kSecureBootType_HabAuth,
                            RT10yy_uidef.kSecureBootType_HabCrypto,
                            RT10yy_uidef.kSecureBootType_OtfadCrypto]
hasRemappedFuse = False
availableBootDevices = [RT10yy_uidef.kBootDevice_FlexspiNor]
flexspiNorDevice = uidef.kFlexspiNorDevice_Adesto_AT25SF128A
flexspiNorMemBase = 0x60000000
xspiNorCfgInfoOffset = 0x400
flexspiNorEfuseBootCfg0Bits = 10
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isSipFlexspiNorDevice = False
isEccTypeSetInFuseMiscConf = False

quadspiNorDevice = None
quadspiNorMemBase = None

efuse_0x450_bit7_4   = {'Boot_Device_Selection':   ['0000 - FlexSPI NOR',
                                                    '0001 - Reserved',
                                                    '0010 - Reserved',
                                                    '0011 - Reserved',
                                                    '0100 - Reserved',
                                                    '0101 - Reserved',
                                                    '0110 - Reserved',
                                                    '0111 - Reserved',
                                                    '1000 - Reserved',
                                                    '1001 - Reserved',
                                                    '1010 - Reserved',
                                                    '1011 - Reserved',
                                                    '1100 - FlexSPI NAND',
                                                    '1101 - FlexSPI NAND',
                                                    '1110 - FlexSPI NAND',
                                                    '1111 - FlexSPI NAND',
                                                    ]}
efuse_0x460_bit13_12 = {'BEE_KEY0_SEL':            ['00 - From Register', '01 - Reserved', '10 - Reserved', '11 - From SW-GP2']}
efuse_0x460_bit15_14 = {'BEE_KEY1_SEL':            ['00 - From Register', '01 - Reserved', '10 - Reserved', '11 - From SW-GP2']}
efuseDescDiffDict = {'0x400_lock_bit7' :        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit14':        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit15':        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit17':        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit20':        RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit25_24':     RT10yy_uidef_efuse.efuse_temp_reserved2,

                     '0x450_bootcfg0_bit7_4':   efuse_0x450_bit7_4,

                     '0x460_bootcfg1_bit13_12': efuse_0x460_bit13_12,
                     '0x460_bootcfg1_bit15_14': efuse_0x460_bit15_14,
                     '0x460_bootcfg1_bit31_30': RT10yy_uidef_efuse.efuse_temp_reserved2,

                     '0x470_bootcfg2_bit0':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit3':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit5':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit6':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit8':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit9':     RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit11':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit12':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit13':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit14':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit15':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit30_24': RT10yy_uidef_efuse.efuse_temp_reserved7,

                     '0x6d0_miscconf0_bit19_16':RT10yy_uidef_efuse.efuse_0x6d0_flexramPartion128KB,

                     '0x6e0_miscconf1_bit0':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit3_1':  RT10yy_uidef_efuse.efuse_temp_reserved3,
                     '0x6e0_miscconf1_bit5_4':  RT10yy_uidef_efuse.efuse_temp_reserved2,
                     '0x6e0_miscconf1_bit6':    RT10yy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit11_8': RT10yy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit15_12':RT10yy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit23_16':RT10yy_uidef_efuse.efuse_temp_reserved8,
                     '0x6e0_miscconf1_bit31_24':RT10yy_uidef_efuse.efuse_temp_reserved8,
                    }

# memory map
memoryRange = {
    # ITCM, 128KByte
    'itcm' : MemoryRange(0x00000000, 0x20000, 'state_mem0.dat'),
    # DTCM, 128KByte
    'dtcm' : MemoryRange(0x20000000, 0x20000, 'state_mem1.dat'),
    # OCRAM, 128KByte
    'ocram' : MemoryRange(0x20200000, 0x20000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 128KB
    'ram' : [0x20203800, 0x20207EF8]
}

