#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from ui import RTxxx_uicore

class secBootRTxxxGen(RTxxx_uicore.secBootRTxxxUi):

    def __init__(self, parent):
        RTxxx_uicore.secBootRTxxxUi.__init__(self, parent)

