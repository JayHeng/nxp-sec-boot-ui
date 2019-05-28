#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from mem import RT10yy_memcore

class secBootRTxxxUi(RT10yy_memcore.secBootRT10yyMem):

    def __init__(self, parent):
        RT10yy_memcore.secBootRT10yyMem.__init__(self, parent)

