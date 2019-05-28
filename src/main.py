#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import threading
import inspect
import ctypes
from main import RTxxx_main
from main import RT10yy_main
from ui import uidef
from ui import uivar
from ui import uilang

g_main_win = None
g_task_detectUsbhid = None
g_task_playSound = None
g_task_allInOneAction = None
g_task_accessMem = None
g_task_increaseGauge = None
g_task_showSettedEfuse = None

def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class secBootMain(RTxxx_main.secBootRTxxxMain):

    def __init__(self, parent):
        RTxxx_main.secBootRTxxxMain.__init__(self, parent)

    def callbackClearLog( self, event ):
        self.clearLog()

    def callbackSaveLog( self, event ):
        self.saveLog()

    def _stopTask( self, thread ):
        _async_raise(thread.ident, SystemExit)

    def _deinitToolToExit( self ):
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Tool, self.toolCommDict)
        uivar.deinitVar()
        #exit(0)
        self._stopTask(g_task_detectUsbhid)
        self._stopTask(g_task_playSound)
        self._stopTask(g_task_allInOneAction)
        self._stopTask(g_task_accessMem)
        self._stopTask(g_task_increaseGauge)
        self._stopTask(g_task_showSettedEfuse)
        global g_main_win
        g_main_win.Show(False)
        try:
            self.Destroy()
        except:
            pass

    def callbackExit( self, event ):
        self._deinitToolToExit()

    def callbackClose( self, event ):
        self._deinitToolToExit()

    def _switchToolRunMode( self ):
        self.applyFuseOperToRunMode()
        self.setSecureBootButtonColor()
        self.enableOneStepForEntryMode()

    def callbackSetRunModeAsEntry( self, event ):
        self.setToolRunMode()
        self._switchToolRunMode()

    def callbackSetRunModeAsMaster( self, event ):
        self.setToolRunMode()
        self._switchToolRunMode()

    def callbackSetUsbDetectionAsDynamic( self, event ):
        self.setUsbDetection()

    def callbackSetUsbDetectionAsStatic( self, event ):
        self.setUsbDetection()

    def callbackSetSoundEffectAsMario( self, event ):
        self.setSoundEffect()

    def callbackSetSoundEffectAsQuiet( self, event ):
        self.setSoundEffect()

    def callbackSetGenSbFileAsYes( self, event ):
        self.setGenSbFile()

    def callbackSetGenSbFileAsNo( self, event ):
        self.setGenSbFile()

    def callbackSetImageReadbackAsAutomatic( self, event ):
        self.setImageReadback()

    def callbackSetImageReadbackAsManual( self, event ):
        self.setImageReadback()

    def callbackSetLanguageAsEnglish( self, event ):
        self.setLanguage()

    def callbackSetLanguageAsChinese( self, event ):
        self.setLanguage()

    def callbackShowHomePage( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['homePage_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['homePage_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowAboutAuthor( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['aboutAuthor_author'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email1'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email2'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_blog'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['aboutAuthor_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowContributors( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['contributors_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['contributors_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowSpecialThanks( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['specialThanks_info'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['specialThanks_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

    def callbackShowRevisionHistory( self, event ):
        msgText = ((uilang.kMsgLanguageContentDict['revisionHistory_v1_0_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_1_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_2_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_3_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_4_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v1_5_0'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['revisionHistory_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()

    g_main_win = secBootMain(None)
    g_main_win.SetTitle(u"NXP MCU Boot Utility v1.5.0")
    g_main_win.Show()

    g_task_detectUsbhid = threading.Thread(target=g_main_win.task_doDetectUsbhid)
    g_task_detectUsbhid.setDaemon(True)
    g_task_detectUsbhid.start()
    g_task_playSound = threading.Thread(target=g_main_win.task_doPlaySound)
    g_task_playSound.setDaemon(True)
    g_task_playSound.start()
    g_task_allInOneAction = threading.Thread(target=g_main_win.task_doAllInOneAction)
    g_task_allInOneAction.setDaemon(True)
    g_task_allInOneAction.start()
    g_task_accessMem = threading.Thread(target=g_main_win.task_doAccessMem)
    g_task_accessMem.setDaemon(True)
    g_task_accessMem.start()
    g_task_increaseGauge = threading.Thread(target=g_main_win.task_doIncreaseGauge)
    g_task_increaseGauge.setDaemon(True)
    g_task_increaseGauge.start()
    g_task_showSettedEfuse = threading.Thread(target=g_main_win.task_doShowSettedEfuse)
    g_task_showSettedEfuse.setDaemon(True)
    g_task_showSettedEfuse.start()

    app.MainLoop()

