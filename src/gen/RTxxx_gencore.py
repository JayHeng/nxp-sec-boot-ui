#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import RTxxx_gendef
sys.path.append(os.path.abspath(".."))
from ui import RTxxx_uicore
from ui import uidef

class secBootRTxxxGen(RTxxx_uicore.secBootRTxxxUi):

    def __init__(self, parent):
        RTxxx_uicore.secBootRTxxxUi.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initGen()

    def RTxxx_initGen( self ):
        pass
