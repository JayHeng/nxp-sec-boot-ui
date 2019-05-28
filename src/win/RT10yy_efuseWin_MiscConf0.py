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
## Class efuseWin_MiscConf0
###########################################################################

class efuseWin_MiscConf0 ( wx.Frame ):

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

		self.m_staticText_byteIdx0 = wx.StaticText( self, wx.ID_ANY, u"               0x6D0[7:0]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx0.Wrap( -1 )

		self.m_staticText_byteIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx0, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx1 = wx.StaticText( self, wx.ID_ANY, u"               0x6D0[15:8]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx1.Wrap( -1 )

		self.m_staticText_byteIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx1, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx2 = wx.StaticText( self, wx.ID_ANY, u"               0x6D0[23:16]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx2.Wrap( -1 )

		self.m_staticText_byteIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx2, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx3 = wx.StaticText( self, wx.ID_ANY, u"               0x6D0[31:24]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
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

		self.m_staticText_bit7 = wx.StaticText( self, wx.ID_ANY, u"BT_Failure_Pin", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit7.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit7, 0, wx.ALL, 5 )

		self.m_staticText_bit6 = wx.StaticText( self, wx.ID_ANY, u"BT_USB_VBUS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit6.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit6, 0, wx.ALL, 5 )

		self.m_staticText_bit5_0 = wx.StaticText( self, wx.ID_ANY, u"BT_PAD_Settings (Speed - Drive Strength - Slew Rate)", wx.DefaultPosition, wx.Size( 530,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit5_0.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit5_0, 0, wx.ALL, 5 )

		m_choice_bit7Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit7Choices, 0 )
		self.m_choice_bit7.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit7, 0, wx.ALL, 5 )

		m_choice_bit6Choices = [ u"0 - Not Handle", u"1 - Handle" ]
		self.m_choice_bit6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit6Choices, 0 )
		self.m_choice_bit6.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit6, 0, wx.ALL, 5 )

		self.m_textCtrl_bit5_0 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 530,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_textCtrl_bit5_0, 0, wx.ALL, 5 )

		self.m_staticText_bit15_13 = wx.StaticText( self, wx.ID_ANY, u"BT_WDOG_Timeout", wx.DefaultPosition, wx.Size( 260,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit15_13.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit15_13, 0, wx.ALL, 5 )

		self.m_staticText_bit12 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit12.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit12, 0, wx.ALL, 5 )

		self.m_staticText_bit11_8 = wx.StaticText( self, wx.ID_ANY, u"BT_Read_Retry_Sequence", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit11_8.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit11_8, 0, wx.ALL, 5 )

		m_choice_bit15_13Choices = [ u"000 - 64s", u"001 - 32s", u"010 - 16s", u"011 - Reserved", u"100 - 8s", u"101 - 4s", u"110 - Reserved", u"111 - Reserved" ]
		self.m_choice_bit15_13 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 260,-1 ), m_choice_bit15_13Choices, 0 )
		self.m_choice_bit15_13.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit15_13, 0, wx.ALL, 5 )

		m_choice_bit12Choices = [ u"x - N/A" ]
		self.m_choice_bit12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit12Choices, 0 )
		self.m_choice_bit12.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit12, 0, wx.ALL, 5 )

		m_choice_bit11_8Choices = [ u"0000 - Don't use read retry(RR) sequence", u"0001 - Micron 20nm RR sequence", u"0010 - Toshiba A19nm RR sequence", u"0011 - Toshiba 19nm RR sequence", u"0100 - SanDisk 19nm RR sequence", u"0101 - SanDisk 1ynmRR sequence", u"0110 - Reserved", u"0111 - Reserved", u"1000 - Reserved", u"1001 - Reserved", u"1010 - Reserved", u"1011 - Reserved", u"1100 - Reserved", u"1101 - Reserved", u"1110 - Reserved", u"1111 - Reserved" ]
		self.m_choice_bit11_8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit11_8Choices, 0 )
		self.m_choice_bit11_8.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit11_8, 0, wx.ALL, 5 )

		self.m_staticText_bit23_22 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit23_22.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit23_22, 0, wx.ALL, 5 )

		self.m_staticText_bit21_20 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit21_20.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit21_20, 0, wx.ALL, 5 )

		self.m_staticText_bit19_16 = wx.StaticText( self, wx.ID_ANY, u"Default_FlexRAM_Partion", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit19_16.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit19_16, 0, wx.ALL, 5 )

		m_choice_bit23_22Choices = [ u"xx - N/A" ]
		self.m_choice_bit23_22 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit23_22Choices, 0 )
		self.m_choice_bit23_22.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit23_22, 0, wx.ALL, 5 )

		m_choice_bit21_20Choices = [ u"xx - N/A" ]
		self.m_choice_bit21_20 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit21_20Choices, 0 )
		self.m_choice_bit21_20.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit21_20, 0, wx.ALL, 5 )

		m_choice_bit19_16Choices = [ u"xxxx - ", u"0000 - " ]
		self.m_choice_bit19_16 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit19_16Choices, 0 )
		self.m_choice_bit19_16.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit19_16, 0, wx.ALL, 5 )

		self.m_staticText_bit31_30 = wx.StaticText( self, wx.ID_ANY, u"SD_Calibration_Step", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit31_30.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit31_30, 0, wx.ALL, 5 )

		self.m_staticText_bit29_28 = wx.StaticText( self, wx.ID_ANY, u"BT_LPSPI_Speed", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit29_28.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit29_28, 0, wx.ALL, 5 )

		self.m_staticText_bit27 = wx.StaticText( self, wx.ID_ANY, u"BT_LPSPI_Addr", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit27.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit27, 0, wx.ALL, 5 )

		self.m_staticText_bit26_25 = wx.StaticText( self, wx.ID_ANY, u"BT_LPSPI_Port", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit26_25.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit26_25, 0, wx.ALL, 5 )

		self.m_staticText_bit24 = wx.StaticText( self, wx.ID_ANY, u"Recovery_BT", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit24.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit24, 0, wx.ALL, 5 )

		m_choice_bit31_30Choices = [ u"00 - 1", u"01 - Reserved", u"10 - Reserved", u"11 - Reserved" ]
		self.m_choice_bit31_30 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit31_30Choices, 0 )
		self.m_choice_bit31_30.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit31_30, 0, wx.ALL, 5 )

		m_choice_bit29_28Choices = [ u"00 - 20MHz", u"01 - 10MHz", u"10 - 5MHz", u"11 - 2MHz" ]
		self.m_choice_bit29_28 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit29_28Choices, 0 )
		self.m_choice_bit29_28.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit29_28, 0, wx.ALL, 5 )

		m_choice_bit27Choices = [ u"0 - 3bytes (24-bit)", u"1 - 2bytes (16-bit)" ]
		self.m_choice_bit27 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit27Choices, 0 )
		self.m_choice_bit27.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit27, 0, wx.ALL, 5 )

		m_choice_bit26_25Choices = [ u"00 - LPSPI1", u"01 - LPSPI2", u"10 - LPSPI3", u"11 - LPSPI4" ]
		self.m_choice_bit26_25 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit26_25Choices, 0 )
		self.m_choice_bit26_25.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit26_25, 0, wx.ALL, 5 )

		m_choice_bit24Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit24 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit24Choices, 0 )
		self.m_choice_bit24.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit24, 0, wx.ALL, 5 )

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


