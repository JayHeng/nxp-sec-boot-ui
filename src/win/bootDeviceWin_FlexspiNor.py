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
## Class bootDeviceWin_FlexspiNor
###########################################################################

class bootDeviceWin_FlexspiNor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 656,398 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_deviceModel = wx.StaticText( self, wx.ID_ANY, u"Use Typical Device Model:", wx.DefaultPosition, wx.Size( 149,-1 ), 0 )
		self.m_staticText_deviceModel.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_deviceModel, 0, wx.ALL, 5 )

		m_choice_deviceModeChoices = [ u"No", u"ISSI_IS25LPxxxA_IS25WPxxxA", u"ISSI_IS26KSxxxS", u"Macronix_MX25UMxxx45G_MX66UMxxx45G_MX25LMxxx45G", u"Macronix_MX25UM51345G", u"Micron_MT35X", u"Adesto_AT25SFxxxA", u"Adesto_ATXPxxx", u"Cypress_S26KSxxxS", u"GigaDevice_GD25LBxxxE", u"GigaDevice_GD25LTxxxE", u"GigaDevice_GD25LXxxxE", u"Winbond_W25QxxxJV" ]
		self.m_choice_deviceMode = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 340,-1 ), m_choice_deviceModeChoices, 0 )
		self.m_choice_deviceMode.SetSelection( 0 )
		wSizer_win.Add( self.m_choice_deviceMode, 0, wx.ALL, 5 )

		self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText_winNull0.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_winNull0, 0, wx.ALL, 5 )

		self.m_notebook_norOpt0 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_norOpt0 = wx.Panel( self.m_notebook_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_norOpt0 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_deviceType = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Device Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_deviceType.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_deviceType, 0, wx.ALL, 5 )

		m_choice_deviceTypeChoices = [ u"QuadSPI SDR NOR", u"QuadSPI DDR NOR", u"Hyper Flash 1.8V", u"Hyper Flash 3.0V", u"Macronix Octal DDR", u"Macronix Octal SDR", u"Micron Octal DDR", u"Micron Octal SDR", u"Adesto EcoXIP DDR", u"Adesto EcoXIP SDR" ]
		self.m_choice_deviceType = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_deviceTypeChoices, 0 )
		self.m_choice_deviceType.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_deviceType, 0, wx.ALL, 5 )

		self.m_staticText_queryPads = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Query Pads:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_queryPads.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_queryPads, 0, wx.ALL, 5 )

		m_choice_queryPadsChoices = [ u"1", u"4", u"8" ]
		self.m_choice_queryPads = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_queryPadsChoices, 0 )
		self.m_choice_queryPads.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_queryPads, 0, wx.ALL, 5 )

		self.m_staticText_cmdPads = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Cmd Pads:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cmdPads.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_cmdPads, 0, wx.ALL, 5 )

		m_choice_cmdPadsChoices = [ u"1", u"4", u"8" ]
		self.m_choice_cmdPads = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_cmdPadsChoices, 0 )
		self.m_choice_cmdPads.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_cmdPads, 0, wx.ALL, 5 )

		self.m_staticText_quadModeSetting = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Quad Mode Setting:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_quadModeSetting.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_quadModeSetting, 0, wx.ALL, 5 )

		m_choice_quadModeSettingChoices = [ u"Not Configured", u"Set StatusReg1[6]", u"Set StatusReg2[1]", u"Set StatusReg2[7]", u"Set StatusReg2[1] by 0x31" ]
		self.m_choice_quadModeSetting = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_quadModeSettingChoices, 0 )
		self.m_choice_quadModeSetting.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_quadModeSetting, 0, wx.ALL, 5 )

		self.m_staticText_miscMode = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Misc Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_miscMode.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_miscMode, 0, wx.ALL, 5 )

		m_choice_miscModeChoices = [ u"Disabled", u"0_4_4 Mode", u"0_8_8 Mode", u"Data Order Swapped" ]
		self.m_choice_miscMode = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_miscModeChoices, 0 )
		self.m_choice_miscMode.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_miscMode, 0, wx.ALL, 5 )

		self.m_staticText_maxFrequency = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Max Frequency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_maxFrequency.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_maxFrequency, 0, wx.ALL, 5 )

		m_choice_maxFrequencyChoices = [ u"30MHz", u"50MHz", u"60MHz", u"75MHz", u"80MHz", u"100MHz", u"133MHz", u"166MHz" ]
		self.m_choice_maxFrequency = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_maxFrequencyChoices, 0 )
		self.m_choice_maxFrequency.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_maxFrequency, 0, wx.ALL, 5 )

		self.m_staticText_hasOption1 = wx.StaticText( self.m_panel_norOpt0, wx.ID_ANY, u"Has Option1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_hasOption1.Wrap( -1 )

		gSizer_norOpt0.Add( self.m_staticText_hasOption1, 0, wx.ALL, 5 )

		m_choice_hasOption1Choices = [ u"No", u"Yes" ]
		self.m_choice_hasOption1 = wx.Choice( self.m_panel_norOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_hasOption1Choices, 0 )
		self.m_choice_hasOption1.SetSelection( 0 )
		gSizer_norOpt0.Add( self.m_choice_hasOption1, 0, wx.ALL, 5 )


		self.m_panel_norOpt0.SetSizer( gSizer_norOpt0 )
		self.m_panel_norOpt0.Layout()
		gSizer_norOpt0.Fit( self.m_panel_norOpt0 )
		self.m_notebook_norOpt0.AddPage( self.m_panel_norOpt0, u"Nor Option0", False )

		wSizer_win.Add( self.m_notebook_norOpt0, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_norOpt1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_norOpt1 = wx.Panel( self.m_notebook_norOpt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_norOpt1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_flashConnection = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"Flash Connection:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_flashConnection.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_flashConnection, 0, wx.ALL, 5 )

		m_choice_flashConnectionChoices = [ u"Single Port A", u"Parallel", u"Single Port B", u"Both Ports" ]
		self.m_choice_flashConnection = wx.Choice( self.m_panel_norOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_flashConnectionChoices, 0 )
		self.m_choice_flashConnection.SetSelection( 0 )
		gSizer_norOpt1.Add( self.m_choice_flashConnection, 0, wx.ALL, 5 )

		self.m_staticText_driveStrength = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"Drive Strength:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_driveStrength.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_driveStrength, 0, wx.ALL, 5 )

		self.m_textCtrl_driveStrength = wx.TextCtrl( self.m_panel_norOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer_norOpt1.Add( self.m_textCtrl_driveStrength, 0, wx.ALL, 5 )

		self.m_staticText_dqsPinmuxGroup = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"DQS Pinmux Group:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_dqsPinmuxGroup.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_dqsPinmuxGroup, 0, wx.ALL, 5 )

		self.m_textCtrl_dqsPinmuxGroup = wx.TextCtrl( self.m_panel_norOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer_norOpt1.Add( self.m_textCtrl_dqsPinmuxGroup, 0, wx.ALL, 5 )

		self.m_staticText_enableSecondPinmux = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"Enable Second Pinmux:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_enableSecondPinmux.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_enableSecondPinmux, 0, wx.ALL, 5 )

		m_choice_enableSecondPinmuxChoices = [ u"No", u"Yes" ]
		self.m_choice_enableSecondPinmux = wx.Choice( self.m_panel_norOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enableSecondPinmuxChoices, 0 )
		self.m_choice_enableSecondPinmux.SetSelection( 0 )
		gSizer_norOpt1.Add( self.m_choice_enableSecondPinmux, 0, wx.ALL, 5 )

		self.m_staticText_statusOverride = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"Status Override:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_statusOverride.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_statusOverride, 0, wx.ALL, 5 )

		self.m_textCtrl_statusOverride = wx.TextCtrl( self.m_panel_norOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer_norOpt1.Add( self.m_textCtrl_statusOverride, 0, wx.ALL, 5 )

		self.m_staticText_dummyCycles = wx.StaticText( self.m_panel_norOpt1, wx.ID_ANY, u"Dummy Cycles:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		self.m_staticText_dummyCycles.Wrap( -1 )

		gSizer_norOpt1.Add( self.m_staticText_dummyCycles, 0, wx.ALL, 5 )

		self.m_textCtrl_dummyCycles = wx.TextCtrl( self.m_panel_norOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer_norOpt1.Add( self.m_textCtrl_dummyCycles, 0, wx.ALL, 5 )


		self.m_panel_norOpt1.SetSizer( gSizer_norOpt1 )
		self.m_panel_norOpt1.Layout()
		gSizer_norOpt1.Fit( self.m_panel_norOpt1 )
		self.m_notebook_norOpt1.AddPage( self.m_panel_norOpt1, u"Nor Option1", False )

		wSizer_win.Add( self.m_notebook_norOpt1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_winNull1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 356,-1 ), 0 )
		self.m_staticText_winNull1.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_winNull1, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_cancel, 0, wx.ALL, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_choice_deviceMode.Bind( wx.EVT_CHOICE, self.callbackUseTypicalDeviceModel )
		self.m_choice_hasOption1.Bind( wx.EVT_CHOICE, self.callbackHasOption1 )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackUseTypicalDeviceModel( self, event ):
		event.Skip()

	def callbackHasOption1( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


