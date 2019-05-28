#! /usr/bin/env python
import wx
import sys
import os
import uivar
import RT10yy_uidef
sys.path.append(os.path.abspath(".."))
from win import bootDeviceWin_FlexspiNand

class secBootUiFlexspiNand(bootDeviceWin_FlexspiNand.bootDeviceWin_FlexspiNand):
    def __init__(self, parent):
        bootDeviceWin_FlexspiNand.bootDeviceWin_FlexspiNand.__init__(self, parent)
        flexspiNandOpt, flexspiNandFcbOpt, flexspiNandImageInfo, flexspiNandKeyBlob = uivar.getBootDeviceConfiguration(RT10yy_uidef.kBootDevice_FlexspiNand)
        self.flexspiNandOpt = flexspiNandOpt
        self.flexspiNandFcbOpt = flexspiNandFcbOpt
        self.flexspiNandImageInfo = flexspiNandImageInfo
        self.flexspiNandKeyBlob = flexspiNandKeyBlob

    def _getFrequence( self ):
        txt = self.m_choice_Max_Freq.GetString(self.m_choice_Max_Freq.GetSelection())
        if txt == '30MHz':
            val = 0x1
        elif txt == '50MHz':
            val = 0x2
        elif txt == '60MHz':
            val = 0x3
        elif txt == '75MHz':
            val = 0x4
        elif txt == '80MHz':
            val = 0x5
        elif txt == '100MHz':
            val = 0x6
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xFFFFFFF0) | (val << 0)

    def _getPageSize( self ):
        txt = self.m_choice_Page_Size.GetString(self.m_choice_Page_Size.GetSelection())
        if txt == '2KB':
            val = 0x2
        elif txt == '4KB':
            val = 0x4
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xFFFFFF0F) | (val << 4)

    def _getPagePerBlock( self ):
        txt = self.m_choice_Pages.GetString(self.m_choice_Pages.GetSelection())
        if txt == '64':
            val = 0x0
        elif txt == '128':
            val = 0x1
        elif txt == '256':
            val = 0x2
        elif txt == '32':
            val = 0x3
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xFFFFF0FF) | (val << 8)


    def _getFlashSize( self ):
        txt = self.m_choice_Flash_size.GetString(self.m_choice_Flash_size.GetSelection())
        if txt == '512M':
            val = 0x0
        elif txt == '1GB':
            val = 0x1
        elif txt == '2GB':
            val = 0x2
        elif txt == '4GB':
            val = 0x4
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xFFF0FFFF) | (val << 16)


    def _getMultiplane( self ):
        txt = self.m_choice_planes.GetString(self.m_choice_planes.GetSelection())
        if txt == '1 plane':
            val = 0x0
        elif txt == '2 planes':
            val = 0x1
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xFFFF0FFF) | (val << 12)

    def _getOptionSize( self ):
        txt = self.m_choice_Option_size.GetString(self.m_choice_Option_size.GetSelection())
        if txt == '0':
            val = 0x0
        elif txt == '1':
            val = 0x1
        elif txt == '2':
            val = 0x2
        elif txt == '3':
            val = 0x3
        elif txt == '4':
            val = 0x4
        elif txt == '5':
            val = 0x5
        elif txt == '6':
            val = 0x6
        elif txt == '7':
            val = 0x7
        elif txt == '8':
            val = 0x8
        elif txt == '9':
            val = 0x9
        elif txt == '10':
            val = 0xA
        elif txt == '11':
            val = 0xB
        elif txt == '12':
            val = 0xC
        elif txt == '13':
            val = 0xD
        elif txt == '14':
            val = 0xE
        elif txt == '15':
            val = 0xF
        else:
            pass
        self.flexspiNandOpt = (self.flexspiNandOpt & 0xF0FFFFFF) | (val << 24)


    def _getFCBSize( self ):
        txt = self.m_choice_Size.GetString(self.m_choice_Size.GetSelection())
        if txt == '3':
            val = 0x3
        elif txt == '4':
            val = 0x4
        elif txt == '5':
            val = 0x5
        elif txt == '6':
            val = 0x6
        elif txt == '7':
            val = 0x7
        elif txt == '8':
            val = 0x8
        elif txt == '9':
            val = 0x9
        elif txt == '10':
            val = 0x10
        else:
            pass
        self.flexspiNandFcbOpt = (self.flexspiNandFcbOpt & 0xFFFFFFF0) | (val << 0)

    def _getAddressType( self ):
        txt = self.m_choice_address_type.GetString(self.m_choice_address_type.GetSelection())
        if txt == 'byte address':
            val = 0x0
        elif txt == 'block address':
            val = 0x1
        else:
            pass
        self.flexspiNandFcbOpt = (self.flexspiNandFcbOpt & 0xFFFFF0FF) | (val << 8)


    def _getSearchStride( self ):
        txt = self.m_choice_search_stride.GetString(self.m_choice_search_stride.GetSelection())
        if txt == '64 pages':
            val = 0x0
        elif txt == '128 pages':
            val = 0x1
        elif txt == '256 pages':
            val = 0x2
        elif txt == '32 pages':
            val = 0x3
        else:
            pass
        self.flexspiNandFcbOpt = (self.flexspiNandFcbOpt & 0xFF0FFFFF) | (val << 20)


    def _getSearchCount( self ):
        txt = self.m_choice_search_count.GetString(self.m_choice_search_count.GetSelection())
        if txt == '1':
            val = 0x1
        elif txt == '2':
            val = 0x2
        elif txt == '3':
            val = 0x3
        elif txt == '4':
            val = 0x4
        else:
            pass
        self.flexspiNandFcbOpt = (self.flexspiNandFcbOpt & 0xF0FFFFFF) | (val << 24)

    ################################# may be exist problem Need to be confirmed#################################
    def _getBlockCountandID( self ):
        val_block_count = int(self.m_textCtrl_block_count.GetLineText(0))
        val_block_id = int(self.m_textCtrl_block_id.GetLineText(0))
        if val_block_id > val_block_count:
            wx.MessageBox('Block ID Error', 'Confirm', wx.OK)
        if val_block_count > 8:
            wx.MessageBox('Max Block Number Error', 'Confirm', wx.OK)
        self.flexspiNandImageInfo = (self.flexspiNandImageInfo & 0xFFFF0000) | (val_block_id << 0)
        self.flexspiNandImageInfo = (self.flexspiNandImageInfo & 0x0000FFFF) | (val_block_count << 16)

    ################################# may be exist problem Need to be confirmed#################################

    def _getImageIndex( self ):
        txt = self.m_choice_image_index.GetString(self.m_choice_image_index.GetSelection())
        if txt == '0':
            val = 0x0
        elif txt == '1':
            val = 0x1
        elif txt == '2':
            val = 0x2
        elif txt == '3':
            val = 0x3
        elif txt == '4':
            val = 0x4
        elif txt == '5':
            val = 0x5
        elif txt == '6':
            val = 0x6
        elif txt == '7':
            val = 0x7
        elif txt == '8':
            val = 0x8
        elif txt == '9':
            val = 0x9
        elif txt == '10':
            val = 0xA
        elif txt == '11':
            val = 0xB
        elif txt == '12':
            val = 0xC
        elif txt == '13':
            val = 0xD
        elif txt == '14':
            val = 0xE
        elif txt == '15':
            val = 0xF
        else:
            pass
        if (self.flexspiNandKeyBlob & 0x0F000000) == 0x01000000:
            self.flexspiNandKeyBlob = (self.flexspiNandKeyBlob & 0xFFFFFFF0) | (val << 0)

    def _getDekSize( self ):
        txt = self.m_choice_dek_size.GetString(self.m_choice_dek_size.GetSelection())
        if txt == '128bits':
            val = 0x0
        else:
            pass
        if (self.flexspiNandKeyBlob & 0x0F000000) == 0x00000000:
            self.flexspiNandKeyBlob = (self.flexspiNandKeyBlob & 0xFFFFFF0F) | (val << 4)

    def _getKeyBlobInfoSize( self ):
        txt = self.m_choice_keyblob_infosize.GetString(self.m_choice_keyblob_infosize.GetSelection())
        if txt == '0':
            val = 0x0
        elif txt == '1':
            val = 0x1
        elif txt == '2':
            val = 0x2
        elif txt == '3':
            val = 0x3
        elif txt == '4':
            val = 0x4
        elif txt == '5':
            val = 0x5
        elif txt == '6':
            val = 0x6
        elif txt == '7':
            val = 0x7
        elif txt == '8':
            val = 0x8
        elif txt == '9':
            val = 0x9
        elif txt == '10':
            val = 0xA
        elif txt == '11':
            val = 0xB
        elif txt == '12':
            val = 0xC
        elif txt == '13':
            val = 0xD
        elif txt == '14':
            val = 0xE
        elif txt == '15':
            val = 0xF
        else:
            pass
        if (self.flexspiNandKeyBlob & 0x0F000000) == 0x00000000:
            if txt != '3':
                wx.MessageBox('keyblob_info size must equal to 3 if Type = Update', 'Confirm', wx.OK )
        else:
            self.flexspiNandKeyBlob = (self.flexspiNandKeyBlob & 0xFF0FFFFF) | (val << 20)

    def _getType( self ):
        txt = self.m_choice_type.GetString(self.m_choice_type.GetSelection())
        if txt == 'Update':
            val = 0x0
        elif txt == 'Program':
            val = 0x1
        else:
            pass
        self.flexspiNandKeyBlob = (self.flexspiNandKeyBlob & 0xF0FFFFFF) | (val << 24)

    def cancel_of_FLEXSPI_NAND(self, event):
        self.Show(False)

    def apply_of_FLEXSPI_NAND(self, event):
        self._getFrequence()
        self._getPageSize()
        self._getPageSize()
        self._getPagePerBlock()
        self._getFlashSize()
        self._getMultiplane()
        self._getOptionSize()
        self._getFCBSize()
        self._getAddressType()
        self._getSearchStride()
        self._getSearchCount()
        self._getBlockCountandID()
        self._getType()
        self._getImageIndex()
        self._getDekSize()
        self._getKeyBlobInfoSize()
        uivar.setBootDeviceConfiguration(RT10yy_uidef.kBootDevice_FlexspiNand, self.flexspiNandOpt, self.flexspiNandFcbOpt, self.flexspiNandImageInfo, self.flexspiNandKeyBlob)
        self.Show(False)

    def OnClose_FLEXSPI_NAND(self, event):
        ret = wx.MessageBox('Do you really want to leave?', 'Confirm', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            self.Show(False)