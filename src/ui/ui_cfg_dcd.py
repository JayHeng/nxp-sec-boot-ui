#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import shutil
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_DCD
from gen import RTyyyy_gendef
from run import RTyyyy_rundef
from utils import sound

class secBootUiCfgDcd(bootDeviceWin_DCD.bootDeviceWin_DCD):

    def __init__(self, parent):
        bootDeviceWin_DCD.bootDeviceWin_DCD.__init__(self, parent)
        self._setLanguage()
        dcdCtrlDict, dcdSettingsDict = uivar.getBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_Dcd)
        self.dcdCtrlDict = dcdCtrlDict.copy()
        self.dcdSettingsDict = dcdSettingsDict.copy()
        self.destBinFilename = None
        self.destCfgFilename = None
        self.dcdModelFolder = None

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_dcdOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_dcdOpt'][langIndex])
        self.m_staticText_dcdSource.SetLabel(uilang.kSubLanguageContentDict['sText_dcdSource'][langIndex])
        self.m_staticText_dcdBinFile.SetLabel(uilang.kSubLanguageContentDict['sText_dcdBinFile'][langIndex])
        self.m_staticText_dcdCfgFile.SetLabel(uilang.kSubLanguageContentDict['sText_dcdCfgFile'][langIndex])
        self.m_staticText_dcdPurpose.SetLabel(uilang.kSubLanguageContentDict['sText_dcdPurpose'][langIndex])
        self.m_staticText_sdramBase.SetLabel(uilang.kSubLanguageContentDict['sText_sdramBase'][langIndex])
        self.m_notebook_dcdDesc.SetPageText(0, uilang.kSubLanguageContentDict['panel_dcdDesc'][langIndex])
        self.m_staticText_dcdModel.SetLabel(uilang.kSubLanguageContentDict['sText_dcdModel'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_dcd_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_dcd_cancel'][langIndex])

    def setNecessaryInfo( self, binFilename, cfgFilename, dcdModelFolder ):
        self.destBinFilename = binFilename
        self.destCfgFilename = cfgFilename
        self.dcdModelFolder = dcdModelFolder
        self._recoverLastSettings()

    def _recoverLastSettings ( self ):
        self.m_choice_dcdSource.SetSelection(self.m_choice_dcdSource.FindString(self.dcdSettingsDict['dcdSource']))
        self.m_filePicker_dcdBinFile.SetPath(self.dcdSettingsDict['userBinFile'])
        self.m_filePicker_dcdCfgFile.SetPath(self.dcdSettingsDict['userCfgFile'])
        self.m_choice_dcdPurpose.SetSelection(self.m_choice_dcdPurpose.FindString(self.dcdSettingsDict['dcdPurpose']))
        self.m_choice_dcdModel.SetSelection(self.m_choice_dcdModel.FindString(self.dcdSettingsDict['deviceModel']))
        self._getDcdSource()
        self._getDcdPurpose()
        if self.dcdSettingsDict['sdramBase'] != None:
            self.m_textCtrl_sdramBase.Clear()
            self.m_textCtrl_sdramBase.write(self.dcdSettingsDict['sdramBase'])
        self._getDeviceModel()
        if self.dcdSettingsDict['dcdDesc'] != None:
            self.m_textCtrl_dcdDesc.Clear()
            self.m_textCtrl_dcdDesc.write(self.dcdSettingsDict['dcdDesc'])

    def _getDcdSource( self ):
        txt = self.m_choice_dcdSource.GetString(self.m_choice_dcdSource.GetSelection())
        self.dcdSettingsDict['dcdSource'] = txt
        if txt == 'Disable DCD':
            self.dcdCtrlDict['isDcdEnabled'] = False
            self.m_filePicker_dcdBinFile.Enable( False )
            self.m_filePicker_dcdCfgFile.Enable( False )
            self.m_choice_dcdPurpose.Enable( False )
            self.m_textCtrl_sdramBase.Enable( False )
            self.m_panel_dcdDesc.Enable( False )
        elif txt == 'Use DCD bin file':
            self.dcdCtrlDict['isDcdEnabled'] = True
            self.m_filePicker_dcdBinFile.Enable( True )
            self.m_filePicker_dcdCfgFile.Enable( False )
            self.m_choice_dcdPurpose.Enable( True )
            self.m_panel_dcdDesc.Enable( False )
            self._getDcdPurpose()
            self._getDeviceModel()
        elif txt == 'Use DCD cfg file':
            self.dcdCtrlDict['isDcdEnabled'] = True
            self.m_filePicker_dcdBinFile.Enable( False )
            self.m_filePicker_dcdCfgFile.Enable( True )
            self.m_choice_dcdPurpose.Enable( True )
            self.m_panel_dcdDesc.Enable( False )
            self._getDcdPurpose()
            self._getDeviceModel()
        elif txt == 'Use DCD descriptor':
            self.dcdCtrlDict['isDcdEnabled'] = True
            self.m_filePicker_dcdBinFile.Enable( False )
            self.m_filePicker_dcdCfgFile.Enable( False )
            self.m_choice_dcdPurpose.Enable( True )
            self.m_panel_dcdDesc.Enable( True )
            self._getDcdPurpose()
            self._getDeviceModel()
        else:
            pass

    def popupMsgBox( self, msgStr ):
        messageText = (msgStr)
        wx.MessageBox(messageText, "Error", wx.OK | wx.ICON_INFORMATION)

    def _getDcdBinFile( self ):
        status = True
        if self.dcdSettingsDict['dcdSource'] == 'Use DCD bin file':
            dcdBinFile = self.m_filePicker_dcdBinFile.GetPath().encode('utf-8').encode("gbk")
            if os.path.isfile(dcdBinFile):
                shutil.copy(dcdBinFile, self.destBinFilename)
                self.dcdSettingsDict['userBinFile'] = dcdBinFile.decode("gbk")
                self.dcdCtrlDict['dcdFileType'] = RTyyyy_gendef.kUserDcdFileType_Bin
            else:
                status = False
                self.dcdSettingsDict['userBinFile'] = 'N/A'
                self.popupMsgBox('You should specify a dcd bin file')
        return status

    def _getDcdCfgFile( self ):
        status = True
        if self.dcdSettingsDict['dcdSource'] == 'Use DCD cfg file':
            dcdCfgFile = self.m_filePicker_dcdCfgFile.GetPath().encode('utf-8').encode("gbk")
            if os.path.isfile(dcdCfgFile):
                shutil.copy(dcdCfgFile, self.destCfgFilename)
                self.dcdSettingsDict['userCfgFile'] = dcdCfgFile.decode("gbk")
                self.dcdCtrlDict['dcdFileType'] = RTyyyy_gendef.kUserDcdFileType_Cfg
            else:
                status = False
                self.dcdSettingsDict['userCfgFile'] = 'N/A'
                self.popupMsgBox('You should specify a dcd cfg file')
        return status

    def _getDcdPurpose( self ):
        if self.dcdSettingsDict['dcdSource'] != 'Disable DCD':
            txt = self.m_choice_dcdPurpose.GetString(self.m_choice_dcdPurpose.GetSelection())
            if txt == 'Misc':
                self.m_textCtrl_sdramBase.Enable( False )
                self.dcdSettingsDict['sdramBase'] = None
            elif txt == 'SDRAM':
                self.m_textCtrl_sdramBase.Enable( True )
            else:
                pass
            self.dcdSettingsDict['dcdPurpose'] = txt

    def _getSdramBase( self ):
        status = True
        if self.dcdSettingsDict['dcdSource'] != 'Disable DCD' and \
           self.dcdSettingsDict['dcdPurpose'] == 'SDRAM':
            hexText = self.m_textCtrl_sdramBase.GetLineText(0)
            status = False
            val32 = None
            if len(hexText) > 2 and hexText[0:2] == '0x':
                try:
                    val32 = int(hexText[2:len(hexText)], 16)
                    if val32 >= RTyyyy_rundef.kBootDeviceMemBase_SemcSdram and val32 < RTyyyy_rundef.kBootDeviceMemBase_SemcSdram + RTyyyy_rundef.kBootDeviceMemMaxSize_SemcSdram:
                        status = True
                        self.dcdSettingsDict['sdramBase'] = hexText
                    else:
                        self.popupMsgBox('SDRAM base should be in the range of 0x%x - 0x%x' %(RTyyyy_rundef.kBootDeviceMemBase_SemcSdram, (RTyyyy_rundef.kBootDeviceMemBase_SemcSdram + RTyyyy_rundef.kBootDeviceMemMaxSize_SemcSdram - 1)))
                except:
                    self.popupMsgBox('Illegal input detected! You should input like this format: 0x80000000')
            else:
                self.popupMsgBox('Illegal input detected! You should input like this format: 0x80000000')
        else:
            self.dcdSettingsDict['sdramBase'] = None
        return status

    def _getDeviceModel( self ):
        if self.dcdSettingsDict['dcdSource'] == 'Use DCD descriptor':
            txt = self.m_choice_dcdModel.GetString(self.m_choice_dcdModel.GetSelection())
            if txt == 'No':
                self.m_textCtrl_dcdDesc.Clear()
                self.m_textCtrl_dcdDesc.LoadFile(os.path.join(self.dcdModelFolder, 'template', RTyyyy_gendef.kStdDcdFilename_Cfg))
            elif txt == 'Micron_MT48LC16M16A2' or txt == 'ISSI_IS42S16160J':
                self.m_textCtrl_dcdDesc.Clear()
                self.m_textCtrl_dcdDesc.LoadFile(os.path.join(self.dcdModelFolder, txt, RTyyyy_gendef.kStdDcdFilename_Cfg))
            else:
                pass
            self.dcdSettingsDict['deviceModel'] = txt

    def _getDcdDesc( self ):
        status = True
        if self.dcdSettingsDict['dcdSource'] == 'Use DCD descriptor':
            if self.m_textCtrl_dcdDesc.GetLineLength(0):
                self.m_textCtrl_dcdDesc.SaveFile(self.destCfgFilename)
                self.dcdCtrlDict['dcdFileType'] = RTyyyy_gendef.kUserDcdFileType_Cfg
                fileLen = os.path.getsize(self.destCfgFilename)
                with open(self.destCfgFilename, 'rb') as fileObj:
                    self.dcdSettingsDict['dcdDesc'] = fileObj.read(fileLen)
                    fileObj.close()
            else:
                status = False
                self.popupMsgBox('You need to enter the descriptor code!')
        return status

    def callbackSetDcdSource( self, event ):
        self._getDcdSource()

    def callbackSetDcdPurpose( self, event ):
        self._getDcdPurpose()

    def callbackSetDeviceModel( self, event ):
        self._getDeviceModel()

    def callbackOk( self, event ):
        self._getDcdSource()
        if not self._getDcdBinFile():
            return
        if not self._getDcdCfgFile():
            return
        if not self._getSdramBase():
            return
        if not self._getDcdDesc():
            return
        uivar.setBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_Dcd, self.dcdCtrlDict, self.dcdSettingsDict)
        uivar.setRuntimeSettings(False)
        self.Show(False)
        runtimeSettings = uivar.getRuntimeSettings()
        sound.playSoundEffect(runtimeSettings[1], runtimeSettings[2], uidef.kSoundEffectFilename_Progress)

    def callbackCancel( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

    def callbackClose( self, event ):
        uivar.setRuntimeSettings(False)
        self.Show(False)

