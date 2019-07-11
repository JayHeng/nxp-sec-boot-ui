#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import math
import serial.tools.list_ports
import pywinusb.hid
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import secBootWin
from run import rundef
from utils import sound

kRetryDetectTimes = 5

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

        self.flashloaderResident = None
        self._initFlashloaderResident()
        self.setFlashloaderResident()

        self.updateConnectStatus()

        self.mcuSeries = None
        self.mcuDevice = None
        self.bootDevice = None
        self.isMcuSeriesChanged = False
        self._initTargetSetupValue()
        self.setTargetSetupValue()

        self.isUartPortSelected = None
        self.isUsbhidPortSelected = None
        self.uartComPort = None
        self.uartBaudrate = None
        self.usbhidVid = None
        self.usbhidPid = None
        self.isUsbhidConnected = False
        self.usbhidToConnect = [None] * 2
        self._initPortSetupValue()

        self.soundEffectFilenameForTask = None

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

    def _initFlashloaderResident( self ):
        if self.toolCommDict['flashloaderResident'] == None:
            self.m_menuItem_flashloaderResidentDefault.Check(True)
            self.m_menuItem_flashloaderResidentItcm.Check(False)
            self.m_menuItem_flashloaderResidentDtcm.Check(False)
            self.m_menuItem_flashloaderResidentOcram.Check(False)
        elif self.toolCommDict['flashloaderResident'] == 'itcm':
            self.m_menuItem_flashloaderResidentDefault.Check(False)
            self.m_menuItem_flashloaderResidentItcm.Check(True)
            self.m_menuItem_flashloaderResidentDtcm.Check(False)
            self.m_menuItem_flashloaderResidentOcram.Check(False)
        elif self.toolCommDict['flashloaderResident'] == 'dtcm':
            self.m_menuItem_flashloaderResidentDefault.Check(False)
            self.m_menuItem_flashloaderResidentItcm.Check(False)
            self.m_menuItem_flashloaderResidentDtcm.Check(True)
            self.m_menuItem_flashloaderResidentOcram.Check(False)
        elif self.toolCommDict['flashloaderResident'] == 'ocram':
            self.m_menuItem_flashloaderResidentDefault.Check(False)
            self.m_menuItem_flashloaderResidentItcm.Check(False)
            self.m_menuItem_flashloaderResidentDtcm.Check(False)
            self.m_menuItem_flashloaderResidentOcram.Check(True)
        else:
            pass

    def setFlashloaderResident( self ):
        if self.m_menuItem_flashloaderResidentDefault.IsChecked():
            self.flashloaderResident = None
        elif self.m_menuItem_flashloaderResidentItcm.IsChecked():
            self.flashloaderResident = 'itcm'
        elif self.m_menuItem_flashloaderResidentDtcm.IsChecked():
            self.flashloaderResident = 'dtcm'
        elif self.m_menuItem_flashloaderResidentOcram.IsChecked():
            self.flashloaderResident = 'ocram'
        else:
            pass
        self.toolCommDict['flashloaderResident'] = self.flashloaderResident

    def checkIfSubWinHasBeenOpened( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        if not runtimeSettings[0]:
            uivar.setRuntimeSettings(True)
            return False
        else:
            return True

    def _initTargetSetupValue( self ):
        self.m_choice_mcuSeries.Clear()
        self.m_choice_mcuSeries.SetItems(uidef.kMcuSeries_Latest)
        self.toolCommDict['mcuSeries'] = 0
        self.m_choice_mcuSeries.SetSelection(self.toolCommDict['mcuSeries'])

        self.m_choice_mcuDevice.Clear()
        self.m_choice_mcuDevice.SetItems(uidef.kMcuDevice_Latest)
        self.m_choice_mcuDevice.SetSelection(self.toolCommDict['mcuDevice'])

    def refreshBootDeviceList( self ):
        if self.tgt.availableBootDevices != None:
            self.m_choice_bootDevice.Clear()
            self.m_choice_bootDevice.SetItems(self.tgt.availableBootDevices)
            retSel = self.m_choice_bootDevice.FindString(self.bootDevice)
            if retSel != wx.NOT_FOUND:
                self.m_choice_bootDevice.SetSelection(retSel)
            else:
                self.m_choice_bootDevice.SetSelection(0)

    def _detectMcuSeries( self ):
        mcuDevice = self.m_choice_mcuDevice.GetString(self.m_choice_mcuDevice.GetSelection())
        mcuSeries = uidef.kMcuSeries_iMXRT10yy
        if mcuDevice in uidef.kMcuDevice_iMXRT11yy:
            mcuSeries = uidef.kMcuSeries_iMXRT11yy
        elif mcuDevice in uidef.kMcuDevice_iMXRTxxx:
            mcuSeries = uidef.kMcuSeries_iMXRTxxx
        elif mcuDevice in uidef.kMcuDevice_iMXRT10yy:
            mcuSeries = uidef.kMcuSeries_iMXRT10yy
        else:
            pass
        if self.mcuSeries != None and self.mcuSeries != mcuSeries:
            self.isMcuSeriesChanged = True
        self.mcuSeries = mcuSeries

    def setTargetSetupValue( self ):
        self._detectMcuSeries()
        self.mcuDevice = self.m_choice_mcuDevice.GetString(self.m_choice_mcuDevice.GetSelection())
        self.toolCommDict['mcuDevice'] = self.m_choice_mcuDevice.GetSelection()

    def task_doPlaySound( self ):
        while True:
            if self.soundEffectFilenameForTask != None:
                self.playSoundEffect(self.soundEffectFilenameForTask)
                self.soundEffectFilenameForTask = None
            time.sleep(1)

    def _initPortSetupValue( self ):
        if self.toolCommDict['isUsbhidPortSelected']:
            self.m_radioBtn_uart.SetValue(False)
            self.m_radioBtn_usbhid.SetValue(True)
        else:
            self.m_radioBtn_uart.SetValue(True)
            self.m_radioBtn_usbhid.SetValue(False)
        usbIdList = []
        if self.mcuSeries in uidef.kMcuSeries_iMXRTyyyy:
            usbIdList = self.RTyyyy_getUsbid()
        elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            usbIdList = self.RTxxx_getUsbid()
        else:
            pass
        self.setPortSetupValue(uidef.kConnectStage_Rom, usbIdList)

    def task_doDetectUsbhid( self ):
        while True:
            if self.isUsbhidPortSelected:
                self._retryToDetectUsbhidDevice(False)
            time.sleep(1)

    def _retryToDetectUsbhidDevice( self, needToRetry = True ):
        usbVid = [None]
        usbPid = [None]
        self.isUsbhidConnected = False
        retryCnt = 1
        if needToRetry:
            retryCnt = kRetryDetectTimes
        while retryCnt > 0:
            # Auto detect USB-HID device
            hidFilter = pywinusb.hid.HidDeviceFilter(vendor_id = int(self.usbhidToConnect[0], 16), product_id = int(self.usbhidToConnect[1], 16))
            hidDevice = hidFilter.get_devices()
            if (not self.isDymaticUsbDetection) or (len(hidDevice) > 0):
                self.isUsbhidConnected = True
                usbVid[0] = self.usbhidToConnect[0]
                usbPid[0] = self.usbhidToConnect[1]
                break
            retryCnt = retryCnt - 1
            if retryCnt != 0:
                time.sleep(2)
            else:
                usbVid[0] = 'N/A - Not Found'
                usbPid[0] = usbVid[0]
        if self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection()) != usbVid[0] or \
           self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection()) != usbPid[0]:
            self.m_choice_portVid.Clear()
            self.m_choice_portVid.SetItems(usbVid)
            self.m_choice_portVid.SetSelection(0)
            self.m_choice_baudPid.Clear()
            self.m_choice_baudPid.SetItems(usbPid)
            self.m_choice_baudPid.SetSelection(0)

    def adjustPortSetupValue( self, connectStage=uidef.kConnectStage_Rom, usbIdList=[] ):
        self.hasDynamicLableBeenInit = True
        self.isUartPortSelected = self.m_radioBtn_uart.GetValue()
        self.isUsbhidPortSelected = self.m_radioBtn_usbhid.GetValue()
        if self.isUartPortSelected:
            self.m_staticText_portVid.SetLabel(uilang.kMainLanguageContentDict['sText_comPort'][self.languageIndex])
            self.m_staticText_baudPid.SetLabel(uilang.kMainLanguageContentDict['sText_baudrate'][self.languageIndex])
            # Auto detect available ports
            comports = list(serial.tools.list_ports.comports())
            ports = [None] * len(comports)
            for i in range(len(comports)):
                comport = list(comports[i])
                ports[i] = comport[0]
            lastPort = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
            lastBaud = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
            self.m_choice_portVid.Clear()
            self.m_choice_portVid.SetItems(ports)
            if lastPort in ports:
                self.m_choice_portVid.SetSelection(self.m_choice_portVid.FindString(lastPort))
            else:
                self.m_choice_portVid.SetSelection(0)
            baudItems = ['115200']
            if connectStage == uidef.kConnectStage_Rom:
                baudItems = rundef.kUartSpeed_Sdphost
            elif connectStage == uidef.kConnectStage_Flashloader:
                baudItems = rundef.kUartSpeed_Blhost
            else:
                pass
            self.m_choice_baudPid.Clear()
            self.m_choice_baudPid.SetItems(baudItems)
            if lastBaud in baudItems:
                self.m_choice_baudPid.SetSelection(self.m_choice_baudPid.FindString(lastBaud))
            else:
                self.m_choice_baudPid.SetSelection(0)
        elif self.isUsbhidPortSelected:
            self.m_staticText_portVid.SetLabel(uilang.kMainLanguageContentDict['sText_vid'][self.languageIndex])
            self.m_staticText_baudPid.SetLabel(uilang.kMainLanguageContentDict['sText_pid'][self.languageIndex])
            if connectStage == uidef.kConnectStage_Rom:
                self.usbhidToConnect[0] = usbIdList[0]
                self.usbhidToConnect[1] = usbIdList[1]
                self._retryToDetectUsbhidDevice(False)
            elif connectStage == uidef.kConnectStage_Flashloader:
                self.usbhidToConnect[0] = usbIdList[2]
                self.usbhidToConnect[1] = usbIdList[3]
                self._retryToDetectUsbhidDevice(False)
            else:
                pass
        else:
            pass

    def setPortSetupValue( self, connectStage=uidef.kConnectStage_Rom, usbIdList=[], retryToDetectUsb=False, showError=False ):
        self.adjustPortSetupValue(connectStage, usbIdList)
        self.updatePortSetupValue(retryToDetectUsb, showError)

    def updatePortSetupValue( self, retryToDetectUsb=False, showError=False ):
        status = True
        self.isUartPortSelected = self.m_radioBtn_uart.GetValue()
        self.isUsbhidPortSelected = self.m_radioBtn_usbhid.GetValue()
        if self.isUartPortSelected:
            self.uartComPort = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
            self.uartBaudrate = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
        elif self.isUsbhidPortSelected:
            if self.isUsbhidConnected:
                self.usbhidVid = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
                self.usbhidPid = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
            else:
                self._retryToDetectUsbhidDevice(retryToDetectUsb)
                if not self.isUsbhidConnected:
                    status = False
                    if showError:
                        if self.languageIndex == uilang.kLanguageIndex_English:
                            self.popupMsgBox('Cannnot find USB-HID device (vid=%s, pid=%s), Please connect USB cable to your board first!' %(self.usbhidToConnect[0], self.usbhidToConnect[1]))
                        elif self.languageIndex == uilang.kLanguageIndex_Chinese:
                            self.popupMsgBox(u"找不到USB-HID设备 (vid=%s, pid=%s), 请先将USB线连接到板子！" %(self.usbhidToConnect[0], self.usbhidToConnect[1]))
                        else:
                            pass
                else:
                    self.usbhidVid = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
                    self.usbhidPid = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
        else:
            pass
        self.toolCommDict['isUsbhidPortSelected'] = self.isUsbhidPortSelected
        return status

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

    def showPageInMainBootSeqWin(self, pageIndex ):
        if pageIndex != self.m_notebook_imageSeq.GetSelection():
            self.m_notebook_imageSeq.SetSelection(pageIndex)

    def initSecureBootTypeList( self ):
        if self.tgt.availableSecureBootTypes != None:
            self.m_choice_secureBootType.Clear()
            self.m_choice_secureBootType.SetItems(self.tgt.availableSecureBootTypes)
            return True
        else:
            return False

    def refreshSecureBootTypeList( self ):
        if self.initSecureBootTypeList():
            retSel = self.m_choice_secureBootType.FindString(self.secureBootType)
            if retSel != wx.NOT_FOUND:
                self.m_choice_secureBootType.SetSelection(retSel)
            else:
                self.m_choice_secureBootType.SetSelection(0)

    def invalidateStepButtonColor( self, stepName, excuteResult ):
        invalidColor = None
        allInOneSoundEffect = None
        stepSoundEffect = None
        if excuteResult:
            invalidColor = uidef.kBootSeqColor_Invalid
            allInOneSoundEffect = uidef.kSoundEffectFilename_Success
            stepSoundEffect = uidef.kSoundEffectFilename_Progress
        else:
            invalidColor = uidef.kBootSeqColor_Failed
            allInOneSoundEffect = uidef.kSoundEffectFilename_Failure
        if stepName == uidef.kSecureBootSeqStep_AllInOne:
            self.m_button_allInOneAction.SetBackgroundColour( invalidColor )
            self.soundEffectFilenameForTask = allInOneSoundEffect
        else:
            if stepName == uidef.kSecureBootSeqStep_GenCert:
                self.m_button_genCert.SetBackgroundColour( invalidColor )
            elif stepName == uidef.kSecureBootSeqStep_GenImage:
                self.m_button_genImage.SetBackgroundColour( invalidColor )
                if self.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
                    if excuteResult and (not(self.secureBootType in RTyyyy_uidef.kSecureBootType_HwCrypto)):
                        self.showPageInMainBootSeqWin(uidef.kPageIndex_ImageLoadingSequence)
                elif self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
                    self.showPageInMainBootSeqWin(uidef.kPageIndex_ImageLoadingSequence)
            elif stepName == uidef.kSecureBootSeqStep_PrepHwCrypto:
                self.m_button_prepHwCrypto.SetBackgroundColour( invalidColor )
                if excuteResult:
                    self.showPageInMainBootSeqWin(uidef.kPageIndex_ImageLoadingSequence)
            elif stepName == uidef.kSecureBootSeqStep_ProgSrk:
                self.m_button_progSrk.SetBackgroundColour( invalidColor )
            elif stepName == uidef.kSecureBootSeqStep_OperHwCrypto:
                self.m_button_operHwCrypto.SetBackgroundColour( invalidColor )
            elif stepName == uidef.kSecureBootSeqStep_FlashImage:
                self.m_button_flashImage.SetBackgroundColour( invalidColor )
            elif stepName == uidef.kSecureBootSeqStep_ProgDek:
                self.m_button_progDek.SetBackgroundColour( invalidColor )
            else:
                pass
            if stepSoundEffect != None:
                self.playSoundEffect(stepSoundEffect)
        self.Refresh()

    def resetSecureBootSeqColor( self ):
        self.resetCertificateColor()
        self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_genImage1_browseApp.Enable( False )
        self.m_panel_genImage2_habCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_genImage2_habCryptoAlgo.Enable( False )
        self.m_panel_genImage3_enableCertForHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_genImage3_enableCertForHwCrypto.Enable( False )
        self.m_button_genImage.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_genImage.Enable( False )
        self.resetKeyStorageRegionColor()
        self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_flashImage1_showImage.Enable( False )
        self.m_button_flashImage.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_flashImage.Enable( False )
        self.m_panel_progDek1_showHabDek.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_progDek1_showHabDek.Enable( False )
        self.m_textCtrl_habDek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_textCtrl_habDek128bit.Enable( False )
        self.m_button_progDek.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_progDek.Enable( False )
        self.Refresh()

    def resetKeyStorageRegionColor( self ):
        self.m_panel_prepHwCrypto1_hwCryptoKeyRegion.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_prepHwCrypto1_hwCryptoKeyRegion.Enable( False )
        self.m_panel_prepHwCrypto2_hwCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_prepHwCrypto2_hwCryptoAlgo.Enable( False )
        self.m_button_prepHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_prepHwCrypto.Enable( False )
        self.m_panel_operHwCrypto1_hwCryptoKeyInfo.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_operHwCrypto1_hwCryptoKeyInfo.Enable( False )
        self.m_panel_operHwCrypto2_showGp4Dek.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_operHwCrypto2_showGp4Dek.Enable( False )
        self.m_textCtrl_gp4Dek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_textCtrl_gp4Dek128bit.Enable( False )
        self.m_panel_operHwCrypto3_showSwgp2Dek.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_operHwCrypto3_showSwgp2Dek.Enable( False )
        self.m_textCtrl_swgp2Dek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_textCtrl_swgp2Dek128bit.Enable( False )
        self.m_button_operHwCrypto.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_operHwCrypto.Enable( False )
        self.Refresh()

    def resetCertificateColor( self ):
        self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_textCtrl_serial.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_textCtrl_keyPass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_panel_doAuth1_certInput.Enable( False )
        self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_doAuth2_certFmt.Enable( False )
        self.m_button_genCert.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_genCert.Enable( False )
        self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_progSrk1_showSrk.Enable( False )
        self.m_textCtrl_srk256bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_textCtrl_srk256bit.Enable( False )
        self.m_button_progSrk.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_button_progSrk.Enable( False )
        self.Refresh()

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

    def getUserAppFilePath( self ):
        appPath = self.m_filePicker_appPath.GetPath()
        self.toolCommDict['appFilename'] = appPath.encode("utf-8")
        return appPath.encode('utf-8').encode("gbk")

    def _setUserBinaryBaseField( self ):
        txt = self.m_choice_appFormat.GetString(self.m_choice_appFormat.GetSelection())
        if txt == uidef.kAppImageFormat_AutoDetect or txt == uidef.kAppImageFormat_RawBinary:
            self.m_textCtrl_appBaseAddr.Enable(True)
        else:
            self.m_textCtrl_appBaseAddr.Enable(False)

    def getUserAppFileFormat( self ):
        self.toolCommDict['appFormat'] = self.m_choice_appFormat.GetSelection()
        self._setUserBinaryBaseField()
        return self.m_choice_appFormat.GetString(self.m_choice_appFormat.GetSelection())

    def getUserBinaryBaseAddress( self ):
        self.toolCommDict['appBinBaseAddr'] = self.m_textCtrl_appBaseAddr.GetLineText(0)
        return self.getVal32FromHexText(self.m_textCtrl_appBaseAddr.GetLineText(0))

    def convertLongIntHexText( self, hexText ):
        lastStr = hexText[len(hexText) - 1]
        if lastStr == 'l' or lastStr == 'L':
            return hexText[0:len(hexText) - 1]
        else:
            return hexText

    def getVal32FromHexText( self, hexText ):
        status = False
        val32 = None
        if len(hexText) > 2 and hexText[0:2] == '0x':
            try:
                val32 = int(hexText[2:len(hexText)], 16)
                status = True
            except:
                pass
        if not status:
            self.popupMsgBox(uilang.kMsgLanguageContentDict['inputError_illegalFormat'][self.languageIndex])
        return status, val32

    def getComMemStartAddress( self ):
        return self.getVal32FromHexText(self.m_textCtrl_memStart.GetLineText(0))

    def getComMemByteLength( self ):
        return self.getVal32FromHexText(self.m_textCtrl_memLength.GetLineText(0))

    def getComMemBinFile( self ):
        memBinFile = self.m_filePicker_memBinFile.GetPath()
        return memBinFile.encode('utf-8').encode("gbk")

    def needToSaveReadbackImageData( self ):
        return self.m_checkBox_saveImageData.GetValue()

    def getImageDataFileToSave( self ):
        savedBinFile = self.m_filePicker_savedBinFile.GetPath()
        return savedBinFile.encode('utf-8').encode("gbk")

    def setImageDataFilePath( self, filePath ):
        self.m_filePicker_savedBinFile.SetPath(filePath)

    def printMem( self , memStr, strColor=uidef.kMemBlockColor_Padding ):
        self.m_textCtrl_bootDeviceMem.SetDefaultStyle(wx.TextAttr(strColor, uidef.kMemBlockColor_Background))
        self.m_textCtrl_bootDeviceMem.AppendText(memStr + "\n")

    def clearMem( self ):
        self.m_textCtrl_bootDeviceMem.Clear()

    def showImageLayout( self , imgPath ):
        self.m_bitmap_bootableImage.SetBitmap(wx.Bitmap( imgPath, wx.BITMAP_TYPE_ANY ))

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
        self.m_menu_tools.SetLabel(self.m_menu_tools.FindItem(uilang.kMainLanguageContentDict['subMenu_flashloaderResident'][lastIndex]), uilang.kMainLanguageContentDict['subMenu_flashloaderResident'][langIndex])
        self.m_menuItem_flashloaderResidentDefault.SetItemLabel(uilang.kMainLanguageContentDict['mItem_flashloaderResidentDefault'][langIndex])
        self.m_menuItem_flashloaderResidentItcm.SetItemLabel(uilang.kMainLanguageContentDict['mItem_flashloaderResidentItcm'][langIndex])
        self.m_menuItem_flashloaderResidentDtcm.SetItemLabel(uilang.kMainLanguageContentDict['mItem_flashloaderResidentDtcm'][langIndex])
        self.m_menuItem_flashloaderResidentOcram.SetItemLabel(uilang.kMainLanguageContentDict['mItem_flashloaderResidentOcram'][langIndex])
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
