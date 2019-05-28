#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from mem import memcore

class secBootRTxxxUi(memcore.secBootMem):

    def __init__(self, parent):
        memcore.secBootMem.__init__(self, parent)

