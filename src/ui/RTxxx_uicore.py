#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import RTxxx_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from main import RT10yy_main

class secBootRTxxxUi(RT10yy_main.secBootRT10yyMain):

    def __init__(self, parent):
        RT10yy_main.secBootRT10yyMain.__init__(self, parent)
        if self.mcuSeries == uidef.kMcuSeries_iMXRTxxx:
            self.RTxxx_initUi()

    def RTxxx_initUi( self ):
        self._RTxxx_initTargetSetupValue()
        self.RTxxx_setTargetSetupValue()

        self.secureBootType = None
        self._RTxxx_initSecureBootSeqValue()
        self._RTxxx_initSecureBootSeqColor()

    def _RTxxx_initTargetSetupValue( self ):
        self.m_choice_bootDevice.Clear()
        self.m_choice_bootDevice.SetItems(RTxxx_uidef.kBootDevice_Latest)
        totalSel = self.m_choice_bootDevice.GetCount()
        if self.toolCommDict['bootDevice'] < totalSel:
            self.m_choice_bootDevice.SetSelection(self.toolCommDict['bootDevice'])
        else:
            self.m_choice_bootDevice.SetSelection(0)

    def _RTxxx_refreshBootDeviceList( self ):
        if self.tgt.availableBootDevices != None:
            self.m_choice_bootDevice.Clear()
            self.m_choice_bootDevice.SetItems(self.tgt.availableBootDevices)
            retSel = self.m_choice_bootDevice.FindString(self.bootDevice)
            if retSel != wx.NOT_FOUND:
                self.m_choice_bootDevice.SetSelection(retSel)
            else:
                self.m_choice_bootDevice.SetSelection(0)

    def RTxxx_setTargetSetupValue( self ):
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.RTxxx_createMcuTarget()
        self.refreshBootDeviceList()
        self.bootDevice = self.m_choice_bootDevice.GetString(self.m_choice_bootDevice.GetSelection())
        self.toolCommDict['bootDevice'] = self.m_choice_bootDevice.GetSelection()

    def _RTxxx_initSecureBootSeqValue( self ):
        self.m_choice_secureBootType.Clear()
        self.m_choice_secureBootType.SetItems(RTxxx_uidef.kSecureBootType_Latest)
        totalSel = self.m_choice_secureBootType.GetCount()
        if self.toolCommDict['secBootType'] < totalSel:
            self.m_choice_secureBootType.SetSelection(self.toolCommDict['secBootType'])
        else:
            self.m_choice_secureBootType.SetSelection(0)

    def _RTxxx_initSecureBootSeqColor ( self ):
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.RTxxx_setSecureBootSeqColor()

    def RTxxx_setSecureBootButtonColor( self, needToPlaySound=True ):
        activeColor = None
        optionalColor = None
        setEnable = None
        if self.isToolRunAsEntryMode:
            activeColor = uidef.kBootSeqColor_Invalid
            optionalColor = uidef.kBootSeqColor_Invalid
        else:
            activeColor = uidef.kBootSeqColor_Active
            optionalColor = uidef.kBootSeqColor_Optional
        setEnable = not self.isToolRunAsEntryMode
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        if self.secureBootType == RTxxx_uidef.kSecureBootType_PlainUnsigned or \
           self.secureBootType == RTxxx_uidef.kSecureBootType_PlainCrc:
            self.m_button_genImage.Enable( setEnable )
            self.m_button_genImage.SetBackgroundColour( activeColor )
            self.m_button_flashImage.Enable( setEnable )
            self.m_button_flashImage.SetBackgroundColour( activeColor )
        else:
            pass
        self.m_button_allInOneAction.Enable( True )
        self.m_button_allInOneAction.SetBackgroundColour( uidef.kBootSeqColor_Active )
        self.Refresh()
        if needToPlaySound:
            self.soundEffectFilenameForTask = uidef.kSoundEffectFilename_Restart

    def _RTxxx_getImgName( self ):
        memType = ''
        memType = 'nor_'
        return memType

    def RTxxx_setSecureBootSeqColor( self , needToPlaySound=True ):
        self.hasDynamicLableBeenInit = True
        self.secureBootType = self.m_choice_secureBootType.GetString(self.m_choice_secureBootType.GetSelection())
        self.refreshSecureBootTypeList()
        self.toolCommDict['secBootType'] = self.m_choice_secureBootType.GetSelection()
        self.resetSecureBootSeqColor()
        if self.secureBootType == RTxxx_uidef.kSecureBootType_PlainUnsigned:
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_u'][self.languageIndex])
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType = self._RTxxx_getImgName()
            imgPath = "../img/RTxxx/" + strMemType + "image_unsigned.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_u'][self.languageIndex])
        elif self.secureBootType == RTxxx_uidef.kSecureBootType_PlainCrc:
            self.m_panel_genImage1_browseApp.Enable( True )
            self.m_panel_genImage1_browseApp.SetBackgroundColour( uidef.kBootSeqColor_Active )
            self.m_button_genImage.SetLabel(uilang.kMainLanguageContentDict['button_genImage_c'][self.languageIndex])
            self.m_panel_flashImage1_showImage.Enable( True )
            self.m_panel_flashImage1_showImage.SetBackgroundColour( uidef.kBootSeqColor_Active )
            strMemType = self._RTxxx_getImgName()
            imgPath = "../img/RTxxx/" + strMemType + "image_crc.png"
            self.showImageLayout(imgPath.encode('utf-8'))
            self.m_button_flashImage.SetLabel(uilang.kMainLanguageContentDict['button_flashImage_c'][self.languageIndex])
        else:
            pass
        self.RTxxx_setSecureBootButtonColor(needToPlaySound)
        self.Refresh()
