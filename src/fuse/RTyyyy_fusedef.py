import sys, os

kMaxEfuseWords  = 80

##################################################

kEfuseIndex_START  = 0x0
kEfuseIndex_LOCK  = kEfuseIndex_START

kEfuseIndex_TESTER0  = 0x1
kEfuseIndex_TESTER1  = 0x2
kEfuseIndex_TESTER2  = 0x3
kEfuseIndex_TESTER3  = 0x4

kEfuseIndex_BOOT_CFG0  = 0x5
kEfuseIndex_BOOT_CFG1  = 0x6
kEfuseIndex_BOOT_CFG2  = 0x7

kEfuseIndex_OTPMK0 = 0x10
kEfuseIndex_OTPMK1 = 0x11
kEfuseIndex_OTPMK2 = 0x12
kEfuseIndex_OTPMK3 = 0x13
kEfuseIndex_OTPMK4 = 0x14
kEfuseIndex_OTPMK5 = 0x15
kEfuseIndex_OTPMK6 = 0x16
kEfuseIndex_OTPMK7 = 0x17

kEfuseIndex_SRK0 = 0x18
kEfuseIndex_SRK1 = 0x19
kEfuseIndex_SRK2 = 0x1A
kEfuseIndex_SRK3 = 0x1B
kEfuseIndex_SRK4 = 0x1C
kEfuseIndex_SRK5 = 0x1D
kEfuseIndex_SRK6 = 0x1E
kEfuseIndex_SRK7 = 0x1F

kEfuseIndex_OTFAD_KEY = 0x22
kEfuseIndex_OTFAD_CFG = 0x23

kEfuseIndex_SW_GP2_0 = 0x29
kEfuseIndex_SW_GP2_1 = 0x2A
kEfuseIndex_SW_GP2_2 = 0x2B
kEfuseIndex_SW_GP2_3 = 0x2C

kEfuseIndex_MISC_CONF0 = 0x2D
kEfuseIndex_MISC_CONF1 = 0x2E

kEfuseIndex_GP4_0 = 0x3C
kEfuseIndex_GP4_1 = 0x3D
kEfuseIndex_GP4_2 = 0x3E
kEfuseIndex_GP4_3 = 0x3F

##################################################

kEfuseMask_LockLow    = 0x0FFFFFFF
kEfuseMask_LockHigh   = 0xF0000000
kEfuseMask_LockSrk    = 0x00004000
kEfuseMask_RLockGp4   = 0x00000080
kEfuseMask_WLockGp4   = 0x03000000
kEfuseMask_WLockSwGp2 = 0x00200000
kEfuseMask_RLockSwGp2 = 0x00800000
kEfuseShift_LockLow  = 0
kEfuseShift_LockHigh = 28

kEfuseMask_SecConfig0 = 0x00000002
kEfuseMask_SecConfig1 = 0x00000002
kEfuseShift_SecConfig0 = 1
kEfuseShift_SecConfig1 = 1
kEfuseLocation_SecConfig0 = kEfuseIndex_TESTER3
kEfuseLocation_SecConfig1 = kEfuseIndex_BOOT_CFG1

kEfuseMask_BtFuseSel = 0x00000010
kEfuseShift_BtFuseSel = 4
kEfuseLocation_BtFuseSel = kEfuseIndex_BOOT_CFG1

kEfuseMask_HwCryptoKey0Sel = 0x00003000
kEfuseMask_HwCryptoKey1Sel = 0x0000C000
kEfuseShift_HwCryptoKey0Sel = 12
kEfuseShift_HwCryptoKey1Sel = 14
kEfuseLocation_HwCryptoKeySel = kEfuseIndex_BOOT_CFG1

kEfuseMask_OtfadKeyScrambleAlign  = 0x000000FF
kEfuseShift_OtfadKeyScrambleAlign = 0
kEfuseMask_OtfadEnable  = 0x00000100
kEfuseShift_OtfadEnable = 8
kEfuseMask_OtfadKeyScrambleEnable  = 0x00000400
kEfuseShift_OtfadKeyScrambleEnable = 10
kEfuseLocation_OtfadEnable = kEfuseIndex_OTFAD_CFG

kEfuseMask_DefaultFlexramPart  = 0x000F0000
kEfuseShift_DefaultFlexramPart = 16
kEfuseMask_EepromEnable        = 0x01000000
kEfuseShift_EepromEnable       = 24
kEfuseMask_LpspiIndex          = 0x06000000
kEfuseShift_LpspiIndex         = 25
kEfuseMask_SpiAddressing       = 0x08000000
kEfuseShift_SpiAddressing      = 27
kEfuseMask_LpspiSpeed          = 0x30000000
kEfuseShift_LpspiSpeed         = 28
kEfuseLocation_LpspiCfg        = kEfuseIndex_MISC_CONF0

kEfuseMask_RawNandPortSize   = 0x00000008
kEfuseShift_RawNandPortSize  = 3
kEfuseMask_RawNandEccEdoSet  = 0x00000010
kEfuseShift_RawNandEccEdoSet = 4
kEfuseMask_RawNandEccStatus  = 0x01000000
kEfuseShift_RawNandEccStatus = 24
kEfuseLocation_SemcNandCfg   = kEfuseIndex_MISC_CONF1

##################################################

kHabStatus_FAB     = 0x0
kHabStatus_Open    = 0x1
kHabStatus_Closed0 = 0x2
kHabStatus_Closed1 = 0x3

kBeeKeySel_FromReg       = 0x0
kBeeKeySel_FromGp4       = 0x1
kBeeKeySel_FromOtpmkHigh = 0x2
kBeeKeySel_FromSwGp2     = 0x3

kOtfadKeySel_FromOtpmkLow  = 0x0
kOtfadKeySel_FromOtpmkHigh = 0x1
kOtfadKeySel_Reserved      = 0x2
kOtfadKeySel_FromSwGp2     = 0x3

kSpiAddressing_3Bytes = 0x0
kSpiAddressing_2Bytes = 0x1

##################################################
kEfuseRemapIndex_Src  = 0x30
kEfuseRemapIndex_Dest = 0x40
kEfuseRemapLen = 16

##################################################
kEfuseEntryModeRegion0IndexStart = 0x01
kEfuseEntryModeRegion0IndexEnd   = 0x02
kEfuseEntryModeRegion1IndexStart = 0x05
kEfuseEntryModeRegion1IndexEnd   = 0x07
kEfuseEntryModeRegion2IndexStart = 0x18
kEfuseEntryModeRegion2IndexEnd   = 0x1F
kEfuseEntryModeRegion3IndexStart = 0x29
kEfuseEntryModeRegion3IndexEnd   = 0x2E
kEfuseEntryModeRegion4IndexStart = 0x4C
kEfuseEntryModeRegion4IndexEnd   = 0x4F

##################################################
kEfuseValue_Invalid = 0xdeadbeef
kEfuseValue_Blank   = 0x00000000
