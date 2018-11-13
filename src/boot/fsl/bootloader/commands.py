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

from collections import namedtuple

# Command constants.
kCommandTag_FlashEraseAll         = 0x01
kCommandTag_FlashEraseRegion      = 0x02
kCommandTag_ReadMemory            = 0x03
kCommandTag_WriteMemory           = 0x04
kCommandTag_FillMemory            = 0x05
kCommandTag_FlashSecurityDisable  = 0x06
kCommandTag_GetProperty           = 0x07
kCommandTag_ReceiveSBFile         = 0x08
kCommandTag_Execute               = 0x09
kCommandTag_Call                  = 0x0a
kCommandTag_Reset                 = 0x0b
kCommandTag_SetProperty           = 0x0c
kCommandTag_FlashEraseAllUnsecure = 0x0d
kCommandTag_FlashProgramOnce      = 0x0e,
kCommandTag_FlashReadOnce         = 0x0f,
kCommandTag_FlashReadResource     = 0x10,
kCommandTag_ConfigureMemory       = 0x11,
kCommandTag_ReliableUpdate        = 0x12,
kCommandTag_GenerateKeyBlob       = 0x13,
kCommandTag_KeyProvisoning        = 0x15,

Command = namedtuple('Command', 'tag, propertyMask, name')

Commands = {
    kCommandTag_FlashEraseAll         : Command(kCommandTag_FlashEraseAll,         0x00000001, 'flash-erase-all'),
    kCommandTag_FlashEraseRegion      : Command(kCommandTag_FlashEraseRegion,      0x00000002, 'flash-erase-region'),
    kCommandTag_ReadMemory            : Command(kCommandTag_ReadMemory,            0x00000004, 'read-memory'),
    kCommandTag_WriteMemory           : Command(kCommandTag_WriteMemory,           0x00000008, 'write-memory'),
    kCommandTag_FillMemory            : Command(kCommandTag_FillMemory,            0x00000010, 'fill-memory'),
    kCommandTag_FlashSecurityDisable  : Command(kCommandTag_FlashSecurityDisable,  0x00000020, 'flash-security-disable'),
    kCommandTag_GetProperty           : Command(kCommandTag_GetProperty,           0x00000040, 'get-property'),
    kCommandTag_ReceiveSBFile         : Command(kCommandTag_ReceiveSBFile,         0x00000080, 'receive-sb-file'),
    kCommandTag_Execute               : Command(kCommandTag_Execute,               0x00000100, 'execute'),
    kCommandTag_Call                  : Command(kCommandTag_Call,                  0x00000200, 'call'),
    kCommandTag_Reset                 : Command(kCommandTag_Reset,                 0x00000400, 'reset'),
    kCommandTag_SetProperty           : Command(kCommandTag_SetProperty,           0x00000800, 'set-property'),
    kCommandTag_FlashEraseAllUnsecure : Command(kCommandTag_FlashEraseAllUnsecure, 0x00001000, 'flash-erase-all-unsecure'),
    kCommandTag_FlashProgramOnce      : Command(kCommandTag_FlashProgramOnce,      0x00002000, 'flash-program-once'),
    kCommandTag_FlashReadOnce         : Command(kCommandTag_FlashReadOnce,         0x00004000, 'flash-read-once'),
    kCommandTag_FlashReadResource     : Command(kCommandTag_FlashReadResource,     0x00008000, 'flash-read-resource'),
    kCommandTag_ConfigureMemory       : Command(kCommandTag_ConfigureMemory,       0x00010000, 'configure-memory'),
    kCommandTag_ReliableUpdate        : Command(kCommandTag_ReliableUpdate,        0x00100000, 'reliable-update'),
    kCommandTag_GenerateKeyBlob       : Command(kCommandTag_GenerateKeyBlob,       0x00200000, 'generate-key-blob'),
    kCommandTag_KeyProvisoning        : Command(kCommandTag_KeyProvisoning,        0x00400000, 'key-provisioning'),
}

