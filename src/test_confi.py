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
## Class MyFrame_SEMC_NOR
###########################################################################

class MyFrame_SEMC_NOR ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SEMC_NOR", pos = wx.DefaultPosition, size = wx.Size( 483,229 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		sbSizer_SEMC_NOR = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.staticText_SEMC_NOR = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Configurations of SEMC NOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SEMC_NOR.Wrap( -1 )
		
		sbSizer_SEMC_NOR.Add( self.staticText_SEMC_NOR, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_SEMC_NOR = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.staticText_PCS_Port = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"PCS Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PCS_Port.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_PCS_Port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_PCS_PortChoices = [ u"CSX0", u"CSX1", u"CSX2", u"CSX3", u"A8" ]
		self.comboBox_PCS_Port = wx.ComboBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"PCS Port Select! ", wx.DefaultPosition, wx.Size( 125,25 ), comboBox_PCS_PortChoices, 0 )
		wSizer_SEMC_NOR.Add( self.comboBox_PCS_Port, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.staticText_ADV_Polarity = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"     ADV Port Polarity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ADV_Polarity.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_ADV_Polarity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_ADV_PolarityChoices = [ u"Low active", u"High active" ]
		self.comboBox_ADV_Polarity = wx.ComboBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"ADV Polarity!", wx.DefaultPosition, wx.Size( 125,25 ), comboBox_ADV_PolarityChoices, 0 )
		wSizer_SEMC_NOR.Add( self.comboBox_ADV_Polarity, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.staticText_DataPort_Size = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Data Port Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_DataPort_Size.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_DataPort_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_DataPort_SizeChoices = [ u"8bits", u"8bits", u"16bits", u"24bits" ]
		self.comboBox_DataPort_Size = wx.ComboBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Data Port Size!", wx.DefaultPosition, wx.Size( 100,25 ), comboBox_DataPort_SizeChoices, 0 )
		wSizer_SEMC_NOR.Add( self.comboBox_DataPort_Size, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.staticText_Timing_Mode = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"     AC Timing Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Timing_Mode.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_Timing_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_Timing_ModeChoices = [ u"Safe mode", u"Fast mode", u"User defined(Field 0x04-0x19)" ]
		self.comboBox_Timing_Mode = wx.ComboBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Timing Mode!", wx.DefaultPosition, wx.Size( 125,25 ), comboBox_Timing_ModeChoices, 0 )
		wSizer_SEMC_NOR.Add( self.comboBox_Timing_Mode, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.staticText_Command_Set = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Command Set:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Command_Set.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_Command_Set, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_Command_SetChoices = [ u"EPSCD - As Micron MT28EW", u"SFMCD - As Micron MT28GU" ]
		self.comboBox_Command_Set = wx.ComboBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Command Set!", wx.DefaultPosition, wx.Size( 160,25 ), comboBox_Command_SetChoices, 0 )
		wSizer_SEMC_NOR.Add( self.comboBox_Command_Set, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer_SEMC_NOR.Add( wSizer_SEMC_NOR, 1, wx.EXPAND, 5 )
		
		sdbSizer_SEMC_NOR = wx.StdDialogButtonSizer()
		self.sdbSizer_SEMC_NOROK = wx.Button( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_OK )
		sdbSizer_SEMC_NOR.AddButton( self.sdbSizer_SEMC_NOROK )
		self.sdbSizer_SEMC_NORCancel = wx.Button( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_CANCEL )
		sdbSizer_SEMC_NOR.AddButton( self.sdbSizer_SEMC_NORCancel )
		sdbSizer_SEMC_NOR.Realize();
		
		sbSizer_SEMC_NOR.Add( sdbSizer_SEMC_NOR, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer_SEMC_NOR )
		self.Layout()
		
		self.Centre( wx.BOTH )


		
		self.sdbSizer_SEMC_NORCancel.Bind( wx.EVT_BUTTON, self.cancel_of_SEMC_NOR )
		self.sdbSizer_SEMC_NOROK.Bind( wx.EVT_BUTTON, self.apply_of_SEMC_NOR )
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def cancel_of_SEMC_NOR( self, event ):
                
                self.Show(False)
                event.Skip()
	
	def apply_of_SEMC_NOR( self, event ):
                
                self.Show(False)
		event.Skip()

###########################################################################
## Class MyFrame_SEMC_NAND
###########################################################################

class MyFrame_SEMC_NAND ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SEMC_NAND", pos = wx.DefaultPosition, size = wx.Size( 479,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		sbSizer_SEMC_NAND = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.staticText_SEMC_NAND = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Configuration of SEMC NAND", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SEMC_NAND.Wrap( -1 )
		
		sbSizer_SEMC_NAND.Add( self.staticText_SEMC_NAND, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.staticText_ECC_Status = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Device ECC Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ECC_Status.Wrap( -1 )
		
		wSizer1.Add( self.staticText_ECC_Status, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_ECC_StatusChoices = [ u"Enable", u"Disable" ]
		self.comboBox_ECC_Status = wx.ComboBox( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"ECC Status!", wx.DefaultPosition, wx.Size( 100,25 ), comboBox_ECC_StatusChoices, 0 )
		wSizer1.Add( self.comboBox_ECC_Status, 0, wx.ALL, 5 )
		
		self.staticText_ECC_Type = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"ECC Check Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ECC_Type.Wrap( -1 )
		
		wSizer1.Add( self.staticText_ECC_Type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_ECC_TypeChoices = [ u"Software (1bit SEC)", u"Hardware (Device)" ]
		self.comboBox_ECC_Type = wx.ComboBox( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"ECC Type!", wx.DefaultPosition, wx.Size( 120,-1 ), comboBox_ECC_TypeChoices, 0 )
		wSizer1.Add( self.comboBox_ECC_Type, 0, wx.ALL, 5 )
		
		self.staticText_DatePort_Size = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"IO Port Size:           ", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.staticText_DatePort_Size.Wrap( -1 )
		
		wSizer1.Add( self.staticText_DatePort_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_DatePort_SizeChoices = [ u"8bits", u"16bits" ]
		self.comboBox_DatePort_Size = wx.ComboBox( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Data Port Size!", wx.Point( -1,-1 ), wx.Size( 100,-1 ), comboBox_DatePort_SizeChoices, 0 )
		wSizer1.Add( self.comboBox_DatePort_Size, 0, wx.ALL, 5 )
		
		self.staticText_EDO_Mode = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"EDO Mode:           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EDO_Mode.Wrap( -1 )
		
		wSizer1.Add( self.staticText_EDO_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBox_EDO_ModeChoices = [ u"EDO Disable", u"EDO Enable" ]
		self.comboBox_EDO_Mode = wx.ComboBox( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"EDO Mode!", wx.DefaultPosition, wx.DefaultSize, comboBox_EDO_ModeChoices, 0 )
		wSizer1.Add( self.comboBox_EDO_Mode, 0, wx.ALL, 5 )
		
		
		sbSizer_SEMC_NAND.Add( wSizer1, 1, wx.EXPAND, 5 )
		
		sdbSizer_SEMC_NAND = wx.StdDialogButtonSizer()
		self.sdbSizer_SEMC_NANDOK = wx.Button( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_OK )
		sdbSizer_SEMC_NAND.AddButton( self.sdbSizer_SEMC_NANDOK )
		self.sdbSizer_SEMC_NANDCancel = wx.Button( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_CANCEL )
		sdbSizer_SEMC_NAND.AddButton( self.sdbSizer_SEMC_NANDCancel )
		sdbSizer_SEMC_NAND.Realize();
		
		sbSizer_SEMC_NAND.Add( sdbSizer_SEMC_NAND, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer_SEMC_NAND )
		self.Layout()
		
		self.Centre( wx.BOTH )


		
		self.sdbSizer_SEMC_NANDCancel.Bind( wx.EVT_BUTTON, self.cancel_of_SEMC_NAND )
		self.sdbSizer_SEMC_NANDOK.Bind( wx.EVT_BUTTON, self.apply_of_SEMC_NAND )
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def cancel_of_SEMC_NAND( self, event ):
                
                self.Show(False)
                event.Skip()
	
	def apply_of_SEMC_NAND( self, event ):
                
                self.Show(False)
		event.Skip()
	
###########################################################################
## Class secBootWin
###########################################################################

class secBootWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"nxpSecBoot", pos = wx.DefaultPosition, size = wx.Size( 930,730 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_help = wx.Menu()
		self.m_menu_about = wx.Menu()
		self.m_menu_help.AppendSubMenu( self.m_menu_about, u"About" )

		self.m_menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar )

		bSizer_win = wx.BoxSizer( wx.VERTICAL )

		wSizer_logo = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1Logo = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
		self.m_staticText_null1Logo.Wrap( -1 )

		wSizer_logo.Add( self.m_staticText_null1Logo, 0, wx.ALL, 5 )

		self.m_bitmap_nxp = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 80,30 ), 0 )
		wSizer_logo.Add( self.m_bitmap_nxp, 0, wx.ALL, 5 )


		bSizer_win.Add( wSizer_logo, 1, wx.EXPAND, 5 )

		wSizer_func = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_setup = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_targetSetup = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), 0 )
		self.m_panel_targetSetup = wx.Panel( self.m_notebook_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_targetSetup.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_targetSetup = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_mcuSeries = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"MCU Series:", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText_mcuSeries.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_mcuSeries, 0, wx.ALL, 5 )

		m_choice_mcuSeriesChoices = [ u"i.MXRT", u"LPC", u"Kinetis" ]
		self.m_choice_mcuSeries = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 135,-1 ), m_choice_mcuSeriesChoices, 0 )
		self.m_choice_mcuSeries.SetSelection( 0 )
		wSizer_targetSetup.Add( self.m_choice_mcuSeries, 0, wx.ALL, 5 )

		self.m_staticText_mcuDevice = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"MCU Device:", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText_mcuDevice.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_mcuDevice, 0, wx.ALL, 5 )

		m_choice_mcuDeviceChoices = [ u"i.MXRT105x", u"i.MXRT106x", u"i.MXRT102x" ]
		self.m_choice_mcuDevice = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 135,-1 ), m_choice_mcuDeviceChoices, 0 )
		self.m_choice_mcuDevice.SetSelection( 0 )
		wSizer_targetSetup.Add( self.m_choice_mcuDevice, 0, wx.ALL, 5 )

		self.m_staticText_bootDevice = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, u"Boot Device:", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText_bootDevice.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_bootDevice, 0, wx.ALL, 5 )

		m_choice_bootDeviceChoices = [ u"FLEXSPI NOR", u"FLEXSPI NAND", u"SEMC NOR", u"SEMC NAND", u"SD/eMMC", u"LPSPI NOR,EEPROM" ]
		self.m_choice_bootDevice = wx.Choice( self.m_panel_targetSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 135,-1 ), m_choice_bootDeviceChoices, 0 )
		self.m_choice_bootDevice.SetSelection( 0 )
		wSizer_targetSetup.Add( self.m_choice_bootDevice, 0, wx.ALL, 5 )

		self.m_staticText_null1TargetSetup = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 226,5 ), 0 )
		self.m_staticText_null1TargetSetup.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_null1TargetSetup, 0, wx.ALL, 5 )

		self.m_staticText_null2TargetSetup = wx.StaticText( self.m_panel_targetSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 15,-1 ), 0 )
		self.m_staticText_null2TargetSetup.Wrap( -1 )

		wSizer_targetSetup.Add( self.m_staticText_null2TargetSetup, 0, wx.ALL, 5 )

		self.m_button_BootDeviceConfiguration = wx.Button( self.m_panel_targetSetup, wx.ID_ANY, u"Boot Device Configuration", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		wSizer_targetSetup.Add( self.m_button_BootDeviceConfiguration, 0, wx.ALL, 5 )


		self.m_panel_targetSetup.SetSizer( wSizer_targetSetup )
		self.m_panel_targetSetup.Layout()
		wSizer_targetSetup.Fit( self.m_panel_targetSetup )
		self.m_notebook_targetSetup.AddPage( self.m_panel_targetSetup, u"Target Setup", False )

		bSizer_setup.Add( self.m_notebook_targetSetup, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_portSetup = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_portSetup = wx.Panel( self.m_notebook_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer_portSetup = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		self.m_staticText_null1PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null1PortSetup, 0, wx.ALL, 5 )

		self.m_radioBtn_uart = wx.RadioButton( self.m_panel_portSetup, wx.ID_ANY, u"UART", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		wSizer_portSetup.Add( self.m_radioBtn_uart, 0, wx.ALL, 5 )

		self.m_radioBtn_usbhid = wx.RadioButton( self.m_panel_portSetup, wx.ID_ANY, u"USB-HID", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		wSizer_portSetup.Add( self.m_radioBtn_usbhid, 0, wx.ALL, 5 )

		self.m_staticText_portVid = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, u"COM Port:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_portVid.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_portVid, 0, wx.ALL, 5 )

		m_choice_portVidChoices = []
		self.m_choice_portVid = wx.Choice( self.m_panel_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 155,-1 ), m_choice_portVidChoices, 0 )
		self.m_choice_portVid.SetSelection( 0 )
		wSizer_portSetup.Add( self.m_choice_portVid, 0, wx.ALL, 5 )

		self.m_staticText_baudPid = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, u"Baudrate:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_baudPid.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_baudPid, 0, wx.ALL, 5 )

		m_choice_baudPidChoices = []
		self.m_choice_baudPid = wx.Choice( self.m_panel_portSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( 155,-1 ), m_choice_baudPidChoices, 0 )
		self.m_choice_baudPid.SetSelection( 0 )
		wSizer_portSetup.Add( self.m_choice_baudPid, 0, wx.ALL, 5 )

		self.m_staticText_null2PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 226,5 ), 0 )
		self.m_staticText_null2PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null2PortSetup, 0, wx.ALL, 5 )

		self.m_staticText_null3PortSetup = wx.StaticText( self.m_panel_portSetup, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_null3PortSetup.Wrap( -1 )

		wSizer_portSetup.Add( self.m_staticText_null3PortSetup, 0, wx.ALL, 5 )

		self.m_bitmap_connectLed = wx.StaticBitmap( self.m_panel_portSetup, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		wSizer_portSetup.Add( self.m_bitmap_connectLed, 0, wx.ALL, 5 )

		self.m_button_connect = wx.Button( self.m_panel_portSetup, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer_portSetup.Add( self.m_button_connect, 0, wx.ALL, 5 )


		self.m_panel_portSetup.SetSizer( wSizer_portSetup )
		self.m_panel_portSetup.Layout()
		wSizer_portSetup.Fit( self.m_panel_portSetup )
		self.m_notebook_portSetup.AddPage( self.m_panel_portSetup, u"Port Setup", False )

		bSizer_setup.Add( self.m_notebook_portSetup, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_deviceStatus = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel26 = wx.Panel( self.m_notebook_deviceStatus, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook_deviceStatus.AddPage( self.m_panel26, u"Device Status", False )

		bSizer_setup.Add( self.m_notebook_deviceStatus, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer_func.Add( bSizer_setup, 1, wx.EXPAND, 5 )

		bSizer_boot = wx.BoxSizer( wx.VERTICAL )

		wSizer_bootType = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1BootType = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 295,-1 ), 0 )
		self.m_staticText_null1BootType.Wrap( -1 )

		wSizer_bootType.Add( self.m_staticText_null1BootType, 0, wx.ALL, 5 )

		self.m_staticText_secureBootType = wx.StaticText( self, wx.ID_ANY, u"Secure Boot Type:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText_secureBootType.Wrap( -1 )

		wSizer_bootType.Add( self.m_staticText_secureBootType, 0, wx.ALL, 5 )

		m_choice_secureBootTypeChoices = [ u"Unsigned (XIP) image Boot", u"Signed (XIP) Image Boot", u"HAB Signed Encrypted Image Boot", u"BEE (Signed) Encrypted XIP Image Boot" ]
		self.m_choice_secureBootType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_secureBootTypeChoices, 0 )
		self.m_choice_secureBootType.SetSelection( 0 )
		wSizer_bootType.Add( self.m_choice_secureBootType, 0, wx.ALL, 5 )


		bSizer_boot.Add( wSizer_bootType, 1, wx.EXPAND, 5 )

		self.m_notebook_imageSeq = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,400 ), 0 )
		self.m_notebook_imageSeq.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel_genSeq = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_genSeq.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel_genSeq.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		wSizer_genSeq = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_panel_doAuth = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_doAuth.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		bSizer_doAuth = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_doAuth1_certInput = wx.Panel( self.m_panel_doAuth, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_certInput = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_doAuth1_certInput, wx.ID_ANY, u"Step 1:" ), wx.VERTICAL )

		self.m_staticText_serial = wx.StaticText( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"serial (8 digits):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_serial.Wrap( -1 )

		sbSizer_certInput.Add( self.m_staticText_serial, 0, wx.ALL, 5 )

		self.m_textCtrl_serial = wx.TextCtrl( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"12345678", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		sbSizer_certInput.Add( self.m_textCtrl_serial, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_keyPass = wx.StaticText( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"key_pass (text):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keyPass.Wrap( -1 )

		sbSizer_certInput.Add( self.m_staticText_keyPass, 0, wx.ALL, 5 )

		self.m_textCtrl_keyPass = wx.TextCtrl( sbSizer_certInput.GetStaticBox(), wx.ID_ANY, u"abcdefg", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer_certInput.Add( self.m_textCtrl_keyPass, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth1_certInput.SetSizer( sbSizer_certInput )
		self.m_panel_doAuth1_certInput.Layout()
		sbSizer_certInput.Fit( self.m_panel_doAuth1_certInput )
		bSizer_doAuth.Add( self.m_panel_doAuth1_certInput, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_doAuth2_certFmt = wx.Panel( self.m_panel_doAuth, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_certFmt = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_doAuth2_certFmt, wx.ID_ANY, u"Certificate Format:" ), wx.VERTICAL )

		m_choice_certFmtChoices = [ u"X.509v3" ]
		self.m_choice_certFmt = wx.Choice( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_certFmtChoices, 0 )
		self.m_choice_certFmt.SetSelection( 0 )
		sbSizer_certFmt.Add( self.m_choice_certFmt, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_hashAlgo = wx.StaticText( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, u"Hash Algorithm:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_hashAlgo.Wrap( -1 )

		sbSizer_certFmt.Add( self.m_staticText_hashAlgo, 0, wx.ALL, 5 )

		m_choice_hashAlgoChoices = [ u"SHA-256" ]
		self.m_choice_hashAlgo = wx.Choice( sbSizer_certFmt.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_hashAlgoChoices, 0 )
		self.m_choice_hashAlgo.SetSelection( 0 )
		sbSizer_certFmt.Add( self.m_choice_hashAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth2_certFmt.SetSizer( sbSizer_certFmt )
		self.m_panel_doAuth2_certFmt.Layout()
		sbSizer_certFmt.Fit( self.m_panel_doAuth2_certFmt )
		bSizer_doAuth.Add( self.m_panel_doAuth2_certFmt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_doAuth = wx.Button( self.m_panel_doAuth, wx.ID_ANY, u"Run CST Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_doAuth.Add( self.m_button_doAuth, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_doAuth.SetSizer( bSizer_doAuth )
		self.m_panel_doAuth.Layout()
		bSizer_doAuth.Fit( self.m_panel_doAuth )
		wSizer_genSeq.Add( self.m_panel_doAuth, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_genImage = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_genImage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		bSizer_genImage = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_genImage1_browseApp = wx.Panel( self.m_panel_genImage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_browseApp = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_genImage1_browseApp, wx.ID_ANY, u"Step 3:" ), wx.VERTICAL )

		self.m_staticText_appPath = wx.StaticText( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"App Image File (.elf/.srec):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_appPath.Wrap( -1 )

		sbSizer_browseApp.Add( self.m_staticText_appPath, 0, wx.ALL, 5 )

		self.m_filePicker_appPath = wx.FilePickerCtrl( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 260,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer_browseApp.Add( self.m_filePicker_appPath, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText_bdPath = wx.StaticText( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"Matched BD File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_bdPath.Wrap( -1 )

		sbSizer_browseApp.Add( self.m_staticText_bdPath, 0, wx.ALL, 5 )

		self.m_textCtrl_bdPath = wx.TextCtrl( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"example.bd", wx.DefaultPosition, wx.Size( 260,-1 ), 0 )
		self.m_textCtrl_bdPath.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_browseApp.Add( self.m_textCtrl_bdPath, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button_advBdSettings = wx.Button( sbSizer_browseApp.GetStaticBox(), wx.ID_ANY, u"Advanced BD Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_browseApp.Add( self.m_button_advBdSettings, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage1_browseApp.SetSizer( sbSizer_browseApp )
		self.m_panel_genImage1_browseApp.Layout()
		sbSizer_browseApp.Fit( self.m_panel_genImage1_browseApp )
		bSizer_genImage.Add( self.m_panel_genImage1_browseApp, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_genImage2_habCryptoAlgo = wx.Panel( self.m_panel_genImage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sbSizer_habCryptoAlgo = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_genImage2_habCryptoAlgo, wx.ID_ANY, u"HAB Encryption Algorithm:" ), wx.VERTICAL )

		m_choice_habCryptoAlgoChoices = [ u"AES-128" ]
		self.m_choice_habCryptoAlgo = wx.Choice( sbSizer_habCryptoAlgo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_habCryptoAlgoChoices, 0 )
		self.m_choice_habCryptoAlgo.SetSelection( 0 )
		sbSizer_habCryptoAlgo.Add( self.m_choice_habCryptoAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage2_habCryptoAlgo.SetSizer( sbSizer_habCryptoAlgo )
		self.m_panel_genImage2_habCryptoAlgo.Layout()
		sbSizer_habCryptoAlgo.Fit( self.m_panel_genImage2_habCryptoAlgo )
		bSizer_genImage.Add( self.m_panel_genImage2_habCryptoAlgo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_genImage = wx.Button( self.m_panel_genImage, wx.ID_ANY, u"Run elftosb Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_genImage.Add( self.m_button_genImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_genImage.SetSizer( bSizer_genImage )
		self.m_panel_genImage.Layout()
		bSizer_genImage.Fit( self.m_panel_genImage )
		wSizer_genSeq.Add( self.m_panel_genImage, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee = wx.Panel( self.m_panel_genSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_prepBee = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_prepBee1_beeKeyRegion = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_keyStorageRegion = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee1_beeKeyRegion, wx.ID_ANY, u"Step 5:" ), wx.VERTICAL )

		self.m_staticText_keyStorageRegion = wx.StaticText( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, u"Key Storage Region:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keyStorageRegion.Wrap( -1 )

		sbSizer_keyStorageRegion.Add( self.m_staticText_keyStorageRegion, 0, wx.ALL, 5 )

		m_choice_keyStorageRegionChoices = [ u"Fuse OTPMK", u"Fuse GP4", u"Fuse SW_GP2 ", u"Fuse GP4&SW_GP2", wx.EmptyString ]
		self.m_choice_keyStorageRegion = wx.Choice( sbSizer_keyStorageRegion.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_keyStorageRegionChoices, 0 )
		self.m_choice_keyStorageRegion.SetSelection( 0 )
		sbSizer_keyStorageRegion.Add( self.m_choice_keyStorageRegion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee1_beeKeyRegion.SetSizer( sbSizer_keyStorageRegion )
		self.m_panel_prepBee1_beeKeyRegion.Layout()
		sbSizer_keyStorageRegion.Fit( self.m_panel_prepBee1_beeKeyRegion )
		bSizer_prepBee.Add( self.m_panel_prepBee1_beeKeyRegion, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee2_beeKeyInput = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_beeKeyInput = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee2_beeKeyInput, wx.ID_ANY, u"User Encryption Key:" ), wx.VERTICAL )

		self.m_textCtrl_beeKeyInput = wx.TextCtrl( sbSizer_beeKeyInput.GetStaticBox(), wx.ID_ANY, u"ABCDEFABCDEFABCD", wx.DefaultPosition, wx.Size( 145,40 ), wx.TE_MULTILINE )
		sbSizer_beeKeyInput.Add( self.m_textCtrl_beeKeyInput, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee2_beeKeyInput.SetSizer( sbSizer_beeKeyInput )
		self.m_panel_prepBee2_beeKeyInput.Layout()
		sbSizer_beeKeyInput.Fit( self.m_panel_prepBee2_beeKeyInput )
		bSizer_prepBee.Add( self.m_panel_prepBee2_beeKeyInput, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee3_advKeySettings = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_advKeySettings = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee3_advKeySettings, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_button_advKeySettings = wx.Button( sbSizer_advKeySettings.GetStaticBox(), wx.ID_ANY, u"Anvanced Key Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_advKeySettings.Add( self.m_button_advKeySettings, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee3_advKeySettings.SetSizer( sbSizer_advKeySettings )
		self.m_panel_prepBee3_advKeySettings.Layout()
		sbSizer_advKeySettings.Fit( self.m_panel_prepBee3_advKeySettings )
		bSizer_prepBee.Add( self.m_panel_prepBee3_advKeySettings, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_prepBee4_beeCryptoAlgo = wx.Panel( self.m_panel_prepBee, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_beeCryptoAlgo = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_prepBee4_beeCryptoAlgo, wx.ID_ANY, u"BEE Encryption Algorithm:" ), wx.VERTICAL )

		m_choice_beeCryptoAlgoChoices = [ u"AES-128" ]
		self.m_choice_beeCryptoAlgo = wx.Choice( sbSizer_beeCryptoAlgo.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_beeCryptoAlgoChoices, 0 )
		self.m_choice_beeCryptoAlgo.SetSelection( 0 )
		sbSizer_beeCryptoAlgo.Add( self.m_choice_beeCryptoAlgo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee4_beeCryptoAlgo.SetSizer( sbSizer_beeCryptoAlgo )
		self.m_panel_prepBee4_beeCryptoAlgo.Layout()
		sbSizer_beeCryptoAlgo.Fit( self.m_panel_prepBee4_beeCryptoAlgo )
		bSizer_prepBee.Add( self.m_panel_prepBee4_beeCryptoAlgo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_prepBee = wx.Button( self.m_panel_prepBee, wx.ID_ANY, u"Run image_enc Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_prepBee.Add( self.m_button_prepBee, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_prepBee.SetSizer( bSizer_prepBee )
		self.m_panel_prepBee.Layout()
		bSizer_prepBee.Fit( self.m_panel_prepBee )
		wSizer_genSeq.Add( self.m_panel_prepBee, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_genSeq.SetSizer( wSizer_genSeq )
		self.m_panel_genSeq.Layout()
		wSizer_genSeq.Fit( self.m_panel_genSeq )
		self.m_notebook_imageSeq.AddPage( self.m_panel_genSeq, u"Image Generation Sequence", True )
		self.m_panel_bootSeq = wx.Panel( self.m_notebook_imageSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_bootSeq.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )

		wSizer_bootSeq = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_panel_progSrk = wx.Panel( self.m_panel_bootSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_progSrk = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_progSrk1_showSrk = wx.Panel( self.m_panel_progSrk, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showSrk = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_progSrk1_showSrk, wx.ID_ANY, u"Step 2:" ), wx.VERTICAL )

		self.m_staticText_srk256bit = wx.StaticText( sbSizer_showSrk.GetStaticBox(), wx.ID_ANY, u"Program below public SRK data (256bits) to Fuse SRK Region:", wx.DefaultPosition, wx.Size( 100,60 ), 0 )
		self.m_staticText_srk256bit.Wrap( -1 )

		sbSizer_showSrk.Add( self.m_staticText_srk256bit, 0, wx.ALL, 5 )

		self.m_textCtrl_srk256bit = wx.TextCtrl( sbSizer_showSrk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,140 ), wx.TE_MULTILINE )
		self.m_textCtrl_srk256bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showSrk.Add( self.m_textCtrl_srk256bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progSrk1_showSrk.SetSizer( sbSizer_showSrk )
		self.m_panel_progSrk1_showSrk.Layout()
		sbSizer_showSrk.Fit( self.m_panel_progSrk1_showSrk )
		bSizer_progSrk.Add( self.m_panel_progSrk1_showSrk, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_progSrk = wx.Button( self.m_panel_progSrk, wx.ID_ANY, u"Run blhost Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_progSrk.Add( self.m_button_progSrk, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progSrk.SetSizer( bSizer_progSrk )
		self.m_panel_progSrk.Layout()
		bSizer_progSrk.Fit( self.m_panel_progSrk )
		wSizer_bootSeq.Add( self.m_panel_progSrk, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_progDek = wx.Panel( self.m_panel_bootSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_progDek = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_progDek1_showDek = wx.Panel( self.m_panel_progDek, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_showDek = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_progDek1_showDek, wx.ID_ANY, u"Step 4:" ), wx.VERTICAL )

		self.m_staticText_dek128bit = wx.StaticText( sbSizer_showDek.GetStaticBox(), wx.ID_ANY, u"Use below DEK data (128bits) to generate keyblob and program it to flash for HAB:", wx.DefaultPosition, wx.Size( 100,80 ), 0 )
		self.m_staticText_dek128bit.Wrap( -1 )

		sbSizer_showDek.Add( self.m_staticText_dek128bit, 0, wx.ALL, 5 )

		self.m_textCtrl_dek128bit = wx.TextCtrl( sbSizer_showDek.GetStaticBox(), wx.ID_ANY, u"01234567\nABCDEFAB\n01234567\n89abcde", wx.DefaultPosition, wx.Size( 100,70 ), wx.TE_MULTILINE )
		self.m_textCtrl_dek128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_showDek.Add( self.m_textCtrl_dek128bit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progDek1_showDek.SetSizer( sbSizer_showDek )
		self.m_panel_progDek1_showDek.Layout()
		sbSizer_showDek.Fit( self.m_panel_progDek1_showDek )
		bSizer_progDek.Add( self.m_panel_progDek1_showDek, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_progDek = wx.Button( self.m_panel_progDek, wx.ID_ANY, u"Run blhost Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_progDek.Add( self.m_button_progDek, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_progDek.SetSizer( bSizer_progDek )
		self.m_panel_progDek.Layout()
		bSizer_progDek.Fit( self.m_panel_progDek )
		wSizer_bootSeq.Add( self.m_panel_progDek, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_operBeeKey = wx.Panel( self.m_panel_bootSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_operBeeKey = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_operBeeKey1_readOtpmk = wx.Panel( self.m_panel_operBeeKey, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_readOtpmk = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_operBeeKey1_readOtpmk, wx.ID_ANY, u"Step 6:" ), wx.VERTICAL )

		self.m_staticText_otpmk128bit = wx.StaticText( sbSizer_readOtpmk.GetStaticBox(), wx.ID_ANY, u"Readback default encryption key data from Fuse OTPMK region:", wx.DefaultPosition, wx.Size( 135,50 ), 0 )
		self.m_staticText_otpmk128bit.Wrap( -1 )

		sbSizer_readOtpmk.Add( self.m_staticText_otpmk128bit, 0, wx.ALL, 5 )

		self.m_textCtrl_otpmk128bit = wx.TextCtrl( sbSizer_readOtpmk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,40 ), wx.TE_MULTILINE )
		self.m_textCtrl_otpmk128bit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		sbSizer_readOtpmk.Add( self.m_textCtrl_otpmk128bit, 0, wx.ALL, 5 )


		self.m_panel_operBeeKey1_readOtpmk.SetSizer( sbSizer_readOtpmk )
		self.m_panel_operBeeKey1_readOtpmk.Layout()
		sbSizer_readOtpmk.Fit( self.m_panel_operBeeKey1_readOtpmk )
		bSizer_operBeeKey.Add( self.m_panel_operBeeKey1_readOtpmk, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_operBeeKey2_progBeeKey = wx.Panel( self.m_panel_operBeeKey, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer_progBeeKey = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_operBeeKey2_progBeeKey, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText_progBeeKey = wx.StaticText( sbSizer_progBeeKey.GetStaticBox(), wx.ID_ANY, u"Program user encryption key data in Fuse Key Region for BEE:", wx.DefaultPosition, wx.Size( 135,50 ), 0 )
		self.m_staticText_progBeeKey.Wrap( -1 )

		sbSizer_progBeeKey.Add( self.m_staticText_progBeeKey, 0, wx.ALL, 5 )


		self.m_panel_operBeeKey2_progBeeKey.SetSizer( sbSizer_progBeeKey )
		self.m_panel_operBeeKey2_progBeeKey.Layout()
		sbSizer_progBeeKey.Fit( self.m_panel_operBeeKey2_progBeeKey )
		bSizer_operBeeKey.Add( self.m_panel_operBeeKey2_progBeeKey, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_operBeeKey = wx.Button( self.m_panel_operBeeKey, wx.ID_ANY, u"Run blhost Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_operBeeKey.Add( self.m_button_operBeeKey, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_operBeeKey.SetSizer( bSizer_operBeeKey )
		self.m_panel_operBeeKey.Layout()
		bSizer_operBeeKey.Fit( self.m_panel_operBeeKey )
		wSizer_bootSeq.Add( self.m_panel_operBeeKey, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_flashImage = wx.Panel( self.m_panel_bootSeq, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_flashImage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		bSizer_flashImage = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_flashImage1_showImage = wx.Panel( self.m_panel_flashImage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel_flashImage1_showImage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		sbSizer_showImage = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_flashImage1_showImage, wx.ID_ANY, u"Step 7:" ), wx.VERTICAL )

		self.m_staticText_showImage = wx.StaticText( sbSizer_showImage.GetStaticBox(), wx.ID_ANY, u"Program final bootable image to flash:", wx.DefaultPosition, wx.Size( 120,100 ), 0 )
		self.m_staticText_showImage.Wrap( -1 )

		sbSizer_showImage.Add( self.m_staticText_showImage, 0, wx.ALL, 5 )

		self.m_bitmap_bootableImage = wx.StaticBitmap( sbSizer_showImage.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_showImage.Add( self.m_bitmap_bootableImage, 0, wx.ALL, 5 )


		self.m_panel_flashImage1_showImage.SetSizer( sbSizer_showImage )
		self.m_panel_flashImage1_showImage.Layout()
		sbSizer_showImage.Fit( self.m_panel_flashImage1_showImage )
		bSizer_flashImage.Add( self.m_panel_flashImage1_showImage, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_flashImage = wx.Button( self.m_panel_flashImage, wx.ID_ANY, u"Run blhost Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_flashImage.Add( self.m_button_flashImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel_flashImage.SetSizer( bSizer_flashImage )
		self.m_panel_flashImage.Layout()
		bSizer_flashImage.Fit( self.m_panel_flashImage )
		wSizer_bootSeq.Add( self.m_panel_flashImage, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel_bootSeq.SetSizer( wSizer_bootSeq )
		self.m_panel_bootSeq.Layout()
		wSizer_bootSeq.Fit( self.m_panel_bootSeq )
		self.m_notebook_imageSeq.AddPage( self.m_panel_bootSeq, u"Image Boot Sequence", False )

		bSizer_boot.Add( self.m_notebook_imageSeq, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_bootLog = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_panel_log = wx.Panel( self.m_notebook_bootLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_log.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_log = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_showLog = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_log = wx.TextCtrl( self.m_panel_log, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 530,85 ), wx.TE_MULTILINE )
		bSizer_showLog.Add( self.m_textCtrl_log, 0, wx.ALL, 5 )


		wSizer_log.Add( bSizer_showLog, 1, wx.EXPAND, 5 )

		bSizer_logAction = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_null1LogAction = wx.StaticText( self.m_panel_log, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,3 ), 0 )
		self.m_staticText_null1LogAction.Wrap( -1 )

		bSizer_logAction.Add( self.m_staticText_null1LogAction, 0, wx.ALL, 5 )

		self.m_button_clearLog = wx.Button( self.m_panel_log, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_clearLog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_logAction.Add( self.m_button_clearLog, 0, wx.ALL, 5 )

		self.m_button_saveLog = wx.Button( self.m_panel_log, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_saveLog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_logAction.Add( self.m_button_saveLog, 0, wx.ALL, 5 )


		wSizer_log.Add( bSizer_logAction, 1, wx.EXPAND, 5 )

		bSizer_actionGauge = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge_action = wx.Gauge( self.m_panel_log, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 630,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge_action.SetValue( 100 )
		bSizer_actionGauge.Add( self.m_gauge_action, 0, wx.ALL, 5 )


		wSizer_log.Add( bSizer_actionGauge, 1, wx.EXPAND, 5 )


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
		self.m_choice_secureBootType.Bind( wx.EVT_CHOICE, self.callbackSwitchSecureBootType )
		self.m_choice_keyStorageRegion.Bind( wx.EVT_CHOICE, self.callbackSwitchKeyStorageRegion )



		self.m_button_BootDeviceConfiguration.Bind( wx.EVT_BUTTON, self.Boot_Device_Configuration )
                self.m_button_BootDeviceConfiguration.SetToolTipString("This is Boot_Device_Configuration.")



		self.m_button_doAuth.Bind( wx.EVT_BUTTON, self.RUN_CST_Tool )
                self.m_button_doAuth.SetToolTipString("This is the first step to run CST tool.")
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Virtual event handlers, overide them in your derived class
	def callbackSwitchSecureBootType( self, event ):
		event.Skip()

	def callbackSwitchKeyStorageRegion( self, event ):
		event.Skip()

	def RUN_CST_Tool( self, event ):
                if frame2.m_checkBox3.GetValue() == 1:
                        print "choose 333:",frame2.m_checkBox2.GetValue()
                self.m_notebook_imageSeq.SetSelection(1)
                
		event.Skip()
	def Boot_Device_Configuration( self, event ):
                if frame.m_choice_mcuSeries.GetSelection() == 0:
                        if frame.m_choice_bootDevice.GetSelection() == 0:
                                frame_semc_nor = MyFrame_SEMC_NOR(None)
                                frame_semc_nor.Show(True)
                        elif frame.m_choice_bootDevice.GetSelection() == 1:
                                frame_semc_nand = MyFrame_SEMC_NAND(None)
                                frame_semc_nand.Show(True)
                        else :
                                dlg_boot = wx.MessageDialog(None,'Please select NOR OR NAND !', 'Confirmation',wx.OK|wx.ICON_QUESTION)
                                dlg_boot.ShowModal()
                else :
                        dlg_mcu = wx.MessageDialog(None,'Please select i.MXRT !', 'Confirmation',wx.OK|wx.ICON_QUESTION)
                        dlg_mcu.ShowModal()
                        
		event.Skip()


	
       
app=wx.App()
frame=secBootWin(None)
frame.Show(True)
app.MainLoop()
