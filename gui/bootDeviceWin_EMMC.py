import wx
import wx.xrc


###########################################################################
## Class MyFrame_EMMC
###########################################################################

class bootDeviceWin_EMMC(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(522, 572), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Bind(wx.EVT_CLOSE, self.OnClose_EMMC)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        wSizer_EMMC = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_notebook_EMMC = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_EMMC = wx.Panel(self.m_notebook_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        gSizer_EMMC = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_BOOT_CONFIG = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY,
                                                      u"BOOT_CONFIG_ENABLE:              ", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.m_staticText_BOOT_CONFIG.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_CONFIG, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BOOT_CONFIGChoices = [u"Ignored", u"Be Written into device"]
        self.m_choice_BOOT_CONFIG = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(120, -1),
                                              m_choice_BOOT_CONFIGChoices, 0)
        self.m_choice_BOOT_CONFIG.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_BOOT_CONFIG, 0, wx.ALL, 5)

        self.m_staticText_BOOT_ACK = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"BOOT_ACK:", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText_BOOT_ACK.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_ACK, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BOOT_ACKChoices = [u"NO ACK", u"ACK"]
        self.m_choice_BOOT_ACK = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(80, -1),
                                           m_choice_BOOT_ACKChoices, 0)
        self.m_choice_BOOT_ACK.SetSelection(0)
        self.m_choice_BOOT_ACK.SetMinSize(wx.Size(95, -1))

        gSizer_EMMC.Add(self.m_choice_BOOT_ACK, 0, wx.ALL, 5)

        self.m_staticText_BOOT_BUS = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"BOOT_BUS_CONDITIONS:",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_BOOT_BUS.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_BUS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Boot_BusConditionChoices = [u"Reset to x1,SDR,Normal", u"Retain boot config"]
        self.m_choice_Boot_BusCondition = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                    m_choice_Boot_BusConditionChoices, 0)
        self.m_choice_Boot_BusCondition.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_Boot_BusCondition, 0, wx.ALL, 5)

        self.m_staticText_BOOT_MODE = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"BOOT_MODE:", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_BOOT_MODE.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_MODE, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BOOT_MODEChoices = [u"Normal", u"HS", u"DDR"]
        self.m_choice_BOOT_MODE = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            m_choice_BOOT_MODEChoices, 0)
        self.m_choice_BOOT_MODE.SetSelection(0)
        self.m_choice_BOOT_MODE.SetMinSize(wx.Size(83, -1))

        gSizer_EMMC.Add(self.m_choice_BOOT_MODE, 0, wx.ALL, 5)

        self.m_staticText_PARTITION_ACCESS = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"PARTITION_ACCESS:",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_PARTITION_ACCESS.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_PARTITION_ACCESS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PARTITION_ACCESSChoices = [u"User data area", u"Boot partition 1", u"Boot partition 2", u"RPMB",
                                            u"General Purpose parition 1", u"General Purpose parition 2",
                                            u"General Purpose parition 3", u"General Purpose parition 4"]
        self.m_choice_PARTITION_ACCESS = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                                   m_choice_PARTITION_ACCESSChoices, 0)
        self.m_choice_PARTITION_ACCESS.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_PARTITION_ACCESS, 0, wx.ALL, 5)

        self.m_staticText_BUS_WIDTH1 = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"BUS_WIDTH:", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText_BUS_WIDTH1.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BUS_WIDTH1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BUS_WIDTHChoices = [u"x1 SDR", u"x4 SDR", u"x8 SDR", u"x4 DDR", u"x8 DDR"]
        self.m_choice_BUS_WIDTH = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(75, -1),
                                            m_choice_BUS_WIDTHChoices, 0)
        self.m_choice_BUS_WIDTH.SetSelection(0)
        self.m_choice_BUS_WIDTH.SetMinSize(wx.Size(90, -1))

        gSizer_EMMC.Add(self.m_choice_BUS_WIDTH, 0, wx.ALL, 5)

        self.m_staticText_BOOT_PARTITION = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY,
                                                         u"BOOT_PARTITION_ENABLE:", wx.DefaultPosition,
                                                         wx.DefaultSize, 0)
        self.m_staticText_BOOT_PARTITION.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_PARTITION, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BOOT_PARTITIONChoices = [u"Not enabled", u"Boot partition 1", u"Boot partition 2", u"User data area"]
        self.m_choice_BOOT_PARTITION = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(120, -1),
                                                 m_choice_BOOT_PARTITIONChoices, 0)
        self.m_choice_BOOT_PARTITION.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_BOOT_PARTITION, 0, wx.ALL, 5)

        self.m_staticText_PWR_UP = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"PWR_UP_TIME:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.m_staticText_PWR_UP.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_PWR_UP, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_UPChoices = [u"5ms", u"2.5ms"]
        self.m_choice_PWR_UP = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          m_choice_PWR_UPChoices, 0)
        self.m_choice_PWR_UP.SetSelection(0)
        self.m_choice_PWR_UP.SetMinSize(wx.Size(77, -1))

        gSizer_EMMC.Add(self.m_choice_PWR_UP, 0, wx.ALL, 5)

        self.m_staticText_BOOT_BUS = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"BOOT_BUS_WIDTH:          ",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_BOOT_BUS.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_BOOT_BUS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_BOOT_BUSChoices = [u"x1(SDR),x4(DDR)", u"x4(SDR,DDR)", u"x8(SDR,DDR)"]
        self.m_choice_BOOT_BUS = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1),
                                            m_choice_BOOT_BUSChoices, 0)
        self.m_choice_BOOT_BUS.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_BOOT_BUS, 0, wx.ALL, 5)

        self.m_staticText_PWR_DOWN = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"PWR_DOWN_TIME:", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_staticText_PWR_DOWN.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_PWR_DOWN, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_DOWNChoices = [u"20ms", u"10ms", u"5ms", u"2.5ms"]
        self.m_choice_PWR_DOWN = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           m_choice_PWR_DOWNChoices, 0)
        self.m_choice_PWR_DOWN.SetSelection(0)
        self.m_choice_PWR_DOWN.SetMinSize(wx.Size(55, -1))

        gSizer_EMMC.Add(self.m_choice_PWR_DOWN, 0, wx.ALL, 5)

        self.m_staticText_1V8 = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"1V8_ENABLE:                      ",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_1V8.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_1V8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_1V8Choices = [u"not set vselect pin", u"set vselect pin high"]
        self.m_choice_1V8 = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      m_choice_1V8Choices, 0)
        self.m_choice_1V8.SetSelection(0)
        self.m_choice_1V8.SetMinSize(wx.Size(150, -1))

        gSizer_EMMC.Add(self.m_choice_1V8, 0, wx.ALL, 5)

        self.m_staticText_TIMING = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY, u"TIMING_INTERFACE:",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_TIMING.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_TIMING, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_TIMINGChoices = [u"Normal",u"HS"]
        self.m_choice_TIMING = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          m_choice_TIMINGChoices, 0)
        self.m_choice_TIMING.SetSelection(0)
        self.m_choice_TIMING.SetMinSize(wx.Size(-1, -1))

        gSizer_EMMC.Add(self.m_choice_TIMING, 0, wx.ALL, 5)

        self.m_staticText_PWR_CYCLE = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY,
                                                     u"PWR_CYCLE_ENABLE:",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_PWR_CYCLE.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_PWR_CYCLE, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_CYCLEChoices = [u"disable", u"enable"]
        self.m_choice_PWR_CYCLE = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             m_choice_PWR_CYCLEChoices, 0)
        self.m_choice_PWR_CYCLE.SetSelection(0)
        self.m_choice_PWR_CYCLE.SetMinSize(wx.Size(100, -1))

        gSizer_EMMC.Add(self.m_choice_PWR_CYCLE, 0, wx.ALL, 5)

        self.m_staticText_PWR_POLARITY = wx.StaticText(self.m_panel_EMMC, wx.ID_ANY,u"PWR_POLARITY:",
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_PWR_POLARITY.Wrap(-1)

        gSizer_EMMC.Add(self.m_staticText_PWR_POLARITY, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PWR_POLARITYChoices = [u"Power down when uSDHC.RST set low", u"Power down when uSDHC.RST set high"]
        self.m_choice_PWR_POLARITY = wx.Choice(self.m_panel_EMMC, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                                m_choice_PWR_POLARITYChoices, 0)
        self.m_choice_PWR_POLARITY.SetSelection(0)
        gSizer_EMMC.Add(self.m_choice_PWR_POLARITY, 0, wx.ALL, 5)

        self.m_panel_EMMC.SetSizer(gSizer_EMMC)
        self.m_panel_EMMC.Layout()
        gSizer_EMMC.Fit(self.m_panel_EMMC)
        self.m_notebook_EMMC.AddPage(self.m_panel_EMMC, u"EMMC Option", False)

        wSizer_EMMC.Add(self.m_notebook_EMMC, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText_EMMC = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.Size(300, -1), 0)
        self.m_staticText_EMMC.Wrap(-1)

        wSizer_EMMC.Add(self.m_staticText_EMMC, 0, wx.ALL, 5)

        m_sdbSizer_EMMC = wx.StdDialogButtonSizer()
        self.m_sdbSizer_EMMCOK = wx.Button(self, wx.ID_OK)
        m_sdbSizer_EMMC.AddButton(self.m_sdbSizer_EMMCOK)
        self.m_sdbSizer_EMMCCancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer_EMMC.AddButton(self.m_sdbSizer_EMMCCancel)
        m_sdbSizer_EMMC.Realize();

        wSizer_EMMC.Add(m_sdbSizer_EMMC, 1, wx.EXPAND, 5)

        self.SetSizer(wSizer_EMMC)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_sdbSizer_EMMCCancel.Bind(wx.EVT_BUTTON, self.cancel_of_EMMC)
        self.m_sdbSizer_EMMCOK.Bind(wx.EVT_BUTTON, self.apply_of_EMMC)

    def __del__(self):
        pass
        # Virtual event handlers, overide them in your derived class

    def cancel_of_EMMC(self, event):
        event.Skip()

    def apply_of_EMMC(self, event):
        event.Skip()

    def OnClose_EMMC(self, event):
        event.Skip()