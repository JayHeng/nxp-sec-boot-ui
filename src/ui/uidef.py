import wx
import sys, os

kBootSeqColor_Invalid  = wx.Colour( 64, 64, 64 )
kBootSeqColor_Optional = wx.Colour( 166, 255, 255 )
kBootSeqColor_Active   = wx.Colour( 147, 255, 174 )
kBootSeqColor_Failed   = wx.Colour( 255, 0, 0 )

kConnectStage_Rom            = 1
kConnectStage_Flashloader    = 2
kConnectStage_ExternalMemory = 3
kConnectStage_Reset          = 4

kMcuSeries_iMXRT     = 'i.MXRT'
kMcuSeries_iMXRT10yy = 'RT10yy'
kMcuSeries_iMXRTxxx  = 'RTxxx'
kMcuSeries_iMXRT11yy = 'RT11yy'
kMcuSeries_iMXRTyyyy = [kMcuSeries_iMXRT10yy, kMcuSeries_iMXRT11yy]
kMcuSeries_LPC       = 'LPC'
kMcuSeries_Kinetis   = 'Kinetis'

kMcuSeries_v1_0_0 = [kMcuSeries_iMXRT]
kMcuSeries_v2_0_0 = [kMcuSeries_iMXRT]
kMcuSeries_Latest = kMcuSeries_v2_0_0

kMcuDevice_iMXRT500  = 'i.MXRT5xx'
kMcuDevice_iMXRT500S = 'i.MXRT5xxS'
kMcuDevice_iMXRT600  = 'i.MXRT6xx'
kMcuDevice_iMXRT600S = 'i.MXRT6xxS'
kMcuDevice_iMXRTxxx = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600]

kMcuDevice_iMXRT1011 = 'i.MXRT1011'
kMcuDevice_iMXRT1015 = 'i.MXRT1015'
kMcuDevice_iMXRT102x = 'i.MXRT102x'
kMcuDevice_iMXRT105x = 'i.MXRT105x'
kMcuDevice_iMXRT106x = 'i.MXRT106x'
kMcuDevice_iMXRT1064 = 'i.MXRT1064 SIP'
kMcuDevice_iMXRT10yy = [kMcuDevice_iMXRT1011, kMcuDevice_iMXRT1015, kMcuDevice_iMXRT102x, kMcuDevice_iMXRT105x, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT1064]

kMcuDevice_iMXRT117x = 'i.MXRT117x'
kMcuDevice_iMXRT11yy = [kMcuDevice_iMXRT117x]

kMcuDevice_v1_0_0 = [kMcuDevice_iMXRT102x, kMcuDevice_iMXRT105x, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT1064]
kMcuDevice_v1_1_0 = [kMcuDevice_iMXRT1015, kMcuDevice_iMXRT102x, kMcuDevice_iMXRT105x, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT1064]
kMcuDevice_v2_0_0 = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600, kMcuDevice_iMXRT1011, kMcuDevice_iMXRT1015, kMcuDevice_iMXRT102x, kMcuDevice_iMXRT105x, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT1064, kMcuDevice_iMXRT117x]
kMcuDevice_Latest = kMcuDevice_v2_0_0

kBootDevice_XspiNor        = 'XSPI NOR'

kFlexspiNorDevice_None                  = 'No'
kFlexspiNorDevice_ISSI_IS25LP064A       = 'ISSI_IS25LP064A_IS25WP064A'
kFlexspiNorDevice_ISSI_IS26KS512S       = 'ISSI_IS26KS512S'
kFlexspiNorDevice_MXIC_MX25UM51245G     = 'MXIC_MX25UM51245G_MX66UM51245G_MX25LM51245G'
kFlexspiNorDevice_MXIC_MX25UM51345G     = 'MXIC_MX25UM51345G'
kFlexspiNorDevice_Micron_MT35X          = 'Micron_MT35X'
kFlexspiNorDevice_Adesto_AT25SF128A     = 'Adesto_AT25SF128A'
kFlexspiNorDevice_Adesto_ATXP032        = 'Adesto_ATXP032'
kFlexspiNorDevice_Cypress_S26KS512S     = 'Cypress_S26KS512S'
kFlexspiNorDevice_GigaDevice_GD25LB256E = 'GigaDevice_GD25LB256E'
kFlexspiNorDevice_GigaDevice_GD25LT256E = 'GigaDevice_GD25LT256E'
kFlexspiNorDevice_GigaDevice_GD25LX256E = 'GigaDevice_GD25LX256E'
kFlexspiNorDevice_Winbond_W25Q128JV     = 'Winbond_W25Q128JV'

kFlexspiNorOpt0_ISSI_IS25LP064A       = 0xc0000007
kFlexspiNorOpt0_ISSI_IS26KS512S       = 0xc0233007
kFlexspiNorOpt0_MXIC_MX25UM51245G     = 0xc0403037
kFlexspiNorOpt0_MXIC_MX25UM51345G     = 0xc0403007
kFlexspiNorOpt0_Micron_MT35X          = 0xc0600006
kFlexspiNorOpt0_Adesto_AT25SF128A     = 0xc0000007
kFlexspiNorOpt0_Adesto_ATXP032        = 0xc0803007
kFlexspiNorOpt0_Cypress_S26KS512S     = 0xc0233007
kFlexspiNorOpt0_GigaDevice_GD25LB256E = 0xc0000007
kFlexspiNorOpt0_GigaDevice_GD25LT256E = 0xc0000008
kFlexspiNorOpt0_GigaDevice_GD25LX256E = 0xc0600008
kFlexspiNorOpt0_Winbond_W25Q128JV     = 0xc0000207

kAdvancedSettings_Tool      = 0
kAdvancedSettings_Cert      = 1
kAdvancedSettings_BD        = 2
kAdvancedSettings_OtpmkKey  = 3
kAdvancedSettings_UserKeys  = 4

kAppImageFormat_AutoDetect  = 'Auto-detect image format'
kAppImageFormat_AxfFromMdk  = '.out(axf) from Keil MDK'
kAppImageFormat_ElfFromIar  = '.out(elf) from IAR EWARM'
kAppImageFormat_AxfFromMcux = '.out(axf) from MCUXpresso'
kAppImageFormat_ElfFromGcc  = '.out(elf) from GCC ARM'
kAppImageFormat_MotoSrec    = 'Motorola S-Records (.srec/.s19)'
kAppImageFormat_IntelHex    = 'Intel Extended Hex (.hex)'
kAppImageFormat_RawBinary   = 'Raw Binary (.bin)'

kSoundEffectFilename_Success  = 'levelwin_success.wav'
kSoundEffectFilename_Failure  = 'dead_failure.wav'
kSoundEffectFilename_Progress = 'getcoin_progress.wav'
kSoundEffectFilename_Restart  = 'pluslife_restart.wav'

kMemBlockColor_Background = wx.WHITE
kMemBlockColor_Padding    = wx.BLACK

kSecureBootSeqStep_AllInOne   = 0
kSecureBootSeqStep_GenCert    = 1
kSecureBootSeqStep_GenImage   = 2
kSecureBootSeqStep_PrepBee    = 3
kSecureBootSeqStep_ProgSrk    = 4
kSecureBootSeqStep_OperBee    = 5
kSecureBootSeqStep_FlashImage = 6
kSecureBootSeqStep_ProgDek    = 7

kPageIndex_ImageGenerationSequence = 0
kPageIndex_ImageLoadingSequence    = 1
kPageIndex_EfuseOperationUtility   = 2
kPageIndex_BootDeviceMemory        = 3
