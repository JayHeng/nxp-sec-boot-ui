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
## Class advSettingsWin_FlexibleUserKeys_Bee
###########################################################################

class advSettingsWin_FlexibleUserKeys_Bee ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 934,657 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_win = wx.BoxSizer( wx.VERTICAL )

		wSizer_Opt = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_encryptionOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_encryptionOpt = wx.Panel( self.m_notebook_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer_encryptionOpt = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_engineSel = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Engine Selection:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engineSel.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_engineSel, 0, wx.ALL, 5 )

		m_choice_engineSelChoices = [ u"Engine 0", u"Engine 1", u"Both Engines" ]
		self.m_choice_engineSel = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engineSelChoices, 0 )
		self.m_choice_engineSel.SetSelection( 0 )
		wSizer_encryptionOpt.Add( self.m_choice_engineSel, 0, wx.ALL, 5 )

		self.m_staticText_null0EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 9,-1 ), 0 )
		self.m_staticText_null0EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null0EncryptionOpt, 0, wx.ALL, 5 )

		self.m_staticText_beeEngKeySel = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"BEE Engine Key Selection:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_beeEngKeySel.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_beeEngKeySel, 0, wx.ALL, 5 )

		m_choice_beeEngKeySelChoices = [ u"Random Key", u"Zero Key" ]
		self.m_choice_beeEngKeySel = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_beeEngKeySelChoices, 0 )
		self.m_choice_beeEngKeySel.SetSelection( 1 )
		wSizer_encryptionOpt.Add( self.m_choice_beeEngKeySel, 0, wx.ALL, 5 )

		self.m_staticText_imageType = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Image Type:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_imageType.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_imageType, 0, wx.ALL, 5 )

		m_choice_imageTypeChoices = [ u"Non-Bootable", u"Bootable" ]
		self.m_choice_imageType = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_imageTypeChoices, 0 )
		self.m_choice_imageType.SetSelection( 1 )
		wSizer_encryptionOpt.Add( self.m_choice_imageType, 0, wx.ALL, 5 )

		self.m_staticText_null1EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 9,-1 ), 0 )
		self.m_staticText_null1EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null1EncryptionOpt, 0, wx.ALL, 5 )

		self.m_staticText_xipBaseAddr = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"XIP Base Address:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_xipBaseAddr.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_xipBaseAddr, 0, wx.ALL, 5 )

		m_choice_xipBaseAddrChoices = [ u"0x60000000" ]
		self.m_choice_xipBaseAddr = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_xipBaseAddrChoices, 0 )
		self.m_choice_xipBaseAddr.SetSelection( 0 )
		wSizer_encryptionOpt.Add( self.m_choice_xipBaseAddr, 0, wx.ALL, 5 )

		self.m_staticText_null2EncryptionOpt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 890,2 ), 0 )
		self.m_staticText_null2EncryptionOpt.Wrap( -1 )

		wSizer_encryptionOpt.Add( self.m_staticText_null2EncryptionOpt, 0, wx.ALL, 5 )


		self.m_panel_encryptionOpt.SetSizer( wSizer_encryptionOpt )
		self.m_panel_encryptionOpt.Layout()
		wSizer_encryptionOpt.Fit( self.m_panel_encryptionOpt )
		self.m_notebook_encryptionOpt.AddPage( self.m_panel_encryptionOpt, u"Encryption Option", False )

		wSizer_Opt.Add( self.m_notebook_encryptionOpt, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_win.Add( wSizer_Opt, 1, wx.EXPAND, 5 )

		wSizer_Info = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_engine0Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_engine0Info = wx.Panel( self.m_notebook_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_engine0Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_engine0keySource = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Key Source:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0keySource.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0keySource, 0, wx.ALL, 5 )

		m_choice_engine0keySourceChoices = [ u"Fuse SW-GP2", u"Fuse GP4[127:0]" ]
		self.m_choice_engine0keySource = wx.Choice( self.m_panel_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine0keySourceChoices, 0 )
		self.m_choice_engine0keySource.SetSelection( 0 )
		gSizer_engine0Info.Add( self.m_choice_engine0keySource, 0, wx.ALL, 5 )

		self.m_staticText_engine0UserKeyData = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0UserKeyData.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0UserKeyData = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_engine0AesMode = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"AES Mode:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0AesMode.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0AesMode, 0, wx.ALL, 5 )

		m_choice_engine0AesModeChoices = [ u"CTR" ]
		self.m_choice_engine0AesMode = wx.Choice( self.m_panel_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine0AesModeChoices, 0 )
		self.m_choice_engine0AesMode.SetSelection( 0 )
		self.m_choice_engine0AesMode.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_choice_engine0AesMode.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer_engine0Info.Add( self.m_choice_engine0AesMode, 0, wx.ALL, 5 )

		self.m_staticText_engine0FacCnt = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region Count:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0FacCnt.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0FacCnt, 0, wx.ALL, 5 )

		m_choice_engine0FacCntChoices = [ u"1", u"2", u"3" ]
		self.m_choice_engine0FacCnt = wx.Choice( self.m_panel_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine0FacCntChoices, 0 )
		self.m_choice_engine0FacCnt.SetSelection( 0 )
		gSizer_engine0Info.Add( self.m_choice_engine0FacCnt, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac0Start = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 0 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac0Start.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac0Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac0Start = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, u"0x60001000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac0Start, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac0Length = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 0 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac0Length.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac0Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac0Length = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, u"0x2000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac0Length, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac1Start = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 1 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac1Start.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac1Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac1Start = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac1Start, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac1Length = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 1 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac1Length.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac1Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac1Length = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac1Length, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac2Start = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 2 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac2Start.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac2Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac2Start = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac2Start, 0, wx.ALL, 5 )

		self.m_staticText_engine0Fac2Length = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Protected Region 2 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Fac2Length.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Fac2Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine0Fac2Length = wx.TextCtrl( self.m_panel_engine0Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine0Info.Add( self.m_textCtrl_engine0Fac2Length, 0, wx.ALL, 5 )

		self.m_staticText_engine0AccessPermision = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Access Permision:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0AccessPermision.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0AccessPermision, 0, wx.ALL, 5 )

		m_choice_engine0AccessPermisionChoices = [ u"No Limitation" ]
		self.m_choice_engine0AccessPermision = wx.Choice( self.m_panel_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine0AccessPermisionChoices, 0 )
		self.m_choice_engine0AccessPermision.SetSelection( 0 )
		gSizer_engine0Info.Add( self.m_choice_engine0AccessPermision, 0, wx.ALL, 5 )

		self.m_staticText_engine0Lock = wx.StaticText( self.m_panel_engine0Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine0Lock.Wrap( -1 )

		gSizer_engine0Info.Add( self.m_staticText_engine0Lock, 0, wx.ALL, 5 )

		m_choice_engine0LockChoices = [ u"No Lock" ]
		self.m_choice_engine0Lock = wx.Choice( self.m_panel_engine0Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine0LockChoices, 0 )
		self.m_choice_engine0Lock.SetSelection( 0 )
		gSizer_engine0Info.Add( self.m_choice_engine0Lock, 0, wx.ALL, 5 )


		self.m_panel_engine0Info.SetSizer( gSizer_engine0Info )
		self.m_panel_engine0Info.Layout()
		gSizer_engine0Info.Fit( self.m_panel_engine0Info )
		self.m_notebook_engine0Info.AddPage( self.m_panel_engine0Info, u"BEE Engine 0 Info", False )

		wSizer_Info.Add( self.m_notebook_engine0Info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_engine1Info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_engine1Info = wx.Panel( self.m_notebook_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_engine1Info = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_engine1keySource = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Key Source:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1keySource.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1keySource, 0, wx.ALL, 5 )

		m_choice_engine1keySourceChoices = [ u"Fuse SW-GP2", u"Fuse GP4[127:0]" ]
		self.m_choice_engine1keySource = wx.Choice( self.m_panel_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine1keySourceChoices, 0 )
		self.m_choice_engine1keySource.SetSelection( 1 )
		gSizer_engine1Info.Add( self.m_choice_engine1keySource, 0, wx.ALL, 5 )

		self.m_staticText_engine1UserKeyData = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"User Key Data (16-bytes):", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1UserKeyData.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1UserKeyData, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1UserKeyData = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, u"0123456789abcdeffedcba9876543210", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1UserKeyData, 0, wx.ALL, 5 )

		self.m_staticText_engine1AesMode = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"AES Mode:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1AesMode.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1AesMode, 0, wx.ALL, 5 )

		m_choice_engine1AesModeChoices = [ u"CTR" ]
		self.m_choice_engine1AesMode = wx.Choice( self.m_panel_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine1AesModeChoices, 0 )
		self.m_choice_engine1AesMode.SetSelection( 0 )
		gSizer_engine1Info.Add( self.m_choice_engine1AesMode, 0, wx.ALL, 5 )

		self.m_staticText_engine1FacCnt = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region Count:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1FacCnt.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1FacCnt, 0, wx.ALL, 5 )

		m_choice_engine1FacCntChoices = [ u"1", u"2", u"3" ]
		self.m_choice_engine1FacCnt = wx.Choice( self.m_panel_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine1FacCntChoices, 0 )
		self.m_choice_engine1FacCnt.SetSelection( 0 )
		gSizer_engine1Info.Add( self.m_choice_engine1FacCnt, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac0Start = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 0 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac0Start.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac0Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac0Start = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, u"0x60003000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac0Start, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac0Length = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 0 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac0Length.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac0Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac0Length = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, u"0xc000", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac0Length, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac1Start = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 1 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac1Start.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac1Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac1Start = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac1Start, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac1Length = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 1 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac1Length.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac1Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac1Length = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac1Length, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac2Start = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 2 Start:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac2Start.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac2Start, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac2Start = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac2Start, 0, wx.ALL, 5 )

		self.m_staticText_engine1Fac2Length = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Protected Region 2 Length:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Fac2Length.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Fac2Length, 0, wx.ALL, 5 )

		self.m_textCtrl_engine1Fac2Length = wx.TextCtrl( self.m_panel_engine1Info, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		gSizer_engine1Info.Add( self.m_textCtrl_engine1Fac2Length, 0, wx.ALL, 5 )

		self.m_staticText_engine1AccessPermision = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Access Permision:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1AccessPermision.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1AccessPermision, 0, wx.ALL, 5 )

		m_choice_engine1AccessPermisionChoices = [ u"No Limitation" ]
		self.m_choice_engine1AccessPermision = wx.Choice( self.m_panel_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine1AccessPermisionChoices, 0 )
		self.m_choice_engine1AccessPermision.SetSelection( 0 )
		gSizer_engine1Info.Add( self.m_choice_engine1AccessPermision, 0, wx.ALL, 5 )

		self.m_staticText_engine1Lock = wx.StaticText( self.m_panel_engine1Info, wx.ID_ANY, u"Region Lock:", wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		self.m_staticText_engine1Lock.Wrap( -1 )

		gSizer_engine1Info.Add( self.m_staticText_engine1Lock, 0, wx.ALL, 5 )

		m_choice_engine1LockChoices = [ u"No Lock" ]
		self.m_choice_engine1Lock = wx.Choice( self.m_panel_engine1Info, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice_engine1LockChoices, 0 )
		self.m_choice_engine1Lock.SetSelection( 0 )
		gSizer_engine1Info.Add( self.m_choice_engine1Lock, 0, wx.ALL, 5 )


		self.m_panel_engine1Info.SetSizer( gSizer_engine1Info )
		self.m_panel_engine1Info.Layout()
		gSizer_engine1Info.Fit( self.m_panel_engine1Info )
		self.m_notebook_engine1Info.AddPage( self.m_panel_engine1Info, u"BEE Engine 1 Info", True )

		wSizer_Info.Add( self.m_notebook_engine1Info, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_win.Add( wSizer_Info, 1, wx.EXPAND, 5 )

		wSizer_action = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null0Action = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 477,-1 ), 0 )
		self.m_staticText_null0Action.Wrap( -1 )

		wSizer_action.Add( self.m_staticText_null0Action, 0, wx.ALL, 5 )

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
		self.m_choice_engineSel.Bind( wx.EVT_CHOICE, self.callbackChangeEngineSelection )
		self.m_choice_engine0keySource.Bind( wx.EVT_CHOICE, self.callbackChangeEngine0KeySource )
		self.m_choice_engine0FacCnt.Bind( wx.EVT_CHOICE, self.callbackChangeEngine0FacCnt )
		self.m_choice_engine1keySource.Bind( wx.EVT_CHOICE, self.callbackChangeEngine1KeySource )
		self.m_choice_engine1FacCnt.Bind( wx.EVT_CHOICE, self.callbackChangeEngine1FacCnt )
		self.m_button_genRandomKey.Bind( wx.EVT_BUTTON, self.callbackGenRandomUserKey )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackChangeEngineSelection( self, event ):
		event.Skip()

	def callbackChangeEngine0KeySource( self, event ):
		event.Skip()

	def callbackChangeEngine0FacCnt( self, event ):
		event.Skip()

	def callbackChangeEngine1KeySource( self, event ):
		event.Skip()

	def callbackChangeEngine1FacCnt( self, event ):
		event.Skip()

	def callbackGenRandomUserKey( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


