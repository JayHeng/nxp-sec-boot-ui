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
from run import RTyyyy_rundef

cpu = 'MIMXRT1176'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x013D'
hasSdpReadRegisterCmd = None
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = None
flashloaderJumpAddr = None
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = [RTyyyy_uidef.kSecureBootType_Development,
                            RTyyyy_uidef.kSecureBootType_HabAuth,
                            #RTyyyy_uidef.kSecureBootType_HabCrypto,
                            RTyyyy_uidef.kSecureBootType_OtfadCrypto,
                            #RTyyyy_uidef.kSecureBootType_IeeCrypto
                            ]
hasRemappedFuse = False
availableBootDevices = [RTyyyy_uidef.kBootDevice_FlexspiNor,
                        RTyyyy_uidef.kBootDevice_SemcNand]
flexspiNorDevice = uidef.kFlexspiNorDevice_ISSI_IS25LP064A
flexspiNorMemBase = 0x30000000
xspiNorCfgInfoOffset = 0x400
flexspiNorEfuseBootCfg0Bits = 12
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isSipFlexspiNorDevice = False
isEccTypeSetInFuseMiscConf = True
isSwEccSetAsDefaultInNandOpt = False

quadspiNorDevice = None
quadspiNorMemBase = None

registerAddrDict = RTyyyy_rundef.registerAddrDict_RT11yy
registerDefnDict  = RTyyyy_rundef.registerDefnDict_RT11yy

efusemapIndexDict = RTyyyy_uidef_efuse.efusemapIndexDict_RT11yy
efusemapDefnDict  = RTyyyy_uidef_efuse.efusemapDefnDict_RT11yy

efuseDescDiffDict = {
                     '0xc70_flexramcfg_bit21_16':RTyyyy_uidef_efuse.efuse_0xc70_flexramPartion512KB,
                    }

# memory map
memoryRange = {
    # ITCM, 512KByte
    'itcm' : MemoryRange(0x00000000, 0x80000, 'state_mem0.dat'),
    # DTCM, 512KByte
    'dtcm' : MemoryRange(0x20000000, 0x80000, 'state_mem1.dat'),
    # OCRAM, 2MByte
    'ocram' : MemoryRange(0x20200000, 0x200000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 2MB
    'ram' : [0x20203800, 0x20207F58]
}

