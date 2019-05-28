#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from run import RTxxx_runcore

class secBootRTxxxMain(RTxxx_runcore.secBootRTxxxRun):

    def __init__(self, parent):
        RTxxx_runcore.secBootRTxxxRun.__init__(self, parent)

