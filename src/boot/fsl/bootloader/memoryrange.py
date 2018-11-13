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

import os
import exceptions

##
# @brief Failure trying to merge two MemoryRange objects.
class MemoryMergeFailure(exceptions.RuntimeError):
    def __init__(self):
        super(MemoryMergeFailure, self).__init__("Memory merge error")

##
# @brief Represents a region of memory with a defined length.
class MemoryRange(object):
    def __init__(self, start, length, filename=None, isFlash=False, flashSectorSize=0, flashBlockCount=0, flashAlignmentSize=4, eraseAlignmentSize=4, offsetInFile=0, sizeInFile=-1):
        self.start = start
        self.length = length
        self.end = start + length - 1

        self.backingFilename = filename
        self.simulatorFilename = filename  # Deprecated. Use self.backingFilename instead.
        self.offsetInFile = offsetInFile
        
        # -1 means to use the default.
        if sizeInFile == -1:
            # If a backing store file was given, then assume the whole memory range comes from
            # the file. Otherwise set sizeInFile to 0 since we don't have a backing store.
            if filename is not None:
                self.sizeInFile = self.length
            else:
                self.sizeInFile = 0
        else:
            self.sizeInFile = self.sizeInFile

        self.isFlash = isFlash
        self.flashSectorSize = flashSectorSize
        self.flashBlockCount = flashBlockCount
        self.flashAlignmentSize = flashAlignmentSize
        self.eraseAlignmentSize = eraseAlignmentSize
    
    def hasBackingStore(self):
        return self.backingFilename is not None
    
    def getData(self):
        if self.hasBackingStore():
            with open(self.backingFilename, 'rb') as dataFile:
                dataFile.seek(self.offsetInFile)
                data = bytearray(dataFile.read(self.sizeInFile))
        else:
            data = bytearray()
        
        # Extend by adding zero bytes if the size in file is smaller than total size.
        if self.sizeInFile < self.length:
            data += b'\x00' * (self.length - self.sizeInFile)
        
        return data
    
    def __repr__(self):
        return "<%s@0x%x: 0x%08x-0x%08x>" % (
            self.__class__.__name__, id(self), self.start, self.end)
    
    ##
    # @brief Merge this memory range with another.
    #
    # @return A new MemoryRange instance.
    # @exception MemoryMergeFailure The @a other memory range is not contiguous with this one,
    #       or two the ranges are incompatible in one way or another.
    def mergeWith(self, other):
        # Either both ranges have no backing, or the same file.
        isSameBacking = ((self.backingFilename is None and other.backingFilename is None) or
            ((self.backingFilename is not None and other.backingFilename is not None) and
                os.path.samefile(self.backingFilename, other.backingFilename)))
        
        # Check if the two are compatible.
        if ((not isSameBacking) or (self.isFlash != other.isFlash) or
            (self.flashSectorSize != other.flashSectorSize)):
            raise MemoryMergeFailure()
        
        # Does either range completely subsume the other?
        if (self.start <= other.start) and (self.end >= other.end):
            return self
        elif (other.start <= self.start) and (other.end >= self.end):
            return other
        
        newStart = 0
        newEnd = 0
        newOffsetInFile = 0
        if (other.start >= self.start) and (other.start <= self.end + 1):
            newStart = self.start
            newEnd = other.end
            newOffsetInFile = self.offsetInFile
        elif (other.end + 1 >= self.start) and (other.end <= self.end):
            newStart = other.start
            newEnd = self.end
            newOffsetInFile = other.offsetInFile
        else:
            raise MemoryMergeFailure()
        newLength = newEnd - newStart + 1
        
        newRange = MemoryRange(newStart, newLength, filename=self.backingFilename,
            isFlash=self.isFlash, flashSectorSize=self.flashSectorSize,
            flashBlockCount=self.flashBlockCount, offsetInFile=newOffsetInFile) #,
            #sizeInFile=self.sizeInFile)
        return newRange
    
    ##
    # @brief Tests whether this range fully contains another.
    def contains(self, other):
        return ((other.start >= self.start) and (other.start <= self.end) and
                (other.end >= self.start) and (other.end <= self.end))
    
    ##
    # @brief Tests whether this range and another overlap any amount.
    def intersects(self, other):
        return (((other.start >= self.start) and (other.start <= self.end)) or
                ((other.end >= self.start) and (other.end <= self.end)))
    
    def __eq__(self, other):
        if not isinstance(other, MemoryRange):
            return False
        return (other.start == self.start) and (other.end == self.end)

