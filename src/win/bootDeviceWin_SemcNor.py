# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class bootDeviceWin_SemcNor
###########################################################################

class bootDeviceWin_SemcNor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 661,371 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_deviceModel = wx.StaticText( self, wx.ID_ANY, u"Use Typical Device Model:", wx.DefaultPosition, wx.Size( 149,-1 ), 0 )
		self.m_staticText_deviceModel.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_deviceModel, 0, wx.ALL, 5 )

		m_choice_deviceMode_SEMCNORChoices = [ u"No", u"Micron_MT28EW128ABA", u"Micron_MT28UG128ABA" ]
		self.m_choice_deviceMode_SEMCNOR = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 240,-1 ), m_choice_deviceMode_SEMCNORChoices, 0 )
		self.m_choice_deviceMode_SEMCNOR.SetSelection( 1 )
		wSizer_win.Add( self.m_choice_deviceMode_SEMCNOR, 0, wx.ALL, 5 )

		self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.m_staticText_winNull0.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_winNull0, 0, wx.ALL, 5 )

		self.m_notebook_norOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_norOpt = wx.Panel( self.m_notebook_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_norOpt = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_CfiTimingMode = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"CFI Timing Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CfiTimingMode.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_CfiTimingMode, 0, wx.ALL, 5 )

		m_choice_CFITimingModeChoices = [ u"Safe mode", u"Fast mode", u"User defined" ]
		self.m_choice_CFITimingMode = wx.Choice( self.m_panel_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 108,-1 ), m_choice_CFITimingModeChoices, 0 )
		self.m_choice_CFITimingMode.SetSelection( 0 )
		gSizer_norOpt.Add( self.m_choice_CFITimingMode, 0, wx.ALL, 5 )

		self.m_staticText_AdvPolarity = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"ADV Polarity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_AdvPolarity.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_AdvPolarity, 0, wx.ALL, 5 )

		m_choice_AdvPolarityChoices = [ u"Low active", u"High active" ]
		self.m_choice_AdvPolarity = wx.Choice( self.m_panel_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 108,-1 ), m_choice_AdvPolarityChoices, 0 )
		self.m_choice_AdvPolarity.SetSelection( 0 )
		gSizer_norOpt.Add( self.m_choice_AdvPolarity, 0, wx.ALL, 5 )

		self.m_staticText_ioPortSize = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"I/O Port Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ioPortSize.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_ioPortSize, 0, wx.ALL, 5 )

		m_choice_ioPortSizeChoices = [ u"x8 bits", u"x16 bits", u"x24 bits" ]
		self.m_choice_ioPortSize = wx.Choice( self.m_panel_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 108,-1 ), m_choice_ioPortSizeChoices, 0 )
		self.m_choice_ioPortSize.SetSelection( 0 )
		gSizer_norOpt.Add( self.m_choice_ioPortSize, 0, wx.ALL, 5 )

		self.m_staticText_PcsPort = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"PCS Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PcsPort.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_PcsPort, 0, wx.ALL, 5 )

		m_choice_PcsPortChoices = [ u"CSX0" ]
		self.m_choice_PcsPort = wx.Choice( self.m_panel_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 108,-1 ), m_choice_PcsPortChoices, 0 )
		self.m_choice_PcsPort.SetSelection( 0 )
		gSizer_norOpt.Add( self.m_choice_PcsPort, 0, wx.ALL, 5 )

		self.m_staticText_CommandSet = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"Command Set:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CommandSet.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_CommandSet, 0, wx.ALL, 5 )

		m_choice_CommandSetChoices = [ u"MT28EW", u"MT28GU" ]
		self.m_choice_CommandSet = wx.Choice( self.m_panel_norOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 108,-1 ), m_choice_CommandSetChoices, 0 )
		self.m_choice_CommandSet.SetSelection( 0 )
		gSizer_norOpt.Add( self.m_choice_CommandSet, 0, wx.ALL, 5 )


		self.m_panel_norOpt.SetSizer( gSizer_norOpt )
		self.m_panel_norOpt.Layout()
		gSizer_norOpt.Fit( self.m_panel_norOpt )
		self.m_notebook_norOpt.AddPage( self.m_panel_norOpt, u"Nor Option", False )

		wSizer_win.Add( self.m_notebook_norOpt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_userOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_norOpt = wx.Panel( self.m_notebook_userOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_norOpt = wx.GridSizer( 0, 5, 0, 0 )

		self.m_staticText_tCES = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tCES:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCES.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tCES, 0, wx.ALL, 5 )

		self.m_textCtrl_tCES = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tCES, 0, wx.ALL, 5 )

		self.m_staticText_winNull = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_winNull.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_winNull, 0, wx.ALL, 5 )

		self.m_staticText_tCEH = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tCEH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCEH.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tCEH, 0, wx.ALL, 5 )

		self.m_textCtrl_tCEH = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tCEH, 0, wx.ALL, 5 )

		self.m_staticText_tCEITV = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tCEITV:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCEITV.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tCEITV, 0, wx.ALL, 5 )

		self.m_textCtrlt_CEITV = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrlt_CEITV, 0, wx.ALL, 5 )

		self.m_staticText_winNull = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_winNull.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_winNull, 0, wx.ALL, 5 )

		self.m_staticText_tAS = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tAS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tAS.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tAS, 0, wx.ALL, 5 )

		self.m_textCtrl_tAS = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tAS, 0, wx.ALL, 5 )

		self.m_staticText_tAH = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tAH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tAH.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tAH, 0, wx.ALL, 5 )

		self.m_textCtrl_tAH = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tAH, 0, wx.ALL, 5 )

		self.m_staticText_winNull = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_winNull.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_winNull, 0, wx.ALL, 5 )

		self.m_staticText_tTA = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tTA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tTA.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tTA, 0, wx.ALL, 5 )

		self.m_textCtrl_tTA = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tTA, 0, wx.ALL, 5 )

		self.m_staticText_tWEL = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tWEL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tWEL.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tWEL, 0, wx.ALL, 5 )

		self.m_textCtrl_tWEL = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tWEL, 0, wx.ALL, 5 )

		self.m_staticText_winNull = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_winNull.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_winNull, 0, wx.ALL, 5 )

		self.m_staticText_tWEH = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tWEH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tWEH.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tWEH, 0, wx.ALL, 5 )

		self.m_textCtrl_tWEH = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tWEH, 0, wx.ALL, 5 )

		self.m_staticText_tAWDH = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tAWDH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tAWDH.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tAWDH, 0, wx.ALL, 5 )

		self.m_textCtrl_tAWDH = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tAWDH, 0, wx.ALL, 5 )

		self.m_staticText_winNull = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.m_staticText_winNull.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_winNull, 0, wx.ALL, 5 )

		self.m_staticText_tREL = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tREL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tREL.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tREL, 0, wx.ALL, 5 )

		self.m_textCtrl_tREL = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tREL, 0, wx.ALL, 5 )

		self.m_staticText_tREH = wx.StaticText( self.m_panel_norOpt, wx.ID_ANY, u"tREH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tREH.Wrap( -1 )

		gSizer_norOpt.Add( self.m_staticText_tREH, 0, wx.ALL, 5 )

		self.m_textCtrl_tREH = wx.TextCtrl( self.m_panel_norOpt, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gSizer_norOpt.Add( self.m_textCtrl_tREH, 0, wx.ALL, 5 )


		self.m_panel_norOpt.SetSizer( gSizer_norOpt )
		self.m_panel_norOpt.Layout()
		gSizer_norOpt.Fit( self.m_panel_norOpt )
		self.m_notebook_userOpt.AddPage( self.m_panel_norOpt, u"Nor Option", False )

		wSizer_win.Add( self.m_notebook_userOpt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		self.m_staticText_winNull0.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_winNull0, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_cancel, 0, wx.ALL, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_choice_deviceMode_SEMCNOR.Bind( wx.EVT_CHOICE, self.callbackUseTypicalDeviceModel_SEMCNOR )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackUseTypicalDeviceModel_SEMCNOR( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


