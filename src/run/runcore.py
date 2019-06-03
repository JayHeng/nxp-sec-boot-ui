#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import rundef
sys.path.append(os.path.abspath(".."))
from gen import gencore
from ui import uidef
from ui import uivar
from ui import uilang

##
# @brief
class secBootRun(gencore.secBootGen):

    def __init__(self, parent):
        gencore.secBootGen.__init__(self, parent)

    def showAsOptimalMemoryUnit( self, memSizeBytes ):
        strMemSize = ''
        if memSizeBytes >= 0x40000000:
            strMemSize = str(memSizeBytes / 0x40000000) + ' GB'
        elif memSizeBytes >= 0x100000:
            strMemSize = str(memSizeBytes / 0x100000) + ' MB'
        elif memSizeBytes >= 0x400:
            strMemSize = str(memSizeBytes / 0x400) + ' KB'
        else:
            strMemSize = str(memSizeBytes) + ' Bytes'
        return strMemSize


