#! /usr/bin/env python

# Copyright (c) 2013 Freescale Semiconductor, Inc.
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

# Property constants.
kPropertyTag_CurrentVersion         = 0x01
kPropertyTag_AvailablePeripherals   = 0x02
kPropertyTag_FlashStartAddress      = 0x03
kPropertyTag_FlashSizeInBytes       = 0x04
kPropertyTag_FlashSectorSize        = 0x05
kPropertyTag_FlashBlockCount        = 0x06
kPropertyTag_AvailableCommands      = 0x07
kPropertyTag_CrcCheckStatus         = 0x08
kPropertyTag_Reserved_0x09          = 0x09 # Reserved for further use
kPropertyTag_VerifyWrites           = 0x0a
kPropertyTag_MaxPacketSize          = 0x0b
kPropertyTag_ReservedRegions        = 0x0c
kPropertyTag_ValidateRegions        = 0x0d
kPropertyTag_RAMStartAddress        = 0x0e
kPropertyTag_RAMSizeInBytes         = 0x0f
kPropertyTag_SystemDeviceIdent      = 0x10
kPropertyTag_FlashSecurityState     = 0x11 
kPropertyTag_UniqueDeviceIdent      = 0x12
kPropertyTag_FacSupportFlag         = 0x13
kPropertyTag_FacSegmentSize         = 0x14
kPropertyTag_FacSegmentCount        = 0x15
kPropertyTag_FlashReadMargin        = 0x16
kPropertyTag_Reserved_0x17          = 0x17 # Reserved for further use
kPropertyTag_TargetVersion          = 0x18
kPropertyTag_ExternalMemoryAttribles= 0x19
kPropertyTag_ReliableUpdateStatus   = 0x1a
kPropertyTag_Invalid                = 0xFF

# Version constants
kBootloaderVersion_1_0_0 = 0x4B010000
kBootloaderVersion_1_1_0 = 0x4B010100
kBootloaderVersion_1_1_1 = 0x4B010101
kBootloaderVersion_1_2_0 = 0x4B010200
kBootloaderVersion_1_3_0 = 0x4B010300
kBootloaderVersion_1_4_0 = 0x4B010400
kBootloaderVersion_1_4_1 = 0x4B010401
kBootloaderVersion_1_5_0 = 0x4B010500
kBootloaderVersion_1_5_1 = 0x4B010501
kBootloaderVersion_2_0_0 = 0x4B020000
kBootloaderVersion_2_1_0 = 0x4B020100
kBootloaderVersion_2_2_0 = 0x4B020200

kBootloaderVersionDict = {
    "kBootloaderVersion_1_0_0" : 0x4B010000,
    "kBootloaderVersion_1_1_0" : 0x4B010100,
    "kBootloaderVersion_1_1_1" : 0x4B010101,
    "kBootloaderVersion_1_2_0" : 0x4B010200,
    "kBootloaderVersion_1_3_0" : 0x4B010300,
    "kBootloaderVersion_1_4_0" : 0x4B010400,
    "kBootloaderVersion_1_4_1" : 0x4B010401,
    "kBootloaderVersion_1_5_0" : 0x4B010500,
    "kBootloaderVersion_1_5_1" : 0x4B010501,
    "kBootloaderVersion_2_0_0" : 0x4B020000,
    "kBootloaderVersion_2_1_0" : 0x4B020100,
    "kBootloaderVersion_2_2_0" : 0x4B020200
}

# Target version
kTargetVersion_1_0_0 = 0x54010000
kTargetVersion_1_1_0 = 0x54010100

kTargetVersionDict = {
    "kTargetVersion_1_0_0" : 0x54010000,
    "kTargetVersion_1_1_0" : 0x54010100
}

