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
## Class advSettingsWin_FlexibleUserKeys_Otfad
###########################################################################

class advSettingsWin_FlexibleUserKeys_Otfad ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 934,656 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_win = wx.BoxSizer( wx.VERTICAL )

		wSizer_Opt = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_encryptionOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_encryptionOpt = wx.Panel( self.m_notebook_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer_encryptionOpt = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_totalRegions = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Total Regions:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_totalRegions.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_totalRegions, 0, wx.ALL, 5 )

		m_choice_totalRegionsChoices = [ u"1", u"2", u"3", u"4" ]
		self.m_choice_totalRegions = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_totalRegionsChoices, 0 )
		self.m_choice_totalRegions.SetSelection( 0 )
		wSizer_encryptionOpt.Add( self.m_choice_totalRegions, 0, wx.ALL, 5 )

		self.m_staticText_null0EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 9,-1 ), 0 )
		self.m_staticText_null0EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null0EncryptionOpt, 0, wx.ALL, 5 )

		self.m_staticText_xipBaseAddr = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"XIP Base Address:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_xipBaseAddr.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_xipBaseAddr, 0, wx.ALL, 5 )

		m_choice_xipBaseAddrChoices = [ u"0x60000000" ]
		self.m_choice_xipBaseAddr = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_xipBaseAddrChoices, 0 )
		self.m_choice_xipBaseAddr.SetSelection( 0 )
		wSizer_encryptionOpt.Add( self.m_choice_xipBaseAddr, 0, wx.ALL, 5 )

		self.m_staticText_kekSource = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Kek Source:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_kekSource.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_kekSource, 0, wx.ALL, 5 )

		m_choice_kekSourceChoices = [ u"Fuse SW-GP2" ]
		self.m_choice_kekSource = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_kekSourceChoices, 0 )
		self.m_choice_kekSource.SetSelection( 0 )
		wSizer_encryptionOpt.Add( self.m_choice_kekSource, 0, wx.ALL, 5 )

		self.m_staticText_null1EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 9,-1 ), 0 )
		self.m_staticText_null1EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null1EncryptionOpt, 0, wx.ALL, 5 )

		self.m_staticText_kekData = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Kek Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_kekData.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_kekData, 0, wx.ALL, 5 )

		self.m_textCtrl_kekData = wx.TextCtrl( self.m_panel_encryptionOpt, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		wSizer_encryptionOpt.Add( self.m_textCtrl_kekData, 0, wx.ALL, 5 )

		self.m_staticText_scrambleAlgo = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Scramble Algorithm:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_scrambleAlgo.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_scrambleAlgo, 0, wx.ALL, 5 )

		self.m_textCtrl_scrambleAlgo = wx.TextCtrl( self.m_panel_encryptionOpt, wx.ID_ANY, u"0x33aa55cc", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		wSizer_encryptionOpt.Add( self.m_textCtrl_scrambleAlgo, 0, wx.ALL, 5 )

		self.m_staticText_null2EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 9,-1 ), 0 )
		self.m_staticText_null2EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null2EncryptionOpt, 0, wx.ALL, 5 )

		self.m_staticText_scrambleAlignment = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Scramble Alignment:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_scrambleAlignment.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_scrambleAlignment, 0, wx.ALL, 5 )

		self.m_textCtrl_scrambleAlignment = wx.TextCtrl( self.m_panel_encryptionOpt, wx.ID_ANY, u"0x1b", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		wSizer_encryptionOpt.Add( self.m_textCtrl_scrambleAlignment, 0, wx.ALL, 5 )

		self.m_staticText_null3EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 890,2 ), 0 )
		self.m_staticText_null3EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null3EncryptionOpt, 0, wx.ALL, 5 )


		self.m_panel_encryptionOpt.SetSizer( wSizer_encryptionOpt )
		self.m_panel_encryptionOpt.Layout()
		wSizer_encryptionOpt.Fit( self.m_panel_encryptionOpt )
		self.m_notebook_encryptionOpt.AddPage( self.m_panel_encryptionOpt, u"Encryption Option", False )

		wSizer_Opt.Add( self.m_notebook_encryptionOpt, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_win.Add( wSizer_Opt, 1, wx.EXPAND, 5 )

		wSizer_Info = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_region0Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_region0Info = wx.Panel( self.m_notebook_region0Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_region0Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_region0UserKeyData = wx.StaticText( self.m_panel_region0Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region0UserKeyData.Wrap( -1 )

		gSizer_region0Info.Add( self.m_staticText_region0UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_region0UserKeyData = wx.TextCtrl( self.m_panel_region0Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region0Info.Add( self.m_textCtrl_region0UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_region0CounterData = wx.StaticText( self.m_panel_region0Info, wx.ID_ANY, u"Counter Data (8-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region0CounterData.Wrap( -1 )

		gSizer_region0Info.Add( self.m_staticText_region0CounterData, 0, wx.ALL, 5 )

		self.m_textCtrl_region0CounterData = wx.TextCtrl( self.m_panel_region0Info, wx.ID_ANY, u"0020406001030507", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region0Info.Add( self.m_textCtrl_region0CounterData, 0, wx.ALL, 5 )

		self.m_staticText_region0FacStart = wx.StaticText( self.m_panel_region0Info, wx.ID_ANY, u"Protected Region Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region0FacStart.Wrap( -1 )

		gSizer_region0Info.Add( self.m_staticText_region0FacStart, 0, wx.ALL, 5 )

		self.m_textCtrl_region0FacStart = wx.TextCtrl( self.m_panel_region0Info, wx.ID_ANY, u"0x60001000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region0Info.Add( self.m_textCtrl_region0FacStart, 0, wx.ALL, 5 )

		self.m_staticText_region0FacLength = wx.StaticText( self.m_panel_region0Info, wx.ID_ANY, u"Protected Region Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region0FacLength.Wrap( -1 )

		gSizer_region0Info.Add( self.m_staticText_region0FacLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region0FacLength = wx.TextCtrl( self.m_panel_region0Info, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region0Info.Add( self.m_textCtrl_region0FacLength, 0, wx.ALL, 5 )

		self.m_staticText_region0Lock = wx.StaticText( self.m_panel_region0Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region0Lock.Wrap( -1 )

		gSizer_region0Info.Add( self.m_staticText_region0Lock, 0, wx.ALL, 5 )

		m_choice_region0LockChoices = [ u"No Lock" ]
		self.m_choice_region0Lock = wx.Choice( self.m_panel_region0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_region0LockChoices, 0 )
		self.m_choice_region0Lock.SetSelection( 0 )
		gSizer_region0Info.Add( self.m_choice_region0Lock, 0, wx.ALL, 5 )


		self.m_panel_region0Info.SetSizer( gSizer_region0Info )
		self.m_panel_region0Info.Layout()
		gSizer_region0Info.Fit( self.m_panel_region0Info )
		self.m_notebook_region0Info.AddPage( self.m_panel_region0Info, u"OTFAD Region 0 Info", False )

		wSizer_Info.Add( self.m_notebook_region0Info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_region1Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_region1Info = wx.Panel( self.m_notebook_region1Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_region1Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_region1UserKeyData = wx.StaticText( self.m_panel_region1Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region1UserKeyData.Wrap( -1 )

		gSizer_region1Info.Add( self.m_staticText_region1UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_region1UserKeyData = wx.TextCtrl( self.m_panel_region1Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region1Info.Add( self.m_textCtrl_region1UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_region1CounterData = wx.StaticText( self.m_panel_region1Info, wx.ID_ANY, u"Counter Data (8-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region1CounterData.Wrap( -1 )

		gSizer_region1Info.Add( self.m_staticText_region1CounterData, 0, wx.ALL, 5 )

		self.m_textCtrl_region1CounterData = wx.TextCtrl( self.m_panel_region1Info, wx.ID_ANY, u"0020406001030507", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region1Info.Add( self.m_textCtrl_region1CounterData, 0, wx.ALL, 5 )

		self.m_staticText_region1FacStart = wx.StaticText( self.m_panel_region1Info, wx.ID_ANY, u"Protected Region Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region1FacStart.Wrap( -1 )

		gSizer_region1Info.Add( self.m_staticText_region1FacStart, 0, wx.ALL, 5 )

		self.m_textCtrl_region1FacStart = wx.TextCtrl( self.m_panel_region1Info, wx.ID_ANY, u"0x60003000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region1Info.Add( self.m_textCtrl_region1FacStart, 0, wx.ALL, 5 )

		self.m_staticText_region1FacLength = wx.StaticText( self.m_panel_region1Info, wx.ID_ANY, u"Protected Region Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region1FacLength.Wrap( -1 )

		gSizer_region1Info.Add( self.m_staticText_region1FacLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region1FacLength = wx.TextCtrl( self.m_panel_region1Info, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region1Info.Add( self.m_textCtrl_region1FacLength, 0, wx.ALL, 5 )

		self.m_staticText_region1Lock = wx.StaticText( self.m_panel_region1Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region1Lock.Wrap( -1 )

		gSizer_region1Info.Add( self.m_staticText_region1Lock, 0, wx.ALL, 5 )

		m_choice_region1LockChoices = [ u"No Lock" ]
		self.m_choice_region1Lock = wx.Choice( self.m_panel_region1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_region1LockChoices, 0 )
		self.m_choice_region1Lock.SetSelection( 0 )
		gSizer_region1Info.Add( self.m_choice_region1Lock, 0, wx.ALL, 5 )


		self.m_panel_region1Info.SetSizer( gSizer_region1Info )
		self.m_panel_region1Info.Layout()
		gSizer_region1Info.Fit( self.m_panel_region1Info )
		self.m_notebook_region1Info.AddPage( self.m_panel_region1Info, u"OTFAD Region 1 Info", False )

		wSizer_Info.Add( self.m_notebook_region1Info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_region2Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_region2Info = wx.Panel( self.m_notebook_region2Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_region2Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_region2UserKeyData = wx.StaticText( self.m_panel_region2Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region2UserKeyData.Wrap( -1 )

		gSizer_region2Info.Add( self.m_staticText_region2UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_region2UserKeyData = wx.TextCtrl( self.m_panel_region2Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region2Info.Add( self.m_textCtrl_region2UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_region2CounterData = wx.StaticText( self.m_panel_region2Info, wx.ID_ANY, u"Counter Data (8-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region2CounterData.Wrap( -1 )

		gSizer_region2Info.Add( self.m_staticText_region2CounterData, 0, wx.ALL, 5 )

		self.m_textCtrl_region2CounterData = wx.TextCtrl( self.m_panel_region2Info, wx.ID_ANY, u"0020406001030507", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region2Info.Add( self.m_textCtrl_region2CounterData, 0, wx.ALL, 5 )

		self.m_staticText_region2FacStart = wx.StaticText( self.m_panel_region2Info, wx.ID_ANY, u"Protected Region Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region2FacStart.Wrap( -1 )

		gSizer_region2Info.Add( self.m_staticText_region2FacStart, 0, wx.ALL, 5 )

		self.m_textCtrl_region2FacStart = wx.TextCtrl( self.m_panel_region2Info, wx.ID_ANY, u"0x60005000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region2Info.Add( self.m_textCtrl_region2FacStart, 0, wx.ALL, 5 )

		self.m_staticText_region2FacLength = wx.StaticText( self.m_panel_region2Info, wx.ID_ANY, u"Protected Region Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region2FacLength.Wrap( -1 )

		gSizer_region2Info.Add( self.m_staticText_region2FacLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region2FacLength = wx.TextCtrl( self.m_panel_region2Info, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region2Info.Add( self.m_textCtrl_region2FacLength, 0, wx.ALL, 5 )

		self.m_staticText_region2Lock = wx.StaticText( self.m_panel_region2Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region2Lock.Wrap( -1 )

		gSizer_region2Info.Add( self.m_staticText_region2Lock, 0, wx.ALL, 5 )

		m_choice_region2LockChoices = [ u"No Lock" ]
		self.m_choice_region2Lock = wx.Choice( self.m_panel_region2Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_region2LockChoices, 0 )
		self.m_choice_region2Lock.SetSelection( 0 )
		gSizer_region2Info.Add( self.m_choice_region2Lock, 0, wx.ALL, 5 )


		self.m_panel_region2Info.SetSizer( gSizer_region2Info )
		self.m_panel_region2Info.Layout()
		gSizer_region2Info.Fit( self.m_panel_region2Info )
		self.m_notebook_region2Info.AddPage( self.m_panel_region2Info, u"OTFAD Region 2 Info", False )

		wSizer_Info.Add( self.m_notebook_region2Info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_region3Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_region3Info = wx.Panel( self.m_notebook_region3Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_region3Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_region3UserKeyData = wx.StaticText( self.m_panel_region3Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region3UserKeyData.Wrap( -1 )

		gSizer_region3Info.Add( self.m_staticText_region3UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_region3UserKeyData = wx.TextCtrl( self.m_panel_region3Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region3Info.Add( self.m_textCtrl_region3UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_region3CounterData = wx.StaticText( self.m_panel_region3Info, wx.ID_ANY, u"Counter Data (8-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region3CounterData.Wrap( -1 )

		gSizer_region3Info.Add( self.m_staticText_region3CounterData, 0, wx.ALL, 5 )

		self.m_textCtrl_region3CounterData = wx.TextCtrl( self.m_panel_region3Info, wx.ID_ANY, u"0020406001030507", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region3Info.Add( self.m_textCtrl_region3CounterData, 0, wx.ALL, 5 )

		self.m_staticText_region3FacStart = wx.StaticText( self.m_panel_region3Info, wx.ID_ANY, u"Protected Region Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region3FacStart.Wrap( -1 )

		gSizer_region3Info.Add( self.m_staticText_region3FacStart, 0, wx.ALL, 5 )

		self.m_textCtrl_region3FacStart = wx.TextCtrl( self.m_panel_region3Info, wx.ID_ANY, u"0x60007000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region3Info.Add( self.m_textCtrl_region3FacStart, 0, wx.ALL, 5 )

		self.m_staticText_region3FacLength = wx.StaticText( self.m_panel_region3Info, wx.ID_ANY, u"Protected Region Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region3FacLength.Wrap( -1 )

		gSizer_region3Info.Add( self.m_staticText_region3FacLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region3FacLength = wx.TextCtrl( self.m_panel_region3Info, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_region3Info.Add( self.m_textCtrl_region3FacLength, 0, wx.ALL, 5 )

		self.m_staticText_region3Lock = wx.StaticText( self.m_panel_region3Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_region3Lock.Wrap( -1 )

		gSizer_region3Info.Add( self.m_staticText_region3Lock, 0, wx.ALL, 5 )

		m_choice_region3LockChoices = [ u"No Lock" ]
		self.m_choice_region3Lock = wx.Choice( self.m_panel_region3Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_region3LockChoices, 0 )
		self.m_choice_region3Lock.SetSelection( 0 )
		gSizer_region3Info.Add( self.m_choice_region3Lock, 0, wx.ALL, 5 )


		self.m_panel_region3Info.SetSizer( gSizer_region3Info )
		self.m_panel_region3Info.Layout()
		gSizer_region3Info.Fit( self.m_panel_region3Info )
		self.m_notebook_region3Info.AddPage( self.m_panel_region3Info, u"OTFAD Region 3 Info", False )

		wSizer_Info.Add( self.m_notebook_region3Info, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_win.Add( wSizer_Info, 1, wx.EXPAND, 5 )

		wSizer_action = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null0Action = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 277,-1 ), 0 )
		self.m_staticText_null0Action.Wrap( -1 )

		wSizer_action.Add( self.m_staticText_null0Action, 0, wx.ALL, 5 )

		self.m_button_genRandomKek = wx.Button( self, wx.ID_ANY, u"Generate Random Kek", wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
		wSizer_action.Add( self.m_button_genRandomKek, 0, wx.ALL, 5 )

		self.m_button_genRandomKey = wx.Button( self, wx.ID_ANY, u"Generate Random User Key", wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
		wSizer_action.Add( self.m_button_genRandomKey, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_action.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_action.Add( self.m_button_cancel, 0, wx.ALL, 5 )


		bSizer_win.Add( wSizer_action, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_choice_totalRegions.Bind( wx.EVT_CHOICE, self.callbackChangeTotalRegions )
		self.m_button_genRandomKek.Bind( wx.EVT_BUTTON, self.callbackGenRandomKek )
		self.m_button_genRandomKey.Bind( wx.EVT_BUTTON, self.callbackGenRandomUserKey )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackChangeTotalRegions( self, event ):
		event.Skip()

	def callbackGenRandomKek( self, event ):
		event.Skip()

	def callbackGenRandomUserKey( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


