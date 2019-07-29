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
from _main import RTxxx_main
from _main import RTyyyy_main
from ui import RTyyyy_uidef
from ui import RTxxx_uidef
from ui import uidef
from ui import uivar
from ui import uilang
from ui import ui_cfg_flexspinor
from ui import ui_cfg_flexspinand
from ui import ui_cfg_semcnor
from ui import ui_cfg_semcnand
from ui import ui_cfg_usdhcsd
from ui import ui_cfg_usdhcmmc
from ui import ui_cfg_lpspinor

g_main_win = None
g_task_detectUsbhid = None
g_task_playSound = None
g_task_increaseGauge = None
g_task_accessMem = None
g_RTyyyy_task_allInOneAction = None
g_RTxxx_task_allInOneAction = None
g_RTyyyy_task_showSettedEfuse = None

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

        self.isAccessMemTaskPending = False
        self.accessMemType = ''
        self.lastTime = None

    def _startGaugeTimer( self ):
        self.lastTime = time.time()
        self.initGauge()

    def _stopGaugeTimer( self ):
        self.deinitGauge()
        self.updateCostTime()

    def callbackSetMcuSeries( self, event ):
        pass

    def callbackSetMcuDevice( self, event ):
        self.setTargetSetupValue()
        self._setUartUsbPort()
        if self.isMcuSeriesChanged:
            if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
                self.RTyyyy_callbackSetMcuSeries()
            elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
                self.RTxxx_callbackSetMcuSeries()
            else:
                pass
            self.isMcuSeriesChanged = False
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackSetMcuDevice()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackSetMcuDevice()
        else:
            pass

    def callbackSetBootDevice( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackSetBootDevice()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackSetBootDevice()
        else:
            pass

    def callbackBootDeviceConfiguration( self, event ):
        if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or \
           self.bootDevice == RTxxx_uidef.kBootDevice_FlexspiNor or \
           self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
            if self.tgt.isSipFlexspiNorDevice:
                self.popupMsgBox(uilang.kMsgLanguageContentDict['bootDeviceInfo_hasOnchipSerialNor'][self.languageIndex])
                return
        if self.checkIfSubWinHasBeenOpened():
            return
        if self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNor or \
           self.bootDevice == RTxxx_uidef.kBootDevice_FlexspiNor or \
           self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
            flexspiNorFrame = ui_cfg_flexspinor.secBootUiCfgFlexspiNor(None)
            if self.bootDevice == RTxxx_uidef.kBootDevice_QuadspiNor:
                flexspiNorFrame.SetTitle(uilang.kSubLanguageContentDict['quadspinor_title'][self.languageIndex])
            else:
                flexspiNorFrame.SetTitle(uilang.kSubLanguageContentDict['flexspinor_title'][self.languageIndex])
            flexspiNorFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_FlexspiNand:
            flexspiNandFrame = ui_cfg_flexspinand.secBootUiFlexspiNand(None)
            flexspiNandFrame.SetTitle(u"FlexSPI NAND Device Configuration")
            flexspiNandFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNor:
            semcNorFrame = ui_cfg_semcnor.secBootUiSemcNor(None)
            semcNorFrame.SetTitle(u"SEMC NOR Device Configuration")
            semcNorFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_SemcNand:
            semcNandFrame = ui_cfg_semcnand.secBootUiCfgSemcNand(None)
            semcNandFrame.SetTitle(uilang.kSubLanguageContentDict['semcnand_title'][self.languageIndex])
            semcNandFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_UsdhcSd:
            usdhcSdFrame = ui_cfg_usdhcsd.secBootUiUsdhcSd(None)
            usdhcSdFrame.SetTitle(uilang.kSubLanguageContentDict['usdhcsd_title'][self.languageIndex])
            usdhcSdFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_UsdhcMmc:
            usdhcMmcFrame = ui_cfg_usdhcmmc.secBootUiUsdhcMmc(None)
            usdhcMmcFrame.SetTitle(uilang.kSubLanguageContentDict['usdhcmmc_title'][self.languageIndex])
            usdhcMmcFrame.Show(True)
        elif self.bootDevice == RTyyyy_uidef.kBootDevice_LpspiNor:
            lpspiNorFrame = ui_cfg_lpspinor.secBootUiCfgLpspiNor(None)
            lpspiNorFrame.SetTitle(uilang.kSubLanguageContentDict['lpspinor_title'][self.languageIndex])
            lpspiNorFrame.Show(True)
        else:
            pass

    def _setUartUsbPort( self ):
        usbIdList = []
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            usbIdList = self.RTyyyy_getUsbid()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            usbIdList = self.RTxxx_getUsbid()
        else:
            pass
        retryToDetectUsb = False
        showError = True
        self.setPortSetupValue(self.connectStage, usbIdList, retryToDetectUsb, showError)

    def callbackSetUartPort( self, event ):
        self._setUartUsbPort()

    def callbackSetUsbhidPort( self, event ):
        self._setUartUsbPort()

    def callbackSetOneStep( self, event ):
        if not self.isToolRunAsEntryMode:
            self.getOneStepConnectMode()
        else:
            self.initOneStepConnectMode()
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_cannotSetOneStep'][self.languageIndex])

    def callbackConnectToDevice( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackConnectToDevice()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackConnectToDevice()
        else:
            pass

    def callbackSetSecureBootType( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackSetSecureBootType()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackSetSecureBootType()
        else:
            pass

    def callbackAllInOneAction( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackAllInOneAction()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackAllInOneAction()
        else:
            pass

    def callbackChangedAppFile( self, event ):
        self.getUserAppFilePath()
        self.setCostTime(0)
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_setSecureBootButtonColor()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_setSecureBootButtonColor()
        else:
            pass

    def callbackSetAppFormat( self, event ):
        self.getUserAppFileFormat()

    def callbackGenImage( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackGenImage()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackGenImage()
        else:
            pass

    def callbackFlashImage( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackFlashImage()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackFlashImage()
        else:
            pass

    def task_doAccessMem( self ):
        while True:
            if self.isAccessMemTaskPending:
                if self.accessMemType == 'ScanFuse':
                    self.scanAllFuseRegions()
                    if self.isSbFileEnabledToGen:
                        self.initSbEfuseBdfileContent()
                elif self.accessMemType == 'BurnFuse':
                    self.burnAllFuseRegions()
                    if self.isSbFileEnabledToGen:
                        self.genSbEfuseImage()
                elif self.accessMemType == 'SaveFuse':
                    self.SaveFuseRegions()
                elif self.accessMemType == 'LoadFuse':
                    self.LoadFuseRegions()
                elif self.accessMemType == 'ReadMem':
                    if self.connectStage == uidef.kConnectStage_ExternalMemory:
                        self.readRamMemory()
                    elif self.connectStage == uidef.kConnectStage_Reset:
                        self.readBootDeviceMemory()
                    else:
                        pass
                elif self.accessMemType == 'EraseMem':
                    self.eraseBootDeviceMemory()
                elif self.accessMemType == 'WriteMem':
                    if self.connectStage == uidef.kConnectStage_ExternalMemory:
                        self.writeRamMemory()
                    elif self.connectStage == uidef.kConnectStage_Reset:
                        self.writeBootDeviceMemory()
                    else:
                        pass
                else:
                    pass
                self.isAccessMemTaskPending = False
                self._stopGaugeTimer()
            time.sleep(1)

    def callbackScanFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'ScanFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackBurnFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'BurnFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackSaveFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'SaveFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackLoadFuse( self, event ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'LoadFuse'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackViewMem( self, event ):
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_callbackViewMem()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_callbackViewMem()
        else:
            pass

    def callbackClearMem( self, event ):
        self.clearMem()

    def _doReadMem( self ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'ReadMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackReadMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doReadMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def _doEraseMem( self ):
        if self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'EraseMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotCfgBootDevice'][self.languageIndex])

    def callbackEraseMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doEraseMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def _doWriteMem( self ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self._startGaugeTimer()
            self.isAccessMemTaskPending = True
            self.accessMemType = 'WriteMem'
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackWriteMem( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doWriteMem()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

    def _doExecuteApp( self ):
        if self.connectStage == uidef.kConnectStage_ExternalMemory or \
           self.connectStage == uidef.kConnectStage_Reset:
            self.executeAppInFlexram()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['connectError_hasnotEnterFl'][self.languageIndex])

    def callbackExecuteApp( self, event ):
        if not self.isToolRunAsEntryMode:
            self._doExecuteApp()
        else:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['operMemError_notAvailUnderEntry'][self.languageIndex])

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
        self._stopTask(g_task_increaseGauge)
        self._stopTask(g_task_accessMem)
        self._stopTask(g_RTyyyy_task_allInOneAction)
        self._stopTask(g_RTxxx_task_allInOneAction)
        self._stopTask(g_RTyyyy_task_showSettedEfuse)
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
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_switchToolRunMode()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_switchToolRunMode()
        else:
            pass
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

    def callbackSetFlashloaderResidentToDefault( self, event ):
        self.setFlashloaderResident()

    def callbackSetFlashloaderResidentToItcm( self, event ):
        self.setFlashloaderResident()

    def callbackSetFlashloaderResidentToDtcm( self, event ):
        self.setFlashloaderResident()

    def callbackSetFlashloaderResidentToOcram( self, event ):
        self.setFlashloaderResident()

    def _doSetLanguage( self ):
        self.setLanguage()
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            self.RTyyyy_setLanguage()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_setLanguage()
        else:
            pass

    def callbackSetLanguageAsEnglish( self, event ):
        self._doSetLanguage()

    def callbackSetLanguageAsChinese( self, event ):
        self._doSetLanguage()

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
                   (uilang.kMsgLanguageContentDict['revisionHistory_v2_0_0'][self.languageIndex]) +
                   (uilang.kMsgLanguageContentDict['revisionHistory_v2_1_0'][self.languageIndex]))
        wx.MessageBox(msgText, uilang.kMsgLanguageContentDict['revisionHistory_title'][self.languageIndex], wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()

    g_main_win = secBootMain(None)
    g_main_win.SetTitle(u"NXP MCU Boot Utility v2.0.0")
    g_main_win.Show()

    g_task_detectUsbhid = threading.Thread(target=g_main_win.task_doDetectUsbhid)
    g_task_detectUsbhid.setDaemon(True)
    g_task_detectUsbhid.start()
    g_task_playSound = threading.Thread(target=g_main_win.task_doPlaySound)
    g_task_playSound.setDaemon(True)
    g_task_playSound.start()
    g_task_increaseGauge = threading.Thread(target=g_main_win.task_doIncreaseGauge)
    g_task_increaseGauge.setDaemon(True)
    g_task_increaseGauge.start()
    g_task_accessMem = threading.Thread(target=g_main_win.task_doAccessMem)
    g_task_accessMem.setDaemon(True)
    g_task_accessMem.start()

    g_RTyyyy_task_allInOneAction = threading.Thread(target=g_main_win.RTyyyy_task_doAllInOneAction)
    g_RTyyyy_task_allInOneAction.setDaemon(True)
    g_RTyyyy_task_allInOneAction.start()
    g_RTxxx_task_allInOneAction = threading.Thread(target=g_main_win.RTxxx_task_doAllInOneAction)
    g_RTxxx_task_allInOneAction.setDaemon(True)
    g_RTxxx_task_allInOneAction.start()

    g_RTyyyy_task_showSettedEfuse = threading.Thread(target=g_main_win.RTyyyy_task_doShowSettedEfuse)
    g_RTyyyy_task_showSettedEfuse.setDaemon(True)
    g_RTyyyy_task_showSettedEfuse.start()

    app.MainLoop()

