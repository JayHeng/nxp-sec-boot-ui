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
## Class advSettingsWin_FixedOtpmkKey
###########################################################################

class advSettingsWin_FixedOtpmkKey ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 725,302 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_encryptionOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_encryptionOpt = wx.Panel( self.m_notebook_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_encryptionOpt = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_keySource = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Key Source:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keySource.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_keySource, 0, wx.ALL, 5 )

		m_choice_keySourceChoices = [ u"Fuse OTPMK - SNVS[127:0]", u"Fuse OTPMK - SNVS[255:128]" ]
		self.m_choice_keySource = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), m_choice_keySourceChoices, 0 )
		self.m_choice_keySource.SetSelection( 0 )
		gSizer_encryptionOpt.Add( self.m_choice_keySource, 0, wx.ALL, 5 )

		self.m_staticText_aesMode = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"AES Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_aesMode.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_aesMode, 0, wx.ALL, 5 )

		m_choice_aesModeChoices = [ u"CTR" ]
		self.m_choice_aesMode = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), m_choice_aesModeChoices, 0 )
		self.m_choice_aesMode.SetSelection( 0 )
		gSizer_encryptionOpt.Add( self.m_choice_aesMode, 0, wx.ALL, 5 )

		self.m_staticText_regionCnt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Region Count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_regionCnt.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_regionCnt, 0, wx.ALL, 5 )

		m_choice_regionCntChoices = [ u"0 - Whole Image", u"1 - User Defined", u"2 - User Defined", u"3 - User Defined", u"4 - User Defined" ]
		self.m_choice_regionCnt = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), m_choice_regionCntChoices, 0 )
		self.m_choice_regionCnt.SetSelection( 0 )
		gSizer_encryptionOpt.Add( self.m_choice_regionCnt, 0, wx.ALL, 5 )

		self.m_staticText_redundantImageOffset = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Redundant image offset (in 256KB):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_redundantImageOffset.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_redundantImageOffset, 0, wx.ALL, 5 )

		self.m_textCtrl_redundantImageOffset = wx.TextCtrl( self.m_panel_encryptionOpt, wx.ID_ANY, u"0x0", wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
		gSizer_encryptionOpt.Add( self.m_textCtrl_redundantImageOffset, 0, wx.ALL, 5 )


		self.m_panel_encryptionOpt.SetSizer( gSizer_encryptionOpt )
		self.m_panel_encryptionOpt.Layout()
		gSizer_encryptionOpt.Fit( self.m_panel_encryptionOpt )
		self.m_notebook_encryptionOpt.AddPage( self.m_panel_encryptionOpt, u"Encryption Option", False )

		wSizer_win.Add( self.m_notebook_encryptionOpt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_regionInfo = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_regionInfo = wx.Panel( self.m_notebook_regionInfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_regionInfo = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_regionStart = wx.StaticText( self.m_panel_regionInfo, wx.ID_ANY, u"Region Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_regionStart.Wrap( -1 )

		gSizer_regionInfo.Add( self.m_staticText_regionStart, 0, wx.ALL, 5 )

		self.m_staticText_regionLength = wx.StaticText( self.m_panel_regionInfo, wx.ID_ANY, u"Region Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_regionLength.Wrap( -1 )

		gSizer_regionInfo.Add( self.m_staticText_regionLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region0Start = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, u"0x60001000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region0Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region0Length = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, u"0x1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region0Length, 0, wx.ALL, 5 )

		self.m_textCtrl_region1Start = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, u"0x60002000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region1Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region1Length = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, u"0xe000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region1Length, 0, wx.ALL, 5 )

		self.m_textCtrl_region2Start = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region2Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region2Length = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region2Length, 0, wx.ALL, 5 )

		self.m_textCtrl_region3Start = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region3Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region3Length = wx.TextCtrl( self.m_panel_regionInfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_regionInfo.Add( self.m_textCtrl_region3Length, 0, wx.ALL, 5 )


		self.m_panel_regionInfo.SetSizer( gSizer_regionInfo )
		self.m_panel_regionInfo.Layout()
		gSizer_regionInfo.Fit( self.m_panel_regionInfo )
		self.m_notebook_regionInfo.AddPage( self.m_panel_regionInfo, u"Encrypted Region Info", False )

		wSizer_win.Add( self.m_notebook_regionInfo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 428,-1 ), 0 )
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
		self.m_choice_regionCnt.Bind( wx.EVT_CHOICE, self.callbackChangeRegionCount )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackChangeRegionCount( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


