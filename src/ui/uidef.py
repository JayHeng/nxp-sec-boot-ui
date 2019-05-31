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