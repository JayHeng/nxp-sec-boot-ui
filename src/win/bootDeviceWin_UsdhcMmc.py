# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class bootDeviceWin_UsdhcMmc
###########################################################################

class bootDeviceWin_UsdhcMmc ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 664,426 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_notebook_mmcOpt0 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_mmcrOpt0 = wx.Panel( self.m_notebook_mmcOpt0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer_mmcOpt0 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText_busWidth = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Bus Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_busWidth.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_busWidth, 0, wx.ALL, 5 )

        m_choice_busWidthChoices = [ u"1bit", u"4bit", u"8bit", u"4bit DDR", u"8bit DDR" ]
        self.m_choice_busWidth = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_busWidthChoices, 0 )
        self.m_choice_busWidth.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_busWidth, 0, wx.ALL, 5 )

        self.m_staticText_timingInterface = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Timing Interface:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_timingInterface.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_timingInterface, 0, wx.ALL, 5 )

        m_choice_timingInterfaceChoices = [ u"Non-HighSpeed", u"HighSpeed", u"HighSpeed 200", u"HighSpeed 400", u"HighSpeed 26MHz", u"HighSpeed 52MHz", u"HighSpeed DDR52" ]
        self.m_choice_timingInterface = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_timingInterfaceChoices, 0 )
        self.m_choice_timingInterface.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_timingInterface, 0, wx.ALL, 5 )

        self.m_staticText_partitionAccess = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Partition Access:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_partitionAccess.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_partitionAccess, 0, wx.ALL, 5 )

        m_choice_partitionAccessChoices = [ u"User Area Normal", u"Read/Write Boot1", u"Read/Write Boot2", u"Replay Protected Mem Block", u"General Purpose1", u"General Purpose2", u"General Purpose3", u"General Purpose4" ]
        self.m_choice_partitionAccess = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_partitionAccessChoices, 0 )
        self.m_choice_partitionAccess.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_partitionAccess, 0, wx.ALL, 5 )

        self.m_staticText_enableBootConfig = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Enable Boot Config:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_enableBootConfig.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_enableBootConfig, 0, wx.ALL, 5 )

        m_choice_enableBootConfigChoices = [ u"No", u"Yes" ]
        self.m_choice_enableBootConfig = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enableBootConfigChoices, 0 )
        self.m_choice_enableBootConfig.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_enableBootConfig, 0, wx.ALL, 5 )

        self.m_staticText_bootBusWidth = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Boot Bus Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_bootBusWidth.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_bootBusWidth, 0, wx.ALL, 5 )

        m_choice_bootBusWidthChoices = [ u"1bit-SDR, 4bit-DDR", u"4bit-SDR, 4bit-DDR", u"8bit-SDR, 8bit-DDR" ]
        self.m_choice_bootBusWidth = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_bootBusWidthChoices, 0 )
        self.m_choice_bootBusWidth.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_bootBusWidth, 0, wx.ALL, 5 )

        self.m_staticText_bootMode = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Boot Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_bootMode.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_bootMode, 0, wx.ALL, 5 )

        m_choice_bootModeChoices = [ u"SDR Non-HighSpeed", u"SDR HighSpeed", u"DDR" ]
        self.m_choice_bootMode = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_bootModeChoices, 0 )
        self.m_choice_bootMode.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_bootMode, 0, wx.ALL, 5 )

        self.m_staticText_enableBootPartition = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Enable Boot Partition:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_enableBootPartition.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_enableBootPartition, 0, wx.ALL, 5 )

        m_choice_enableBootPartitionChoices = [ u"No", u"Boot1", u"Boot2", u"User Area" ]
        self.m_choice_enableBootPartition = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enableBootPartitionChoices, 0 )
        self.m_choice_enableBootPartition.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_enableBootPartition, 0, wx.ALL, 5 )

        self.m_staticText_enableBootAck = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Enable Boot Ack:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_enableBootAck.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_enableBootAck, 0, wx.ALL, 5 )

        m_choice_enableBootAckChoices = [ u"No", u"Yes" ]
        self.m_choice_enableBootAck = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enableBootAckChoices, 0 )
        self.m_choice_enableBootAck.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_enableBootAck, 0, wx.ALL, 5 )

        self.m_staticText_resetBootBusConditions = wx.StaticText( self.m_panel_mmcrOpt0, wx.ID_ANY, u"Reset Boot Bus Conditions:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_resetBootBusConditions.Wrap( -1 )

        gSizer_mmcOpt0.Add( self.m_staticText_resetBootBusConditions, 0, wx.ALL, 5 )

        m_choice_resetBootBusConditionsChoices = [ u"Reset to 1bit-SDR", u"Retain Boot Bus Width" ]
        self.m_choice_resetBootBusConditions = wx.Choice( self.m_panel_mmcrOpt0, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_resetBootBusConditionsChoices, 0 )
        self.m_choice_resetBootBusConditions.SetSelection( 0 )
        gSizer_mmcOpt0.Add( self.m_choice_resetBootBusConditions, 0, wx.ALL, 5 )


        self.m_panel_mmcrOpt0.SetSizer( gSizer_mmcOpt0 )
        self.m_panel_mmcrOpt0.Layout()
        gSizer_mmcOpt0.Fit( self.m_panel_mmcrOpt0 )
        self.m_notebook_mmcOpt0.AddPage( self.m_panel_mmcrOpt0, u"MMC Option0", False )

        wSizer_win.Add( self.m_notebook_mmcOpt0, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_notebook_mmcOpt1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_mmcOpt1 = wx.Panel( self.m_notebook_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer_mmcOpt1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText_enable1V8 = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Enable 1.8V:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        self.m_staticText_enable1V8.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_enable1V8, 0, wx.ALL, 5 )

        m_choice_enable1V8Choices = [ u"No", u"Yes" ]
        self.m_choice_enable1V8 = wx.Choice( self.m_panel_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enable1V8Choices, 0 )
        self.m_choice_enable1V8.SetSelection( 0 )
        gSizer_mmcOpt1.Add( self.m_choice_enable1V8, 0, wx.ALL, 5 )

        self.m_staticText_enablePowerCycle = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Enable Power Cycle:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_enablePowerCycle.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_enablePowerCycle, 0, wx.ALL, 5 )

        m_choice_enablePowerCycleChoices = [ u"No", u"Yes" ]
        self.m_choice_enablePowerCycle = wx.Choice( self.m_panel_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_enablePowerCycleChoices, 0 )
        self.m_choice_enablePowerCycle.SetSelection( 0 )
        gSizer_mmcOpt1.Add( self.m_choice_enablePowerCycle, 0, wx.ALL, 5 )

        self.m_staticText_powerPolarity = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Power Polarity:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_powerPolarity.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_powerPolarity, 0, wx.ALL, 5 )

        m_choice_powerPolarityChoices = [ u"RST Low-Disable", u"RST High-Disable" ]
        self.m_choice_powerPolarity = wx.Choice( self.m_panel_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_powerPolarityChoices, 0 )
        self.m_choice_powerPolarity.SetSelection( 0 )
        gSizer_mmcOpt1.Add( self.m_choice_powerPolarity, 0, wx.ALL, 5 )

        self.m_staticText_powerUpTime = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Power Up Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_powerUpTime.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_powerUpTime, 0, wx.ALL, 5 )

        m_choice_powerUpTimeChoices = [ u"5ms", u"2.5ms" ]
        self.m_choice_powerUpTime = wx.Choice( self.m_panel_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_powerUpTimeChoices, 0 )
        self.m_choice_powerUpTime.SetSelection( 0 )
        gSizer_mmcOpt1.Add( self.m_choice_powerUpTime, 0, wx.ALL, 5 )

        self.m_staticText_powerDownTime = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Power Down Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_powerDownTime.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_powerDownTime, 0, wx.ALL, 5 )

        m_choice_powerDownTimeChoices = [ u"20ms", u"10ms", u"5ms", u"2.5ms" ]
        self.m_choice_powerDownTime = wx.Choice( self.m_panel_mmcOpt1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), m_choice_powerDownTimeChoices, 0 )
        self.m_choice_powerDownTime.SetSelection( 0 )
        gSizer_mmcOpt1.Add( self.m_choice_powerDownTime, 0, wx.ALL, 5 )

        self.m_staticText_enablePermConfig = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Enable Perm Config:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        self.m_staticText_enablePermConfig.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_enablePermConfig, 0, wx.ALL, 5 )

        self.m_textCtrl_enablePermConfig = wx.TextCtrl( self.m_panel_mmcOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        gSizer_mmcOpt1.Add( self.m_textCtrl_enablePermConfig, 0, wx.ALL, 5 )

        self.m_staticText_permBootConfigProt = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Perm Boot Config Prot:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        self.m_staticText_permBootConfigProt.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_permBootConfigProt, 0, wx.ALL, 5 )

        self.m_textCtrl_permBootConfigProt = wx.TextCtrl( self.m_panel_mmcOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        gSizer_mmcOpt1.Add( self.m_textCtrl_permBootConfigProt, 0, wx.ALL, 5 )

        self.m_staticText_driverStrength = wx.StaticText( self.m_panel_mmcOpt1, wx.ID_ANY, u"Driver Strength:", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        self.m_staticText_driverStrength.Wrap( -1 )

        gSizer_mmcOpt1.Add( self.m_staticText_driverStrength, 0, wx.ALL, 5 )

        self.m_textCtrl_driverStrength = wx.TextCtrl( self.m_panel_mmcOpt1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        gSizer_mmcOpt1.Add( self.m_textCtrl_driverStrength, 0, wx.ALL, 5 )


        self.m_panel_mmcOpt1.SetSizer( gSizer_mmcOpt1 )
        self.m_panel_mmcOpt1.Layout()
        gSizer_mmcOpt1.Fit( self.m_panel_mmcOpt1 )
        self.m_notebook_mmcOpt1.AddPage( self.m_panel_mmcOpt1, u"MMC Option1", False )

        wSizer_win.Add( self.m_notebook_mmcOpt1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
        self.m_staticText_winNull0.Wrap( -1 )

        wSizer_win.Add( self.m_staticText_winNull0, 0, wx.ALL, 5 )

        self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        wSizer_win.Add( self.m_button_ok, 0, wx.ALL, 5 )

        self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        wSizer_win.Add( self.m_button_cancel, 0, wx.ALL, 5 )


        self.SetSizer( wSizer_win )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.callbackClose )
        self.m_choice_enableBootConfig.Bind( wx.EVT_CHOICE, self.callbackEnableBootConfig )
        self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
        self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def callbackClose( self, event ):
        event.Skip()

    def callbackEnableBootConfig( self, event ):
        event.Skip()

    def callbackOk( self, event ):
        event.Skip()

    def callbackCancel( self, event ):
        event.Skip()


