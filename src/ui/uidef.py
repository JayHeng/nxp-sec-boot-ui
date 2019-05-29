import wx
import sys, os

kConnectStage_Rom            = 1
kConnectStage_Flashloader    = 2
kConnectStage_ExternalMemory = 3
kConnectStage_Reset          = 4

kMcuSeries_iMXRT10yy = 'i.MXRT10yy'
kMcuSeries_iMXRTxxx  = 'i.MXRTxxx'
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

kSoundEffectFilename_Success  = 'levelwin_success.wav'
kSoundEffectFilename_Failure  = 'dead_failure.wav'
kSoundEffectFilename_Progress = 'getcoin_progress.wav'
kSoundEffectFilename_Restart  = 'pluslife_restart.wav'