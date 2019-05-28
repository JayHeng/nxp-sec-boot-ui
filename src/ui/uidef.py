import wx
import sys, os

kMcuSeries_iMXRT   = 'i.MXRT'
kMcuSeries_LPC     = 'LPC'
kMcuSeries_Kinetis = 'Kinetis'

kMcuSeries_v1_0_0 = [kMcuSeries_iMXRT]
kMcuSeries_Latest = kMcuSeries_v1_0_0

kAdvancedSettings_Tool      = 0
kAdvancedSettings_Cert      = 1
kAdvancedSettings_BD        = 2
kAdvancedSettings_OtpmkKey  = 3
kAdvancedSettings_UserKeys  = 4

kSoundEffectFilename_Success  = 'levelwin_success.wav'
kSoundEffectFilename_Failure  = 'dead_failure.wav'
kSoundEffectFilename_Progress = 'getcoin_progress.wav'
kSoundEffectFilename_Restart  = 'pluslife_restart.wav'