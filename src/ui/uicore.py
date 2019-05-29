#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import math
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import secBootWin
from utils import sound

s_isGaugeWorking = False
s_curGauge = 0
s_maxGauge = 0
s_gaugeIntervalSec = 1

class secBootUi(secBootWin.secBootWin):

    def __init__(self, parent):
        secBootWin.secBootWin.__init__(self, parent)
        self.m_bitmap_nxp.SetBitmap(wx.Bitmap( u"../img/logo_nxp.png", wx.BITMAP_TYPE_ANY ))

        self.exeBinRoot = os.getcwd()
        self.exeTopRoot = os.path.dirname(self.exeBinRoot)
        exeMainFile = os.path.join(self.exeTopRoot, 'src', 'main.py')
        if not os.path.isfile(exeMainFile):
            self.exeTopRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        uivar.setRuntimeSettings(None, self.exeTopRoot)
        uivar.initVar(os.path.join(self.exeTopRoot, 'bin', 'nsb_settings.json'))
        toolCommDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Tool)
        self.toolCommDict = toolCommDict.copy()

        self.logFolder = os.path.join(self.exeTopRoot, 'gen', 'log_file')
        self.logFilename = os.path.join(self.exeTopRoot, 'gen', 'log_file', 'log.txt')

        self.connectStatusColor = None
        self.hasDynamicLableBeenInit = False

        self.languageIndex = 0
        self._initLanguage()
        self.setLanguage()

        self.isToolRunAsEntryMode = None
        self._initToolRunMode()
        self.setToolRunMode()

        self.isDymaticUsbDetection = None
        self._initUsbDetection()
        self.setUsbDetection()

        self.isQuietSoundEffect = None
        self._initSoundEffect()
        self.setSoundEffect()

        self.isSbFileEnabledToGen = None
        self._initGenSbFile()
        self.setGenSbFile()

        self.isAutomaticImageReadback = None
        self._initImageReadback()
        self.setImageReadback()

        self.updateConnectStatus()

        self.mcuSeries = None
        self.mcuDevice = None
        self.bootDevice = None
        self._initTargetSetupValue()
        self.setTargetSetupValue()

        self.isOneStepConnectMode = None
        self.initOneStepConnectMode()

    def _initToolRunMode( self ):
        if self.toolCommDict['isToolRunAsEntryMode']:
            self.m_menuItem_runModeEntry.Check(True)
            self.m_menuItem_runModeMaster.Check(False)
        else:
            self.m_menuItem_runModeEntry.Check(False)
            self.m_menuItem_runModeMaster.Check(True)

    def setToolRunMode( self ):
        self.isToolRunAsEntryMode = self.m_menuItem_runModeEntry.IsChecked()
        self.toolCommDict['isToolRunAsEntryMode'] = self.isToolRunAsEntryMode

    def _initUsbDetection( self ):
        if self.toolCommDict['isDymaticUsbDetection']:
            self.m_menuItem_usbDetectionDynamic.Check(True)
            self.m_menuItem_usbDetectionStatic.Check(False)
        else:
            self.m_menuItem_usbDetectionDynamic.Check(False)
            self.m_menuItem_usbDetectionStatic.Check(True)

    def setUsbDetection( self ):
        self.isDymaticUsbDetection = self.m_menuItem_usbDetectionDynamic.IsChecked()
        self.toolCommDict['isDymaticUsbDetection'] = self.isDymaticUsbDetection

    def _initSoundEffect( self ):
        if self.toolCommDict['isQuietSoundEffect']:
            self.m_menuItem_soundEffectQuiet.Check(True)
            self.m_menuItem_soundEffectMario.Check(False)
        else:
            self.m_menuItem_soundEffectQuiet.Check(False)
            self.m_menuItem_soundEffectMario.Check(True)

    def setSoundEffect( self ):
        self.isQuietSoundEffect = self.m_menuItem_soundEffectQuiet.IsChecked()
        self.toolCommDict['isQuietSoundEffect'] = self.isQuietSoundEffect
        uivar.setRuntimeSettings(None, None, self.isQuietSoundEffect)

    def playSoundEffect( self, soundFilename ):
        sound.playSoundEffect(self.exeTopRoot, self.isQuietSoundEffect, soundFilename)

    def _initGenSbFile( self ):
        if self.toolCommDict['isSbFileEnabledToGen']:
            self.m_menuItem_genSbFileYes.Check(True)
            self.m_menuItem_genSbFileNo.Check(False)
        else:
            self.m_menuItem_genSbFileYes.Check(False)
            self.m_menuItem_genSbFileNo.Check(True)

    def setGenSbFile( self ):
        self.isSbFileEnabledToGen = self.m_menuItem_genSbFileYes.IsChecked()
        self.toolCommDict['isSbFileEnabledToGen'] = self.isSbFileEnabledToGen

    def _initImageReadback( self ):
        if self.toolCommDict['isAutomaticImageReadback']:
            self.m_menuItem_imageReadbackAutomatic.Check(True)
            self.m_menuItem_imageReadbackManual.Check(False)
        else:
            self.m_menuItem_imageReadbackAutomatic.Check(False)
            self.m_menuItem_imageReadbackManual.Check(True)

    def setImageReadback( self ):
        self.isAutomaticImageReadback = self.m_menuItem_imageReadbackAutomatic.IsChecked()
        self.toolCommDict['isAutomaticImageReadback'] = self.isAutomaticImageReadback

    def _initTargetSetupValue( self ):
        self.m_choice_mcuSeries.Clear()
        self.m_choice_mcuSeries.SetItems(uidef.kMcuSeries_Latest)
        self.m_choice_mcuSeries.SetSelection(self.toolCommDict['mcuSeries'])

    def setTargetSetupValue( self ):
        self.mcuSeries = self.m_choice_mcuSeries.GetString(self.m_choice_mcuSeries.GetSelection())
        self.toolCommDict['mcuSeries'] = self.m_choice_mcuSeries.GetSelection()

    def updateConnectStatus( self, color='black' ):
        self.connectStatusColor = color
        if color == 'black':
            self.m_button_connect.SetLabel(uilang.kMainLanguageContentDict['button_connect_black'][self.languageIndex])
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_black.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'yellow':
            self.m_button_connect.SetLabel(uilang.kMainLanguageContentDict['button_connect_yellow'][self.languageIndex])
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_yellow.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'green':
            self.m_button_connect.SetLabel(uilang.kMainLanguageContentDict['button_connect_green'][self.languageIndex])
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_green.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'blue':
            self.m_button_connect.SetLabel(uilang.kMainLanguageContentDict['button_connect_blue'][self.languageIndex])
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_blue.png", wx.BITMAP_TYPE_ANY ))
            self.playSoundEffect(uidef.kSoundEffectFilename_Progress)
        elif color == 'red':
            self.m_button_connect.SetLabel(uilang.kMainLanguageContentDict['button_connect_red'][self.languageIndex])
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_red.png", wx.BITMAP_TYPE_ANY ))
        else:
            pass

    def initOneStepConnectMode( self ):
        self.m_checkBox_oneStepConnect.SetValue(self.toolCommDict['isOneStepChecked'])
        self.getOneStepConnectMode()

    def getOneStepConnectMode( self ):
        self.isOneStepConnectMode = self.m_checkBox_oneStepConnect.GetValue()
        self.toolCommDict['isOneStepChecked'] = self.isOneStepConnectMode

    def enableOneStepForEntryMode( self ):
        if self.isToolRunAsEntryMode:
            self.m_checkBox_oneStepConnect.SetValue(True)
            self.toolCommDict['isOneStepChecked'] = True

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr.encode('utf-8'))
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def printLog( self, logStr ):
        try:
            self.m_textCtrl_log.write(logStr + "\n")
        except:
            pass

    def clearLog( self ):
        self.m_textCtrl_log.Clear()

    def saveLog( self ):
        self.m_textCtrl_log.SaveFile(self.logFilename)
        msgText = (('Log is saved in file: ' + self.logFilename + ' \n').encode('utf-8'))
        wx.MessageBox(msgText, "Log Info", wx.OK | wx.ICON_INFORMATION)

    def task_doIncreaseGauge( self ):
        while True:
            self._increaseGauge()
            global s_gaugeIntervalSec
            time.sleep(s_gaugeIntervalSec)

    def _increaseGauge( self ):
        global s_isGaugeWorking
        global s_curGauge
        global s_maxGauge
        global s_gaugeIntervalSec
        if s_isGaugeWorking:
            gaugePercentage = s_curGauge * 1.0 / s_maxGauge
            if gaugePercentage <= 0.9:
                s_gaugeIntervalSec = int(gaugePercentage  / 0.1) * 0.5 + 0.5
                self.m_gauge_action.SetValue(s_curGauge)
                s_curGauge += 1
            self.updateCostTime()

    def initGauge( self ):
        global s_isGaugeWorking
        global s_curGauge
        global s_maxGauge
        global s_gaugeIntervalSec
        s_isGaugeWorking = True
        s_curGauge = 0
        s_gaugeIntervalSec = 0.5
        s_maxGauge = self.m_gauge_action.GetRange()
        self.m_gauge_action.SetValue(s_curGauge)

    def deinitGauge( self ):
        global s_isGaugeWorking
        global s_curGauge
        global s_maxGauge
        global s_gaugeIntervalSec
        s_isGaugeWorking = False
        s_curGauge = s_maxGauge
        s_gaugeIntervalSec = 1
        self.m_gauge_action.SetValue(s_maxGauge)

    def printDeviceStatus( self, statusStr ):
        self.m_textCtrl_deviceStatus.write(statusStr + "\n")

    def clearDeviceStatus( self ):
        self.m_textCtrl_deviceStatus.Clear()

    def _initLanguage( self ):
        if self.toolCommDict['isEnglishLanguage']:
            self.m_menuItem_english.Check(True)
            self.m_menuItem_chinese.Check(False)
        else:
            self.m_menuItem_english.Check(False)
            self.m_menuItem_chinese.Check(True)

    def _getLastLangIndex( self ):
        label = self.m_staticText_mcuSeries.GetLabel()
        labelList = uilang.kMainLanguageContentDict['sText_mcuSeries'][:]
        for index in range(len(labelList)):
            if label == labelList[index]:
                return index
        return 0

    def setLanguage( self ):
        isEnglishLanguage = self.m_menuItem_english.IsChecked()
        self.toolCommDict['isEnglishLanguage'] = isEnglishLanguage
        lastIndex = self._getLastLangIndex()
        langIndex = 0
        if isEnglishLanguage:
            langIndex = uilang.kLanguageIndex_English
        else:
            langIndex = uilang.kLanguageIndex_Chinese
        self.languageIndex = langIndex
        uivar.setRuntimeSettings(None, None, None, self.languageIndex)
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_File, uilang.kMainLanguageContentDict['menu_file'][langIndex])
        self.m_menuItem_exit.SetItemLabel(uilang.kMainLanguageContentDict['mItem_exit'][langIndex])
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_Edit, uilang.kMainLanguageContentDict['menu_edit'][langIndex])
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_View, uilang.kMainLanguageContentDict['menu_view'][langIndex])
        # Hard way to set label for submenu
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_Tools, uilang.kMainLanguageContentDict['menu_tools'][langIndex])
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_runMode'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_runMode'][langIndex])
        self.m_menuItem_runModeEntry.SetItemLabel(uilang.kMainLanguageContentDict['mItem_runModeEntry'][langIndex])
        self.m_menuItem_runModeMaster.SetItemLabel(uilang.kMainLanguageContentDict['mItem_runModeMaster'][langIndex])
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_usbDetection'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_usbDetection'][langIndex])
        self.m_menuItem_usbDetectionDynamic.SetItemLabel(uilang.kMainLanguageContentDict['mItem_usbDetectionDynamic'][langIndex])
        self.m_menuItem_usbDetectionStatic.SetItemLabel(uilang.kMainLanguageContentDict['mItem_usbDetectionStatic'][langIndex])
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_soundEffect'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_soundEffect'][langIndex])
        self.m_menuItem_soundEffectMario.SetItemLabel(uilang.kMainLanguageContentDict['mItem_soundEffectMario'][langIndex])
        self.m_menuItem_soundEffectQuiet.SetItemLabel(uilang.kMainLanguageContentDict['mItem_soundEffectQuiet'][langIndex])
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_genSbFile'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_genSbFile'][langIndex])
        self.m_menuItem_genSbFileYes.SetItemLabel(uilang.kMainLanguageContentDict['mItem_genSbFileYes'][langIndex])
        self.m_menuItem_genSbFileNo.SetItemLabel(uilang.kMainLanguageContentDict['mItem_genSbFileNo'][langIndex])
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_imageReadback'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_imageReadback'][langIndex])
        self.m_menuItem_imageReadbackAutomatic.SetItemLabel(uilang.kMainLanguageContentDict['mItem_imageReadbackAutomatic'][langIndex])
        self.m_menuItem_imageReadbackManual.SetItemLabel(uilang.kMainLanguageContentDict['mItem_imageReadbackManual'][langIndex])
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_Window, uilang.kMainLanguageContentDict['menu_window'][langIndex])
        self.m_menubar.SetMenuLabel(uilang.kMenuPosition_Help, uilang.kMainLanguageContentDict['menu_help'][langIndex])
        self.m_menuItem_homePage.SetItemLabel(uilang.kMainLanguageContentDict['mItem_homePage'][langIndex])
        self.m_menuItem_aboutAuthor.SetItemLabel(uilang.kMainLanguageContentDict['mItem_aboutAuthor'][langIndex])
        self.m_menuItem_contributors.SetItemLabel(uilang.kMainLanguageContentDict['mItem_contributors'][langIndex])
        self.m_menuItem_specialThanks.SetItemLabel(uilang.kMainLanguageContentDict['mItem_specialThanks'][langIndex])
        self.m_menuItem_revisionHistory.SetItemLabel(uilang.kMainLanguageContentDict['mItem_revisionHistory'][langIndex])

        self.m_notebook_targetSetup.SetPageText(0, uilang.kMainLanguageContentDict['panel_targetSetup'][langIndex])
        self.m_staticText_mcuSeries.SetLabel(uilang.kMainLanguageContentDict['sText_mcuSeries'][langIndex])
        self.m_staticText_mcuDevice.SetLabel(uilang.kMainLanguageContentDict['sText_mcuDevice'][langIndex])
        self.m_staticText_bootDevice.SetLabel(uilang.kMainLanguageContentDict['sText_bootDevice'][langIndex])
        self.m_button_bootDeviceConfiguration.SetLabel(uilang.kMainLanguageContentDict['button_bootDeviceConfiguration'][langIndex])
        self.m_button_deviceConfigurationData.SetLabel(uilang.kMainLanguageContentDict['button_deviceConfigurationData'][langIndex])

        self.m_notebook_portSetup.SetPageText(0, uilang.kMainLanguageContentDict['panel_portSetup'][langIndex])
        self.m_radioBtn_uart.SetLabel(uilang.kMainLanguageContentDict['radioBtn_uart'][langIndex])
        self.m_radioBtn_usbhid.SetLabel(uilang.kMainLanguageContentDict['radioBtn_usbhid'][langIndex])
        if self.hasDynamicLableBeenInit:
            if self.isUartPortSelected:
                self.m_staticText_portVid.SetLabel(uilang.kMainLanguageContentDict['sText_comPort'][langIndex])
                self.m_staticText_baudPid.SetLabel(uilang.kMainLanguageContentDict['sText_baudrate'][langIndex])
            elif self.isUsbhidPortSelected:
                self.m_staticText_portVid.SetLabel(uilang.kMainLanguageContentDict['sText_vid'][langIndex])
                self.m_staticText_baudPid.SetLabel(uilang.kMainLanguageContentDict['sText_pid'][langIndex])
            else:
                pass
        self.m_checkBox_oneStepConnect.SetLabel(uilang.kMainLanguageContentDict['checkBox_oneStepConnect'][langIndex])
        if self.connectStatusColor != None:
            self.updateConnectStatus(self.connectStatusColor)

        self.m_notebook_deviceStatus.SetPageText(0, uilang.kMainLanguageContentDict['panel_deviceStatus'][langIndex])

        self.m_staticText_secureBootType.SetLabel(uilang.kMainLanguageContentDict['sText_secureBootType'][langIndex])
        self.m_button_allInOneAction.SetLabel(uilang.kMainLanguageContentDict['button_allInOneAction'][langIndex])

        self.m_notebook_bootLog.SetPageText(0, uilang.kMainLanguageContentDict['panel_log'][langIndex])
        self.m_button_clearLog.SetLabel(uilang.kMainLanguageContentDict['button_clearLog'][langIndex])
        self.m_button_saveLog.SetLabel(uilang.kMainLanguageContentDict['button_SaveLog'][langIndex])

    def setCostTime( self, costTimeSec ):
        minValueStr = '00'
        secValueStr = '00'
        millisecValueStr = '000'
        if costTimeSec != 0:
            costTimeSecMod = math.modf(costTimeSec)
            minValue = int(costTimeSecMod[1] / 60)
            if minValue < 10:
                minValueStr = '0' + str(minValue)
            elif minValue <= 59:
                minValueStr = str(minValue)
            else:
                minValueStr = 'xx'
            secValue = int(costTimeSecMod[1]) % 60
            if secValue < 10:
                secValueStr = '0' + str(secValue)
            else:
                secValueStr = str(secValue)
            millisecValue = int(costTimeSecMod[0] * 1000)
            if millisecValue < 10:
                millisecValueStr = '00' + str(millisecValue)
            elif millisecValue < 100:
                millisecValueStr = '0' + str(millisecValue)
            else:
                millisecValueStr = str(millisecValue)
        self.m_staticText_costTime.SetLabel(' ' + minValueStr + ':' + secValueStr + '.' + millisecValueStr)

    def updateCostTime( self ):
        curTime = time.time()
        self.setCostTime(curTime - self.lastTime)
