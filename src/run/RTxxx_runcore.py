#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from gen import RTxxx_gencore

class secBootRTxxxRun(RTxxx_gencore.secBootRTxxxGen):

    def __init__(self, parent):
        RTxxx_gencore.secBootRTxxxGen.__init__(self, parent)

