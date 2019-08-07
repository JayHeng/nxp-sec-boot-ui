#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
import os
import RTyyyy_uidef
import uidef
import uivar
import uilang
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_SemcNand
from utils import sound

class secBootUiCfgSemcNand(bootDeviceWin_SemcNand.bootDeviceWin_SemcNand):

    def __init__(self, parent):
        bootDeviceWin_SemcNand.bootDeviceWin_SemcNand.__init__(self, parent)
        self._setLanguage()
        semcNandOpt, semcNandFcbOpt, semcNandImageInfoList = uivar.getBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_SemcNand)
        self.semcNandOpt = semcNandOpt
        self.semcNandFcbOpt = semcNandFcbOpt
        self.semcNandImageInfoList = semcNandImageInfoList[:]
        self.isSwEccSetAsDefaultInNandOpt = True

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_nandOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_nandOpt'][langIndex])
        self.m_staticText_onfiVersion.SetLabel(uilang.kSubLanguageContentDict['sText_onfiVersion'][langIndex])
        self.m_staticText_onfiTimingMode.SetLabel(uilang.kSubLanguageContentDict['sText_onfiTimingMode'][langIndex])
        self.m_staticText_edoMode.SetLabel(uilang.kSubLanguageContentDict['sText_edoMode'][langIndex])
        self.m_staticText_ioPortSize.SetLabel(uilang.kSubLanguageContentDict['sText_ioPortSize'][langIndex])
        self.m_staticText_pcsPort.SetLabel(uilang.kSubLanguageContentDict['sText_pcsPort'][langIndex])
        self.m_staticText_eccType.SetLabel(uilang.kSubLanguageContentDict['sText_eccType'][langIndex])
        self.m_staticText_eccStatus.SetLabel(uilang.kSubLanguageContentDict['sText_eccStatus'][langIndex])
        self.m_notebook_fcbOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_fcbOpt'][langIndex])
        self.m_staticText_searchCount.SetLabel(uilang.kSubLanguageContentDict['sText_searchCount'][langIndex])
        self.m_staticText_searchStride.SetLabel(uilang.kSubLanguageContentDict['sText_searchStride'][langIndex])
        self.m_staticText_imageCopies.SetLabel(uilang.kSubLanguageContentDict['sText_imageCopies'][langIndex])
        self.m_notebook_imageInfo.SetPageText(0, uilang.kSubLanguageContentDict['panel_imageInfo'][langIndex])
        self.m_staticText_blockIndex.SetLabel(uilang.kSubLanguageContentDict['sText_blockIndex'][langIndex])
        self.m_staticText_blockCount.SetLabel(uilang.kSubLanguageContentDict['sText_blockCount'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_semcnand_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_semcnand_cancel'][langIndex])

    def setNecessaryInfo( self, isSwEccSetAsDefaultInNandOpt ):
        self.isSwEccSetAsDefaultInNandOpt = isSwEccSetAsDefaultInNandOpt
        self._recoverLastSettings()

    def _updateImageInfoField ( self, imageCopies ):
        if imageCopies < 2:
            self.m_textCtrl_image1Idx.Clear()
            self.m_textCtrl_image1Cnt.Clear()
            self.m_textCtrl_image1Idx.Enable( False )
            self.m_textCtrl_image1Cnt.Enable( False )
        else:
            self.m_textCtrl_image1Idx.Enable( True )
            self.m_textCtrl_image1Cnt.Enable( True )
        if imageCopies < 3:
            self.m_textCtrl_image2Idx.Clear()
            self.m_textCtrl_image2Cnt.Clear()
            self.m_textCtrl_image2Idx.Enable( False )
            self.m_textCtrl_image2Cnt.Enable( False )
        else:
            self.m_textCtrl_image2Idx.Enable( True )
            self.m_textCtrl_image2Cnt.Enable( True )
        if imageCopies < 4:
            self.m_textCtrl_image3Idx.Clear()
            self.m_textCtrl_image3Cnt.Clear()
            self.m_textCtrl_image3Idx.Enable( False )
            self.m_textCtrl_image3Cnt.Enable( False )
        else:
            self.m_textCtrl_image3Idx.Enable( True )
            self.m_textCtrl_image3Cnt.Enable( True )
        if imageCopies < 5:
            self.m_textCtrl_image4Idx.Clear()
            self.m_textCtrl_image4Cnt.Clear()
            self.m_textCtrl_image4Idx.Enable( False )
            self.m_textCtrl_image4Cnt.Enable( False )
        else:
            self.m_textCtrl_image4Idx.Enable( True )
            self.m_textCtrl_image4Cnt.Enable( True )
        if imageCopies < 6:
            self.m_textCtrl_image5Idx.Clear()
            self.m_textCtrl_image5Cnt.Clear()
            self.m_textCtrl_image5Idx.Enable( False )
            self.m_textCtrl_image5Cnt.Enable( False )
        else:
            self.m_textCtrl_image5Idx.Enable( True )
            self.m_textCtrl_image5Cnt.Enable( True )
        if imageCopies < 7:
            self.m_textCtrl_image6Idx.Clear()
            self.m_textCtrl_image6Cnt.Clear()
            self.m_textCtrl_image6Idx.Enable( False )
            self.m_textCtrl_image6Cnt.Enable( False )
        else:
            self.m_textCtrl_image6Idx.Enable( True )
            self.m_textCtrl_image6Cnt.Enable( True )
        if imageCopies < 8:
            self.m_textCtrl_image7Idx.Clear()
            self.m_textCtrl_image7Cnt.Clear()
            self.m_textCtrl_image7Idx.Enable( False )
            self.m_textCtrl_image7Cnt.Enable( False )
        else:
            self.m_textCtrl_image7Idx.Enable( True )
            self.m_textCtrl_image7Cnt.Enable( True )

    def _recoverLastSettings ( self ):
        onfiVersion = (self.semcNandOpt & 0x00000007) >> 0
        self.m_choice_onfiVersion.SetSelection(onfiVersion - 1)

        edoMode = (self.semcNandOpt & 0x00000008) >> 3
        self.m_choice_edoMode.SetSelection(edoMode)

        onfiTimingMode = (self.semcNandOpt & 0x00000070) >> 4
        self.m_choice_onfiTimingMode.SetSelection(onfiTimingMode)

        ioPortSize = (self.semcNandOpt & 0x00000300) >> 8
        self.m_choice_ioPortSize.SetSelection(ioPortSize - 1)

        pcsPort = (self.semcNandOpt & 0x00007000) >> 12
        self.m_choice_pcsPort.SetSelection(pcsPort)

        eccType = (self.semcNandOpt & 0x00010000) >> 16
        if self.isSwEccSetAsDefaultInNandOpt:
            self.m_choice_eccType.SetSelection(eccType)
        else:
            self.m_choice_eccType.SetSelection((eccType + 1) % 2)

        eccStatus = (self.semcNandOpt & 0x00020000) >> 17
        self.m_choice_eccStatus.SetSelection(eccStatus)

        searchCount = (self.semcNandFcbOpt & 0x0000000F) >> 0
        self.m_choice_searchCount.SetSelection(searchCount - 1)

        searchStride = (self.semcNandFcbOpt & 0x0000FF00) >> 8
        self.m_textCtrl_searchStride.Clear()
        self.m_textCtrl_searchStride.write(str(searchStride))

        imageCopies = (self.semcNandFcbOpt & 0x000F0000) >> 16
        self.m_choice_imageCopies.SetSelection(imageCopies - 1)

        self._updateImageInfoField(imageCopies)

        if imageCopies > 0:
            imageIdx = self.semcNandImageInfoList[0] >> 16
            imageCnt = self.semcNandImageInfoList[0] & 0x0000FFFF
            self.m_textCtrl_image0Idx.Clear()
            self.m_textCtrl_image0Cnt.Clear()
            self.m_textCtrl_image0Idx.write(str(imageIdx))
            self.m_textCtrl_image0Cnt.write(str(imageCnt))
        if imageCopies > 1:
            imageIdx = self.semcNandImageInfoList[1] >> 16
            imageCnt = self.semcNandImageInfoList[1] & 0x0000FFFF
            self.m_textCtrl_image1Idx.Clear()
            self.m_textCtrl_image1Cnt.Clear()
            self.m_textCtrl_image1Idx.write(str(imageIdx))
            self.m_textCtrl_image1Cnt.write(str(imageCnt))
        if imageCopies > 2:
            imageIdx = self.semcNandImageInfoList[2] >> 16
            imageCnt = self.semcNandImageInfoList[2] & 0x0000FFFF
            self.m_textCtrl_image2Idx.Clear()
            self.m_textCtrl_image2Cnt.Clear()
            self.m_textCtrl_image2Idx.write(str(imageIdx))
            self.m_textCtrl_image2Cnt.write(str(imageCnt))
        if imageCopies > 3:
            imageIdx = self.semcNandImageInfoList[3] >> 16
            imageCnt = self.semcNandImageInfoList[3] & 0x0000FFFF
            self.m_textCtrl_image3Idx.Clear()
            self.m_textCtrl_image3Cnt.Clear()
            self.m_textCtrl_image3Idx.write(str(imageIdx))
            self.m_textCtrl_image3Cnt.write(str(imageCnt))
        if imageCopies > 4:
            imageIdx = self.semcNandImageInfoList[4] >> 16
            imageCnt = self.semcNandImageInfoList[4] & 0x0000FFFF
            self.m_textCtrl_image4Idx.Clear()
            self.m_textCtrl_image4Cnt.Clear()
            self.m_textCtrl_image4Idx.write(str(imageIdx))
            self.m_textCtrl_image4Cnt.write(str(imageCnt))
        if imageCopies > 5:
            imageIdx = self.semcNandImageInfoList[5] >> 16
            imageCnt = self.semcNandImageInfoList[5] & 0x0000FFFF
            self.m_textCtrl_image5Idx.Clear()
            self.m_textCtrl_image5Cnt.Clear()
            self.m_textCtrl_image5Idx.write(str(imageIdx))
            self.m_textCtrl_image5Cnt.write(str(imageCnt))
        if imageCopies > 6:
            imageIdx = self.semcNandImageInfoList[6] >> 16
            imageCnt = self.semcNandImageInfoList[6] & 0x0000FFFF
            self.m_textCtrl_image6Idx.Clear()
            self.m_textCtrl_image6Cnt.Clear()
            self.m_textCtrl_image6Idx.write(str(imageIdx))
            self.m_textCtrl_image6Cnt.write(str(imageCnt))
        if imageCopies > 7:
            imageIdx = self.semcNandImageInfoList[7] >> 16
            imageCnt = self.semcNandImageInfoList[7] & 0x0000FFFF
            self.m_textCtrl_image7Idx.Clear()
            self.m_textCtrl_image7Cnt.Clear()
            self.m_textCtrl_image7Idx.write(str(imageIdx))
            self.m_textCtrl_image7Cnt.write(str(imageCnt))

    def _getOnfiVersion( self ):
        txt = self.m_choice_onfiVersion.GetString(self.m_choice_onfiVersion.GetSelection())
        if txt == 'ONFI 1.x':
            val = 0x1
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFFFFF8) | (val << 0)

    def _getEdoMode( self ):
        txt = self.m_choice_edoMode.GetString(self.m_choice_edoMode.GetSelection())
        if txt == 'Disabled':
            val = 0x0
        elif txt == 'Enabled':
            val = 0x1
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFFFFF7) | (val << 3)

    def _getOnfiTimingMode( self ):
        txt = self.m_choice_onfiTimingMode.GetString(self.m_choice_onfiTimingMode.GetSelection())
        if txt == 'Mode0 - 10MHz':
            val = 0x0
        elif txt == 'Mode1 - 20MHz':
            val = 0x1
        elif txt == 'Mode2 - 28MHz':
            val = 0x2
        elif txt == 'Mode3 - 33MHz':
            val = 0x3
        elif txt == 'Mode4 - 40MHz':
            val = 0x4
        elif txt == 'Mode5 - 50MHz':
            val = 0x5
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFFFF8F) | (val << 4)

    def _getIoPortSize( self ):
        txt = self.m_choice_ioPortSize.GetString(self.m_choice_ioPortSize.GetSelection())
        if txt == 'x8 bits':
            val = 0x1
        elif txt == 'x16 bits':
            val = 0x2
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFFFCFF) | (val << 8)

    def _getPcsPort( self ):
        txt = self.m_choice_pcsPort.GetString(self.m_choice_pcsPort.GetSelection())
        if txt == 'CSX0':
            val = 0x0
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFF8FFF) | (val << 12)

    def _getEccType( self ):
        txt = self.m_choice_eccType.GetString(self.m_choice_eccType.GetSelection())
        if self.isSwEccSetAsDefaultInNandOpt:
            zeroSelStr = 'SW - 1bit ECC'
            oneSelStr = 'HW'
        else:
            zeroSelStr = 'HW'
            oneSelStr = 'SW - 1bit ECC'
        if txt == zeroSelStr:
            val = 0x0
        elif txt == oneSelStr:
            val = 0x1
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFEFFFF) | (val << 16)

    def _getEccStatus( self ):
        txt = self.m_choice_eccStatus.GetString(self.m_choice_eccStatus.GetSelection())
        if txt == 'Enabled':
            val = 0x0
        elif txt == 'Disabled':
            val = 0x1
        else:
            pass
        self.semcNandOpt = (self.semcNandOpt & 0xFFFDFFFF) | (val << 17)

    def _getSearchCount( self ):
        val = int(self.m_choice_searchCount.GetString(self.m_choice_searchCount.GetSelection()))
        self.semcNandFcbOpt = (self.semcNandFcbOpt & 0xFFFFFFF0) | (val << 0)

    def _getSearchStride( self ):
        val = int(self.m_textCtrl_searchStride.GetLineText(0))
        self.semcNandFcbOpt = (self.semcNandFcbOpt & 0xFFFF00FF) | (val << 8)

    def _getImageCopies( self ):
        val = int(self.m_choice_imageCopies.GetString(self.m_choice_imageCopies.GetSelection()))
        self.semcNandFcbOpt = (self.semcNandFcbOpt & 0xFFF0FFFF) | (val << 16)

    def _getImageInfo( self ):
        imageCopies = int(self.m_choice_imageCopies.GetString(self.m_choice_imageCopies.GetSelection()))
        if imageCopies > 0:
            self.semcNandImageInfoList[0] = (int(self.m_textCtrl_image0Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image0Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[0] = None
        if imageCopies > 1:
            self.semcNandImageInfoList[1] = (int(self.m_textCtrl_image1Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image1Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[1] = None
        if imageCopies > 2:
            self.semcNandImageInfoList[2] = (int(self.m_textCtrl_image2Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image2Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[2] = None
        if imageCopies > 3:
            self.semcNandImageInfoList[3] = (int(self.m_textCtrl_image3Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image3Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[3] = None
        if imageCopies > 4:
            self.semcNandImageInfoList[4] = (int(self.m_textCtrl_image4Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image4Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[4] = None
        if imageCopies > 5:
            self.semcNandImageInfoList[5] = (int(self.m_textCtrl_image5Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image5Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[5] = None
        if imageCopies > 6:
            self.semcNandImageInfoList[6] = (int(self.m_textCtrl_image6Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image6Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[6] = None
        if imageCopies > 7:
            self.semcNandImageInfoList[7] = (int(self.m_textCtrl_image7Idx.GetLineText(0)) << 16) + int(self.m_textCtrl_image7Cnt.GetLineText(0))
        else:
            self.semcNandImageInfoList[7] = None

    def callbackChangeImageCopies( self, event ):
        imageCopies = int(self.m_choice_imageCopies.GetString(self.m_choice_imageCopies.GetSelection()))
        self._updateImageInfoField(imageCopies)

    def callbackOk( self, event ):
        self._getOnfiVersion()
        self._getEdoMode()
        self._getOnfiTimingMode()
        self._getIoPortSize()
        self._getPcsPort()
        self._getEccType()
        self._getEccStatus()
        self._getSearchCount()
        self._getSearchStride()
        self._getImageCopies()
        self._getImageInfo()
        uivar.setBootDeviceConfiguration(RTyyyy_uidef.kBootDevice_SemcNand, self.semcNandOpt, self.semcNandFcbOpt, self.semcNandImageInfoList)
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
