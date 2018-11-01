import wx
import sys, os
from ui import uicore
from ui import nxpSecBoot

class secBootMain(uicore.secBootUi):

    def __init__(self, parent):
        uicore.secBootUi.__init__(self, parent)

    def callbackSwitchSecureBootType( self, event ):
        self.setSecureBootSeqColor()

    def callbackSwitchKeyStorageRegion( self, event ):
        self.setKeyStorageRegionColor()
        
    def callbackRUN_CST_Tool( self, event ):
        self.RUN_CST_Tool()
        
    def callbackBoot_Device_Configuration( self, event ):      
        self.Boot_Device_Configuration()

if __name__ == '__main__':
    app = wx.App()

    main_win = secBootMain(None)
    main_win.SetTitle(u"nxpSecBoot v0.1.0")
    main_win.Show()

    app.MainLoop()
