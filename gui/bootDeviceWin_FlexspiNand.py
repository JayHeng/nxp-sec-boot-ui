import wx
import wx.xrc


###########################################################################
## Class MyFrame_FLEXSPI_NAND
###########################################################################

class bootDeviceWin_FlexspiNand(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(723, 320), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Bind(wx.EVT_CLOSE, self.OnClose_FLEXSPI_NAND)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        wSizer_FLEXSPI_NAND = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_notebook_NAND_Option = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_Nand_Option = wx.Panel(self.m_notebook_NAND_Option, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        gSizer_Nand_Option = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_Max_Freq = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Max Freq:",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Max_Freq.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_Max_Freq, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Max_FreqChoices = [u"30MHz", u"50MHz", u"60MHz", u"75MHz", u"80MHz", u"100MHz"]
        self.m_choice_Max_Freq = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(70, 25),
                                           m_choice_Max_FreqChoices, 0)
        self.m_choice_Max_Freq.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_Max_Freq, 0, wx.ALL, 5)

        self.m_staticText_Page_Size = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Page Size (KBytes):",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Page_Size.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_Page_Size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Page_SizeChoices = [u"2KB", u"4KB"]
        self.m_choice_Page_Size = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, 25),
                                            m_choice_Page_SizeChoices, 0)
        self.m_choice_Page_Size.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_Page_Size, 0, wx.ALL, 5)

        self.m_staticText_Pages = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Pages Per Block:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Pages.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_Pages, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PagesChoices = [u"64", u"128", u"256", u"32"]
        self.m_choice_Pages = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(60, 25),
                                        m_choice_PagesChoices, 0)
        self.m_choice_Pages.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_Pages, 0, wx.ALL, 5)

        self.m_staticText_Flash_size = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Flash size:",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Flash_size.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_Flash_size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Flash_sizeChoices = [u"512M", u"1GB", u"2GB", u"4GB"]
        self.m_choice_Flash_size = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(70, 25),
                                             m_choice_Flash_sizeChoices, 0)
        self.m_choice_Flash_size.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_Flash_size, 0, wx.ALL, 5)

        self.m_staticText_planes = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Has multiplanes:   ",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_planes.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_planes, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_planesChoices = [u"1 plane", u"2 planes"]
        self.m_choice_planes = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, 25),
                                         m_choice_planesChoices, 0)
        self.m_choice_planes.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_planes, 0, wx.ALL, 5)

        self.m_staticText_Option_size = wx.StaticText(self.m_panel_Nand_Option, wx.ID_ANY, u"Option size:        ",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Option_size.Wrap(-1)

        gSizer_Nand_Option.Add(self.m_staticText_Option_size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Option_sizeChoices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12",
                                       u"13", u"14", u"15"]
        self.m_choice_Option_size = wx.Choice(self.m_panel_Nand_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(60, 25),
                                              m_choice_Option_sizeChoices, 0)
        self.m_choice_Option_size.SetSelection(0)
        gSizer_Nand_Option.Add(self.m_choice_Option_size, 0, wx.ALL, 5)

        self.m_panel_Nand_Option.SetSizer(gSizer_Nand_Option)
        self.m_panel_Nand_Option.Layout()
        gSizer_Nand_Option.Fit(self.m_panel_Nand_Option)
        self.m_notebook_NAND_Option.AddPage(self.m_panel_Nand_Option, u"Nand Option", False)

        wSizer_FLEXSPI_NAND.Add(self.m_notebook_NAND_Option, 1, wx.EXPAND | wx.ALL, 5)

        self.m_notebook_FCB_Option = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_FCB_Option = wx.Panel(self.m_notebook_FCB_Option, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL)
        gSizer_FCB_Option = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_Size = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"Size:           ",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Size.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_Size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_SizeChoices = [u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10"]
        self.m_choice_Size = wx.Choice(self.m_panel_FCB_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(60, -1),
                                       m_choice_SizeChoices, 0)
        self.m_choice_Size.SetSelection(0)
        gSizer_FCB_Option.Add(self.m_choice_Size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_address_type = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"address_type:         ",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_address_type.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_address_type, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_address_typeChoices = [u"byte address", u"block address"]
        self.m_choice_address_type = wx.Choice(self.m_panel_FCB_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(90, -1),
                                               m_choice_address_typeChoices, 0)
        self.m_choice_address_type.SetSelection(0)
        gSizer_FCB_Option.Add(self.m_choice_address_type, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_search_stride = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"search_stride:     ",
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_search_stride.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_search_stride, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_search_strideChoices = [u"64 pages", u"128 pages", u"256 pages", u"32 pages"]
        self.m_choice_search_stride = wx.Choice(self.m_panel_FCB_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(60, -1),
                                                m_choice_search_strideChoices, 0)
        self.m_choice_search_stride.SetSelection(0)
        gSizer_FCB_Option.Add(self.m_choice_search_stride, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_search_count = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"search_count:",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_search_count.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_search_count, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_search_countChoices = [u"1", u"2", u"3", u"4"]
        self.m_choice_search_count = wx.Choice(self.m_panel_FCB_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(43, -1),
                                               m_choice_search_countChoices, 0)
        self.m_choice_search_count.SetSelection(0)
        gSizer_FCB_Option.Add(self.m_choice_search_count, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_block_count = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"block_count:          ",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_block_count.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_block_count, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_block_count = wx.TextCtrl(self.m_panel_FCB_Option, wx.ID_ANY, u"0",
                                                  wx.DefaultPosition, wx.Size(90, -1), 0)
        gSizer_FCB_Option.Add(self.m_textCtrl_block_count, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_block_id = wx.StaticText(self.m_panel_FCB_Option, wx.ID_ANY, u"block_id:             ",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_block_id.Wrap(-1)

        gSizer_FCB_Option.Add(self.m_staticText_block_id, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_block_id = wx.TextCtrl(self.m_panel_FCB_Option, wx.ID_ANY, u"0", wx.DefaultPosition,
                                               wx.Size(60, -1), 0)
        gSizer_FCB_Option.Add(self.m_textCtrl_block_id, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel_FCB_Option.SetSizer(gSizer_FCB_Option)
        self.m_panel_FCB_Option.Layout()
        gSizer_FCB_Option.Fit(self.m_panel_FCB_Option)
        self.m_notebook_FCB_Option.AddPage(self.m_panel_FCB_Option, u"FCB Option", False)

        wSizer_FLEXSPI_NAND.Add(self.m_notebook_FCB_Option, 1, wx.EXPAND | wx.ALL, 5)

        self.m_notebook_KeyBlob_Option = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_KeyBlob_Option = wx.Panel(self.m_notebook_KeyBlob_Option, wx.ID_ANY, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer_KeyBlob_Option = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_image_index = wx.StaticText(self.m_panel_KeyBlob_Option, wx.ID_ANY, u"image_index:",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_image_index.Wrap(-1)

        gSizer_KeyBlob_Option.Add(self.m_staticText_image_index, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_image_indexChoices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12",
                                       u"13", u"14", u"15"]
        self.m_choice_image_index = wx.Choice(self.m_panel_KeyBlob_Option, wx.ID_ANY, wx.DefaultPosition,
                                              wx.Size(80, -1), m_choice_image_indexChoices, 0)
        self.m_choice_image_index.SetSelection(0)
        gSizer_KeyBlob_Option.Add(self.m_choice_image_index, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_dek_size = wx.StaticText(self.m_panel_KeyBlob_Option, wx.ID_ANY, u"dek_size:",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_dek_size.Wrap(-1)

        gSizer_KeyBlob_Option.Add(self.m_staticText_dek_size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_dek_sizeChoices = [u"128bits"]
        self.m_choice_dek_size = wx.Choice(self.m_panel_KeyBlob_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1),
                                           m_choice_dek_sizeChoices, 0)
        self.m_choice_dek_size.SetSelection(0)
        gSizer_KeyBlob_Option.Add(self.m_choice_dek_size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_keyblob_infosize = wx.StaticText(self.m_panel_KeyBlob_Option, wx.ID_ANY,
                                                           u"keyblob_info size:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_keyblob_infosize.Wrap(-1)

        gSizer_KeyBlob_Option.Add(self.m_staticText_keyblob_infosize, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_keyblob_infosizeChoices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11",
                                            u"12", u"13", u"14", u"15"]
        self.m_choice_keyblob_infosize = wx.Choice(self.m_panel_KeyBlob_Option, wx.ID_ANY, wx.DefaultPosition,
                                                   wx.Size(80, -1), m_choice_keyblob_infosizeChoices, 0)
        self.m_choice_keyblob_infosize.SetSelection(0)
        gSizer_KeyBlob_Option.Add(self.m_choice_keyblob_infosize, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_type = wx.StaticText(self.m_panel_KeyBlob_Option, wx.ID_ANY, u"type:              ",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_type.Wrap(-1)

        gSizer_KeyBlob_Option.Add(self.m_staticText_type, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_typeChoices = [u"Update", u"Program"]
        self.m_choice_type = wx.Choice(self.m_panel_KeyBlob_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                       m_choice_typeChoices, 0)
        self.m_choice_type.SetSelection(0)
        gSizer_KeyBlob_Option.Add(self.m_choice_type, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel_KeyBlob_Option.SetSizer(gSizer_KeyBlob_Option)
        self.m_panel_KeyBlob_Option.Layout()
        gSizer_KeyBlob_Option.Fit(self.m_panel_KeyBlob_Option)
        self.m_notebook_KeyBlob_Option.AddPage(self.m_panel_KeyBlob_Option, u"KeyBlob Option", False)

        wSizer_FLEXSPI_NAND.Add(self.m_notebook_KeyBlob_Option, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText_FLEXSPI_NAND = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
                                                       wx.Size(500, -1), 0)
        self.m_staticText_FLEXSPI_NAND.Wrap(-1)

        wSizer_FLEXSPI_NAND.Add(self.m_staticText_FLEXSPI_NAND, 0, wx.ALL, 5)

        m_sdbSizer_FLEXSPI_NAND = wx.StdDialogButtonSizer()
        self.m_sdbSizer_FLEXSPI_NANDOK = wx.Button(self, wx.ID_OK)
        m_sdbSizer_FLEXSPI_NAND.AddButton(self.m_sdbSizer_FLEXSPI_NANDOK)
        self.m_sdbSizer_FLEXSPI_NANDCancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer_FLEXSPI_NAND.AddButton(self.m_sdbSizer_FLEXSPI_NANDCancel)
        m_sdbSizer_FLEXSPI_NAND.Realize();

        wSizer_FLEXSPI_NAND.Add(m_sdbSizer_FLEXSPI_NAND, 1, wx.EXPAND | wx.ALIGN_BOTTOM, 5)

        self.SetSizer(wSizer_FLEXSPI_NAND)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_sdbSizer_FLEXSPI_NANDCancel.Bind(wx.EVT_BUTTON, self.cancel_of_FLEXSPI_NAND)
        self.m_sdbSizer_FLEXSPI_NANDOK.Bind(wx.EVT_BUTTON, self.apply_of_FLEXSPI_NAND)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def cancel_of_FLEXSPI_NAND(self, event):
        event.Skip()

    def apply_of_FLEXSPI_NAND(self, event):
        event.Skip()

    def OnClose_FLEXSPI_NAND(self, event):
        event.Skip()