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
## Class efuseWin_BootCfg0_FlexspiNor_12bits
###########################################################################

class efuseWin_BootCfg0_FlexspiNor_12bits ( wx.Frame ):

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

		self.m_staticText_byteIdx0 = wx.StaticText( self, wx.ID_ANY, u"               0x450[7:0]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx0.Wrap( -1 )

		self.m_staticText_byteIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx0, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx1 = wx.StaticText( self, wx.ID_ANY, u"               0x450[15:8]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx1.Wrap( -1 )

		self.m_staticText_byteIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx1, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx2 = wx.StaticText( self, wx.ID_ANY, u"               0x450[23:16]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx2.Wrap( -1 )

		self.m_staticText_byteIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx2, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx3 = wx.StaticText( self, wx.ID_ANY, u"               0x450[31:24]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
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

		self.m_staticText_bit7_4 = wx.StaticText( self, wx.ID_ANY, u"Boot Device Selection", wx.DefaultPosition, wx.Size( 350,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit7_4.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit7_4, 0, wx.ALL, 5 )

		self.m_staticText_bit3_2 = wx.StaticText( self, wx.ID_ANY, u"Hold_Time", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit3_2.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit3_2, 0, wx.ALL, 5 )

		self.m_staticText_bit1 = wx.StaticText( self, wx.ID_ANY, u"EncryptedXIP", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit1.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit1, 0, wx.ALL, 5 )

		self.m_staticText_bit0 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit0.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit0, 0, wx.ALL, 5 )

		m_choice_bit7_4Choices = [ u"0000 - FlexSPI NOR" ]
		self.m_choice_bit7_4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit7_4Choices, 0 )
		self.m_choice_bit7_4.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit7_4, 0, wx.ALL, 5 )

		m_choice_bit3_2Choices = [ u"00 - 500us", u"01 - 1ms", u"10 - 3ms", u"11 - 10ms" ]
		self.m_choice_bit3_2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit3_2Choices, 0 )
		self.m_choice_bit3_2.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit3_2, 0, wx.ALL, 5 )

		m_choice_bit1Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit1Choices, 0 )
		self.m_choice_bit1.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit1, 0, wx.ALL, 5 )

		m_choice_bit0Choices = [ u"x - N/A" ]
		self.m_choice_bit0 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit0Choices, 0 )
		self.m_choice_bit0.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit0, 0, wx.ALL, 5 )

		self.m_staticText_bit15 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit15.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit15, 0, wx.ALL, 5 )

		self.m_staticText_bit14 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit14.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit14, 0, wx.ALL, 5 )

		self.m_staticText_bit13 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit13.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit13, 0, wx.ALL, 5 )

		self.m_staticText_bit12 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit12.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit12, 0, wx.ALL, 5 )

		self.m_staticText_bit11 = wx.StaticText( self, wx.ID_ANY, u"Infinit_Loop", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit11.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit11, 0, wx.ALL, 5 )

		self.m_staticText_bit10_8 = wx.StaticText( self, wx.ID_ANY, u"Flash_Type", wx.DefaultPosition, wx.Size( 260,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit10_8.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit10_8, 0, wx.ALL, 5 )

		m_choice_bit15Choices = [ u"x - N/A" ]
		self.m_choice_bit15 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit15Choices, 0 )
		self.m_choice_bit15.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit15, 0, wx.ALL, 5 )

		m_choice_bit14Choices = [ u"x - N/A" ]
		self.m_choice_bit14 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit14Choices, 0 )
		self.m_choice_bit14.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit14, 0, wx.ALL, 5 )

		m_choice_bit13Choices = [ u"x - N/A" ]
		self.m_choice_bit13 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit13Choices, 0 )
		self.m_choice_bit13.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit13, 0, wx.ALL, 5 )

		m_choice_bit12Choices = [ u"x - N/A" ]
		self.m_choice_bit12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit12Choices, 0 )
		self.m_choice_bit12.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit12, 0, wx.ALL, 5 )

		m_choice_bit11Choices = [ u"0 - Disabled", u"1 - Enabled" ]
		self.m_choice_bit11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit11Choices, 0 )
		self.m_choice_bit11.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit11, 0, wx.ALL, 5 )

		m_choice_bit10_8Choices = [ u"000 - Device supports 3B read by default", u"001 - Device supports 4B read by default", u"010 - HyperFlash 1V8", u"011 - HyperFlash 3V3", u"100 - MXIC Octal DDR", u"101 - Micron Octal DDR", u"110 - Reserved", u"111 - QSPI supports 3B read (on 2nd pinmux option)" ]
		self.m_choice_bit10_8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 260,-1 ), m_choice_bit10_8Choices, 0 )
		self.m_choice_bit10_8.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit10_8, 0, wx.ALL, 5 )

		self.m_staticText_bit23 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit23.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit23, 0, wx.ALL, 5 )

		self.m_staticText_bit22 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit22.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit22, 0, wx.ALL, 5 )

		self.m_staticText_bit21 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit21.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit21, 0, wx.ALL, 5 )

		self.m_staticText_bit20 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit20.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit20, 0, wx.ALL, 5 )

		self.m_staticText_bit19 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit19.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit19, 0, wx.ALL, 5 )

		self.m_staticText_bit18 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit18.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit18, 0, wx.ALL, 5 )

		self.m_staticText_bit17 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit17.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit17, 0, wx.ALL, 5 )

		self.m_staticText_bit16 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit16.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit16, 0, wx.ALL, 5 )

		m_choice_bit23Choices = [ u"x - N/A" ]
		self.m_choice_bit23 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit23Choices, 0 )
		self.m_choice_bit23.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit23, 0, wx.ALL, 5 )

		m_choice_bit22Choices = [ u"x - N/A" ]
		self.m_choice_bit22 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit22Choices, 0 )
		self.m_choice_bit22.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit22, 0, wx.ALL, 5 )

		m_choice_bit21Choices = [ u"x - N/A" ]
		self.m_choice_bit21 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit21Choices, 0 )
		self.m_choice_bit21.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit21, 0, wx.ALL, 5 )

		m_choice_bit20Choices = [ u"x - N/A" ]
		self.m_choice_bit20 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit20Choices, 0 )
		self.m_choice_bit20.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit20, 0, wx.ALL, 5 )

		m_choice_bit19Choices = [ u"x - N/A" ]
		self.m_choice_bit19 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit19Choices, 0 )
		self.m_choice_bit19.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit19, 0, wx.ALL, 5 )

		m_choice_bit18Choices = [ u"x - N/A" ]
		self.m_choice_bit18 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit18Choices, 0 )
		self.m_choice_bit18.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit18, 0, wx.ALL, 5 )

		m_choice_bit17Choices = [ u"x - N/A" ]
		self.m_choice_bit17 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit17Choices, 0 )
		self.m_choice_bit17.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit17, 0, wx.ALL, 5 )

		m_choice_bit16Choices = [ u"x - N/A" ]
		self.m_choice_bit16 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit16Choices, 0 )
		self.m_choice_bit16.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit16, 0, wx.ALL, 5 )

		self.m_staticText_bit31 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit31.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit31, 0, wx.ALL, 5 )

		self.m_staticText_bit30 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit30.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit30, 0, wx.ALL, 5 )

		self.m_staticText_bit29 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit29.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit29, 0, wx.ALL, 5 )

		self.m_staticText_bit28 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit28.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit28, 0, wx.ALL, 5 )

		self.m_staticText_bit27 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit27.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit27, 0, wx.ALL, 5 )

		self.m_staticText_bit26 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit26.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit26, 0, wx.ALL, 5 )

		self.m_staticText_bit25 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit25.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit25, 0, wx.ALL, 5 )

		self.m_staticText_bit24 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit24.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit24, 0, wx.ALL, 5 )

		m_choice_bit31Choices = [ u"x - N/A" ]
		self.m_choice_bit31 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit31Choices, 0 )
		self.m_choice_bit31.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit31, 0, wx.ALL, 5 )

		m_choice_bit30Choices = [ u"x - N/A" ]
		self.m_choice_bit30 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit30Choices, 0 )
		self.m_choice_bit30.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit30, 0, wx.ALL, 5 )

		m_choice_bit29Choices = [ u"x - N/A" ]
		self.m_choice_bit29 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit29Choices, 0 )
		self.m_choice_bit29.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit29, 0, wx.ALL, 5 )

		m_choice_bit28Choices = [ u"x - N/A" ]
		self.m_choice_bit28 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit28Choices, 0 )
		self.m_choice_bit28.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit28, 0, wx.ALL, 5 )

		m_choice_bit27Choices = [ u"x - N/A" ]
		self.m_choice_bit27 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit27Choices, 0 )
		self.m_choice_bit27.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit27, 0, wx.ALL, 5 )

		m_choice_bit26Choices = [ u"x - N/A" ]
		self.m_choice_bit26 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit26Choices, 0 )
		self.m_choice_bit26.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit26, 0, wx.ALL, 5 )

		m_choice_bit25Choices = [ u"x - N/A" ]
		self.m_choice_bit25 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit25Choices, 0 )
		self.m_choice_bit25.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit25, 0, wx.ALL, 5 )

		m_choice_bit24Choices = [ u"x - N/A" ]
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


