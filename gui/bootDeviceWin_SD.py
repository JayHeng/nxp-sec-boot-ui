import wx
import wx.xrc


###########################################################################
## Class MyFrame_SD
###########################################################################

class bootDeviceWin_SD(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(527, 320), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Bind(wx.EVT_CLOSE, self.OnClose_SD)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        wSizer_SD = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_notebook_SD = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_SD = wx.Panel(self.m_notebook_SD, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer_SD = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_BUS_WIDTH = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"BUS WIDTH:        ",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_BUS_WIDTH.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_BUS_WIDTH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_BUS_WIDTH = wx.TextCtrl(self.m_panel_SD, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.Size(70, -1), 0)
        gSizer_SD.Add(self.m_textCtrl_BUS_WIDTH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_TIMING = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"TIMING_INTERFACE:", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText_TIMING.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_TIMING, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_TIMINGChoices = [u"Normal/SDR12", u"High/SDR25", u"SDR50", u"SDR104"]
        self.m_choice_TIMING = wx.Choice(self.m_panel_SD, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 25),
                                         m_choice_TIMINGChoices, 0)
        self.m_choice_TIMING.SetSelection(0)
        gSizer_SD.Add(self.m_choice_TIMING, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_PWR_UP = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"CPWR_UP_TIME:     ", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText_PWR_UP.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_PWR_UP, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_UPChoices = [u"5ms", u"2.5ms"]
        self.m_choice_PWR_UP = wx.Choice(self.m_panel_SD, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, 25),
                                         m_choice_PWR_UPChoices, 0)
        self.m_choice_PWR_UP.SetSelection(0)
        gSizer_SD.Add(self.m_choice_PWR_UP, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_PWR_CYCLE = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"PWR_CYCLE_ENABLE:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_PWR_CYCLE.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_PWR_CYCLE, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_CYCLEChoices = [u"disable for non-UHSI timing", u"enable for non-UHSI timing"]
        self.m_choice_PWR_CYCLE = wx.Choice(self.m_panel_SD, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 25),
                                            m_choice_PWR_CYCLEChoices, 0)
        self.m_choice_PWR_CYCLE.SetSelection(0)
        gSizer_SD.Add(self.m_choice_PWR_CYCLE, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_Query_PWR_DOWN = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"PWR_DOWN_TIME:",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_Query_PWR_DOWN.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_Query_PWR_DOWN, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Query_PWR_DOWNChoices = [u"20ms", u"10ms", u"5ms", u"2.5ms"]
        self.m_choice_Query_PWR_DOWN = wx.Choice(self.m_panel_SD, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, 25),
                                                 m_choice_Query_PWR_DOWNChoices, 0)
        self.m_choice_Query_PWR_DOWN.SetSelection(0)
        gSizer_SD.Add(self.m_choice_Query_PWR_DOWN, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_PWR_POLARITY = wx.StaticText(self.m_panel_SD, wx.ID_ANY, u"PWR_POLARITY:", wx.DefaultPosition,
                                                       wx.DefaultSize, 0)
        self.m_staticText_PWR_POLARITY.Wrap(-1)

        gSizer_SD.Add(self.m_staticText_PWR_POLARITY, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_POLARITYChoices = [u"Power down when uSDHC.RST set low", u"Power down when uSDHC.RST set high"]
        self.m_choice_PWR_POLARITY = wx.Choice(self.m_panel_SD, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 25),
                                               m_choice_PWR_POLARITYChoices, 0)
        self.m_choice_PWR_POLARITY.SetSelection(0)
        gSizer_SD.Add(self.m_choice_PWR_POLARITY, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel_SD.SetSizer(gSizer_SD)
        self.m_panel_SD.Layout()
        gSizer_SD.Fit(self.m_panel_SD)
        self.m_notebook_SD.AddPage(self.m_panel_SD, u"SD Option", False)

        wSizer_SD.Add(self.m_notebook_SD, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText_SD = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.Size(300, -1), 0)
        self.m_staticText_SD.Wrap(-1)

        wSizer_SD.Add(self.m_staticText_SD, 0, wx.ALL, 5)

        m_sdbSizer_SD = wx.StdDialogButtonSizer()
        self.m_sdbSizer_SDOK = wx.Button(self, wx.ID_OK)
        m_sdbSizer_SD.AddButton(self.m_sdbSizer_SDOK)
        self.m_sdbSizer_SDCancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer_SD.AddButton(self.m_sdbSizer_SDCancel)
        m_sdbSizer_SD.Realize();

        wSizer_SD.Add(m_sdbSizer_SD, 1, wx.EXPAND, 5)

        self.SetSizer(wSizer_SD)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_sdbSizer_SDCancel.Bind(wx.EVT_BUTTON, self.cancel_of_SD)
        self.m_sdbSizer_SDOK.Bind(wx.EVT_BUTTON, self.apply_of_SD)

    def __del__(self):
        pass
        # Virtual event handlers, overide them in your derived class

    def cancel_of_SD(self, event):
        event.Skip()

    def apply_of_SD(self, event):
        event.Skip()

    def OnClose_SD(self, event):
        event.Skip()