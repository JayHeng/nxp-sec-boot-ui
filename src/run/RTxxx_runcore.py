#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import RTxxx_rundef
import boot
sys.path.append(os.path.abspath(".."))
from gen import RTxxx_gencore
from ui import RTxxx_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from boot import bltest
from boot import target
from utils import misc

def createTarget(device, exeBinRoot):
    # Build path to target directory and config file.
    if device == RTxxx_uidef.kMcuDevice_iMXRT500:
        cpu = "MIMXRT595"
    elif device == RTxxx_uidef.kMcuDevice_iMXRT600:
        cpu = "MIMXRT685"
    else:
        pass
    targetBaseDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets', cpu)

    # Check for existing target directory.
    if not os.path.isdir(targetBaseDir):
        targetBaseDir = os.path.join(os.path.dirname(exeBinRoot), 'src', 'targets', cpu)
        if not os.path.isdir(targetBaseDir):
            raise ValueError("Missing target directory at path %s" % targetBaseDir)

    targetConfigFile = os.path.join(targetBaseDir, 'bltargetconfig.py')

    # Check for config file existence.
    if not os.path.isfile(targetConfigFile):
        raise RuntimeError("Missing target config file at path %s" % targetConfigFile)

    # Build locals dict by copying our locals and adjusting file path and name.
    targetConfig = locals().copy()
    targetConfig['__file__'] = targetConfigFile
    targetConfig['__name__'] = 'bltargetconfig'

    # Execute the target config script.
    execfile(targetConfigFile, globals(), targetConfig)

    # Create the target object.
    tgt = target.Target(**targetConfig)

    return tgt, targetBaseDir

class secBootRTxxxRun(RTxxx_gencore.secBootRTxxxGen):

    def __init__(self, parent):
        RTxxx_gencore.secBootRTxxxGen.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initRun()

    def RTxxx_initRun( self ):
        self.RTxxx_createMcuTarget()

    def RTxxx_createMcuTarget( self ):
        self.tgt, self.cpuDir = createTarget(self.mcuDevice, self.exeBinRoot)

