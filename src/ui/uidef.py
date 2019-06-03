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

kMcuSeries_iMXRT10yy = 'RT10yy - CM7'
kMcuSeries_iMXRTxxx  = 'RTxxx - CM33'
kMcuSeries_LPC       = 'LPC'
kMcuSeries_Kinetis   = 'Kinetis'

kMcuSeries_v1_0_0 = [kMcuSeries_iMXRT10yy]
kMcuSeries_v2_0_0 = [kMcuSeries_iMXRT10yy, kMcuSeries_iMXRTxxx]
kMcuSeries_Latest = kMcuSeries_v2_0_0

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