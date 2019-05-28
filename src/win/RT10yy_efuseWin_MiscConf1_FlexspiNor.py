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
## Class efuseWin_MiscConf1_FlexspiNor
###########################################################################

class efuseWin_MiscConf1_FlexspiNor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 860,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_byteIdx = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_address = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_address.Wrap( -1 )

		self.m_staticText_address.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_address, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx0 = wx.StaticText( self, wx.ID_ANY, u"               0x6E0[7:0]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx0.Wrap( -1 )

		self.m_staticText_byteIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx0, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx1 = wx.StaticText( self, wx.ID_ANY, u"               0x6E0[15:8]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx1.Wrap( -1 )

		self.m_staticText_byteIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx1, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx2 = wx.StaticText( self, wx.ID_ANY, u"               0x6E0[23:16]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx2.Wrap( -1 )

		self.m_staticText_byteIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx2, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx3 = wx.StaticText( self, wx.ID_ANY, u"               0x6E0[31:24]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx3.Wrap( -1 )

		self.m_staticText_byteIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx3, 0, wx.ALL, 5 )


		wSizer_win.Add( bSizer_byteIdx, 1, wx.EXPAND, 5 )

		bSizer_bitIdx = wx.BoxSizer( wx.VERTICAL )

		wSizer_bitIdx = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_bitIdx7 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx7.Wrap( -1 )

		self.m_staticText_bitIdx7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx7, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx6 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx6.Wrap( -1 )

		self.m_staticText_bitIdx6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx6, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx5 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx5.Wrap( -1 )

		self.m_staticText_bitIdx5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx5, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx4 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx4.Wrap( -1 )

		self.m_staticText_bitIdx4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx4, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx3 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx3.Wrap( -1 )

		self.m_staticText_bitIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx3, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx2 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx2.Wrap( -1 )

		self.m_staticText_bitIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx2, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx1 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx1.Wrap( -1 )

		self.m_staticText_bitIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx1, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx0 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx0.Wrap( -1 )

		self.m_staticText_bitIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx0, 0, wx.ALL, 5 )

		self.m_staticText_bit7 = wx.StaticText( self, wx.ID_ANY, u"RST_Pin", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit7.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit7, 0, wx.ALL, 5 )

		self.m_staticText_bit6 = wx.StaticText( self, wx.ID_ANY, u"JEDEC_Hw_RST", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit6.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit6, 0, wx.ALL, 5 )

		self.m_staticText_bit5_4 = wx.StaticText( self, wx.ID_ANY, u"xSPI_Flash_Hold_Time", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit5_4.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit5_4, 0, wx.ALL, 5 )

		self.m_staticText_bit3_1 = wx.StaticText( self, wx.ID_ANY, u"xSPI_Flash_BT_Frequency", wx.DefaultPosition, wx.Size( 260,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit3_1.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit3_1, 0, wx.ALL, 5 )

		self.m_staticText_bit0 = wx.StaticText( self, wx.ID_ANY, u"SIP_Test", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit0.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit0, 0, wx.ALL, 5 )

		m_choice_bit7Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit7Choices, 0 )
		self.m_choice_bit7.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit7, 0, wx.ALL, 5 )

		m_choice_bit6Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit6Choices, 0 )
		self.m_choice_bit6.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit6, 0, wx.ALL, 5 )

		m_choice_bit5_4Choices = [ u"x - N/A" ]
		self.m_choice_bit5_4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit5_4Choices, 0 )
		self.m_choice_bit5_4.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit5_4, 0, wx.ALL, 5 )

		m_choice_bit3_1Choices = [ u"x - N/A" ]
		self.m_choice_bit3_1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 260,-1 ), m_choice_bit3_1Choices, 0 )
		self.m_choice_bit3_1.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit3_1, 0, wx.ALL, 5 )

		m_choice_bit0Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit0 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit0Choices, 0 )
		self.m_choice_bit0.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit0, 0, wx.ALL, 5 )

		self.m_staticText_bit15_12 = wx.StaticText( self, wx.ID_ANY, u"xSPI_Flash_Image_Size", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit15_12.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit15_12, 0, wx.ALL, 5 )

		self.m_staticText_bit11_8 = wx.StaticText( self, wx.ID_ANY, u"xSPI_Flash_Dummy_Cycle", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit11_8.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit11_8, 0, wx.ALL, 5 )

		m_choice_bit15_12Choices = [ u"x - N/A" ]
		self.m_choice_bit15_12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit15_12Choices, 0 )
		self.m_choice_bit15_12.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit15_12, 0, wx.ALL, 5 )

		self.m_textCtrl_bit11_8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_textCtrl_bit11_8, 0, wx.ALL, 5 )

		self.m_staticText_bit23_16 = wx.StaticText( self, wx.ID_ANY, u"FlexSPI_NOR_Secondary_Image_Offset (256KB * fuse value)", wx.DefaultPosition, wx.Size( 710,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit23_16.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit23_16, 0, wx.ALL, 5 )

		self.m_textCtrl_bit23_16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 710,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_textCtrl_bit23_16, 0, wx.ALL, 5 )

		self.m_staticText_bit31_24 = wx.StaticText( self, wx.ID_ANY, u"BT_Pin_SEL", wx.DefaultPosition, wx.Size( 710,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit31_24.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit31_24, 0, wx.ALL, 5 )

		self.m_textCtrl_bit31_24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 710,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_textCtrl_bit31_24, 0, wx.ALL, 5 )

		self.m_staticText_null0BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 420,-1 ), 0 )
		self.m_staticText_null0BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null0BitIdx, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_cancel, 0, wx.ALL, 5 )

		self.m_staticText_null1BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 720,1 ), 0 )
		self.m_staticText_null1BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null1BitIdx, 0, wx.ALL, 5 )


		bSizer_bitIdx.Add( wSizer_bitIdx, 1, wx.EXPAND, 5 )


		wSizer_win.Add( bSizer_bitIdx, 1, wx.EXPAND, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


