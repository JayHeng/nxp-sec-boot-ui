#!/usr/bin/env python

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

import sys, os
from fsl.bootloader import memoryrange
from fsl.debugger_utils import kDebuggerType_JLink
import bltestconfig

# @todo Verify cpu and memoryRanges

cpu = 'MK65F18'
board = bltestconfig.target[1]
compiler = bltestconfig.target[2]
build = bltestconfig.target[3]

availableCommands = 0xefff
availablePeripherals = 0x17
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200, 256000] # @todo Verify
deviceMemoryAccessable = True             # @todo Verify
systemDeviceId = 0x650013AC               # @ Device ID

elfFilename = os.path.join(os.path.dirname(__file__), compiler, board, 'output', build, board + '.elf')
binFilename = os.path.join(os.path.dirname(__file__), compiler, board, 'output', build, board + '.bin')
testWorkingDir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test', 'working')
debugger = kDebuggerType_JLink

# flashStartAddress = 0
# flashSize = 2MB
# sectorSize = 4KB
# block count = 4
# flashAlignmentSize = 4 
# eraseAlignmentSize = 16
memoryRange = {'flash':memoryrange.MemoryRange(0, 0x200000, 'state_mem0.dat', True, 4096, 4, 8, 16),

# ramStartAddress = 0x1fff0000
# ramSize = 256KB
               'ram':memoryrange.MemoryRange(0x1fff0000, 0x40000, 'state_mem1.dat'),
              }

