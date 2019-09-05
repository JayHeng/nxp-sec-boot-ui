import sys, os

kGroupEfuseWords = 80
kTotalEfuseWords = 320

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

kOtfadKeySel_FromPuf      = 0x0
kOtfadKeySel_FromUserKey5 = 0x0  # Fixme

kSpiAddressing_3Bytes = 0x0
kSpiAddressing_2Bytes = 0x1

##################################################
kEfuseRemapIndex_Src  = 0x30
kEfuseRemapIndex_Dest = 0x40
kEfuseRemapLen = 16

##################################################
kEfuseValue_Invalid = 0xdeadbeef
kEfuseValue_Blank   = 0x00000000
