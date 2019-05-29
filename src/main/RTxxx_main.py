#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from run import RTxxx_runcore
from ui import uidef

class secBootRTxxxMain(RTxxx_runcore.secBootRTxxxRun):

    def __init__(self, parent):
        RTxxx_runcore.secBootRTxxxRun.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self._RTxxx_initMain()

    def _RTxxx_initMain( self ):
        pass

    def RTxxx_callbackSetMcuSeries( self ):
        self.RTxxx_initUi()
        self.RTxxx_initGen()
        self.RTxxx_initRun()
        self._RTxxx_initMain()
        self.RTxxx_setTargetSetupValue()

    def RTxxx_callbackSetMcuDevice( self ):
        self.RTxxx_setTargetSetupValue()

    def RTxxx_callbackSetBootDevice( self ):
        self.RTxxx_setTargetSetupValue()
