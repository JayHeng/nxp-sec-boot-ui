# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class secBootWin
###########################################################################

class secBootWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NXP MCU Boot Utility", pos = wx.DefaultPosition, size = wx.Size( 1078,730 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_exit )

		self.m_menubar.Append( self.m_menu_file, u"File" )

		self.m_menu_edit = wx.Menu()
		self.m_menubar.Append( self.m_menu_edit, u"Edit" )

		self.m_menu_view = wx.Menu()
		self.m_menu_language = wx.Menu()
		self.m_menuItem_english = wx.MenuItem( self.m_menu_language, wx.ID_ANY, u"EN - English", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_language.Append( self.m_menuItem_english )

		self.m_menuItem_chinese = wx.MenuItem( self.m_menu_language, wx.ID_ANY, u"ZH - 简体中文", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_language.Append( self.m_menuItem_chinese )

		self.m_menu_view.AppendSubMenu( self.m_menu_language, u"Language/语言" )

		self.m_menubar.Append( self.m_menu_view, u"View" )

		self.m_menu_tools = wx.Menu()
		self.m_menu_runMode = wx.Menu()
		self.m_menuItem_runModeEntry = wx.MenuItem( self.m_menu_runMode, wx.ID_ANY, u"Entry", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_runMode.Append( self.m_menuItem_runModeEntry )

		self.m_menuItem_runModeMaster = wx.MenuItem( self.m_menu_runMode, wx.ID_ANY, u"Master", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_runMode.Append( self.m_menuItem_runModeMaster )

		self.m_menu_tools.AppendSubMenu( self.m_menu_runMode, u"Run Mode" )

		self.m_menu_usbDetection = wx.Menu()
		self.m_menuItem_usbDetectionDynamic = wx.MenuItem( self.m_menu_usbDetection, wx.ID_ANY, u"Dynamic", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_usbDetection.Append( self.m_menuItem_usbDetectionDynamic )

		self.m_menuItem_usbDetectionStatic = wx.MenuItem( self.m_menu_usbDetection, wx.ID_ANY, u"Static", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_usbDetection.Append( self.m_menuItem_usbDetectionStatic )

		self.m_menu_tools.AppendSubMenu( self.m_menu_usbDetection, u"USB Detection" )

		self.m_menu_soundEffect = wx.Menu()
		self.m_menuItem_soundEffectMario = wx.MenuItem( self.m_menu_soundEffect, wx.ID_ANY, u"Mario", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_soundEffect.Append( self.m_menuItem_soundEffectMario )

		self.m_menuItem_soundEffectQuiet = wx.MenuItem( self.m_menu_soundEffect, wx.ID_ANY, u"Quiet", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_soundEffect.Append( self.m_menuItem_soundEffectQuiet )

		self.m_menu_tools.AppendSubMenu( self.m_menu_soundEffect, u"Sound Effect" )

		self.m_menu_genSbFile = wx.Menu()
		self.m_menuItem_genSbFileYes = wx.MenuItem( self.m_menu_genSbFile, wx.ID_ANY, u"Yes", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_genSbFile.Append( self.m_menuItem_genSbFileYes )

		self.m_menuItem_genSbFileNo = wx.MenuItem( self.m_menu_genSbFile, wx.ID_ANY, u"No", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_genSbFile.Append( self.m_menuItem_genSbFileNo )

		self.m_menu_tools.AppendSubMenu( self.m_menu_genSbFile, u"Generate .sb file" )

		self.m_menu_imageReadback = wx.Menu()
		self.m_menuItem_imageReadbackAutomatic = wx.MenuItem( self.m_menu_imageReadback, wx.ID_ANY, u"Automatic", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_imageReadback.Append( self.m_menuItem_imageReadbackAutomatic )

		self.m_menuItem_imageReadbackManual = wx.MenuItem( self.m_menu_imageReadback, wx.ID_ANY, u"Manual", wx.EmptyString, wx.ITEM_RADIO )
		self.m_menu_imageReadback.Append( self.m_menuItem_imageReadbackManual )

		self.m_menu_tools.AppendSubMenu( self.m_menu_imageReadback, u"Image Readback" )

		self.m_menubar.Append( self.m_menu_tools, u"Tools" )

		self.m_menu_window = wx.Menu()
		self.m_menubar.Append( self.m_menu_window, u"Window" )

		self.m_menu_help = wx.Menu()
		self.m_menuItem_homePage = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Home Page", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_homePage )

		self.m_menuItem_aboutAuthor = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_aboutAuthor )

		self.m_menuItem_contributors = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Contributors", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_contributors )

		self.m_menuItem_specialThanks = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Special Thanks", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_specialThanks )

		self.m_menuItem_revisionHistory = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Revision History", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_revisionHistory )

		self.m_menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar )

		bSizer_win = wx.BoxSizer( wx.VERTICAL )

		wSizer_func = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_setup = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_targetSetup = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_panel_targetSetup = wx.Panel( self.m_notebook_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_targetSetup.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_targetSetup = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_mcuSeries = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"MCU Series:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.m_staticText_mcuSeries.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_mcuSeries, 0, wx.ALL, 5 )

		m_choice_mcuSeriesChoices = [ u"i.MXRT", u"LPC", u"Kinetis" ]
		self.m_choice_mcuSeries = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_mcuSeriesChoices, 0 )
		self.m_choice_mcuSeries.SetSelection( 0 )
		wSizer_targetSetup.Add( self.m_choice_mcuSeries, 0, wx.ALL, 5 )

		self.m_staticText_mcuDevice = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"MCU Device:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.m_staticText_mcuDevice.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_mcuDevice, 0, wx.ALL, 5 )

		m_choice_mcuDeviceChoices = [ u"i.MXRT1015", u"i.MXRT102x", u"i.MXRT105x", u"i.MXRT106x", u"i.MXRT1064 SIP" ]
		self.m_choice_mcuDevice = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_mcuDeviceChoices, 0 )
		self.m_choice_mcuDevice.SetSelection( 2 )
		wSizer_targetSetup.Add( self.m_choice_mcuDevice, 0, wx.ALL, 5 )

		self.m_staticText_bootDevice = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"Boot Device:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.m_staticText_bootDevice.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_bootDevice, 0, wx.ALL, 5 )

		m_choice_bootDeviceChoices = [ u"FLEXSPI NOR", u"FLEXSPI NAND", u"SEMC NOR", u"SEMC NAND", u"uSDHC SD", u"uSDHC MMC/eMMC", u"LPSPI NOR/EEPROM" ]
		self.m_choice_bootDevice = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_bootDeviceChoices, 0 )
		self.m_choice_bootDevice.SetSelection( 0 )
		wSizer_targetSetup.Add( self.m_choice_bootDevice, 0, wx.ALL, 5 )

		self.m_staticText_null1TargetSetup = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 256,5 ), 0 )
		self.m_staticText_null1TargetSetup.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_null1TargetSetup, 0, wx.ALL, 5 )

		self.m_staticText_null2TargetSetup = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_staticText_null2TargetSetup.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_null2TargetSetup, 0, wx.ALL, 5 )

		self.m_button_bootDeviceConfiguration = wx.Button( self.m_panel_targetSetup, wx.ID_ANY, u"Boot Device Configuration", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		wSizer_targetSetup.Add( self.m_button_bootDeviceConfiguration, 0, wx.ALL, 5 )

		self.m_staticText_null3TargetSetup = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_staticText_null3TargetSetup.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_null3TargetSetup, 0, wx.ALL, 5 )

		self.m_button_deviceConfigurationData = wx.Button( self.m_panel_targetSetup, wx.ID_ANY, u"Device Configuration Data (DCD)", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		wSizer_targetSetup.Add( self.m_button_deviceConfigurationData, 0, wx.ALL, 5 )


		self.m_panel_targetSetup.SetSizer( wSizer_targetSetup )
		self.m_panel_targetSetup.Layout()
		wSizer_targetSetup.Fit( self.m_panel_targetSetup )
		self.m_notebook_targetSetup.AddPage( self.m_panel_targetSetup, u"Target Setup", False )

		bSizer_setup.Add( self.m_notebook_targetSetup, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_portSetup = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_portSetup = wx.Panel( self.m_notebook_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer_portSetup = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText_null1PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null1PortSetup, 0, wx.ALL, 5 )

		self.m_radioBtn_uart = wx.RadioButton( self.m_panel_portSetup, wx.ID_ANY, u"UART", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		wSizer_portSetup.Add( self.m_radioBtn_uart, 0, wx.ALL, 5 )

		self.m_radioBtn_usbhid = wx.RadioButton( self.m_panel_portSetup, wx.ID_ANY, u"USB-HID", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		wSizer_portSetup.Add( self.m_radioBtn_usbhid, 0, wx.ALL, 5 )

		self.m_staticText_portVid = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, u"COM Port:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.m_staticText_portVid.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_portVid, 0, wx.ALL, 5 )

		m_choice_portVidChoices = []
		self.m_choice_portVid = wx.Choice( self.m_panel_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_portVidChoices, 0 )
		self.m_choice_portVid.SetSelection( 0 )
		wSizer_portSetup.Add( self.m_choice_portVid, 0, wx.ALL, 5 )

		self.m_staticText_baudPid = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, u"Baudrate:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.m_staticText_baudPid.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_baudPid, 0, wx.ALL, 5 )

		m_choice_baudPidChoices = []
		self.m_choice_baudPid = wx.Choice( self.m_panel_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_baudPidChoices, 0 )
		self.m_choice_baudPid.SetSelection( 0 )
		wSizer_portSetup.Add( self.m_choice_baudPid, 0, wx.ALL, 5 )

		self.m_staticText_null2PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 256,5 ), 0 )
		self.m_staticText_null2PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null2PortSetup, 0, wx.ALL, 5 )

		self.m_staticText_null3PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.m_staticText_null3PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null3PortSetup, 0, wx.ALL, 5 )

		self.m_bitmap_connectLed = wx.StaticBitmap( self.m_panel_portSetup, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		wSizer_portSetup.Add( self.m_bitmap_connectLed, 0, wx.ALL, 5 )

		self.m_staticText_null4PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null4PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null4PortSetup, 0, wx.ALL, 5 )

		self.m_checkBox_oneStepConnect = wx.CheckBox( self.m_panel_portSetup, wx.ID_ANY, u"One Step", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		wSizer_portSetup.Add( self.m_checkBox_oneStepConnect, 0, wx.ALL, 5 )

		self.m_staticText_null5PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.m_staticText_null5PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null5PortSetup, 0, wx.ALL, 5 )

		self.m_button_connect = wx.Button( self.m_panel_portSetup, wx.ID_ANY, u"Connect to ROM", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		wSizer_portSetup.Add( self.m_button_connect, 0, wx.ALL, 5 )


		self.m_panel_portSetup.SetSizer( wSizer_portSetup )
		self.m_panel_portSetup.Layout()
		wSizer_portSetup.Fit( self.m_panel_portSetup )
		self.m_notebook_portSetup.AddPage( self.m_panel_portSetup, u"Port Setup", False )

		bSizer_setup.Add( self.m_notebook_portSetup, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_deviceStatus = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_deviceStatus = wx.Panel( self.m_notebook_deviceStatus, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_deviceStatus = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_deviceStatus = wx.TextCtrl( self.m_panel_deviceStatus, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,158 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		bSizer_deviceStatus.Add( self.m_textCtrl_deviceStatus, 0, wx.ALL, 5 )


		self.m_panel_deviceStatus.SetSizer( bSizer_deviceStatus )
		self.m_panel_deviceStatus.Layout()
		bSizer_deviceStatus.Fit( self.m_panel_deviceStatus )
		self.m_notebook_deviceStatus.AddPage( self.m_panel_deviceStatus, u"Device Status", False )

		bSizer_setup.Add( self.m_notebook_deviceStatus, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer_func.Add( bSizer_setup, 1, wx.EXPAND, 5 )

		bSizer_boot = wx.BoxSizer( wx.VERTICAL )

		wSizer_bootType = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_secureBootType = wx.StaticText( self, wx.ID_ANY, u"Secure Boot Type:", wx.DefaultPosition, wx.Size( 118,-1 ), 0 )
		self.m_staticText_secureBootType.Wrap( -1 )

		self.m_staticText_secureBootType.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText_secureBootType.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		wSizer_bootType.Add( self.m_staticText_secureBootType, 0, wx.ALL, 5 )

		m_choice_secureBootTypeChoices = [ u"DEV Unsigned Image Boot", u"HAB Signed Image Boot", u"HAB Encrypted Image Boot", u"BEE Encrypted Image Boot" ]
		self.m_choice_secureBootType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 299,-1 ), m_choice_secureBootTypeChoices, 0 )
		self.m_choice_secureBootType.SetSelection( 0 )
		wSizer_bootType.Add( self.m_choice_secureBootType, 0, wx.ALL, 5 )

		self.m_button_allInOneAction = wx.Button( self, wx.ID_ANY, u"All-In-One Action", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
		wSizer_bootType.Add( self.m_button_allInOneAction, 0, wx.ALL, 5 )

		self.m_staticText_null1BootType = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null1BootType.Wrap( -1 )

		wSizer_bootType.Add( self.m_staticText_null1BootType, 0, wx.ALL, 5 )

		self.m_bitmap_nxp = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 80,30 ), 0 )
		wSizer_bootType.Add( self.m_bitmap_nxp, 0, wx.ALL, 5 )


		bSizer_boot.Add( wSizer_bootType, 1, wx.EXPAND, 5 )

		self.m_notebook_imageSeq = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,450 ), 0 )
		self.m_notebook_imageSeq.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel_genSeq = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_genSeq.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel_genSeq.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		wSizer_genSeq = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_panel_doAuth = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_doAuth.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_doAuth = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_doAuth1_certInput = wx.Panel( self.m_panel_doAuth, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_certInput = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_doAuth1_certInput, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_serial = wx.StaticText( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"serial (8 digits):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_serial.Wrap( -1 )

		sbSizer_certInput.Add( self.m_staticText_serial, 0, wx.ALL, 5 )

		self.m_textCtrl_serial = wx.TextCtrl( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"12345678", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sbSizer_certInput.Add( self.m_textCtrl_serial, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_keyPass = wx.StaticText( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"key_pass (text):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keyPass.Wrap( -1 )

		sbSizer_certInput.Add( self.m_staticText_keyPass, 0, wx.ALL, 5 )

		self.m_textCtrl_keyPass = wx.TextCtrl( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"test", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sbSizer_certInput.Add( self.m_textCtrl_keyPass, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_advCertSettings = wx.Button( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"Advanced Cert Settings", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sbSizer_certInput.Add( self.m_button_advCertSettings, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth1_certInput.SetSizer( sbSizer_certInput )
		self.m_panel_doAuth1_certInput.Layout()
		sbSizer_certInput.Fit( self.m_panel_doAuth1_certInput )
		bSizer_doAuth.Add( self.m_panel_doAuth1_certInput, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_doAuth2_certFmt = wx.Panel( self.m_panel_doAuth, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_certFmt = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_doAuth2_certFmt, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_certFmt = wx.StaticText( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, u"Certificate Format:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_certFmt.Wrap( -1 )

		sbSizer_certFmt.Add( self.m_staticText_certFmt, 0, wx.ALL, 5 )

		m_choice_certFmtChoices = [ u"X.509v3" ]
		self.m_choice_certFmt = wx.Choice( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_certFmtChoices, 0 )
		self.m_choice_certFmt.SetSelection( 0 )
		sbSizer_certFmt.Add( self.m_choice_certFmt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_hashAlgo = wx.StaticText( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, u"Hash Algorithm:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_hashAlgo.Wrap( -1 )

		sbSizer_certFmt.Add( self.m_staticText_hashAlgo, 0, wx.ALL, 5 )

		m_choice_hashAlgoChoices = [ u"SHA-256" ]
		self.m_choice_hashAlgo = wx.Choice( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_hashAlgoChoices, 0 )
		self.m_choice_hashAlgo.SetSelection( 0 )
		sbSizer_certFmt.Add( self.m_choice_hashAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth2_certFmt.SetSizer( sbSizer_certFmt )
		self.m_panel_doAuth2_certFmt.Layout()
		sbSizer_certFmt.Fit( self.m_panel_doAuth2_certFmt )
		bSizer_doAuth.Add( self.m_panel_doAuth2_certFmt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_genCert = wx.Button( self.m_panel_doAuth, wx.ID_ANY, u"Generate Certificate,SRK", wx.DefaultPosition, wx.Size( 195,-1 ), 0 )
		bSizer_doAuth.Add( self.m_button_genCert, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth.SetSizer( bSizer_doAuth )
		self.m_panel_doAuth.Layout()
		bSizer_doAuth.Fit( self.m_panel_doAuth )
		wSizer_genSeq.Add( self.m_panel_doAuth, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_genImage = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_genImage.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_genImage = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_genImage1_browseApp = wx.Panel( self.m_panel_genImage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_browseApp = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_genImage1_browseApp, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_appPath = wx.StaticText( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"Application Image File:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText_appPath.Wrap( -1 )

		sbSizer_browseApp.Add( self.m_staticText_appPath, 0, wx.ALL, 5 )

		self.m_filePicker_appPath = wx.FilePickerCtrl( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 280,23 ), wx.FLP_DEFAULT_STYLE )
		sbSizer_browseApp.Add( self.m_filePicker_appPath, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_choice_appFormatChoices = [ u"Auto-detect image format", u".out(axf) from Keil MDK", u".out(elf) from IAR EWARM", u".out(axf) from MCUXpresso", u".out(elf) from GCC ARM", u"Motorola S-Records (.srec/.s19)", u"Intel Extended Hex (.hex)", u"Raw Binary (.bin)" ]
		self.m_choice_appFormat = wx.Choice( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_choice_appFormatChoices, 0 )
		self.m_choice_appFormat.SetSelection( 0 )
		sbSizer_browseApp.Add( self.m_choice_appFormat, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_appBaseAddr = wx.StaticText( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"Base Address for Raw Binary Image:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_appBaseAddr.Wrap( -1 )

		sbSizer_browseApp.Add( self.m_staticText_appBaseAddr, 0, wx.ALL, 5 )

		self.m_textCtrl_appBaseAddr = wx.TextCtrl( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"Eg: 0x00003000", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl_appBaseAddr.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer_browseApp.Add( self.m_textCtrl_appBaseAddr, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage1_browseApp.SetSizer( sbSizer_browseApp )
		self.m_panel_genImage1_browseApp.Layout()
		sbSizer_browseApp.Fit( self.m_panel_genImage1_browseApp )
		bSizer_genImage.Add( self.m_panel_genImage1_browseApp, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_genImage2_habCryptoAlgo = wx.Panel( self.m_panel_genImage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sbSizer_habCryptoAlgo = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_genImage2_habCryptoAlgo, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_habCryptoAlgo = wx.StaticText( sbSizer_habCryptoAlgo.GetStaticBox(), wx.ID_ANY, u"HAB Encryption Algorithm:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_habCryptoAlgo.Wrap( -1 )

		sbSizer_habCryptoAlgo.Add( self.m_staticText_habCryptoAlgo, 0, wx.ALL, 5 )

		m_choice_habCryptoAlgoChoices = [ u"AES-128" ]
		self.m_choice_habCryptoAlgo = wx.Choice( sbSizer_habCryptoAlgo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_habCryptoAlgoChoices, 0 )
		self.m_choice_habCryptoAlgo.SetSelection( 0 )
		sbSizer_habCryptoAlgo.Add( self.m_choice_habCryptoAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage2_habCryptoAlgo.SetSizer( sbSizer_habCryptoAlgo )
		self.m_panel_genImage2_habCryptoAlgo.Layout()
		sbSizer_habCryptoAlgo.Fit( self.m_panel_genImage2_habCryptoAlgo )
		bSizer_genImage.Add( self.m_panel_genImage2_habCryptoAlgo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_genImage3_enableCertForBee = wx.Panel( self.m_panel_genImage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sbSizer_enableCertForBee = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_genImage3_enableCertForBee, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_enableCertForBee = wx.StaticText( sbSizer_enableCertForBee.GetStaticBox(), wx.ID_ANY, u"Enable Certificate for BEE Encryption:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_enableCertForBee.Wrap( -1 )

		sbSizer_enableCertForBee.Add( self.m_staticText_enableCertForBee, 0, wx.ALL, 5 )

		m_choice_enableCertForBeeChoices = [ u"No", u"Yes" ]
		self.m_choice_enableCertForBee = wx.Choice( sbSizer_enableCertForBee.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_enableCertForBeeChoices, 0 )
		self.m_choice_enableCertForBee.SetSelection( 0 )
		sbSizer_enableCertForBee.Add( self.m_choice_enableCertForBee, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage3_enableCertForBee.SetSizer( sbSizer_enableCertForBee )
		self.m_panel_genImage3_enableCertForBee.Layout()
		sbSizer_enableCertForBee.Fit( self.m_panel_genImage3_enableCertForBee )
		bSizer_genImage.Add( self.m_panel_genImage3_enableCertForBee, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_genImage = wx.Button( self.m_panel_genImage, wx.ID_ANY, u"Generate Unsigned Bootable Image", wx.DefaultPosition, wx.Size( 225,-1 ), 0 )
		bSizer_genImage.Add( self.m_button_genImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage.SetSizer( bSizer_genImage )
		self.m_panel_genImage.Layout()
		bSizer_genImage.Fit( self.m_panel_genImage )
		wSizer_genSeq.Add( self.m_panel_genImage, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_prepBee.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_prepBee = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_prepBee1_beeKeyRegion = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_keyStorageRegion = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee1_beeKeyRegion, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_keyStorageRegion = wx.StaticText( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, u"Key Storage Region:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keyStorageRegion.Wrap( -1 )

		sbSizer_keyStorageRegion.Add( self.m_staticText_keyStorageRegion, 0, wx.ALL, 5 )

		m_choice_keyStorageRegionChoices = [ u"Fixed Otpmk(SNVS) Key", u"Flexible User Keys" ]
		self.m_choice_keyStorageRegion = wx.Choice( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_keyStorageRegionChoices, 0 )
		self.m_choice_keyStorageRegion.SetSelection( 1 )
		sbSizer_keyStorageRegion.Add( self.m_choice_keyStorageRegion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_availBeeEngines = wx.StaticText( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, u"Max Available BEE Engines:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_availBeeEngines.Wrap( -1 )

		sbSizer_keyStorageRegion.Add( self.m_staticText_availBeeEngines, 0, wx.ALL, 5 )

		m_choice_availBeeEnginesChoices = [ u"1", u"2" ]
		self.m_choice_availBeeEngines = wx.Choice( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_availBeeEnginesChoices, 0 )
		self.m_choice_availBeeEngines.SetSelection( 0 )
		sbSizer_keyStorageRegion.Add( self.m_choice_availBeeEngines, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_advKeySettings = wx.Button( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, u"Advanced Key Settings", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sbSizer_keyStorageRegion.Add( self.m_button_advKeySettings, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee1_beeKeyRegion.SetSizer( sbSizer_keyStorageRegion )
		self.m_panel_prepBee1_beeKeyRegion.Layout()
		sbSizer_keyStorageRegion.Fit( self.m_panel_prepBee1_beeKeyRegion )
		bSizer_prepBee.Add( self.m_panel_prepBee1_beeKeyRegion, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee2_beeCryptoAlgo = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_beeCryptoAlgo = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee2_beeCryptoAlgo, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_beeCryptoAlgo = wx.StaticText( sbSizer_beeCryptoAlgo.GetStaticBox(), wx.ID_ANY, u"BEE Encryption Algorithm:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_beeCryptoAlgo.Wrap( -1 )

		sbSizer_beeCryptoAlgo.Add( self.m_staticText_beeCryptoAlgo, 0, wx.ALL, 5 )

		m_choice_beeCryptoAlgoChoices = [ u"AES-128" ]
		self.m_choice_beeCryptoAlgo = wx.Choice( sbSizer_beeCryptoAlgo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_beeCryptoAlgoChoices, 0 )
		self.m_choice_beeCryptoAlgo.SetSelection( 0 )
		sbSizer_beeCryptoAlgo.Add( self.m_choice_beeCryptoAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_maxFacCnt = wx.StaticText( sbSizer_beeCryptoAlgo.GetStaticBox(), wx.ID_ANY, u"Max Protection Regions:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_maxFacCnt.Wrap( -1 )

		sbSizer_beeCryptoAlgo.Add( self.m_staticText_maxFacCnt, 0, wx.ALL, 5 )

		m_choice_maxFacCntChoices = [ u"3" ]
		self.m_choice_maxFacCnt = wx.Choice( sbSizer_beeCryptoAlgo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), m_choice_maxFacCntChoices, 0 )
		self.m_choice_maxFacCnt.SetSelection( 0 )
		sbSizer_beeCryptoAlgo.Add( self.m_choice_maxFacCnt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee2_beeCryptoAlgo.SetSizer( sbSizer_beeCryptoAlgo )
		self.m_panel_prepBee2_beeCryptoAlgo.Layout()
		sbSizer_beeCryptoAlgo.Fit( self.m_panel_prepBee2_beeCryptoAlgo )
		bSizer_prepBee.Add( self.m_panel_prepBee2_beeCryptoAlgo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_prepBee = wx.Button( self.m_panel_prepBee, wx.ID_ANY, u"Prepare For Encryption", wx.DefaultPosition, wx.Size( 195,-1 ), 0 )
		bSizer_prepBee.Add( self.m_button_prepBee, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee.SetSizer( bSizer_prepBee )
		self.m_panel_prepBee.Layout()
		bSizer_prepBee.Fit( self.m_panel_prepBee )
		wSizer_genSeq.Add( self.m_panel_prepBee, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_genSeq.SetSizer( wSizer_genSeq )
		self.m_panel_genSeq.Layout()
		wSizer_genSeq.Fit( self.m_panel_genSeq )
		self.m_notebook_imageSeq.AddPage( self.m_panel_genSeq, u"Image Generation Sequence", True )
		self.m_panel_loadSeq = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_loadSeq.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		wSizer_loadSeq = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_panel_progSrk = wx.Panel( self.m_panel_loadSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_progSrk.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_progSrk = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_progSrk1_showSrk = wx.Panel( self.m_panel_progSrk, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showSrk = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_progSrk1_showSrk, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_srk256bit = wx.StaticText( sbSizer_showSrk.GetStaticBox(), wx.ID_ANY, u"Burn below SRK data (256bits) into Fuse SRK0-7 Region:", wx.DefaultPosition, wx.Size( 120,60 ), 0 )
		self.m_staticText_srk256bit.Wrap( -1 )

		sbSizer_showSrk.Add( self.m_staticText_srk256bit, 0, wx.ALL, 5 )

		self.m_textCtrl_srk256bit = wx.TextCtrl( sbSizer_showSrk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,180 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_RICH2 )
		self.m_textCtrl_srk256bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showSrk.Add( self.m_textCtrl_srk256bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progSrk1_showSrk.SetSizer( sbSizer_showSrk )
		self.m_panel_progSrk1_showSrk.Layout()
		sbSizer_showSrk.Fit( self.m_panel_progSrk1_showSrk )
		bSizer_progSrk.Add( self.m_panel_progSrk1_showSrk, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_progSrk = wx.Button( self.m_panel_progSrk, wx.ID_ANY, u"Burn SRK data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_progSrk.Add( self.m_button_progSrk, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progSrk.SetSizer( bSizer_progSrk )
		self.m_panel_progSrk.Layout()
		bSizer_progSrk.Fit( self.m_panel_progSrk )
		wSizer_loadSeq.Add( self.m_panel_progSrk, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_operBee = wx.Panel( self.m_panel_loadSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_operBee.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_operBee = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_operBee1_beeKeyInfo = wx.Panel( self.m_panel_operBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_beeKeyInfo = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_operBee1_beeKeyInfo, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_beeKeyInfo = wx.StaticText( sbSizer_beeKeyInfo.GetStaticBox(), wx.ID_ANY, u"Burn below user DEK data (128bits * n) into below Region for BEE:", wx.DefaultPosition, wx.Size( 130,45 ), 0 )
		self.m_staticText_beeKeyInfo.Wrap( -1 )

		sbSizer_beeKeyInfo.Add( self.m_staticText_beeKeyInfo, 0, wx.ALL, 5 )


		self.m_panel_operBee1_beeKeyInfo.SetSizer( sbSizer_beeKeyInfo )
		self.m_panel_operBee1_beeKeyInfo.Layout()
		sbSizer_beeKeyInfo.Fit( self.m_panel_operBee1_beeKeyInfo )
		bSizer_operBee.Add( self.m_panel_operBee1_beeKeyInfo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_operBee2_showGp4Dek = wx.Panel( self.m_panel_operBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showGp4Dek = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_operBee2_showGp4Dek, wx.ID_ANY, u"Fuse GP4 Region:" ), wx.VERTICAL )

		self.m_textCtrl_gp4Dek128bit = wx.TextCtrl( sbSizer_showGp4Dek.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,100 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_RICH2 )
		self.m_textCtrl_gp4Dek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showGp4Dek.Add( self.m_textCtrl_gp4Dek128bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_operBee2_showGp4Dek.SetSizer( sbSizer_showGp4Dek )
		self.m_panel_operBee2_showGp4Dek.Layout()
		sbSizer_showGp4Dek.Fit( self.m_panel_operBee2_showGp4Dek )
		bSizer_operBee.Add( self.m_panel_operBee2_showGp4Dek, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_operBee3_showSwgp2Dek = wx.Panel( self.m_panel_operBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showSwgp2Dek = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_operBee3_showSwgp2Dek, wx.ID_ANY, u"Fuse SW_GP2 Region:" ), wx.VERTICAL )

		self.m_textCtrl_swgp2Dek128bit = wx.TextCtrl( sbSizer_showSwgp2Dek.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,100 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_RICH2 )
		self.m_textCtrl_swgp2Dek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showSwgp2Dek.Add( self.m_textCtrl_swgp2Dek128bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_operBee3_showSwgp2Dek.SetSizer( sbSizer_showSwgp2Dek )
		self.m_panel_operBee3_showSwgp2Dek.Layout()
		sbSizer_showSwgp2Dek.Fit( self.m_panel_operBee3_showSwgp2Dek )
		bSizer_operBee.Add( self.m_panel_operBee3_showSwgp2Dek, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_operBee = wx.Button( self.m_panel_operBee, wx.ID_ANY, u"Burn DEK data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_operBee.Add( self.m_button_operBee, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_operBee.SetSizer( bSizer_operBee )
		self.m_panel_operBee.Layout()
		bSizer_operBee.Fit( self.m_panel_operBee )
		wSizer_loadSeq.Add( self.m_panel_operBee, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_flashImage = wx.Panel( self.m_panel_loadSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_flashImage.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_flashImage = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_flashImage1_showImage = wx.Panel( self.m_panel_flashImage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel_flashImage1_showImage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		sbSizer_showImage = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_flashImage1_showImage, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_showImage = wx.StaticText( sbSizer_showImage.GetStaticBox(), wx.ID_ANY, u"Program final bootable image to boot device:", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.m_staticText_showImage.Wrap( -1 )

		sbSizer_showImage.Add( self.m_staticText_showImage, 0, wx.ALL, 5 )

		self.m_bitmap_bootableImage = wx.StaticBitmap( sbSizer_showImage.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 160,310 ), 0 )
		sbSizer_showImage.Add( self.m_bitmap_bootableImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_flashImage1_showImage.SetSizer( sbSizer_showImage )
		self.m_panel_flashImage1_showImage.Layout()
		sbSizer_showImage.Fit( self.m_panel_flashImage1_showImage )
		bSizer_flashImage.Add( self.m_panel_flashImage1_showImage, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_flashImage = wx.Button( self.m_panel_flashImage, wx.ID_ANY, u"Load Image", wx.DefaultPosition, wx.Size( 165,-1 ), 0 )
		bSizer_flashImage.Add( self.m_button_flashImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_flashImage.SetSizer( bSizer_flashImage )
		self.m_panel_flashImage.Layout()
		bSizer_flashImage.Fit( self.m_panel_flashImage )
		wSizer_loadSeq.Add( self.m_panel_flashImage, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_progDek = wx.Panel( self.m_panel_loadSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_progDek.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		bSizer_progDek = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_progDek1_showHabDek = wx.Panel( self.m_panel_progDek, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showHabDek = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_progDek1_showHabDek, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_habDek128bit = wx.StaticText( sbSizer_showHabDek.GetStaticBox(), wx.ID_ANY, u"Use below DEK data (128bits) to generate keyblob and program it to flash for HAB:", wx.DefaultPosition, wx.Size( 160,70 ), 0 )
		self.m_staticText_habDek128bit.Wrap( -1 )

		sbSizer_showHabDek.Add( self.m_staticText_habDek128bit, 0, wx.ALL, 5 )

		self.m_textCtrl_habDek128bit = wx.TextCtrl( sbSizer_showHabDek.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,100 ), wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_RICH2 )
		self.m_textCtrl_habDek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showHabDek.Add( self.m_textCtrl_habDek128bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progDek1_showHabDek.SetSizer( sbSizer_showHabDek )
		self.m_panel_progDek1_showHabDek.Layout()
		sbSizer_showHabDek.Fit( self.m_panel_progDek1_showHabDek )
		bSizer_progDek.Add( self.m_panel_progDek1_showHabDek, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_progDek = wx.Button( self.m_panel_progDek, wx.ID_ANY, u"Enable HAB, Load KeyBlob Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_progDek.Add( self.m_button_progDek, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progDek.SetSizer( bSizer_progDek )
		self.m_panel_progDek.Layout()
		bSizer_progDek.Fit( self.m_panel_progDek )
		wSizer_loadSeq.Add( self.m_panel_progDek, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_loadSeq.SetSizer( wSizer_loadSeq )
		self.m_panel_loadSeq.Layout()
		wSizer_loadSeq.Fit( self.m_panel_loadSeq )
		self.m_notebook_imageSeq.AddPage( self.m_panel_loadSeq, u"Image Loading Sequence", False )
		self.m_panel_fuseUtil = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_fuseUtil.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_fuseUtil = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_fuseGroupTxt0 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_fuse400 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Lock", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse400.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt0.Add( self.m_button_fuse400, 0, wx.ALL, 5 )

		self.m_staticText_fuse410 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"UUID0", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse410.Wrap( -1 )

		self.m_staticText_fuse410.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse410, 0, wx.ALL, 5 )

		self.m_staticText_fuse420 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"UUID1", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse420.Wrap( -1 )

		self.m_staticText_fuse420.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse420, 0, wx.ALL, 5 )

		self.m_staticText_fuse430 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x430:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse430.Wrap( -1 )

		self.m_staticText_fuse430.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse430, 0, wx.ALL, 5 )

		self.m_staticText_fuse440 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x440:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse440.Wrap( -1 )

		self.m_staticText_fuse440.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse440, 0, wx.ALL, 5 )

		self.m_button_fuse450 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Cfg0", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse450.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt0.Add( self.m_button_fuse450, 0, wx.ALL, 5 )

		self.m_button_fuse460 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Cfg1", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse460.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt0.Add( self.m_button_fuse460, 0, wx.ALL, 5 )

		self.m_button_fuse470 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Cfg2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse470.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt0.Add( self.m_button_fuse470, 0, wx.ALL, 5 )

		self.m_staticText_fuse480 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x480:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse480.Wrap( -1 )

		self.m_staticText_fuse480.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse480, 0, wx.ALL, 5 )

		self.m_staticText_fuse490 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x490:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse490.Wrap( -1 )

		self.m_staticText_fuse490.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse490, 0, wx.ALL, 5 )

		self.m_staticText_fuse4a0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4a0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4a0.Wrap( -1 )

		self.m_staticText_fuse4a0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse4a0, 0, wx.ALL, 5 )

		self.m_staticText_fuse4b0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4b0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4b0.Wrap( -1 )

		self.m_staticText_fuse4b0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse4b0, 0, wx.ALL, 5 )

		self.m_staticText_fuse4c0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4c0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4c0.Wrap( -1 )

		self.m_staticText_fuse4c0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse4c0, 0, wx.ALL, 5 )

		self.m_staticText_fuse4d0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4d0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4d0.Wrap( -1 )

		self.m_staticText_fuse4d0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt0.Add( self.m_staticText_fuse4d0, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt0, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl0 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse400 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse400, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse410 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse410, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse420 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse420, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse430 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse430, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse440 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse440, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse450 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, u"Boot Cfg0", wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse450, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse460 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, u"Boot Cfg1", wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse460, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse470 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, u"Boot Cfg2", wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse470, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse480 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse480, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse490 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse490, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse4a0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse4a0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse4b0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse4b0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse4c0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse4c0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse4d0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl0.Add( self.m_textCtrl_fuse4d0, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl0, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupTxt1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_fuse4e0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4e0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4e0.Wrap( -1 )

		self.m_staticText_fuse4e0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse4e0, 0, wx.ALL, 5 )

		self.m_staticText_fuse4f0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x4f0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse4f0.Wrap( -1 )

		self.m_staticText_fuse4f0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse4f0, 0, wx.ALL, 5 )

		self.m_staticText_fuse500 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse500.Wrap( -1 )

		self.m_staticText_fuse500.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse500, 0, wx.ALL, 5 )

		self.m_staticText_fuse510 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse510.Wrap( -1 )

		self.m_staticText_fuse510.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse510, 0, wx.ALL, 5 )

		self.m_staticText_fuse520 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse520.Wrap( -1 )

		self.m_staticText_fuse520.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse520, 0, wx.ALL, 5 )

		self.m_staticText_fuse530 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse530.Wrap( -1 )

		self.m_staticText_fuse530.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse530, 0, wx.ALL, 5 )

		self.m_staticText_fuse540 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse540.Wrap( -1 )

		self.m_staticText_fuse540.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse540, 0, wx.ALL, 5 )

		self.m_staticText_fuse550 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse550.Wrap( -1 )

		self.m_staticText_fuse550.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse550, 0, wx.ALL, 5 )

		self.m_staticText_fuse560 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse560.Wrap( -1 )

		self.m_staticText_fuse560.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse560, 0, wx.ALL, 5 )

		self.m_staticText_fuse570 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"OTPMK", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse570.Wrap( -1 )

		self.m_staticText_fuse570.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse570, 0, wx.ALL, 5 )

		self.m_staticText_fuse580 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK0", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse580.Wrap( -1 )

		self.m_staticText_fuse580.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse580.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse580, 0, wx.ALL, 5 )

		self.m_staticText_fuse590 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK1", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse590.Wrap( -1 )

		self.m_staticText_fuse590.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse590.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse590, 0, wx.ALL, 5 )

		self.m_staticText_fuse5a0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5a0.Wrap( -1 )

		self.m_staticText_fuse5a0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5a0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse5a0, 0, wx.ALL, 5 )

		self.m_staticText_fuse5b0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK3", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5b0.Wrap( -1 )

		self.m_staticText_fuse5b0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5b0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt1.Add( self.m_staticText_fuse5b0, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt1, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse4e0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse4e0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse4f0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse4f0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse500 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse500, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse510 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse510, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse520 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse520, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse530 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse530, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse540 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse540, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse550 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse550, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse560 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse560, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse570 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse570, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse580 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse580, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse590 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse590, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse5a0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse5a0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse5b0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl1.Add( self.m_textCtrl_fuse5b0, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl1, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupTxt2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_fuse5c0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK4", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5c0.Wrap( -1 )

		self.m_staticText_fuse5c0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5c0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse5c0, 0, wx.ALL, 5 )

		self.m_staticText_fuse5d0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK5", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5d0.Wrap( -1 )

		self.m_staticText_fuse5d0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5d0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse5d0, 0, wx.ALL, 5 )

		self.m_staticText_fuse5e0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK6", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5e0.Wrap( -1 )

		self.m_staticText_fuse5e0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5e0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse5e0, 0, wx.ALL, 5 )

		self.m_staticText_fuse5f0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SRK7", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse5f0.Wrap( -1 )

		self.m_staticText_fuse5f0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse5f0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse5f0, 0, wx.ALL, 5 )

		self.m_staticText_fuse600 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x600:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse600.Wrap( -1 )

		self.m_staticText_fuse600.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse600, 0, wx.ALL, 5 )

		self.m_staticText_fuse610 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x610:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse610.Wrap( -1 )

		self.m_staticText_fuse610.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse610, 0, wx.ALL, 5 )

		self.m_staticText_fuse620 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x620:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse620.Wrap( -1 )

		self.m_staticText_fuse620.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse620, 0, wx.ALL, 5 )

		self.m_staticText_fuse630 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x630:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse630.Wrap( -1 )

		self.m_staticText_fuse630.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse630, 0, wx.ALL, 5 )

		self.m_staticText_fuse640 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x640:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse640.Wrap( -1 )

		self.m_staticText_fuse640.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse640, 0, wx.ALL, 5 )

		self.m_staticText_fuse650 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x650:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse650.Wrap( -1 )

		self.m_staticText_fuse650.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse650, 0, wx.ALL, 5 )

		self.m_staticText_fuse660 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x660:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse660.Wrap( -1 )

		self.m_staticText_fuse660.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse660, 0, wx.ALL, 5 )

		self.m_staticText_fuse670 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x670:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse670.Wrap( -1 )

		self.m_staticText_fuse670.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse670, 0, wx.ALL, 5 )

		self.m_staticText_fuse680 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x680:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse680.Wrap( -1 )

		self.m_staticText_fuse680.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse680, 0, wx.ALL, 5 )

		self.m_staticText_fuse690 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SwGp2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse690.Wrap( -1 )

		self.m_staticText_fuse690.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse690.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt2.Add( self.m_staticText_fuse690, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt2, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl2 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse5c0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse5c0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse5d0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse5d0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse5e0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse5e0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse5f0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse5f0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse600 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse600, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse610 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse610, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse620 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse620, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse630 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse630, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse640 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse640, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse650 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse650, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse660 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse660, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse670 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse670, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse680 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse680, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse690 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl2.Add( self.m_textCtrl_fuse690, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl2, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupTxt3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_fuse6a0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SwGp2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse6a0.Wrap( -1 )

		self.m_staticText_fuse6a0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse6a0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse6a0, 0, wx.ALL, 5 )

		self.m_staticText_fuse6b0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SwGp2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse6b0.Wrap( -1 )

		self.m_staticText_fuse6b0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse6b0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse6b0, 0, wx.ALL, 5 )

		self.m_staticText_fuse6c0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"SwGp2", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse6c0.Wrap( -1 )

		self.m_staticText_fuse6c0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse6c0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse6c0, 0, wx.ALL, 5 )

		self.m_button_fuse6d0 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Conf0", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse6d0.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt3.Add( self.m_button_fuse6d0, 0, wx.ALL, 5 )

		self.m_button_fuse6e0 = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Conf1", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_button_fuse6e0.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer_fuseGroupTxt3.Add( self.m_button_fuse6e0, 0, wx.ALL, 5 )

		self.m_staticText_fuse6f0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x6f0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse6f0.Wrap( -1 )

		self.m_staticText_fuse6f0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse6f0, 0, wx.ALL, 5 )

		self.m_staticText_fuse700 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x700:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse700.Wrap( -1 )

		self.m_staticText_fuse700.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse700, 0, wx.ALL, 5 )

		self.m_staticText_fuse710 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x710:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse710.Wrap( -1 )

		self.m_staticText_fuse710.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse710, 0, wx.ALL, 5 )

		self.m_staticText_fuse720 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x720:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse720.Wrap( -1 )

		self.m_staticText_fuse720.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse720, 0, wx.ALL, 5 )

		self.m_staticText_fuse730 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x730:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse730.Wrap( -1 )

		self.m_staticText_fuse730.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse730, 0, wx.ALL, 5 )

		self.m_staticText_fuse740 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x740:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse740.Wrap( -1 )

		self.m_staticText_fuse740.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse740, 0, wx.ALL, 5 )

		self.m_staticText_fuse750 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x750:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse750.Wrap( -1 )

		self.m_staticText_fuse750.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse750, 0, wx.ALL, 5 )

		self.m_staticText_fuse760 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x760:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse760.Wrap( -1 )

		self.m_staticText_fuse760.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse760, 0, wx.ALL, 5 )

		self.m_staticText_fuse770 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x770:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse770.Wrap( -1 )

		self.m_staticText_fuse770.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt3.Add( self.m_staticText_fuse770, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt3, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl3 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse6a0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6a0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse6b0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6b0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse6c0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6c0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse6d0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, u"Misc Conf0", wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6d0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse6e0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, u"Misc Conf1", wx.DefaultPosition, wx.Size( 75,20 ), wx.TE_PROCESS_ENTER )
		self.m_textCtrl_fuse6e0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6e0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse6f0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse6f0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse700 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse700, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse710 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse710, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse720 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse720, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse730 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse730, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse740 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse740, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse750 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse750, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse760 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse760, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse770 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl3.Add( self.m_textCtrl_fuse770, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl3, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupTxt4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_fuse780 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x780:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse780.Wrap( -1 )

		self.m_staticText_fuse780.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse780, 0, wx.ALL, 5 )

		self.m_staticText_fuse790 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x790:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse790.Wrap( -1 )

		self.m_staticText_fuse790.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse790, 0, wx.ALL, 5 )

		self.m_staticText_fuse7a0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7a0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7a0.Wrap( -1 )

		self.m_staticText_fuse7a0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7a0, 0, wx.ALL, 5 )

		self.m_staticText_fuse7b0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7b0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7b0.Wrap( -1 )

		self.m_staticText_fuse7b0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7b0, 0, wx.ALL, 5 )

		self.m_staticText_fuse7c0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7c0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7c0.Wrap( -1 )

		self.m_staticText_fuse7c0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7c0, 0, wx.ALL, 5 )

		self.m_staticText_fuse7d0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7d0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7d0.Wrap( -1 )

		self.m_staticText_fuse7d0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7d0, 0, wx.ALL, 5 )

		self.m_staticText_fuse7e0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7e0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7e0.Wrap( -1 )

		self.m_staticText_fuse7e0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7e0, 0, wx.ALL, 5 )

		self.m_staticText_fuse7f0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x7f0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse7f0.Wrap( -1 )

		self.m_staticText_fuse7f0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse7f0, 0, wx.ALL, 5 )

		self.m_staticText_fuse800 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x800:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse800.Wrap( -1 )

		self.m_staticText_fuse800.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse800, 0, wx.ALL, 5 )

		self.m_staticText_fuse810 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x810:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse810.Wrap( -1 )

		self.m_staticText_fuse810.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse810, 0, wx.ALL, 5 )

		self.m_staticText_fuse820 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x820:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse820.Wrap( -1 )

		self.m_staticText_fuse820.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse820, 0, wx.ALL, 5 )

		self.m_staticText_fuse830 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x830:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse830.Wrap( -1 )

		self.m_staticText_fuse830.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse830, 0, wx.ALL, 5 )

		self.m_staticText_fuse840 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x840:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse840.Wrap( -1 )

		self.m_staticText_fuse840.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse840, 0, wx.ALL, 5 )

		self.m_staticText_fuse850 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x850:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse850.Wrap( -1 )

		self.m_staticText_fuse850.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt4.Add( self.m_staticText_fuse850, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt4, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl4 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse780 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse780, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse790 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse790, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7a0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7a0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7b0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7b0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7c0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7c0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7d0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7d0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7e0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7e0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse7f0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse7f0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse800 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse800, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse810 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse810, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse820 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse820, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse830 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse830, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse840 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse840, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse850 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl4.Add( self.m_textCtrl_fuse850, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl4, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupTxt5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_fuse860 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x860:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse860.Wrap( -1 )

		self.m_staticText_fuse860.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse860, 0, wx.ALL, 5 )

		self.m_staticText_fuse870 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x870:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse870.Wrap( -1 )

		self.m_staticText_fuse870.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse870, 0, wx.ALL, 5 )

		self.m_staticText_fuse880 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x880:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse880.Wrap( -1 )

		self.m_staticText_fuse880.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse880, 0, wx.ALL, 5 )

		self.m_staticText_fuse890 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x890:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse890.Wrap( -1 )

		self.m_staticText_fuse890.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse890, 0, wx.ALL, 5 )

		self.m_staticText_fuse8a0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x8a0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8a0.Wrap( -1 )

		self.m_staticText_fuse8a0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8a0, 0, wx.ALL, 5 )

		self.m_staticText_fuse8b0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"0x8b0:", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8b0.Wrap( -1 )

		self.m_staticText_fuse8b0.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8b0, 0, wx.ALL, 5 )

		self.m_staticText_fuse8c0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"Gp4", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8c0.Wrap( -1 )

		self.m_staticText_fuse8c0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse8c0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8c0, 0, wx.ALL, 5 )

		self.m_staticText_fuse8d0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"Gp4", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8d0.Wrap( -1 )

		self.m_staticText_fuse8d0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse8d0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8d0, 0, wx.ALL, 5 )

		self.m_staticText_fuse8e0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"Gp4", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8e0.Wrap( -1 )

		self.m_staticText_fuse8e0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse8e0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8e0, 0, wx.ALL, 5 )

		self.m_staticText_fuse8f0 = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, u"Gp4", wx.DefaultPosition, wx.Size( 31,20 ), 0 )
		self.m_staticText_fuse8f0.Wrap( -1 )

		self.m_staticText_fuse8f0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_fuse8f0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_fuseGroupTxt5.Add( self.m_staticText_fuse8f0, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupTxt5, 1, wx.EXPAND, 5 )

		bSizer_fuseGroupCtrl5 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_fuse860 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse860, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse870 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse870, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse880 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse880, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse890 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse890, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8a0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8a0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8b0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8b0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8c0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8c0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8d0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8d0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8e0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8e0, 0, wx.ALL, 5 )

		self.m_textCtrl_fuse8f0 = wx.TextCtrl( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_textCtrl_fuse8f0, 0, wx.ALL, 5 )

		self.m_staticText_null0Fuse = wx.StaticText( self.m_panel_fuseUtil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 31,15 ), 0 )
		self.m_staticText_null0Fuse.Wrap( -1 )

		bSizer_fuseGroupCtrl5.Add( self.m_staticText_null0Fuse, 0, wx.ALL, 5 )

		self.m_button_scan = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_button_scan, 0, wx.ALL, 5 )

		self.m_button_burn = wx.Button( self.m_panel_fuseUtil, wx.ID_ANY, u"Burn", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		bSizer_fuseGroupCtrl5.Add( self.m_button_burn, 0, wx.ALL, 5 )


		wSizer_fuseUtil.Add( bSizer_fuseGroupCtrl5, 1, wx.EXPAND, 5 )


		self.m_panel_fuseUtil.SetSizer( wSizer_fuseUtil )
		self.m_panel_fuseUtil.Layout()
		wSizer_fuseUtil.Fit( self.m_panel_fuseUtil )
		self.m_notebook_imageSeq.AddPage( self.m_panel_fuseUtil, u"eFuse Operation Utility", False )
		self.m_panel_memView = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_memView.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_memView = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_memStart = wx.StaticText( self.m_panel_memView, wx.ID_ANY, u"Start / Offset:", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText_memStart.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_memStart, 0, wx.ALL, 5 )

		self.m_textCtrl_memStart = wx.TextCtrl( self.m_panel_memView, wx.ID_ANY, u"0x0", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		wSizer_memView.Add( self.m_textCtrl_memStart, 0, wx.ALL, 5 )

		self.m_staticText_memLength = wx.StaticText( self.m_panel_memView, wx.ID_ANY, u"Byte Length:", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText_memLength.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_memLength, 0, wx.ALL, 5 )

		self.m_textCtrl_memLength = wx.TextCtrl( self.m_panel_memView, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		wSizer_memView.Add( self.m_textCtrl_memLength, 0, wx.ALL, 5 )

		self.m_staticText_memBinFile = wx.StaticText( self.m_panel_memView, wx.ID_ANY, u"Bin File:", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText_memBinFile.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_memBinFile, 0, wx.ALL, 5 )

		self.m_filePicker_memBinFile = wx.FilePickerCtrl( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_DEFAULT_STYLE )
		wSizer_memView.Add( self.m_filePicker_memBinFile, 0, wx.ALL, 5 )

		self.m_staticText_null0MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.m_staticText_null0MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null0MemView, 0, wx.ALL, 5 )

		self.m_button_readMem = wx.Button( self.m_panel_memView, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_memView.Add( self.m_button_readMem, 0, wx.ALL, 5 )

		self.m_staticText_null1MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_null1MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null1MemView, 0, wx.ALL, 5 )

		self.m_button_eraseMem = wx.Button( self.m_panel_memView, wx.ID_ANY, u"Erase", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_memView.Add( self.m_button_eraseMem, 0, wx.ALL, 5 )

		self.m_staticText_null2MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_null2MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null2MemView, 0, wx.ALL, 5 )

		self.m_button_writeMem = wx.Button( self.m_panel_memView, wx.ID_ANY, u"Write", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_memView.Add( self.m_button_writeMem, 0, wx.ALL, 5 )

		self.m_staticText_null3MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_null3MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null3MemView, 0, wx.ALL, 5 )

		self.m_button_executeApp = wx.Button( self.m_panel_memView, wx.ID_ANY, u"Execute", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_memView.Add( self.m_button_executeApp, 0, wx.ALL, 5 )

		self.m_textCtrl_bootDeviceMem = wx.TextCtrl( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 740,290 ), wx.TE_MULTILINE|wx.TE_RICH2 )
		self.m_textCtrl_bootDeviceMem.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_textCtrl_bootDeviceMem.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_memView.Add( self.m_textCtrl_bootDeviceMem, 0, wx.ALL, 5 )

		self.m_staticText_null4MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		self.m_staticText_null4MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null4MemView, 0, wx.ALL, 5 )

		self.m_button_viewMem = wx.Button( self.m_panel_memView, wx.ID_ANY, u"View Bootable Image", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		wSizer_memView.Add( self.m_button_viewMem, 0, wx.ALL, 5 )

		self.m_staticText_null5MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_null5MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null5MemView, 0, wx.ALL, 5 )

		self.m_button_clearMem = wx.Button( self.m_panel_memView, wx.ID_ANY, u"Clear The Screen", wx.DefaultPosition, wx.Size( 115,-1 ), 0 )
		wSizer_memView.Add( self.m_button_clearMem, 0, wx.ALL, 5 )

		self.m_staticText_null6MemView = wx.StaticText( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_null6MemView.Wrap( -1 )

		wSizer_memView.Add( self.m_staticText_null6MemView, 0, wx.ALL, 5 )

		self.m_checkBox_saveImageData = wx.CheckBox( self.m_panel_memView, wx.ID_ANY, u"Save image/data file to", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		wSizer_memView.Add( self.m_checkBox_saveImageData, 0, wx.ALL, 5 )

		self.m_filePicker_savedBinFile = wx.FilePickerCtrl( self.m_panel_memView, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 210,-1 ), wx.FLP_DEFAULT_STYLE )
		wSizer_memView.Add( self.m_filePicker_savedBinFile, 0, wx.ALL, 5 )


		self.m_panel_memView.SetSizer( wSizer_memView )
		self.m_panel_memView.Layout()
		wSizer_memView.Fit( self.m_panel_memView )
		self.m_notebook_imageSeq.AddPage( self.m_panel_memView, u"Boot Device Memory", False )

		bSizer_boot.Add( self.m_notebook_imageSeq, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_bootLog = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_panel_log = wx.Panel( self.m_notebook_bootLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_log.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_log = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_showLog = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_log = wx.TextCtrl( self.m_panel_log, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,68 ), wx.TE_MULTILINE )
		bSizer_showLog.Add( self.m_textCtrl_log, 0, wx.ALL, 5 )


		wSizer_log.Add( bSizer_showLog, 1, wx.EXPAND, 5 )

		bSizer_logAction = wx.BoxSizer( wx.VERTICAL )

		self.m_button_clearLog = wx.Button( self.m_panel_log, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_clearLog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_logAction.Add( self.m_button_clearLog, 0, wx.ALL, 5 )

		self.m_button_saveLog = wx.Button( self.m_panel_log, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_saveLog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_logAction.Add( self.m_button_saveLog, 0, wx.ALL, 5 )


		wSizer_log.Add( bSizer_logAction, 1, wx.EXPAND, 5 )

		wSizer_actionGauge = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_costTime = wx.StaticText( self.m_panel_log, wx.ID_ANY, u" 00:00.000", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText_costTime.Wrap( -1 )

		wSizer_actionGauge.Add( self.m_staticText_costTime, 0, wx.ALL, 5 )

		self.m_gauge_action = wx.Gauge( self.m_panel_log, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 680,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge_action.SetValue( 100 )
		wSizer_actionGauge.Add( self.m_gauge_action, 0, wx.ALL, 5 )

		self.m_staticText_null1ActionGauge = wx.StaticText( self.m_panel_log, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 750,1 ), 0 )
		self.m_staticText_null1ActionGauge.Wrap( -1 )

		wSizer_actionGauge.Add( self.m_staticText_null1ActionGauge, 0, wx.ALL, 5 )


		wSizer_log.Add( wSizer_actionGauge, 1, wx.EXPAND, 5 )


		self.m_panel_log.SetSizer( wSizer_log )
		self.m_panel_log.Layout()
		wSizer_log.Fit( self.m_panel_log )
		self.m_notebook_bootLog.AddPage( self.m_panel_log, u"Log", False )

		bSizer_boot.Add( self.m_notebook_bootLog, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer_func.Add( bSizer_boot, 1, wx.EXPAND, 5 )


		bSizer_win.Add( wSizer_func, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_win )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.Bind( wx.EVT_MENU, self.callbackExit, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetLanguageAsEnglish, id = self.m_menuItem_english.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetLanguageAsChinese, id = self.m_menuItem_chinese.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetRunModeAsEntry, id = self.m_menuItem_runModeEntry.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetRunModeAsMaster, id = self.m_menuItem_runModeMaster.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetUsbDetectionAsDynamic, id = self.m_menuItem_usbDetectionDynamic.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetUsbDetectionAsStatic, id = self.m_menuItem_usbDetectionStatic.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetSoundEffectAsMario, id = self.m_menuItem_soundEffectMario.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetSoundEffectAsQuiet, id = self.m_menuItem_soundEffectQuiet.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetGenSbFileAsYes, id = self.m_menuItem_genSbFileYes.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetGenSbFileAsNo, id = self.m_menuItem_genSbFileNo.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetImageReadbackAsAutomatic, id = self.m_menuItem_imageReadbackAutomatic.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackSetImageReadbackAsManual, id = self.m_menuItem_imageReadbackManual.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackShowHomePage, id = self.m_menuItem_homePage.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackShowAboutAuthor, id = self.m_menuItem_aboutAuthor.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackShowContributors, id = self.m_menuItem_contributors.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackShowSpecialThanks, id = self.m_menuItem_specialThanks.GetId() )
		self.Bind( wx.EVT_MENU, self.callbackShowRevisionHistory, id = self.m_menuItem_revisionHistory.GetId() )
		self.m_choice_mcuSeries.Bind( wx.EVT_CHOICE, self.callbackSetMcuSeries )
		self.m_choice_mcuDevice.Bind( wx.EVT_CHOICE, self.callbackSetMcuDevice )
		self.m_choice_bootDevice.Bind( wx.EVT_CHOICE, self.callbackSetBootDevice )
		self.m_button_bootDeviceConfiguration.Bind( wx.EVT_BUTTON, self.callbackBootDeviceConfiguration )
		self.m_button_deviceConfigurationData.Bind( wx.EVT_BUTTON, self.callbackDeviceConfigurationData )
		self.m_radioBtn_uart.Bind( wx.EVT_RADIOBUTTON, self.callbackSetUartPort )
		self.m_radioBtn_usbhid.Bind( wx.EVT_RADIOBUTTON, self.callbackSetUsbhidPort )
		self.m_checkBox_oneStepConnect.Bind( wx.EVT_CHECKBOX, self.callbackSetOneStep )
		self.m_button_connect.Bind( wx.EVT_BUTTON, self.callbackConnectToDevice )
		self.m_choice_secureBootType.Bind( wx.EVT_CHOICE, self.callbackSetSecureBootType )
		self.m_button_allInOneAction.Bind( wx.EVT_BUTTON, self.callbackAllInOneAction )
		self.m_button_advCertSettings.Bind( wx.EVT_BUTTON, self.callbackAdvCertSettings )
		self.m_button_genCert.Bind( wx.EVT_BUTTON, self.callbackGenCert )
		self.m_filePicker_appPath.Bind( wx.EVT_FILEPICKER_CHANGED, self.callbackChangedAppFile )
		self.m_choice_appFormat.Bind( wx.EVT_CHOICE, self.callbackSetAppFormat )
		self.m_choice_enableCertForBee.Bind( wx.EVT_CHOICE, self.callbackSetCertForBee )
		self.m_button_genImage.Bind( wx.EVT_BUTTON, self.callbackGenImage )
		self.m_choice_keyStorageRegion.Bind( wx.EVT_CHOICE, self.callbackSetKeyStorageRegion )
		self.m_button_advKeySettings.Bind( wx.EVT_BUTTON, self.callbackAdvKeySettings )
		self.m_button_prepBee.Bind( wx.EVT_BUTTON, self.callbackDoBeeEncryption )
		self.m_button_progSrk.Bind( wx.EVT_BUTTON, self.callbackProgramSrk )
		self.m_button_operBee.Bind( wx.EVT_BUTTON, self.callbackProgramBeeDek )
		self.m_button_flashImage.Bind( wx.EVT_BUTTON, self.callbackFlashImage )
		self.m_button_progDek.Bind( wx.EVT_BUTTON, self.callbackFlashHabDek )
		self.m_button_fuse400.Bind( wx.EVT_BUTTON, self.callbackSetEfuseLock )
		self.m_button_fuse450.Bind( wx.EVT_BUTTON, self.callbackSetEfuseBootCfg0 )
		self.m_button_fuse460.Bind( wx.EVT_BUTTON, self.callbackSetEfuseBootCfg1 )
		self.m_button_fuse470.Bind( wx.EVT_BUTTON, self.callbackSetEfuseBootCfg2 )
		self.m_textCtrl_fuse400.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseLock )
		self.m_textCtrl_fuse450.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseBootCfg0 )
		self.m_textCtrl_fuse460.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseBootCfg1 )
		self.m_textCtrl_fuse470.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseBootCfg2 )
		self.m_button_fuse6d0.Bind( wx.EVT_BUTTON, self.callbackSetEfuseMiscConf0 )
		self.m_button_fuse6e0.Bind( wx.EVT_BUTTON, self.callbackSetEfuseMiscConf1 )
		self.m_textCtrl_fuse6d0.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseMiscConf0 )
		self.m_textCtrl_fuse6e0.Bind( wx.EVT_TEXT_ENTER, self.callbackEnterEfuseMiscConf1 )
		self.m_button_scan.Bind( wx.EVT_BUTTON, self.callbackScanFuse )
		self.m_button_burn.Bind( wx.EVT_BUTTON, self.callbackBurnFuse )
		self.m_button_readMem.Bind( wx.EVT_BUTTON, self.callbackReadMem )
		self.m_button_eraseMem.Bind( wx.EVT_BUTTON, self.callbackEraseMem )
		self.m_button_writeMem.Bind( wx.EVT_BUTTON, self.callbackWriteMem )
		self.m_button_executeApp.Bind( wx.EVT_BUTTON, self.callbackExecuteApp )
		self.m_button_viewMem.Bind( wx.EVT_BUTTON, self.callbackViewMem )
		self.m_button_clearMem.Bind( wx.EVT_BUTTON, self.callbackClearMem )
		self.m_button_clearLog.Bind( wx.EVT_BUTTON, self.callbackClearLog )
		self.m_button_saveLog.Bind( wx.EVT_BUTTON, self.callbackSaveLog )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackExit( self, event ):
		event.Skip()

	def callbackSetLanguageAsEnglish( self, event ):
		event.Skip()

	def callbackSetLanguageAsChinese( self, event ):
		event.Skip()

	def callbackSetRunModeAsEntry( self, event ):
		event.Skip()

	def callbackSetRunModeAsMaster( self, event ):
		event.Skip()

	def callbackSetUsbDetectionAsDynamic( self, event ):
		event.Skip()

	def callbackSetUsbDetectionAsStatic( self, event ):
		event.Skip()

	def callbackSetSoundEffectAsMario( self, event ):
		event.Skip()

	def callbackSetSoundEffectAsQuiet( self, event ):
		event.Skip()

	def callbackSetGenSbFileAsYes( self, event ):
		event.Skip()

	def callbackSetGenSbFileAsNo( self, event ):
		event.Skip()

	def callbackSetImageReadbackAsAutomatic( self, event ):
		event.Skip()

	def callbackSetImageReadbackAsManual( self, event ):
		event.Skip()

	def callbackShowHomePage( self, event ):
		event.Skip()

	def callbackShowAboutAuthor( self, event ):
		event.Skip()

	def callbackShowContributors( self, event ):
		event.Skip()

	def callbackShowSpecialThanks( self, event ):
		event.Skip()

	def callbackShowRevisionHistory( self, event ):
		event.Skip()

	def callbackSetMcuSeries( self, event ):
		event.Skip()

	def callbackSetMcuDevice( self, event ):
		event.Skip()

	def callbackSetBootDevice( self, event ):
		event.Skip()

	def callbackBootDeviceConfiguration( self, event ):
		event.Skip()

	def callbackDeviceConfigurationData( self, event ):
		event.Skip()

	def callbackSetUartPort( self, event ):
		event.Skip()

	def callbackSetUsbhidPort( self, event ):
		event.Skip()

	def callbackSetOneStep( self, event ):
		event.Skip()

	def callbackConnectToDevice( self, event ):
		event.Skip()

	def callbackSetSecureBootType( self, event ):
		event.Skip()

	def callbackAllInOneAction( self, event ):
		event.Skip()

	def callbackAdvCertSettings( self, event ):
		event.Skip()

	def callbackGenCert( self, event ):
		event.Skip()

	def callbackChangedAppFile( self, event ):
		event.Skip()

	def callbackSetAppFormat( self, event ):
		event.Skip()

	def callbackSetCertForBee( self, event ):
		event.Skip()

	def callbackGenImage( self, event ):
		event.Skip()

	def callbackSetKeyStorageRegion( self, event ):
		event.Skip()

	def callbackAdvKeySettings( self, event ):
		event.Skip()

	def callbackDoBeeEncryption( self, event ):
		event.Skip()

	def callbackProgramSrk( self, event ):
		event.Skip()

	def callbackProgramBeeDek( self, event ):
		event.Skip()

	def callbackFlashImage( self, event ):
		event.Skip()

	def callbackFlashHabDek( self, event ):
		event.Skip()

	def callbackSetEfuseLock( self, event ):
		event.Skip()

	def callbackSetEfuseBootCfg0( self, event ):
		event.Skip()

	def callbackSetEfuseBootCfg1( self, event ):
		event.Skip()

	def callbackSetEfuseBootCfg2( self, event ):
		event.Skip()

	def callbackEnterEfuseLock( self, event ):
		event.Skip()

	def callbackEnterEfuseBootCfg0( self, event ):
		event.Skip()

	def callbackEnterEfuseBootCfg1( self, event ):
		event.Skip()

	def callbackEnterEfuseBootCfg2( self, event ):
		event.Skip()

	def callbackSetEfuseMiscConf0( self, event ):
		event.Skip()

	def callbackSetEfuseMiscConf1( self, event ):
		event.Skip()

	def callbackEnterEfuseMiscConf0( self, event ):
		event.Skip()

	def callbackEnterEfuseMiscConf1( self, event ):
		event.Skip()

	def callbackScanFuse( self, event ):
		event.Skip()

	def callbackBurnFuse( self, event ):
		event.Skip()

	def callbackReadMem( self, event ):
		event.Skip()

	def callbackEraseMem( self, event ):
		event.Skip()

	def callbackWriteMem( self, event ):
		event.Skip()

	def callbackExecuteApp( self, event ):
		event.Skip()

	def callbackViewMem( self, event ):
		event.Skip()

	def callbackClearMem( self, event ):
		event.Skip()

	def callbackClearLog( self, event ):
		event.Skip()

	def callbackSaveLog( self, event ):
		event.Skip()


