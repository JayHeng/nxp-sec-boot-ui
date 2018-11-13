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

import sys
import os
import stat
import conftest
sys.path.append(os.path.abspath("../boot"))
from fsl import bootloader
from fsl.bootloader import properties

##
# @brief Test the bootloader all commands.
class TestAllCommands(object):

    def test_getProperty(self, bl):
        status, results = bl.getProperty(bootloader.properties.kPropertyTag_CurrentVersion)

    def test_fillMemory(self, bl):
        status, results = bl.fillMemory(0x2000, 0x4, 0x12345678)

    def test_readMemory(self, bl):
        status, results = bl.readMemory(0x2000, 0x4)

    def test_efuseReadOnce(self, bl):
        status, results = bl.efuseReadOnce(0x2F)

    def test_listMemory(self, bl):
        status, results = bl.listMemory()


if __name__ == '__main__':
    myAllCommands = TestAllCommands()
    tgt = conftest.tgt()
    myAllCommands.test_getProperty(tgt)
    myAllCommands.test_fillMemory(tgt)
    myAllCommands.test_readMemory(tgt)
    myAllCommands.test_efuseReadOnce(tgt)
    myAllCommands.test_listMemory(tgt)

