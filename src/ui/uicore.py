#! /usr/bin/env python
import wx
import sys
import os
import serial.tools.list_ports
import uidef
import uivar
import ui_semcnand
import ui_semcnor
import ui_flexspinor
import ui_flexspinand
import ui_sd
import ui_emmc
sys.path.append(os.path.abspath("../.."))
from gui import secBootWin
sys.path.append(os.path.abspath(".."))
from run import rundef

g_semcNandOpt = 0xD0000000
g_semcNandFcbOpt = 0x00000000
g_semcNandImageInfo = [None] * 8

class secBootUi(secBootWin.secBootWin):


    def __init__(self, parent):
        secBootWin.secBootWin.__init__(self, parent)
        self.m_bitmap_nxp.SetBitmap(wx.Bitmap( u"../img/logo_nxp.png", wx.BITMAP_TYPE_ANY ))
        self.updateConnectStatus()

        self.mcuSeries = None
        self.mcuDevice = None
        self.bootDevice = None
        self.updateTargetSetupValue()
        uivar.initVar()

        self.isUartPortSelected = None
        self.isUsbhidPortSelected = None
        self.uartComPort = None
        self.uartBaudrate = None
        self.usbhidVid = None
        self.usbhidPid = None
        self._initPortSetupValue()

        self.secureBootType = None
        self.keyStorageRegion = None
        self._initSecureBootSeqColor()



    def runBootDeviceConfiguration( self ):
        if self.bootDevice == uidef.kBootDevice_FlexspiNor:
            if uivar.global_count[1] == 0:
                global flexspiNorFrame
                flexspiNorFrame = ui_flexspinor.secBootUiFlexspiNor(None)
                flexspiNorFrame.SetTitle(u"Flexspi NOR Device Configuration")
                flexspiNorFrame.Show(True)
            else:
                flexspiNorFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_FlexspiNand:
            if uivar.global_count[2] == 0:
                global flexspiNandFrame
                flexspiNandFrame = ui_flexspinand.secBootUiFlexspiNand(None)
                flexspiNandFrame.SetTitle(u"Flexspi NAND Device Configuration")
                flexspiNandFrame.Show(True)
            else:
                flexspiNandFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_SemcNor:
            if uivar.global_count[3] == 0:
                global semcNorFrame
                semcNorFrame = ui_semcnor.secBootUiSemcNor(None)
                semcNorFrame.SetTitle(u"SEMC NOR Device Configuration")
                semcNorFrame.Show(True)
            else:
                semcNorFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_SemcNand:
            if uivar.global_count[4] == 0:
                global semcNandFrame
                semcNandFrame = ui_semcnand.secBootUiSemcNand(None)
                semcNandFrame.SetTitle(u"SEMC NAND Device Configuration")
                semcNandFrame.Show(True)
            else:
                semcNandFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_UsdhcSd:
            if uivar.global_count[5] == 0:
                global usdhcSdFrame
                usdhcSdFrame = ui_sd.secBootUiUsdhcSd(None)
                usdhcSdFrame.SetTitle(u"Usdhc Sd Device Configuration")
                usdhcSdFrame.Show(True)
            else:
                usdhcSdFrame.Show(True)
        elif self.bootDevice == uidef.kBootDevice_UsdhcMmc:
            if uivar.global_count[6] == 0:
                global usdhcMmcFrame
                usdhcMmcFrame = ui_emmc.secBootUiUsdhcMmc(None)
                usdhcMmcFrame.SetTitle(u"Usdhc Mmc Device Configuration")
                usdhcMmcFrame.Show(True)
            else:
                usdhcMmcFrame.Show(True)
        else:
            pass

    def updateTargetSetupValue( self ):
        self.mcuSeries = self.m_choice_mcuSeries.GetString(self.m_choice_mcuSeries.GetSelection())
        self.mcuDevice = self.m_choice_mcuDevice.GetString(self.m_choice_mcuDevice.GetSelection())
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())

    def _initPortSetupValue( self ):
        self.m_radioBtn_uart.SetValue(True)
        self.m_radioBtn_usbhid.SetValue(False)
        self.setPortSetupValue()

    def adjustPortSetupValue( self, connectStage=uidef.kConnectStage_Rom, usbIdList=[] ):
        self.isUartPortSelected = self.m_radioBtn_uart.GetValue()
        self.isUsbhidPortSelected = self.m_radioBtn_usbhid.GetValue()
        self.m_choice_portVid.Clear()
        self.m_choice_baudPid.Clear()
        if self.isUartPortSelected:
            self.m_staticText_portVid.SetLabel('COM Port:')
            self.m_staticText_baudPid.SetLabel('Baudrate:')
            # Auto detect available ports
            comports = list(serial.tools.list_ports.comports())
            ports = [None] * len(comports)
            for i in range(len(comports)):
                comport = list(comports[i])
                ports[i] = comport[0]
            self.m_choice_portVid.SetItems(ports)
            if connectStage == uidef.kConnectStage_Rom:
                self.m_choice_baudPid.SetItems(rundef.kUartSpeed_Sdphost)
            elif connectStage == uidef.kConnectStage_Flashloader:
                self.m_choice_baudPid.SetItems(rundef.kUartSpeed_Blhost)
            else:
                pass
        elif self.isUsbhidPortSelected:
            self.m_staticText_portVid.SetLabel('VID:')
            self.m_staticText_baudPid.SetLabel('PID:')
            usbVid = [None]
            usbPid = [None]
            if connectStage == uidef.kConnectStage_Rom:
                usbVid[0] = usbIdList[0]
                usbPid[0] = usbIdList[1]
                self.m_choice_portVid.SetItems(usbVid)
                self.m_choice_baudPid.SetItems(usbPid)
            elif connectStage == uidef.kConnectStage_Flashloader:
                usbVid[0] = usbIdList[2]
                usbPid[0] = usbIdList[3]
                self.m_choice_portVid.SetItems(usbVid)
                self.m_choice_baudPid.SetItems(usbPid)
            else:
                pass
        else:
            pass
        self.m_choice_portVid.SetSelection(0)
        self.m_choice_baudPid.SetSelection(0)

    def setPortSetupValue( self, connectStage=uidef.kConnectStage_Rom, usbIdList=[] ):
        self.adjustPortSetupValue(connectStage, usbIdList)
        self.updatePortSetupValue()

    def updatePortSetupValue( self ):
        self.isUartPortSelected = self.m_radioBtn_uart.GetValue()
        self.isUsbhidPortSelected = self.m_radioBtn_usbhid.GetValue()
        if self.isUartPortSelected:
            self.uartComPort = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
            self.uartBaudrate = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
        elif self.isUsbhidPortSelected:
            self.usbhidVid = self.m_choice_portVid.GetString(self.m_choice_portVid.GetSelection())
            self.usbhidPid = self.m_choice_baudPid.GetString(self.m_choice_baudPid.GetSelection())
        else:
            pass

    def updateConnectStatus( self, color='black' ):
        if color == 'black':
            self.m_button_connect.SetLabel('Connect to ROM')
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_black.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'yellow':
            self.m_button_connect.SetLabel('Connect to Flashloader')
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_yellow.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'green':
            self.m_button_connect.SetLabel('Configure boot device')
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_green.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'blue':
            self.m_button_connect.SetLabel('Reset device')
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_blue.png", wx.BITMAP_TYPE_ANY ))
        elif color == 'red':
            self.m_button_connect.SetLabel('Reconnect')
            self.m_bitmap_connectLed.SetBitmap(wx.Bitmap( u"../img/led_red.png", wx.BITMAP_TYPE_ANY ))
        else:
            pass

    def _initSecureBootSeqColor ( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
        self.setSecureBootSeqColor()

    def _resetSecureBootSeqColor( self ):
        self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_genImage2_habCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_progDek1_showDek.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self._resetKeyStorageRegionColor()
        self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.Refresh()

    def _resetKeyStorageRegionColor( self ):
        self.m_panel_prepBee1_beeKeyRegion.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_prepBee2_beeKeyInput.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_prepBee3_advKeySettings.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_prepBee4_beeCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_operBeeKey1_readOtpmk.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.m_panel_operBeeKey2_progBeeKey.SetBackgroundColour( uidef.kBootSeqColor_Invalid )
        self.Refresh()

    def setSecureBootSeqColor( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self._resetSecureBootSeqColor()
        if self.secureBootType == uidef.kSecureBootType_Development:
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.secureBootType == uidef.kSecureBootType_HabAuth:
            self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.secureBootType == uidef.kSecureBootType_HabCrypto:
            self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_genImage2_habCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_progDek1_showDek.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
        elif self.secureBootType == uidef.kSecureBootType_BeeCrypto:
            self.m_panel_doAuth1_certInput.SetBackgroundColour( uidef.kBootSeqColor_Inactive )
            self.m_panel_doAuth2_certFmt.SetBackgroundColour( uidef.kBootSeqColor_Inactive )
            self.m_panel_progSrk1_showSrk.SetBackgroundColour( uidef.kBootSeqColor_Inactive )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.setKeyStorageRegionColor()
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
        else:
            pass
        self.Refresh()

    def setKeyStorageRegionColor( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        if self.secureBootType == uidef.kSecureBootType_BeeCrypto:
            self._resetKeyStorageRegionColor()
            self.keyStorageRegion = self.m_choice_keyStorageRegion.GetString(self.m_choice_keyStorageRegion.GetSelection())
            self.m_panel_prepBee1_beeKeyRegion.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_panel_prepBee4_beeCryptoAlgo.SetBackgroundColour( uidef.kBootSeqColor_Active )
            if self.keyStorageRegion == uidef.kKeyStorageRegion_Optmk:
                self.m_panel_operBeeKey1_readOtpmk.SetBackgroundColour( uidef.kBootSeqColor_Active )
            elif self.keyStorageRegion == uidef.kKeyStorageRegion_Gp4 or keyStorageRegion == uidef.kKeyStorageRegion_SwGp2:
                self.m_panel_prepBee2_beeKeyInput.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_operBeeKey2_progBeeKey.SetBackgroundColour( uidef.kBootSeqColor_Active )
            elif self.keyStorageRegion == uidef.kKeyStorageRegion_Gp4SwGp2:
                self.m_panel_prepBee3_advKeySettings.SetBackgroundColour( uidef.kBootSeqColor_Active )
                self.m_panel_operBeeKey2_progBeeKey.SetBackgroundColour( uidef.kBootSeqColor_Active )
            else:
                pass
        self.Refresh()