##
# @brief Add a new MemoryRange to an existing list and merge if needed.
#
# @return The resulting merged list. May be a different list object than the one passed in.
def addRangeToListAndCoalesce(l, r):
    rStart = r.start
    rEnd = r.end
    n = 0
    for n, i in enumerate(l):
        iStart = i.start
        iEnd = i.end
        
        try:
            mergedRange = i.mergeWith(r)
        except MemoryMergeFailure:
            pass
        else:
            l[n] = mergedRange
            return l
        
        if iStart >= rEnd:
            l.insert(n, r)
            return l
    l.append(r)
    return l

##
# @brief Merge contiguous MemoryRange objects.
#
# @param ranges A list of MemoryRange objects.
# @return List of MemoryRange objects.
def coalesceRangeList(ranges):
    result = []
    
    for r in ranges:
        result = addRangeToListAndCoalesce(result, r)
    
    return result

##
# @brief Unit test for memory range merging.
class TestRangeLists:
    def setup_method(self, method):
        print method
        self.a = MemoryRange(0,0x100)
        self.b = MemoryRange(0x100,0x400)
        self.c = MemoryRange(0x800,0x100)
        self.d = MemoryRange(0x700,0x1000)
        self.q = MemoryRange(0x900,0x100)
        self.y = MemoryRange(0x1f000,0x1000)
        self.z = MemoryRange(0x20000,0x1000)
        self.l = [self.a, self.b, self.c, self.q, self.z]
    
    def checkStartLength(self, r, s, l):
        assert r.start == s
        assert r.end == s + l - 1
        assert r.length == l
    
    def test_merge1(self):
        r = self.a.mergeWith(self.b)
        self.checkStartLength(r, 0, 0x500)
    
    def test_merge_list(self):
        l = coalesceRangeList(self.l)
        self.checkStartLength(l[0], 0, 0x500)
        self.checkStartLength(l[1], 0x800, 0x200)
        self.checkStartLength(l[2], 0x20000, 0x1000)
    
    def test_add_list1(self):
        l = addRangeToListAndCoalesce([], self.c)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x800, 0x100)
        
        l = addRangeToListAndCoalesce(l, self.a)
        print l
        assert len(l) == 2
        self.checkStartLength(l[0], 0, 0x100)
        self.checkStartLength(l[1], 0x800, 0x100)
        
        l = addRangeToListAndCoalesce(l, self.z)
        print l
        assert len(l) == 3
        self.checkStartLength(l[0], 0, 0x100)
        self.checkStartLength(l[1], 0x800, 0x100)
        self.checkStartLength(l[2], 0x20000, 0x1000)
        
        l = addRangeToListAndCoalesce(l, self.b)
        print l
        assert len(l) == 3
        self.checkStartLength(l[0], 0, 0x500)
        self.checkStartLength(l[1], 0x800, 0x100)
        self.checkStartLength(l[2], 0x20000, 0x1000)
    
    def test_add_list_ab(self):
        l = addRangeToListAndCoalesce([], self.a)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0, 0x100)
        
        l = addRangeToListAndCoalesce(l, self.b)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0, 0x500)
    
    def test_add_list_ba(self):
        l = addRangeToListAndCoalesce([], self.b)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x100, 0x400)
        
        l = addRangeToListAndCoalesce(l, self.a)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0, 0x500)
    
    def test_add_list_cd(self):
        l = addRangeToListAndCoalesce([], self.c)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x800, 0x100)
        
        l = addRangeToListAndCoalesce(l, self.d)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x700, 0x1000)
    
    def test_add_list_dc(self):
        l = addRangeToListAndCoalesce([], self.d)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x700, 0x1000)
        
        l = addRangeToListAndCoalesce(l, self.c)
        print l
        assert len(l) == 1
        self.checkStartLength(l[0], 0x700, 0x1000)
        
