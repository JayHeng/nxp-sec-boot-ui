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
from win import advSettingsWin_Cert
from utils import sound

class secBootUiSettingsCert(advSettingsWin_Cert.advSettingsWin_Cert):

    def __init__(self, parent):
        advSettingsWin_Cert.advSettingsWin_Cert.__init__(self, parent)
        self._setLanguage()
        self._initCstVersion()
        certSettingsDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Cert)
        self.certSettingsDict = certSettingsDict.copy()
        self._recoverLastSettings()

    def _setLanguage( self ):
        runtimeSettings = uivar.getRuntimeSettings()
        langIndex = runtimeSettings[3]
        self.m_notebook_certOpt.SetPageText(0, uilang.kSubLanguageContentDict['panel_certOpt'][langIndex])
        self.m_staticText_cstVersion.SetLabel(uilang.kSubLanguageContentDict['sText_cstVersion'][langIndex])
        self.m_staticText_useExistingCaKey.SetLabel(uilang.kSubLanguageContentDict['sText_useExistingCaKey'][langIndex])
        self.m_staticText_useEcc.SetLabel(uilang.kSubLanguageContentDict['sText_useEcc'][langIndex])
        self.m_staticText_pkiTreeKeyLen.SetLabel(uilang.kSubLanguageContentDict['sText_pkiTreeKeyLen'][langIndex])
        self.m_staticText_pkiTreeDuration.SetLabel(uilang.kSubLanguageContentDict['sText_pkiTreeDuration'][langIndex])
        self.m_staticText_SRKs.SetLabel(uilang.kSubLanguageContentDict['sText_SRKs'][langIndex])
        self.m_staticText_caFlagSet.SetLabel(uilang.kSubLanguageContentDict['sText_caFlagSet'][langIndex])
        self.m_button_ok.SetLabel(uilang.kSubLanguageContentDict['button_cert_ok'][langIndex])
        self.m_button_cancel.SetLabel(uilang.kSubLanguageContentDict['button_cert_cancel'][langIndex])

    def _initCstVersion( self ):
        self.m_choice_cstVersion.Clear()
        self.m_choice_cstVersion.SetItems(RTyyyy_uidef.kCstVersion_Avail)
        self.m_choice_cstVersion.SetSelection(0)

    def _setPkiTreeKeyLenItems( self ):
        keySel = None
        if self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_1_0 and self.certSettingsDict['useEllipticCurveCrypto'] == 'y':
            keySel = RTyyyy_uidef.kPkiTreeKeySel_IsEcc
        else:
            keySel = RTyyyy_uidef.kPkiTreeKeySel_NotEcc
        self.m_choice_pkiTreeKeyLen.Clear()
        self.m_choice_pkiTreeKeyLen.SetItems(keySel)
        self.m_choice_pkiTreeKeyLen.SetSelection(0)

    def _recoverLastSettings ( self ):
        cstVersion = self.certSettingsDict['cstVersion']
        if cstVersion == RTyyyy_uidef.kCstVersion_v2_3_3:
            self.m_choice_cstVersion.SetSelection(0)
        elif cstVersion == RTyyyy_uidef.kCstVersion_v3_0_1:
            self.m_choice_cstVersion.SetSelection(1)
        elif cstVersion == RTyyyy_uidef.kCstVersion_v3_1_0:
            self.m_choice_cstVersion.SetSelection(2)
        else:
            pass

        useExistingCaKey = self.certSettingsDict['useExistingCaKey']
        if useExistingCaKey == 'n':
            self.m_choice_useExistingCaKey.SetSelection(0)
        else:
            pass

        if self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_1_0:
            self.m_choice_useEcc.Enable( True )
            useEllipticCurveCrypto = self.certSettingsDict['useEllipticCurveCrypto']
            if useEllipticCurveCrypto == 'n':
                self.m_choice_useEcc.SetSelection(0)
            elif useEllipticCurveCrypto == 'y':
                self.m_choice_useEcc.SetSelection(1)
            else:
                pass
        elif self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v2_3_3 or self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_0_1:
            self.m_choice_useEcc.Enable( False )
        else:
            pass

        self._setPkiTreeKeyLenItems()

        pkiTreeKeyLen = self.certSettingsDict['pkiTreeKeyLen']
        if cstVersion == RTyyyy_uidef.kCstVersion_v3_1_0 and useEllipticCurveCrypto == 'y':
            if pkiTreeKeyLen == 'p256':
                self.m_choice_pkiTreeKeyLen.SetSelection(0)
            elif pkiTreeKeyLen == 'p384':
                self.m_choice_pkiTreeKeyLen.SetSelection(1)
            elif pkiTreeKeyLen == 'p521':
                self.m_choice_pkiTreeKeyLen.SetSelection(2)
            else:
                pass
        else:
            self.m_choice_pkiTreeKeyLen.SetSelection((pkiTreeKeyLen / 1024) - 1)

        pkiTreeDuration = self.certSettingsDict['pkiTreeDuration']
        self.m_textCtrl_pkiTreeDuration.Clear()
        self.m_textCtrl_pkiTreeDuration.write(str(pkiTreeDuration))

        SRKs = self.certSettingsDict['SRKs']
        self.m_choice_SRKs.SetSelection(SRKs - 1)

        caFlagSet = self.certSettingsDict['caFlagSet']
        if caFlagSet == 'y':
            self.m_choice_caFlagSet.SetSelection(0)
        elif caFlagSet == 'n':
            self.m_choice_caFlagSet.SetSelection(1)
        else:
            pass

    def _getCstVersion( self ):
        self.certSettingsDict['cstVersion'] = self.m_choice_cstVersion.GetString(self.m_choice_cstVersion.GetSelection())

    def _getUseExistingCaKey( self ):
        txt = self.m_choice_useExistingCaKey.GetString(self.m_choice_useExistingCaKey.GetSelection())
        self.certSettingsDict['useExistingCaKey'] = txt[0].lower()

    def _getUseEllipticCurveCrypto( self ):
        txt = self.m_choice_useEcc.GetString(self.m_choice_useEcc.GetSelection())
        self.certSettingsDict['useEllipticCurveCrypto'] = txt[0].lower()

    def _getPkiTreeKeyLen( self ):
        if self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_1_0 and self.certSettingsDict['useEllipticCurveCrypto'] == 'y':
            self.certSettingsDict['pkiTreeKeyLen'] = self.m_choice_pkiTreeKeyLen.GetString(self.m_choice_pkiTreeKeyLen.GetSelection())
            if self.certSettingsDict['pkiTreeKeyLen'] == 'p256':
                self.certSettingsDict['pkiTreeKeyCn'] = 'prime256v1'
            elif self.certSettingsDict['pkiTreeKeyLen'] == 'p384':
                self.certSettingsDict['pkiTreeKeyCn'] = 'secp384r1'
            elif self.certSettingsDict['pkiTreeKeyLen'] == 'p521':
                self.certSettingsDict['pkiTreeKeyCn'] = 'secp521r1'
            else:
                pass
        else:
            self.certSettingsDict['pkiTreeKeyLen'] = int(self.m_choice_pkiTreeKeyLen.GetString(self.m_choice_pkiTreeKeyLen.GetSelection()))

    def _getPkiTreeDuration( self ):
        self.certSettingsDict['pkiTreeDuration'] = int(self.m_textCtrl_pkiTreeDuration.GetLineText(0))

    def _getSRKs( self ):
        self.certSettingsDict['SRKs'] = int(self.m_choice_SRKs.GetString(self.m_choice_SRKs.GetSelection()))

    def _getCaFlagSet( self ):
        txt = self.m_choice_caFlagSet.GetString(self.m_choice_caFlagSet.GetSelection())
        self.certSettingsDict['caFlagSet'] = txt[0].lower()

    def callbackSwitchCstVersion( self, event ):
        self._getCstVersion()
        if self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_1_0:
            self.m_choice_useEcc.Enable( True )
        elif self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v2_3_3 or self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_0_1:
            self.m_choice_useEcc.Enable( False )
        else:
            pass
        self._setPkiTreeKeyLenItems()

    def callbackUseEcc( self, event ):
        self._getUseEllipticCurveCrypto()
        if self.certSettingsDict['cstVersion'] == RTyyyy_uidef.kCstVersion_v3_1_0:
            self._setPkiTreeKeyLenItems()

    def callbackOk( self, event ):
        self._getCstVersion()
        self._getUseExistingCaKey()
        self._getUseEllipticCurveCrypto()
        self._getPkiTreeKeyLen()
        self._getPkiTreeDuration()
        self._getSRKs()
        self._getCaFlagSet()
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Cert, self.certSettingsDict)
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
