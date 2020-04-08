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
## Class bootDeviceWin_RecoverySpiNor
###########################################################################

class bootDeviceWin_RecoverySpiNor ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 552,256 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_notebook_memOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_memOpt = wx.Panel( self.m_notebook_memOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer_memOpt = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText_deviceType = wx.StaticText( self.m_panel_memOpt, wx.ID_ANY, u"Device Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_deviceType.Wrap( -1 )

        gSizer_memOpt.Add( self.m_staticText_deviceType, 0, wx.ALL, 5 )

        m_choice_deviceTypeChoices = [ u"1bit NOR Flash", u"EEPROM" ]
        self.m_choice_deviceType = wx.Choice( self.m_panel_memOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_deviceTypeChoices, 0 )
        self.m_choice_deviceType.SetSelection( 0 )
        gSizer_memOpt.Add( self.m_choice_deviceType, 0, wx.ALL, 5 )

        self.m_staticText_pageSize = wx.StaticText( self.m_panel_memOpt, wx.ID_ANY, u"Page Size (Bytes):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_pageSize.Wrap( -1 )

        gSizer_memOpt.Add( self.m_staticText_pageSize, 0, wx.ALL, 5 )

        m_choice_pageSizeChoices = [ u"32", u"64", u"128", u"256", u"512", u"1024" ]
        self.m_choice_pageSize = wx.Choice( self.m_panel_memOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_pageSizeChoices, 0 )
        self.m_choice_pageSize.SetSelection( 3 )
        gSizer_memOpt.Add( self.m_choice_pageSize, 0, wx.ALL, 5 )

        self.m_staticText_sectorSize = wx.StaticText( self.m_panel_memOpt, wx.ID_ANY, u"Sector Size (KBytes):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_sectorSize.Wrap( -1 )

        gSizer_memOpt.Add( self.m_staticText_sectorSize, 0, wx.ALL, 5 )

        m_choice_sectorSizeChoices = [ u"4", u"8", u"32", u"64", u"128", u"256" ]
        self.m_choice_sectorSize = wx.Choice( self.m_panel_memOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_sectorSizeChoices, 0 )
        self.m_choice_sectorSize.SetSelection( 0 )
        gSizer_memOpt.Add( self.m_choice_sectorSize, 0, wx.ALL, 5 )

        self.m_staticText_totalSize = wx.StaticText( self.m_panel_memOpt, wx.ID_ANY, u"Total Size (KBytes):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_totalSize.Wrap( -1 )

        gSizer_memOpt.Add( self.m_staticText_totalSize, 0, wx.ALL, 5 )

        m_choice_totalSizeChoices = [ u"32", u"64", u"128", u"256", u"512", u"1024", u"2048", u"4096", u"8192", u"16384", u"32768", u"65536", u"131072", u"262144", u"524288", u"1048576" ]
        self.m_choice_totalSize = wx.Choice( self.m_panel_memOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_totalSizeChoices, 0 )
        self.m_choice_totalSize.SetSelection( 4 )
        gSizer_memOpt.Add( self.m_choice_totalSize, 0, wx.ALL, 5 )


        self.m_panel_memOpt.SetSizer( gSizer_memOpt )
        self.m_panel_memOpt.Layout()
        gSizer_memOpt.Fit( self.m_panel_memOpt )
        self.m_notebook_memOpt.AddPage( self.m_panel_memOpt, u"Memory Option", False )

        wSizer_win.Add( self.m_notebook_memOpt, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_notebook_spiOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_spiOpt = wx.Panel( self.m_notebook_spiOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer_spiOpt = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText_spiIndex = wx.StaticText( self.m_panel_spiOpt, wx.ID_ANY, u"Spi Index:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_spiIndex.Wrap( -1 )

        gSizer_spiOpt.Add( self.m_staticText_spiIndex, 0, wx.ALL, 5 )

        m_choice_spiIndexChoices = [ u"1", u"2", u"3", u"4" ]
        self.m_choice_spiIndex = wx.Choice( self.m_panel_spiOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_spiIndexChoices, 0 )
        self.m_choice_spiIndex.SetSelection( 0 )
        gSizer_spiOpt.Add( self.m_choice_spiIndex, 0, wx.ALL, 5 )

        self.m_staticText_spiPcs = wx.StaticText( self.m_panel_spiOpt, wx.ID_ANY, u"Spi Pcs:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_spiPcs.Wrap( -1 )

        gSizer_spiOpt.Add( self.m_staticText_spiPcs, 0, wx.ALL, 5 )

        m_choice_spiPcsChoices = [ u"0" ]
        self.m_choice_spiPcs = wx.Choice( self.m_panel_spiOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_spiPcsChoices, 0 )
        self.m_choice_spiPcs.SetSelection( 0 )
        gSizer_spiOpt.Add( self.m_choice_spiPcs, 0, wx.ALL, 5 )

        self.m_staticText_spiSpeed = wx.StaticText( self.m_panel_spiOpt, wx.ID_ANY, u"Spi Speed:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText_spiSpeed.Wrap( -1 )

        gSizer_spiOpt.Add( self.m_staticText_spiSpeed, 0, wx.ALL, 5 )

        m_choice_spiSpeedChoices = [ u"20MHz", u"10MHz", u"5MHz", u"2MHz" ]
        self.m_choice_spiSpeed = wx.Choice( self.m_panel_spiOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice_spiSpeedChoices, 0 )
        self.m_choice_spiSpeed.SetSelection( 0 )
        gSizer_spiOpt.Add( self.m_choice_spiSpeed, 0, wx.ALL, 5 )

        self.m_staticText_spiOptNull0 = wx.StaticText( self.m_panel_spiOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_spiOptNull0.Wrap( -1 )

        gSizer_spiOpt.Add( self.m_staticText_spiOptNull0, 0, wx.ALL, 5 )

        self.m_staticText_spiOptNull1 = wx.StaticText( self.m_panel_spiOpt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_spiOptNull1.Wrap( -1 )

        gSizer_spiOpt.Add( self.m_staticText_spiOptNull1, 0, wx.ALL, 5 )


        self.m_panel_spiOpt.SetSizer( gSizer_spiOpt )
        self.m_panel_spiOpt.Layout()
        gSizer_spiOpt.Fit( self.m_panel_spiOpt )
        self.m_notebook_spiOpt.AddPage( self.m_panel_spiOpt, u"Spi Option", False )

        wSizer_win.Add( self.m_notebook_spiOpt, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 265,-1 ), 0 )
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


