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

import os
import elf
from . import commands, memoryrange, peripherals
from .. import misc, debugger_utils

##
# Bootloader target definition.
class Target(object):
    
    def __init__(self, cpu, board='', build='', **kwargs):
                #baseDir='.', elfFile=None, memory={}, availableCommands=0,
                #availablePeripherals=0, deviceMemoryAccessable=False, systemDeviceId=0, isBootROM=False, isCrcCheckSupported=False):
        self.cpu = cpu
        self.board = board
        self.build = build

        self.baseDir = misc.get_dict_default(kwargs, 'baseDir', '.')
        self.elfFilename = misc.get_dict_default(kwargs, 'elfFilename', None)
        self.binFilename = misc.get_dict_default(kwargs, 'binFilename', None)
        self.memoryRange = misc.get_dict_default(kwargs, 'memoryRange', {})
        self.availableCommands = misc.get_dict_default(kwargs, 'availableCommands', 0)
        self.availablePeripherals = misc.get_dict_default(kwargs, 'availablePeripherals', 0)
        self.supportedPeripheralSpeed_uart = misc.get_dict_default(kwargs, 'supportedPeripheralSpeed_uart', None)
        self.deviceMemoryAccessable = misc.get_dict_default(kwargs, 'deviceMemoryAccessable', False)
        self.systemDeviceId = misc.get_dict_default(kwargs, 'systemDeviceId', 0)
        self.testWorkingDir = misc.get_dict_default(kwargs, 'testWorkingDir', None)
        self.debuggerType = misc.get_dict_default(kwargs, 'debugger', None)
        self.isExtendedSBFileSupported = misc.get_dict_default(kwargs, 'isExtendedSBFileSupported', False)

        self._debugger = debugger_utils.createDebugger(self.debuggerType)
        self._debugger.open()
        
        self.elfObject = None
        self.reservedRanges = []

        # Get the target's flash memory region and flash sector size.
        try:
            self.flashMemory = self.memoryRange['flash']
        except KeyError:
            self.flashMemory = None
            self.flashSectorSize = 1
        else:
            self.flashSectorSize = self.flashMemory.flashSectorSize
        
        # Get the target's ram memory region.
        try:
            self.ramMemory = self.memoryRange['ram']
        except KeyError:
            self.ramMemory = None
        
        # Read the elf file info and get reserved ranges.
        if self.elfFilename is not None and os.path.exists(self.elfFilename):
            with open(self.elfFilename, 'rb') as f:
                e = elf.ELFObject()
                e.fromFile(f)
                self.elfObject = e
        
            self.reservedRanges = self._getReservedRanges()

        self.freeFlashRange = self._getFreeRange(self.flashMemory)
        self.freeRamRange = self._getFreeRange(self.ramMemory)

        
    ##
    # @brief Check if a command is supported by the target.
    #
    # @return True if the command is supported. False if not.
    def isCommandSupported(self, tag):
        return bool(commands.Commands[tag].propertyMask & self.availableCommands)
    
    ##
    # @brief Check if a peripheral is supported by the target.
    #
    # @return True if the peripheral is supported. False if not.
    def isPeripheralSupported(self, name):
        return bool(peripherals.PeripheralMasks[name].propertyMask & self.availablePeripherals)
    
    ##
    # @brief Determines the list of reserved memory ranges.
    #
    # @return A list of MemoryRange objects.
    def _getReservedRanges(self):
        if not self.elfObject:
            return []
        
        # Only consider sections whose Write and Alloc flags are both set, and are
        # non-zero in size.
        writeAndAllocFlags = elf.ELFSection.SHF_WRITE | elf.ELFSection.SHF_ALLOC
        alloced = [s for s in self.elfObject.sections if (bool(s.sh_flags & writeAndAllocFlags)) and (s.sh_size > 0)]
        progbits = [s for s in alloced if s.sh_type == elf.ELFSection.SHT_PROGBITS]
        nobits = [s for s in alloced if s.sh_type == elf.ELFSection.SHT_NOBITS]

        ranges = []
        for s in progbits + nobits:
            r = memoryrange.MemoryRange(s.lma, s.sh_size)
            
            # If the reserved region is in flash, we have to sector align it.
            if self.flashMemory is not None:
                if self.flashMemory.contains(r):
                    # Align start and end, recompute length.
                    start = misc.align_down(r.start, self.flashSectorSize)
                    end = misc.align_up(r.end, self.flashSectorSize)
                    length = end - start
                
                    # Create aligned memory range.
                    r = memoryrange.MemoryRange(start, length)
            
            # Only save this range if it is within one of the defined memory regions for
            # this target.
            for i in self.memoryRange.values():
                ## @todo Should add only intersection to list
                if i.intersects(r):
                    ranges = memoryrange.addRangeToListAndCoalesce(ranges, r)
                    break
        
        return ranges
    
    ##
    # @brief Determine free memory range.
    #
    def _getFreeRange(self, fullRange):
        if fullRange is not None:
            # Check if requested range is contained in any reserved range
            for r in self.reservedRanges:
                if fullRange.contains(r):
                    # Return a range that starts after the end of the reserved range and goes to the end of the full range
                    start = r.end + 1
                    len = fullRange.end + 1 - start
                    return memoryrange.MemoryRange(start, len)
        # Requested range not contained in any reserved range, so full range is free
        return fullRange

    ##
    # @brief Reset the target by an external means.
    #
    def reset(self):
        return self._debugger.reset()

    ##
    # @brief 
    #
    def readMemOneItem(self, addr, itemType):
        return self._debugger.readMemOneItem(addr, itemType)

    ##
    # @brief 
    #
    def writeMemOneItem(self, addr, value, itemType):
        return self._debugger.writeMemOneItem(addr, value, itemType)
    
    ##
    # @brief 
    #
    def getPC(self):
        return self._debugger.getPC()    
    
    ##
    # @brief Unlock the target by an external means.
    #
    def unlock(self):
        return self._debugger.unlock()
    
    ##
    # @brief Flash bootloader binary.
    #
    def flashBinary(self):
        return self._debugger.flashBinary(self.binFilename)
    
    ##
    # @brief Close the target.
    #
    def close(self):
        return self._debugger.close()
        
