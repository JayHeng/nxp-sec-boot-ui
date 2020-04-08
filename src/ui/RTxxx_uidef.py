import wx
import sys, os

kConnectStep_Fast   = 2
kConnectStep_Normal = 1

kBootDevice_FlexspiNor     = 'FLEXSPI NOR'
kBootDevice_QuadspiNor     = 'QUADSPI NOR'
kBootDevice_UsdhcSd        = 'uSDHC SD'
kBootDevice_UsdhcMmc       = 'uSDHC MMC'
kBootDevice_FlexcommSpiNor = 'FLEXCOMM SPI NOR'

kBootDevice_v2_0_0 = [kBootDevice_FlexspiNor]
kBootDevice_v2_2_0 = [kBootDevice_FlexspiNor, kBootDevice_FlexcommSpiNor]
kBootDevice_Latest = kBootDevice_v2_2_0

kSecureBootType_PlainUnsigned        = 'Plain Unsigned Image Boot'
kSecureBootType_PlainSigned          = 'Plain Signed Image Boot'
kSecureBootType_PlainCrc             = 'Plain CRC Image Boot'
kSecureBootType_CryptoSigned         = 'Encrypted Signed Image Boot'
kSecureBootType_PlainSignedKeyStore  = 'Plain Signed Image Boot with KeyStore'
kSecureBootType_CryptoSignedKeyStore = 'Encrypted Signed Image Boot with KeyStore'

kSecureBootType_v2_0_0 = [kSecureBootType_PlainUnsigned, kSecureBootType_PlainCrc]
kSecureBootType_Latest = kSecureBootType_v2_0_0

kMemBlockColor_FDCB       = wx.Colour( 0x9f, 0x9f, 0x5f ) #wx.KHAKI
kMemBlockColor_Image      = wx.BLUE

