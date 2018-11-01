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
## Class MyFrame_FLEXSPI_NOR
###########################################################################

class MyFrame_FLEXSPI_NOR ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FLEXSPI_NOR", pos = wx.DefaultPosition, size = wx.Size( 508,268 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE,self.OnClose_FLEXSPI_NOR)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer_FLEXSPI_NOR = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.m_staticText_FLEXSPI_NOR = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Configurations of FLEXSPI NOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_FLEXSPI_NOR.Wrap( -1 )
		
		sbSizer_FLEXSPI_NOR.Add( self.m_staticText_FLEXSPI_NOR, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_FLEXSPI_NOR = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_Max_Freq = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Max Freq:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Max_Freq.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Max_Freq, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Max_FreqChoices = [ u"30MHz", u"50MHz", u"60MHz", u"75MHz", u"80MHz", u"100MHz", u"133MHz", u"166MHz" ]
		self.m_choice_Max_Freq = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,25 ), m_choice_Max_FreqChoices, 0 )
		self.m_choice_Max_Freq.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Max_Freq, 0, wx.ALL, 5 )
		
		self.m_staticText_Per_Enhance = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Performance Enhance:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Per_Enhance.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Per_Enhance, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Per_EnhanceChoices = [ u"Not enabled", u"Enable 0-4-4 mode for High random Read performance" ]
		self.m_choice_Per_Enhance = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 195,25 ), m_choice_Per_EnhanceChoices, 0 )
		self.m_choice_Per_Enhance.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Per_Enhance, 0, wx.ALL, 5 )
		
		self.m_staticText_CMD_pad = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"CMD pad(s):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CMD_pad.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_CMD_pad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_CMD_padChoices = [ u"1", u"4", u"8" ]
		self.m_choice_CMD_pad = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 55,25 ), m_choice_CMD_padChoices, 0 )
		self.m_choice_CMD_pad.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_CMD_pad, 0, wx.ALL, 5 )
		
		self.m_staticText_Quad_Mode = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Quad Mode Entry Setting:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Quad_Mode.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Quad_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Quad_ModeChoices = [ u"Not configure", u"Set bit 6 in Status Register 1", u"Set bit 1 in Status Register 2", u"Set bit 7 in Status Register 2" ]
		self.m_choice_Quad_Mode = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,25 ), m_choice_Quad_ModeChoices, 0 )
		self.m_choice_Quad_Mode.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Quad_Mode, 0, wx.ALL, 5 )
		
		self.m_staticText_Query_CMD_pad = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Query CMD pad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Query_CMD_pad.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Query_CMD_pad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Query_CMD_padChoices = [ u"1", u"4", u"8" ]
		self.m_choice_Query_CMD_pad = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 35,25 ), m_choice_Query_CMD_padChoices, 0 )
		self.m_choice_Query_CMD_pad.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Query_CMD_pad, 0, wx.ALL, 5 )
		
		self.m_staticText_Device_Detection = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Device Detection Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Device_Detection.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Device_Detection, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Device_DetectionChoices = [ u"Read SFDP for SDR commands", u"Read SFDP for DDR Read commands", u"HyperFLASH 1V8", u"HyperFLASH 3V", u"Macronix Octal DDR", u"Micron Octal DDR", u"Adesto EcoXiP DDR" ]
		self.m_choice_Device_Detection = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 195,25 ), m_choice_Device_DetectionChoices, 0 )
		self.m_choice_Device_Detection.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Device_Detection, 0, wx.ALL, 5 )
		
		self.m_staticText_Option_size = wx.StaticText( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, u"Option size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Option_size.Wrap( -1 )
		
		wSizer_FLEXSPI_NOR.Add( self.m_staticText_Option_size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Option_sizeChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
		self.m_choice_Option_size = wx.Choice( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,25 ), m_choice_Option_sizeChoices, 0 )
		self.m_choice_Option_size.SetSelection( 0 )
		wSizer_FLEXSPI_NOR.Add( self.m_choice_Option_size, 0, wx.ALL, 5 )
		
		
		sbSizer_FLEXSPI_NOR.Add( wSizer_FLEXSPI_NOR, 1, wx.EXPAND, 5 )
		
		m_sdbSizer_FLEXSPI_NOR = wx.StdDialogButtonSizer()
		self.m_sdbSizer_FLEXSPI_NOROK = wx.Button( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_OK )
		m_sdbSizer_FLEXSPI_NOR.AddButton( self.m_sdbSizer_FLEXSPI_NOROK )
		self.m_sdbSizer_FLEXSPI_NORCancel = wx.Button( sbSizer_FLEXSPI_NOR.GetStaticBox(), wx.ID_CANCEL )
		m_sdbSizer_FLEXSPI_NOR.AddButton( self.m_sdbSizer_FLEXSPI_NORCancel )
		m_sdbSizer_FLEXSPI_NOR.Realize();
		
		sbSizer_FLEXSPI_NOR.Add( m_sdbSizer_FLEXSPI_NOR, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer_FLEXSPI_NOR )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.m_sdbSizer_FLEXSPI_NORCancel.Bind( wx.EVT_BUTTON, self.cancel_of_FLEXSPI_NOR )
		self.m_sdbSizer_FLEXSPI_NOROK.Bind( wx.EVT_BUTTON, self.apply_of_FLEXSPI_NOR )
	
	def __del__( self ):
		pass


		# Virtual event handlers, overide them in your derived class
	def cancel_of_FLEXSPI_NOR( self, event ):
                
                self.Show(False)
                event.Skip()
	
	def apply_of_FLEXSPI_NOR( self, event ):
                
                self.Show(False)
		event.Skip()

	def OnClose_FLEXSPI_NOR( self, event ):
                ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
                if ret == wx.OK:
                        self.Show(False)





###########################################################################
## Class MyFrame_FLEXSPI_NAND
###########################################################################

class MyFrame_FLEXSPI_NAND ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FLEXSPI_NOR", pos = wx.DefaultPosition, size = wx.Size( 567,410 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE,self.OnClose_FLEXSPI_NAND)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer_FLEXSPI_NAND = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.m_staticText_FLEXSPI_NAND = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Configurations of FLEXSPI NAND", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_FLEXSPI_NAND.Wrap( -1 )
		
		sbSizer_FLEXSPI_NAND.Add( self.m_staticText_FLEXSPI_NAND, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_FLEXSPI_NAND = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_Max_Freq = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Max Freq:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Max_Freq.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_Max_Freq, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Max_FreqChoices = [ u"30MHz", u"50MHz", u"60MHz", u"75MHz", u"80MHz", u"100MHz" ]
		self.m_choice_Max_Freq = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,25 ), m_choice_Max_FreqChoices, 0 )
		self.m_choice_Max_Freq.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_Max_Freq, 0, wx.ALL, 5 )
		
		self.m_staticText_Page_Size = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Page Size (KBytes):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Page_Size.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_Page_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Page_SizeChoices = [ u"2KB", u"4KB" ]
		self.m_choice_Page_Size = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_Page_SizeChoices, 0 )
		self.m_choice_Page_Size.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_Page_Size, 0, wx.ALL, 5 )
		
		self.m_staticText_Pages = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Pages Per Block:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Pages.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_Pages, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PagesChoices = [ u"64", u"128", u"256", u"32" ]
		self.m_choice_Pages = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,25 ), m_choice_PagesChoices, 0 )
		self.m_choice_Pages.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_Pages, 0, wx.ALL, 5 )
		
		self.m_staticText_Flash_size = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Flash size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Flash_size.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_Flash_size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Flash_sizeChoices = [ u"512M", u"1GB", u"2GB", u"4GB" ]
		self.m_choice_Flash_size = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,25 ), m_choice_Flash_sizeChoices, 0 )
		self.m_choice_Flash_size.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_Flash_size, 0, wx.ALL, 5 )
		
		self.m_staticText_planes = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Has multiplanes:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_planes.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_planes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_planesChoices = [ u"1 plane", u"2 planes" ]
		self.m_choice_planes = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_planesChoices, 0 )
		self.m_choice_planes.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_planes, 0, wx.ALL, 5 )
		
		self.m_staticText_Option_size = wx.StaticText( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"Option size:        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Option_size.Wrap( -1 )
		
		wSizer_FLEXSPI_NAND.Add( self.m_staticText_Option_size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Option_sizeChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
		self.m_choice_Option_size = wx.Choice( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,25 ), m_choice_Option_sizeChoices, 0 )
		self.m_choice_Option_size.SetSelection( 0 )
		wSizer_FLEXSPI_NAND.Add( self.m_choice_Option_size, 0, wx.ALL, 5 )
		
		
		sbSizer_FLEXSPI_NAND.Add( wSizer_FLEXSPI_NAND, 1, wx.EXPAND, 5 )
		
		sbSizer_FCB_option = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_ANY, u"FCB option" ), wx.VERTICAL )
		
		wSizer_FCB_option = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_Size = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"Size:           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Size.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_SizeChoices = [ u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10" ]
		self.m_choice_Size = wx.Choice( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), m_choice_SizeChoices, 0 )
		self.m_choice_Size.SetSelection( 0 )
		wSizer_FCB_option.Add( self.m_choice_Size, 0, wx.ALL, 5 )
		
		self.m_staticText_address_type = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"address_type:         ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_address_type.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_address_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_address_typeChoices = [ u"byte address", u"block address" ]
		self.m_choice_address_type = wx.Choice( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice_address_typeChoices, 0 )
		self.m_choice_address_type.SetSelection( 0 )
		wSizer_FCB_option.Add( self.m_choice_address_type, 0, wx.ALL, 5 )
		
		self.m_staticText_search_stride = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"search_stride:     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_search_stride.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_search_stride, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_search_strideChoices = [ u"64 pages", u"128 pages", u"256 pages", u"32 pages" ]
		self.m_choice_search_stride = wx.Choice( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), m_choice_search_strideChoices, 0 )
		self.m_choice_search_stride.SetSelection( 0 )
		wSizer_FCB_option.Add( self.m_choice_search_stride, 0, wx.ALL, 5 )
		
		self.m_staticText_search_count = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"search_count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_search_count.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_search_count, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_search_countChoices = [ u"1", u"2", u"3", u"4" ]
		self.m_choice_search_count = wx.Choice( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 43,-1 ), m_choice_search_countChoices, 0 )
		self.m_choice_search_count.SetSelection( 0 )
		wSizer_FCB_option.Add( self.m_choice_search_count, 0, wx.ALL, 5 )
		
		self.m_staticText_block_count = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"block_count:          ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_block_count.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_block_count, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_block_count = wx.TextCtrl( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_FCB_option.Add( self.m_textCtrl_block_count, 0, wx.ALL, 5 )
		
		self.m_staticText_block_id = wx.StaticText( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"block_id:             ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_block_id.Wrap( -1 )
		
		wSizer_FCB_option.Add( self.m_staticText_block_id, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_block_id = wx.TextCtrl( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		wSizer_FCB_option.Add( self.m_textCtrl_block_id, 0, wx.ALL, 5 )
		
		
		sbSizer_FCB_option.Add( wSizer_FCB_option, 1, wx.EXPAND, 5 )
		
		sbSizer_KeyBlob_Option = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB_option.GetStaticBox(), wx.ID_ANY, u"KeyBlob Option" ), wx.VERTICAL )
		
		wSizer_KeyBlob_Option = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_image_index = wx.StaticText( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, u"image_index:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_image_index.Wrap( -1 )
		
		wSizer_KeyBlob_Option.Add( self.m_staticText_image_index, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_image_indexChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
		self.m_choice_image_index = wx.Choice( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_image_indexChoices, 0 )
		self.m_choice_image_index.SetSelection( 0 )
		wSizer_KeyBlob_Option.Add( self.m_choice_image_index, 0, wx.ALL, 5 )
		
		self.m_staticText_dek_size = wx.StaticText( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, u"dek_size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_dek_size.Wrap( -1 )
		
		wSizer_KeyBlob_Option.Add( self.m_staticText_dek_size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_dek_sizeChoices = [ u"128bits" ]
		self.m_choice_dek_size = wx.Choice( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_dek_sizeChoices, 0 )
		self.m_choice_dek_size.SetSelection( 0 )
		wSizer_KeyBlob_Option.Add( self.m_choice_dek_size, 0, wx.ALL, 5 )
		
		self.m_staticText_keyblob_infosize = wx.StaticText( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, u"keyblob_info size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keyblob_infosize.Wrap( -1 )
		
		wSizer_KeyBlob_Option.Add( self.m_staticText_keyblob_infosize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_keyblob_infosizeChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
		self.m_choice_keyblob_infosize = wx.Choice( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_keyblob_infosizeChoices, 0 )
		self.m_choice_keyblob_infosize.SetSelection( 0 )
		wSizer_KeyBlob_Option.Add( self.m_choice_keyblob_infosize, 0, wx.ALL, 5 )
		
		self.m_staticText_type = wx.StaticText( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, u"type:              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_type.Wrap( -1 )
		
		wSizer_KeyBlob_Option.Add( self.m_staticText_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_typeChoices = [ u"Update, used to update the keyblob context", u"Program - used to notify memory driver to program Keyblob to destination" ]
		self.m_choice_type = wx.Choice( sbSizer_KeyBlob_Option.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_typeChoices, 0 )
		self.m_choice_type.SetSelection( 0 )
		wSizer_KeyBlob_Option.Add( self.m_choice_type, 0, wx.ALL, 5 )
		
		
		sbSizer_KeyBlob_Option.Add( wSizer_KeyBlob_Option, 1, wx.EXPAND, 5 )
		
		
		sbSizer_FCB_option.Add( sbSizer_KeyBlob_Option, 1, wx.EXPAND, 5 )
		
		
		sbSizer_FLEXSPI_NAND.Add( sbSizer_FCB_option, 1, wx.EXPAND, 5 )
		
		m_sdbSizer_FLEXSPI_NAND = wx.StdDialogButtonSizer()
		self.m_sdbSizer_FLEXSPI_NANDOK = wx.Button( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_OK )
		m_sdbSizer_FLEXSPI_NAND.AddButton( self.m_sdbSizer_FLEXSPI_NANDOK )
		self.m_sdbSizer_FLEXSPI_NANDCancel = wx.Button( sbSizer_FLEXSPI_NAND.GetStaticBox(), wx.ID_CANCEL )
		m_sdbSizer_FLEXSPI_NAND.AddButton( self.m_sdbSizer_FLEXSPI_NANDCancel )
		m_sdbSizer_FLEXSPI_NAND.Realize();
		
		sbSizer_FLEXSPI_NAND.Add( m_sdbSizer_FLEXSPI_NAND, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer_FLEXSPI_NAND )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.m_sdbSizer_FLEXSPI_NANDCancel.Bind( wx.EVT_BUTTON, self.cancel_of_FLEXSPI_NAND )
		self.m_sdbSizer_FLEXSPI_NANDOK.Bind( wx.EVT_BUTTON, self.apply_of_FLEXSPI_NAND )
	
	def __del__( self ):
		pass


		# Virtual event handlers, overide them in your derived class
	def cancel_of_FLEXSPI_NAND( self, event ):
                
                self.Show(False)
                event.Skip()
	
	def apply_of_FLEXSPI_NAND( self, event ):
                
                self.Show(False)
		event.Skip()

	def OnClose_FLEXSPI_NAND( self, event ):
                ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
                if ret == wx.OK:
                        self.Show(False)
	
		
###########################################################################
## Class MyFrame_SEMC_NOR
###########################################################################

class MyFrame_SEMC_NOR ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SEMC_NOR", pos = wx.DefaultPosition, size = wx.Size( 520,426 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE,self.OnClose_SEMC_NOR)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer_SEMC_NOR = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.staticText_SEMC_NOR = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Configurations of SEMC NOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SEMC_NOR.Wrap( -1 )
		
		sbSizer_SEMC_NOR.Add( self.staticText_SEMC_NOR, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_SEMC_NOR = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.staticText_PCS_Port = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"PCS Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PCS_Port.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_PCS_Port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PCS_PortChoices = [ u"CSX0", u"CSX1", u"CSX2", u"CSX3", u"A8" ]
		self.m_choice_PCS_Port = wx.Choice( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,25 ), m_choice_PCS_PortChoices, 0 )
		self.m_choice_PCS_Port.SetSelection( 0 )
		self.m_choice_PCS_Port.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		wSizer_SEMC_NOR.Add( self.m_choice_PCS_Port, 0, wx.ALL, 5 )
		
		self.staticText_ADV_Polarity = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"     ADV Port Polarity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ADV_Polarity.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_ADV_Polarity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_ADV_PolarityChoices = [ u"Low active", u"High active" ]
		self.m_choice_ADV_Polarity = wx.Choice( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,25 ), m_choice_ADV_PolarityChoices, 0 )
		self.m_choice_ADV_Polarity.SetSelection( 0 )
		wSizer_SEMC_NOR.Add( self.m_choice_ADV_Polarity, 0, wx.ALL, 5 )
		
		self.staticText_DataPort_Size = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Data Port Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_DataPort_Size.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_DataPort_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_DataPort_SizeChoices = [ u"8bits", u"8bits", u"16bits", u"24bits" ]
		self.m_choice_DataPort_Size = wx.Choice( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_DataPort_SizeChoices, 0 )
		self.m_choice_DataPort_Size.SetSelection( 0 )
		wSizer_SEMC_NOR.Add( self.m_choice_DataPort_Size, 0, wx.ALL, 5 )
		
		self.staticText_Timing_Mode = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"     AC Timing Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Timing_Mode.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_Timing_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Timing_ModeChoices = [ u"Safe mode", u"Fast mode", u"User defined(Field 0x04-0x19)" ]
		self.m_choice_Timing_Mode = wx.Choice( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,25 ), m_choice_Timing_ModeChoices, 0 )
		self.m_choice_Timing_Mode.SetSelection( 0 )
		wSizer_SEMC_NOR.Add( self.m_choice_Timing_Mode, 0, wx.ALL, 5 )
		
		self.staticText_Command_Set = wx.StaticText( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Command Set:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Command_Set.Wrap( -1 )
		
		wSizer_SEMC_NOR.Add( self.staticText_Command_Set, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Command_SetChoices = [ u"EPSCD-As Micron MT28EW", u"SFMCD-As Micron MT28GU" ]
		self.m_choice_Command_Set = wx.Choice( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,25 ), m_choice_Command_SetChoices, 0 )
		self.m_choice_Command_Set.SetSelection( 0 )
		wSizer_SEMC_NOR.Add( self.m_choice_Command_Set, 0, wx.ALL, 5 )
		
		
		sbSizer_SEMC_NOR.Add( wSizer_SEMC_NOR, 1, wx.EXPAND, 5 )
		
		sbSizer_Setting_Nxp = wx.StaticBoxSizer( wx.StaticBox( sbSizer_SEMC_NOR.GetStaticBox(), wx.ID_ANY, u"Setting By NXP" ), wx.VERTICAL )
		
		wSizer_Setting_Nxp = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_tCES = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"tCES:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCES.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tCES, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tCESChoices = [ u"CE setup time in ns" ]
		self.m_choice_tCES = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tCESChoices, 0 )
		self.m_choice_tCES.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tCES, 0, wx.ALL, 5 )
		
		self.m_staticText_tCEH = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"     tCEH:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCEH.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tCEH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tCEHChoices = [ u"CE hold time in ns" ]
		self.m_choice_tCEH = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tCEHChoices, 0 )
		self.m_choice_tCEH.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tCEH, 0, wx.ALL, 5 )
		
		self.m_staticText_tCEITV = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"tCEITV:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tCEITV.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tCEITV, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tCEITVChoices = [ u"CE# interval time in ns" ]
		self.m_choice_tCEITV = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tCEITVChoices, 0 )
		self.m_choice_tCEITV.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tCEITV, 0, wx.ALL, 5 )
		
		self.m_staticText_tAS = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"     tAS:          ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tAS.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tAS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tASChoices = [ u"Address setup time in ns" ]
		self.m_choice_tAS = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tASChoices, 0 )
		self.m_choice_tAS.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tAS, 0, wx.ALL, 5 )
		
		self.m_staticText_tAH = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"tAH:       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tAH.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tAH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tAHChoices = [ u"Address hold time in ns" ]
		self.m_choice_tAH = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tAHChoices, 0 )
		self.m_choice_tAH.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tAH, 0, wx.ALL, 5 )
		
		self.m_staticText_tTA = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"     tTA:         ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tTA.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tTA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tTAChoices = [ u"Turnaround time in ns" ]
		self.m_choice_tTA = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tTAChoices, 0 )
		self.m_choice_tTA.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tTA, 0, wx.ALL, 5 )
		
		self.m_staticText_tWEL = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"tWEL:     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tWEL.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tWEL, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tWELChoices = [ u"WE LOW time in ns" ]
		self.m_choice_tWEL = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tWELChoices, 0 )
		self.m_choice_tWEL.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tWEL, 0, wx.ALL, 5 )
		
		self.m_staticText_tWEH = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"     tWEH:     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tWEH.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tWEH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice14Choices = [ u"WE HIGH time in ns" ]
		self.m_choice14 = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice14Choices, 0 )
		self.m_choice14.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice14, 0, wx.ALL, 5 )
		
		self.m_staticText_tREL = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"tREL:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tREL.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tREL, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tRELChoices = [ u"RE LOW time in ns" ]
		self.m_choice_tREL = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tRELChoices, 0 )
		self.m_choice_tREL.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tREL, 0, wx.ALL, 5 )
		
		self.m_staticText_tREH = wx.StaticText( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, u"     tREH:       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_tREH.Wrap( -1 )
		
		wSizer_Setting_Nxp.Add( self.m_staticText_tREH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_tREHChoices = [ u"RE HIGH time in ns" ]
		self.m_choice_tREH = wx.Choice( sbSizer_Setting_Nxp.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,25 ), m_choice_tREHChoices, 0 )
		self.m_choice_tREH.SetSelection( 0 )
		wSizer_Setting_Nxp.Add( self.m_choice_tREH, 0, wx.ALL, 5 )
		
		
		sbSizer_Setting_Nxp.Add( wSizer_Setting_Nxp, 1, wx.EXPAND, 5 )
		
		
		sbSizer_SEMC_NOR.Add( sbSizer_Setting_Nxp, 1, wx.EXPAND, 5 )
		
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

	def OnClose_SEMC_NOR( self, event ):
                ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
                if ret == wx.OK:
                        self.Show(False)

###########################################################################
## Class MyFrame_SEMC_NAND
###########################################################################

class MyFrame_SEMC_NAND ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SEMC_NAND", pos = wx.DefaultPosition, size = wx.Size( 735,516 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE,self.OnClose_SEMC_NAND)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer_SEMC_NAND = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure" ), wx.VERTICAL )
		
		self.staticText_SEMC_NAND = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Configuration of SEMC NAND", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SEMC_NAND.Wrap( -1 )
		
		sbSizer_SEMC_NAND.Add( self.staticText_SEMC_NAND, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_configure = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.staticText_ECC_Status = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Device ECC Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ECC_Status.Wrap( -1 )
		
		wSizer_configure.Add( self.staticText_ECC_Status, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_ECC_StatusChoices = [ u"Enable", u"Disable" ]
		self.m_choice_ECC_Status = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_ECC_StatusChoices, 0 )
		self.m_choice_ECC_Status.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_ECC_Status, 0, wx.ALL, 5 )
		
		self.staticText_ECC_Type = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"ECC Check Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_ECC_Type.Wrap( -1 )
		
		wSizer_configure.Add( self.staticText_ECC_Type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_ECC_TypeChoices = [ u"Software (1bit SEC)", u"Hardware (Device)" ]
		self.m_choice_ECC_Type = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,25 ), m_choice_ECC_TypeChoices, 0 )
		self.m_choice_ECC_Type.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_ECC_Type, 0, wx.ALL, 5 )
		
		self.staticText_DatePort_Size = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"IO Port Size:           ", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.staticText_DatePort_Size.Wrap( -1 )
		
		wSizer_configure.Add( self.staticText_DatePort_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_DatePort_SizeChoices = [ u"8bits", u"16bits" ]
		self.m_choice_DatePort_Size = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,25 ), m_choice_DatePort_SizeChoices, 0 )
		self.m_choice_DatePort_Size.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_DatePort_Size, 0, wx.ALL, 5 )
		
		self.staticText_EDO_Mode = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"EDO Mode:            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EDO_Mode.Wrap( -1 )
		
		wSizer_configure.Add( self.staticText_EDO_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_EDO_ModeChoices = [ u"EDO Disable", u"EDO Enable" ]
		self.m_choice_EDO_Mode = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_EDO_ModeChoices, 0 )
		self.m_choice_EDO_Mode.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_EDO_Mode, 0, wx.ALL, 5 )
		
		self.m_staticText_Image_Copies = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Image Copies:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image_Copies.Wrap( -1 )
		
		wSizer_configure.Add( self.m_staticText_Image_Copies, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Image_CopiesChoices = [ u"One image", u"Two image", u"Three image", u"Four image", u"Five image", u"Six image", u"Seven image", u"Eight image" ]
		self.m_choice_Image_Copies = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,25 ), m_choice_Image_CopiesChoices, 0 )
		self.m_choice_Image_Copies.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_Image_Copies, 0, wx.ALL, 5 )
		
		self.m_staticText_Search_Stride = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Search Stride:        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Search_Stride.Wrap( -1 )
		
		wSizer_configure.Add( self.m_staticText_Search_Stride, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Search_StrideChoices = [ u"1 block", u"2 block", u"3 block", u"4 block", u"5 block", u"6 block", u"7 block", u"8 block" ]
		self.m_choice_Search_Stride = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,25 ), m_choice_Search_StrideChoices, 0 )
		self.m_choice_Search_Stride.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_Search_Stride, 0, wx.ALL, 5 )
		
		self.m_staticText_Search_Count = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"Search Count:       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Search_Count.Wrap( -1 )
		
		wSizer_configure.Add( self.m_staticText_Search_Count, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Search_CountChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8" ]
		self.m_choice_Search_Count = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), m_choice_Search_CountChoices, 0 )
		self.m_choice_Search_Count.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_Search_Count, 0, wx.ALL, 5 )
		
		self.m_staticText_IPCS_Port = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"IPCS Port:              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_IPCS_Port.Wrap( -1 )
		
		wSizer_configure.Add( self.m_staticText_IPCS_Port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_IPCS_PortChoices = [ u"CSX0" ]
		self.m_choice_IPCS_Port = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,25 ), m_choice_IPCS_PortChoices, 0 )
		self.m_choice_IPCS_Port.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_IPCS_Port, 0, wx.ALL, 5 )
		
		self.m_staticText_ONFI_Mode = wx.StaticText( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"ONFI timing mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ONFI_Mode.Wrap( -1 )
		
		wSizer_configure.Add( self.m_staticText_ONFI_Mode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_ONFI_ModeChoices = [ u"mode 0 (10MHz)" ]
		self.m_choice_ONFI_Mode = wx.Choice( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,25 ), m_choice_ONFI_ModeChoices, 0 )
		self.m_choice_ONFI_Mode.SetSelection( 0 )
		wSizer_configure.Add( self.m_choice_ONFI_Mode, 0, wx.ALL, 5 )
		
		
		sbSizer_SEMC_NAND.Add( wSizer_configure, 1, wx.EXPAND, 5 )
		
		sbSizer_FCB = wx.StaticBoxSizer( wx.StaticBox( sbSizer_SEMC_NAND.GetStaticBox(), wx.ID_ANY, u"FCB Options" ), wx.VERTICAL )
		
		wSizer_FCB = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		sbSizer_Image0 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image0" ), wx.VERTICAL )
		
		gSizer_Image0 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image0_Index = wx.StaticText( sbSizer_Image0.GetStaticBox(), wx.ID_ANY, u"Image0 Index: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image0_Index.Wrap( -1 )
		
		gSizer_Image0.Add( self.m_staticText_Image0_Index, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_Image0_Index = wx.TextCtrl( sbSizer_Image0.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image0.Add( self.m_textCtrl_Image0_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image0_Count = wx.StaticText( sbSizer_Image0.GetStaticBox(), wx.ID_ANY, u"Image0 Count: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image0_Count.Wrap( -1 )
		
		gSizer_Image0.Add( self.m_staticText_Image0_Count, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl__Image0_Count = wx.TextCtrl( sbSizer_Image0.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image0.Add( self.m_textCtrl__Image0_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image0.Add( gSizer_Image0, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image0, 1, wx.EXPAND, 5 )
		
		sbSizer_Image2 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image2" ), wx.VERTICAL )
		
		gSizer_Image2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image2_Index = wx.StaticText( sbSizer_Image2.GetStaticBox(), wx.ID_ANY, u"Image2 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image2_Index.Wrap( -1 )
		
		gSizer_Image2.Add( self.m_staticText_Image2_Index, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_Image2_Index = wx.TextCtrl( sbSizer_Image2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image2.Add( self.m_textCtrl_Image2_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image2_Count = wx.StaticText( sbSizer_Image2.GetStaticBox(), wx.ID_ANY, u"Image2 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image2_Count.Wrap( -1 )
		
		gSizer_Image2.Add( self.m_staticText_Image2_Count, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_Image2_Count = wx.TextCtrl( sbSizer_Image2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image2.Add( self.m_textCtrl_Image2_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image2.Add( gSizer_Image2, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image2, 1, wx.EXPAND, 5 )
		
		sbSizer_Image3 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image3" ), wx.VERTICAL )
		
		gSizer_Image3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image3_Index = wx.StaticText( sbSizer_Image3.GetStaticBox(), wx.ID_ANY, u"Image3 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image3_Index.Wrap( -1 )
		
		gSizer_Image3.Add( self.m_staticText_Image3_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image3_Index = wx.TextCtrl( sbSizer_Image3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image3.Add( self.m_textCtrl_Image3_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image3_Count = wx.StaticText( sbSizer_Image3.GetStaticBox(), wx.ID_ANY, u"Image3 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image3_Count.Wrap( -1 )
		
		gSizer_Image3.Add( self.m_staticText_Image3_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image3_Count = wx.TextCtrl( sbSizer_Image3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image3.Add( self.m_textCtrl_Image3_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image3.Add( gSizer_Image3, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image3, 1, wx.EXPAND, 5 )
		
		sbSizer_Image4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image4" ), wx.VERTICAL )
		
		gSizer_Image4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image4_Index = wx.StaticText( sbSizer_Image4.GetStaticBox(), wx.ID_ANY, u"Image4 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image4_Index.Wrap( -1 )
		
		gSizer_Image4.Add( self.m_staticText_Image4_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image4_Index = wx.TextCtrl( sbSizer_Image4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image4.Add( self.m_textCtrl_Image4_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image4_Count = wx.StaticText( sbSizer_Image4.GetStaticBox(), wx.ID_ANY, u"Image4 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image4_Count.Wrap( -1 )
		
		gSizer_Image4.Add( self.m_staticText_Image4_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image4_Count = wx.TextCtrl( sbSizer_Image4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image4.Add( self.m_textCtrl_Image4_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image4.Add( gSizer_Image4, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image4, 1, wx.EXPAND, 5 )
		
		sbSizer_Image5 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image5" ), wx.VERTICAL )
		
		gSizer_Image5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image5_Index = wx.StaticText( sbSizer_Image5.GetStaticBox(), wx.ID_ANY, u"Image5 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image5_Index.Wrap( -1 )
		
		gSizer_Image5.Add( self.m_staticText_Image5_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image5_Index = wx.TextCtrl( sbSizer_Image5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image5.Add( self.m_textCtrl_Image5_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image5_Count = wx.StaticText( sbSizer_Image5.GetStaticBox(), wx.ID_ANY, u"Image5 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image5_Count.Wrap( -1 )
		
		gSizer_Image5.Add( self.m_staticText_Image5_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image5_Count = wx.TextCtrl( sbSizer_Image5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image5.Add( self.m_textCtrl_Image5_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image5.Add( gSizer_Image5, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image5, 1, wx.EXPAND, 5 )
		
		sbSizer_Image6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image6" ), wx.VERTICAL )
		
		gSizer_Image6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image6_Index = wx.StaticText( sbSizer_Image6.GetStaticBox(), wx.ID_ANY, u"Image6 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image6_Index.Wrap( -1 )
		
		gSizer_Image6.Add( self.m_staticText_Image6_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image6_Index = wx.TextCtrl( sbSizer_Image6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image6.Add( self.m_textCtrl_Image6_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image6_Count = wx.StaticText( sbSizer_Image6.GetStaticBox(), wx.ID_ANY, u"Image6 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image6_Count.Wrap( -1 )
		
		gSizer_Image6.Add( self.m_staticText_Image6_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image6_Count = wx.TextCtrl( sbSizer_Image6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image6.Add( self.m_textCtrl_Image6_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image6.Add( gSizer_Image6, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image6, 1, wx.EXPAND, 5 )
		
		sbSizer_Image7 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image7" ), wx.VERTICAL )
		
		gSizer_Image7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image7_Index = wx.StaticText( sbSizer_Image7.GetStaticBox(), wx.ID_ANY, u"Image7 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image7_Index.Wrap( -1 )
		
		gSizer_Image7.Add( self.m_staticText_Image7_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image7_Index = wx.TextCtrl( sbSizer_Image7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image7.Add( self.m_textCtrl_Image7_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image7_Count = wx.StaticText( sbSizer_Image7.GetStaticBox(), wx.ID_ANY, u"Image7 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image7_Count.Wrap( -1 )
		
		gSizer_Image7.Add( self.m_staticText_Image7_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image7_Count = wx.TextCtrl( sbSizer_Image7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image7.Add( self.m_textCtrl_Image7_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image7.Add( gSizer_Image7, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image7, 1, wx.EXPAND, 5 )
		
		sbSizer_Image8 = wx.StaticBoxSizer( wx.StaticBox( sbSizer_FCB.GetStaticBox(), wx.ID_ANY, u"Image8" ), wx.VERTICAL )
		
		gSizer_Image8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText_Image8_Index = wx.StaticText( sbSizer_Image8.GetStaticBox(), wx.ID_ANY, u"Image8 Index:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image8_Index.Wrap( -1 )
		
		gSizer_Image8.Add( self.m_staticText_Image8_Index, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image8_Index = wx.TextCtrl( sbSizer_Image8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image8.Add( self.m_textCtrl_Image8_Index, 0, wx.ALL, 5 )
		
		self.m_staticText_Image8_Count = wx.StaticText( sbSizer_Image8.GetStaticBox(), wx.ID_ANY, u"Image8 Count:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Image8_Count.Wrap( -1 )
		
		gSizer_Image8.Add( self.m_staticText_Image8_Count, 0, wx.ALL, 5 )
		
		self.m_textCtrl_Image8_Count = wx.TextCtrl( sbSizer_Image8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		gSizer_Image8.Add( self.m_textCtrl_Image8_Count, 0, wx.ALL, 5 )
		
		
		sbSizer_Image8.Add( gSizer_Image8, 1, wx.EXPAND, 5 )
		
		
		wSizer_FCB.Add( sbSizer_Image8, 1, wx.EXPAND, 5 )
		
		
		sbSizer_FCB.Add( wSizer_FCB, 1, wx.EXPAND, 5 )
		
		
		sbSizer_SEMC_NAND.Add( sbSizer_FCB, 1, wx.EXPAND, 5 )
		
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

	def OnClose_SEMC_NAND( self, event ):
                ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
                if ret == wx.OK:
                        self.Show(False)



###########################################################################
## Class MyFrame_SD_EMMC
###########################################################################

class MyFrame_SD_EMMC ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SD_EMMC", pos = wx.DefaultPosition, size = wx.Size( 512,495 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE,self.OnClose_SD_EMMC)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer_SD_EMMC = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_SD = wx.StaticText( self, wx.ID_ANY, u"Configurations of SD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_SD.Wrap( -1 )
		
		self.m_staticText_SD.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer_SD_EMMC.Add( self.m_staticText_SD, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_SD = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_BUS_WIDTH = wx.StaticText( self, wx.ID_ANY, u"BUS WIDTH:        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BUS_WIDTH.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_BUS_WIDTH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_BUS_WIDTH = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		wSizer_SD.Add( self.m_textCtrl_BUS_WIDTH, 0, wx.ALL, 5 )
		
		self.m_staticText_TIMING = wx.StaticText( self, wx.ID_ANY, u"TIMING_INTERFACE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_TIMING.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_TIMING, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_TIMINGChoices = [ u"Normal/SDR12", u"High/SDR25", u"SDR50", u"SDR104" ]
		self.m_choice_TIMING = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 185,25 ), m_choice_TIMINGChoices, 0 )
		self.m_choice_TIMING.SetSelection( 0 )
		wSizer_SD.Add( self.m_choice_TIMING, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_UP = wx.StaticText( self, wx.ID_ANY, u"CPWR_UP_TIME:     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_UP.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_PWR_UP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_UPChoices = [ u"5ms", u"2.5ms" ]
		self.m_choice_PWR_UP = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 55,25 ), m_choice_PWR_UPChoices, 0 )
		self.m_choice_PWR_UP.SetSelection( 0 )
		wSizer_SD.Add( self.m_choice_PWR_UP, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_CYCLE = wx.StaticText( self, wx.ID_ANY, u"PWR_CYCLE_ENABLE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_CYCLE.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_PWR_CYCLE, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_CYCLEChoices = [ u"disable for non-UHSI timing", u"enable" ]
		self.m_choice_PWR_CYCLE = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,25 ), m_choice_PWR_CYCLEChoices, 0 )
		self.m_choice_PWR_CYCLE.SetSelection( 0 )
		wSizer_SD.Add( self.m_choice_PWR_CYCLE, 0, wx.ALL, 5 )
		
		self.m_staticText_Query_PWR_DOWN = wx.StaticText( self, wx.ID_ANY, u"PWR_DOWN_TIME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Query_PWR_DOWN.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_Query_PWR_DOWN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_Query_PWR_DOWNChoices = [ u"20ms", u"10ms", u"5ms", u"2.5ms" ]
		self.m_choice_Query_PWR_DOWN = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 55,25 ), m_choice_Query_PWR_DOWNChoices, 0 )
		self.m_choice_Query_PWR_DOWN.SetSelection( 0 )
		wSizer_SD.Add( self.m_choice_Query_PWR_DOWN, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_POLARITY = wx.StaticText( self, wx.ID_ANY, u"PWR_POLARITY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_POLARITY.Wrap( -1 )
		
		wSizer_SD.Add( self.m_staticText_PWR_POLARITY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_POLARITYChoices = [ u"Power down when uSDHC.RST set low", u"Power down when uSDHC.RST set high" ]
		self.m_choice_PWR_POLARITY = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,25 ), m_choice_PWR_POLARITYChoices, 0 )
		self.m_choice_PWR_POLARITY.SetSelection( 0 )
		wSizer_SD.Add( self.m_choice_PWR_POLARITY, 0, wx.ALL, 5 )
		
		
		bSizer_SD_EMMC.Add( wSizer_SD, 1, wx.EXPAND, 5 )
		
		self.m_staticText_EMMC = wx.StaticText( self, wx.ID_ANY, u"Configurations of EMMC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_EMMC.Wrap( -1 )
		
		self.m_staticText_EMMC.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer_SD_EMMC.Add( self.m_staticText_EMMC, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer_EMMC = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText_BOOT_CONFIG = wx.StaticText( self, wx.ID_ANY, u"BOOT_CONFIG_ENABLE:              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_CONFIG.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_CONFIG, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_CONFIGChoices = [ u"Boot configuration will be ignored", u"Boot configuration will be written into device" ]
		self.m_choice_BOOT_CONFIG = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), m_choice_BOOT_CONFIGChoices, 0 )
		self.m_choice_BOOT_CONFIG.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_BOOT_CONFIG, 0, wx.ALL, 5 )
		
		self.m_staticText_BOOT_ACK = wx.StaticText( self, wx.ID_ANY, u"BOOT_ACK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_ACK.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_ACK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_ACKChoices = [ u"NO ACK", u"ACK" ]
		self.m_choice_BOOT_ACK = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_BOOT_ACKChoices, 0 )
		self.m_choice_BOOT_ACK.SetSelection( 0 )
		self.m_choice_BOOT_ACK.SetMinSize( wx.Size( 95,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_BOOT_ACK, 0, wx.ALL, 5 )
		
		self.m_staticText_BOOT_BUS = wx.StaticText( self, wx.ID_ANY, u"  BOOT_BUS_CONDITIONS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_BUS.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_BUS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_BUSChoices = [ u"Reset to x1,SDR,Normal", u"Retain boot config" ]
		self.m_choice_BOOT_BUS = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_BOOT_BUSChoices, 0 )
		self.m_choice_BOOT_BUS.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_BOOT_BUS, 0, wx.ALL, 5 )
		
		self.m_staticText_BOOT_MODE = wx.StaticText( self, wx.ID_ANY, u"BOOT_MODE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_MODE.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_MODE, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_MODEChoices = [ u"Normal", u"HS", u"DDR" ]
		self.m_choice_BOOT_MODE = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_BOOT_MODEChoices, 0 )
		self.m_choice_BOOT_MODE.SetSelection( 0 )
		self.m_choice_BOOT_MODE.SetMinSize( wx.Size( 83,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_BOOT_MODE, 0, wx.ALL, 5 )
		
		self.m_staticText_PARTITION_ACCESS = wx.StaticText( self, wx.ID_ANY, u"   PARTITION_ACCESS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PARTITION_ACCESS.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_PARTITION_ACCESS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PARTITION_ACCESSChoices = [ u"User data area", u"Boot partition 1", u"Boot partition 2", u"RPMB", u"General Purpose parition 1", u"General Purpose parition 2", u"General Purpose parition 3", u"General Purpose parition 4" ]
		self.m_choice_PARTITION_ACCESS = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), m_choice_PARTITION_ACCESSChoices, 0 )
		self.m_choice_PARTITION_ACCESS.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_PARTITION_ACCESS, 0, wx.ALL, 5 )
		
		self.m_staticText_BUS_WIDTH = wx.StaticText( self, wx.ID_ANY, u"BUS_WIDTH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BUS_WIDTH.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BUS_WIDTH, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BUS_WIDTHChoices = [ u" x1 SDR", u" x4 SDR", u" x8 SDR", u"x4 DDR", u"x8 DDR" ]
		self.m_choice_BUS_WIDTH = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 75,-1 ), m_choice_BUS_WIDTHChoices, 0 )
		self.m_choice_BUS_WIDTH.SetSelection( 0 )
		self.m_choice_BUS_WIDTH.SetMinSize( wx.Size( 90,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_BUS_WIDTH, 0, wx.ALL, 5 )
		
		self.m_staticText_BOOT_PARTITION = wx.StaticText( self, wx.ID_ANY, u"   BOOT_PARTITION_ENABLE:      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_PARTITION.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_PARTITION, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_PARTITIONChoices = [ u"Not enabled", u"Boot partition 1", u"Boot partition 2", u"User data area" ]
		self.m_choice_BOOT_PARTITION = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,-1 ), m_choice_BOOT_PARTITIONChoices, 0 )
		self.m_choice_BOOT_PARTITION.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_BOOT_PARTITION, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_UP = wx.StaticText( self, wx.ID_ANY, u"PWR_UP_TIME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_UP.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_PWR_UP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_UPChoices = [ u"5ms", u"2.5ms" ]
		self.m_choice_PWR_UP = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_PWR_UPChoices, 0 )
		self.m_choice_PWR_UP.SetSelection( 0 )
		self.m_choice_PWR_UP.SetMinSize( wx.Size( 77,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_PWR_UP, 0, wx.ALL, 5 )
		
		self.m_staticText_BOOT_BUS = wx.StaticText( self, wx.ID_ANY, u"    BOOT_BUS_WIDTH:          ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_BOOT_BUS.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_BOOT_BUS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_BOOT_BUSChoices = [ u"x1(SDR),x4(DDR)", u"x4(SDR,DDR)", u"x8(SDR,DDR)" ]
		self.m_choice_BOOT_BUS = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_BOOT_BUSChoices, 0 )
		self.m_choice_BOOT_BUS.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_BOOT_BUS, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_DOWN = wx.StaticText( self, wx.ID_ANY, u"PWR_DOWN_TIME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_DOWN.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_PWR_DOWN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_DOWNChoices = [ u"20ms", u"10ms", u"5ms", u"2.5ms" ]
		self.m_choice_PWR_DOWN = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_PWR_DOWNChoices, 0 )
		self.m_choice_PWR_DOWN.SetSelection( 0 )
		self.m_choice_PWR_DOWN.SetMinSize( wx.Size( 55,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_PWR_DOWN, 0, wx.ALL, 5 )
		
		self.m_staticText_1V8 = wx.StaticText( self, wx.ID_ANY, u"    1V8_ENABLE:                      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_1V8.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_1V8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_1V8Choices = [ u" not set vselect pin", u"set vselect pin high" ]
		self.m_choice_1V8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_1V8Choices, 0 )
		self.m_choice_1V8.SetSelection( 0 )
		self.m_choice_1V8.SetMinSize( wx.Size( 150,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_1V8, 0, wx.ALL, 5 )
		
		self.m_staticText_TIMING = wx.StaticText( self, wx.ID_ANY, u"TIMING_INTERFACE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_TIMING.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_TIMING, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_TIMINGChoices = [ u"HS" ]
		self.m_choice_TIMING = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_TIMINGChoices, 0 )
		self.m_choice_TIMING.SetSelection( 0 )
		self.m_choice_TIMING.SetMinSize( wx.Size( 50,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_TIMING, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_CYCLE = wx.StaticText( self, wx.ID_ANY, u"    PWR_CYCLE_ENABLE:                       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_CYCLE.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_PWR_CYCLE, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_CYCLEChoices = [ u"disable", u"enable" ]
		self.m_choice_PWR_CYCLE = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_PWR_CYCLEChoices, 0 )
		self.m_choice_PWR_CYCLE.SetSelection( 0 )
		self.m_choice_PWR_CYCLE.SetMinSize( wx.Size( 100,-1 ) )
		
		wSizer_EMMC.Add( self.m_choice_PWR_CYCLE, 0, wx.ALL, 5 )
		
		self.m_staticText_PWR_POLARITY = wx.StaticText( self, wx.ID_ANY, u"PWR_POLARITY:                             ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_PWR_POLARITY.Wrap( -1 )
		
		wSizer_EMMC.Add( self.m_staticText_PWR_POLARITY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_PWR_POLARITYChoices = [ u"Power down when uSDHC.RST set low", u"Power down when uSDHC.RST set high" ]
		self.m_choice_PWR_POLARITY = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_PWR_POLARITYChoices, 0 )
		self.m_choice_PWR_POLARITY.SetSelection( 0 )
		wSizer_EMMC.Add( self.m_choice_PWR_POLARITY, 0, wx.ALL, 5 )
		
		
		bSizer_SD_EMMC.Add( wSizer_EMMC, 1, wx.EXPAND, 5 )
		
		m_sdbSizer_SD_EMMC = wx.StdDialogButtonSizer()
		self.m_sdbSizer_SD_EMMCOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer_SD_EMMC.AddButton( self.m_sdbSizer_SD_EMMCOK )
		self.m_sdbSizer_SD_EMMCCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer_SD_EMMC.AddButton( self.m_sdbSizer_SD_EMMCCancel )
		m_sdbSizer_SD_EMMC.Realize();
		
		bSizer_SD_EMMC.Add( m_sdbSizer_SD_EMMC, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_SD_EMMC )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.m_sdbSizer_SD_EMMCCancel.Bind( wx.EVT_BUTTON, self.cancel_of_SD_EMMC )
		self.m_sdbSizer_SD_EMMCOK.Bind( wx.EVT_BUTTON, self.apply_of_SD_EMMC )
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def cancel_of_SD_EMMC( self, event ):
                
                self.Show(False)
                event.Skip()
	
	def apply_of_SD_EMMC( self, event ):
                
                self.Show(False)
		event.Skip()

	def OnClose_SD_EMMC( self, event ):
                ret = wx.MessageBox('Do you really want to leave?',  'Confirm', wx.OK|wx.CANCEL)
                if ret == wx.OK:
                        self.Show(False)
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

		self.m_button_BootDeviceConfiguration.Bind( wx.EVT_BUTTON, self.callbackBoot_Device_Configuration )
                self.m_button_BootDeviceConfiguration.SetToolTipString("This is Boot_Device_Configuration.")



		self.m_button_doAuth.Bind( wx.EVT_BUTTON, self.callbackUN_CST_Tool )
                self.m_button_doAuth.SetToolTipString("This is the first step to run CST tool.")

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackSwitchSecureBootType( self, event ):
		event.Skip()

	def callbackSwitchKeyStorageRegion( self, event ):
		event.Skip()

	def callbackBoot_Device_Configuration( self, event ):
		event.Skip()

	def callbackUN_CST_Tool( self, event ):
		event.Skip()

		


