
import wx
import wx.xrc

###########################################################################
## Class MyFrame_SEMC_NOR
###########################################################################

###########################################################################
## Class MyFrame_SEMC_NOR
###########################################################################

class bootDeviceWin_SemcNor(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(720, 465), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Bind(wx.EVT_CLOSE, self.OnClose_SEMC_NOR)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        wSizer_SEMC_NOR = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_notebook_SEMCNOR_Option = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_SEMCNOR_Option = wx.Panel(self.m_notebook_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer_SEMCNOR_Option = wx.GridSizer(0, 2, 0, 0)

        self.staticText_PCS_Port = wx.StaticText(self.m_panel_SEMCNOR_Option, wx.ID_ANY, u"PCS Port:",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_PCS_Port.Wrap(-1)

        gSizer_SEMCNOR_Option.Add(self.staticText_PCS_Port, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_PCS_PortChoices = [u"CSX0", u"CSX1", u"CSX2", u"CSX3", u"A8"]
        self.m_choice_PCS_Port = wx.Choice(self.m_panel_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition, wx.Size(125, 25),
                                           m_choice_PCS_PortChoices, 0)
        self.m_choice_PCS_Port.SetSelection(0)
        self.m_choice_PCS_Port.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        gSizer_SEMCNOR_Option.Add(self.m_choice_PCS_Port, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.staticText_ADV_Polarity = wx.StaticText(self.m_panel_SEMCNOR_Option, wx.ID_ANY, u"ADV Port Polarity:",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_ADV_Polarity.Wrap(-1)

        gSizer_SEMCNOR_Option.Add(self.staticText_ADV_Polarity, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_ADV_PolarityChoices = [u"Low active", u"High active"]
        self.m_choice_ADV_Polarity = wx.Choice(self.m_panel_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition,
                                               wx.Size(125, 25), m_choice_ADV_PolarityChoices, 0)
        self.m_choice_ADV_Polarity.SetSelection(0)
        gSizer_SEMCNOR_Option.Add(self.m_choice_ADV_Polarity, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.staticText_DataPort_Size = wx.StaticText(self.m_panel_SEMCNOR_Option, wx.ID_ANY, u"Data Port Size:",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_DataPort_Size.Wrap(-1)

        gSizer_SEMCNOR_Option.Add(self.staticText_DataPort_Size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_DataPort_SizeChoices = [u"8bits", u"8bits", u"16bits", u"24bits"]
        self.m_choice_DataPort_Size = wx.Choice(self.m_panel_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition,
                                                wx.Size(100, 25), m_choice_DataPort_SizeChoices, 0)
        self.m_choice_DataPort_Size.SetSelection(0)
        gSizer_SEMCNOR_Option.Add(self.m_choice_DataPort_Size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.staticText_Timing_Mode = wx.StaticText(self.m_panel_SEMCNOR_Option, wx.ID_ANY, u"AC Timing Mode:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_Timing_Mode.Wrap(-1)

        gSizer_SEMCNOR_Option.Add(self.staticText_Timing_Mode, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Timing_ModeChoices = [u"Safe mode", u"Fast mode", u"User defined(Field 0x04-0x19)"]
        self.m_choice_Timing_Mode = wx.Choice(self.m_panel_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition,
                                              wx.Size(125, 25), m_choice_Timing_ModeChoices, 0)
        self.m_choice_Timing_Mode.SetSelection(0)
        gSizer_SEMCNOR_Option.Add(self.m_choice_Timing_Mode, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.staticText_Command_Set = wx.StaticText(self.m_panel_SEMCNOR_Option, wx.ID_ANY, u"Command Set:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_Command_Set.Wrap(-1)

        gSizer_SEMCNOR_Option.Add(self.staticText_Command_Set, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_Command_SetChoices = [u"EPSCD-As Micron MT28EW", u"SFMCD-As Micron MT28GU"]
        self.m_choice_Command_Set = wx.Choice(self.m_panel_SEMCNOR_Option, wx.ID_ANY, wx.DefaultPosition,
                                              wx.Size(160, 25), m_choice_Command_SetChoices, 0)
        self.m_choice_Command_Set.SetSelection(0)
        gSizer_SEMCNOR_Option.Add(self.m_choice_Command_Set, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel_SEMCNOR_Option.SetSizer(gSizer_SEMCNOR_Option)
        self.m_panel_SEMCNOR_Option.Layout()
        gSizer_SEMCNOR_Option.Fit(self.m_panel_SEMCNOR_Option)
        self.m_notebook_SEMCNOR_Option.AddPage(self.m_panel_SEMCNOR_Option, u"SEMC NOR Option", False)

        wSizer_SEMC_NOR.Add(self.m_notebook_SEMCNOR_Option, 1, wx.EXPAND | wx.ALL, 5)

        self.m_notebook_Setting_Nxp = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_Setting_Nxp = wx.Panel(self.m_notebook_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        gSizer_Setting_Nxp = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText_tCES = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tCES:      ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tCES.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tCES, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tCESChoices = [u"CE setup time in ns"]
        self.m_choice_tCES = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tCESChoices, 0)
        self.m_choice_tCES.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tCES, 0, wx.ALL, 5)

        self.m_staticText_tCEH = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tCEH:      ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tCEH.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tCEH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tCEHChoices = [u"CE hold time in ns"]
        self.m_choice_tCEH = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tCEHChoices, 0)
        self.m_choice_tCEH.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tCEH, 0, wx.ALL, 5)

        self.m_staticText_tCEITV = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tCEITV:  ", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_staticText_tCEITV.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tCEITV, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tCEITVChoices = [u"CE# interval time in ns"]
        self.m_choice_tCEITV = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                         m_choice_tCEITVChoices, 0)
        self.m_choice_tCEITV.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tCEITV, 0, wx.ALL, 5)

        self.m_staticText_tAS = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tAS:          ",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_tAS.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tAS, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tASChoices = [u"Address setup time in ns"]
        self.m_choice_tAS = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                      m_choice_tASChoices, 0)
        self.m_choice_tAS.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tAS, 0, wx.ALL, 5)

        self.m_staticText_tAH = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tAH:       ", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText_tAH.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tAH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tAHChoices = [u"Address hold time in ns"]
        self.m_choice_tAH = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                      m_choice_tAHChoices, 0)
        self.m_choice_tAH.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tAH, 0, wx.ALL, 5)

        self.m_staticText_tTA = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tTA:         ", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText_tTA.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tTA, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tTAChoices = [u"Turnaround time in ns"]
        self.m_choice_tTA = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                      m_choice_tTAChoices, 0)
        self.m_choice_tTA.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tTA, 0, wx.ALL, 5)

        self.m_staticText_tWEL = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tWEL:     ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tWEL.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tWEL, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tWELChoices = [u"WE LOW time in ns"]
        self.m_choice_tWEL = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tWELChoices, 0)
        self.m_choice_tWEL.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tWEL, 0, wx.ALL, 5)

        self.m_staticText_tWEH = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tWEH:     ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tWEH.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tWEH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tWEHChoices = [u"WE HIGH time in ns"]
        self.m_choice_tWEH = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tWEHChoices, 0)
        self.m_choice_tWEH.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tWEH, 0, wx.ALL, 5)

        self.m_staticText_tREL = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tREL:      ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tREL.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tREL, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tRELChoices = [u"RE LOW time in ns"]
        self.m_choice_tREL = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tRELChoices, 0)
        self.m_choice_tREL.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tREL, 0, wx.ALL, 5)

        self.m_staticText_tREH = wx.StaticText(self.m_panel_Setting_Nxp, wx.ID_ANY, u"tREH:       ", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_tREH.Wrap(-1)

        gSizer_Setting_Nxp.Add(self.m_staticText_tREH, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tREHChoices = [u"RE HIGH time in ns"]
        self.m_choice_tREH = wx.Choice(self.m_panel_Setting_Nxp, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 25),
                                       m_choice_tREHChoices, 0)
        self.m_choice_tREH.SetSelection(0)
        gSizer_Setting_Nxp.Add(self.m_choice_tREH, 0, wx.ALL, 5)

        self.m_panel_Setting_Nxp.SetSizer(gSizer_Setting_Nxp)
        self.m_panel_Setting_Nxp.Layout()
        gSizer_Setting_Nxp.Fit(self.m_panel_Setting_Nxp)
        self.m_notebook_Setting_Nxp.AddPage(self.m_panel_Setting_Nxp, u"Setting By Nxp", False)

        wSizer_SEMC_NOR.Add(self.m_notebook_Setting_Nxp, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText_SEMC_NOR = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size(490, -1), 0)
        self.m_staticText_SEMC_NOR.Wrap(-1)

        wSizer_SEMC_NOR.Add(self.m_staticText_SEMC_NOR, 0, wx.ALL, 5)

        m_sdbSizer_SEMC_NOR = wx.StdDialogButtonSizer()
        self.m_sdbSizer_SEMC_NOROK = wx.Button(self, wx.ID_OK)
        m_sdbSizer_SEMC_NOR.AddButton(self.m_sdbSizer_SEMC_NOROK)
        self.m_sdbSizer_SEMC_NORCancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer_SEMC_NOR.AddButton(self.m_sdbSizer_SEMC_NORCancel)
        m_sdbSizer_SEMC_NOR.Realize();

        wSizer_SEMC_NOR.Add(m_sdbSizer_SEMC_NOR, 1, wx.EXPAND, 5)

        self.SetSizer(wSizer_SEMC_NOR)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_sdbSizer_SEMC_NORCancel.Bind(wx.EVT_BUTTON, self.cancel_of_SEMC_NOR)
        self.m_sdbSizer_SEMC_NOROK.Bind(wx.EVT_BUTTON, self.apply_of_SEMC_NOR)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancel_of_SEMC_NOR(self, event):
        event.Skip()

    def apply_of_SEMC_NOR(self, event):
        event.Skip()

    def OnClose_SEMC_NOR(self, event):
        event.Skip()