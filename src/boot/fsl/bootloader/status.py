#! /usr/bin/env python

# Copyright (c) 2013 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Utility routine to calculate a status value from a group and code.
def mkstatus(g, c):
    return ((g * 100) + c)

# Status groups.
kStatusGroup_Generic = 0
kStatusGroup_FlashDriver = 1
kStatusGroup_I2CDriver = 2
kStatusGroup_SPIDriver = 3
kStatusGroup_QuadSPIDriver = 4
kStatusGroup_Bootloader = 100
kStatusGroup_SBLoader = 101
kStatusGroup_MemoryInterface = 102
kStatusGroup_PropertyStore = 103
kStatusGroup_AppCrcCheck = 104
kStatusGroup_Packetizer = 105
kStatusGroup_ReliableUpdate = 106

# Generic status codes.
kStatus_Success                     = mkstatus(kStatusGroup_Generic, 0)
kStatus_Fail                        = mkstatus(kStatusGroup_Generic, 1)
kStatus_ReadOnly                    = mkstatus(kStatusGroup_Generic, 2)
kStatus_OutOfRange                  = mkstatus(kStatusGroup_Generic, 3)
kStatus_InvalidArgument             = mkstatus(kStatusGroup_Generic, 4)
kStatus_Timeout                     = mkstatus(kStatusGroup_Generic, 5),
kStatus_NoTransferInProgress        = mkstatus(kStatusGroup_Generic, 6)

# Flash driver errors.
kStatus_FlashSizeError              = mkstatus(kStatusGroup_FlashDriver, 0)
kStatus_FlashAlignmentError         = mkstatus(kStatusGroup_FlashDriver, 1)
kStatus_FlashAddressError           = mkstatus(kStatusGroup_FlashDriver, 2)
kStatus_FlashAccessError            = mkstatus(kStatusGroup_FlashDriver, 3)
kStatus_FlashProtectionViolation    = mkstatus(kStatusGroup_FlashDriver, 4)
kStatus_FlashCommandFailure         = mkstatus(kStatusGroup_FlashDriver, 5)
kStatus_FlashUnknownProperty        = mkstatus(kStatusGroup_FlashDriver, 6)
kStatus_FLASHEraseKeyError          = mkstatus(kStatusGroup_FlashDriver, 7)
kStatus_FLASHRegionExecuteOnly      = mkstatus(kStatusGroup_FlashDriver, 8)
kStatus_FLASHExecuteInRamFunctionNotReady   = mkstatus(kStatusGroup_FlashDriver, 9)
kStatus_FLASHPartitionStatusUpdateFailure   = mkstatus(kStatusGroup_FlashDriver, 10)
kStatus_FLASHSetFlexramAsEepromError   = mkstatus(kStatusGroup_FlashDriver, 11)
kStatus_FLASHRecoverFlexramAsRamError  = mkstatus(kStatusGroup_FlashDriver, 12)
kStatus_FLASHSetFlexramAsRamError   = mkstatus(kStatusGroup_FlashDriver, 13)
kStatus_FLASHRecoverFlexramAsEepromError    = mkstatus(kStatusGroup_FlashDriver, 14)
kStatus_FLASHCommandNotSupported    = mkstatus(kStatusGroup_FlashDriver, 15)
kStatus_FLASHSwapSystemNotInUninitialized   = mkstatus(kStatusGroup_FlashDriver, 16)
kStatus_FLASHSwapIndicatorAddressError  = mkstatus(kStatusGroup_FlashDriver, 17)


# I2C driver errors.
kStatus_I2C_SlaveTxUnderrun         = mkstatus(kStatusGroup_I2CDriver, 0)
kStatus_I2C_SlaveRxOverrun          = mkstatus(kStatusGroup_I2CDriver, 1)
kStatus_I2C_AribtrationLost         = mkstatus(kStatusGroup_I2CDriver, 2)

# SPI driver errors.
kStatus_SPI_SlaveTxUnderrun         = mkstatus(kStatusGroup_SPIDriver, 0)
kStatus_SPI_SlaveRxOverrun          = mkstatus(kStatusGroup_SPIDriver, 1)

# Bootloader errors.
kStatus_UnknownCommand              = mkstatus(kStatusGroup_Bootloader, 0)
kStatus_SecurityViolation           = mkstatus(kStatusGroup_Bootloader, 1)
kStatus_AbortDataPhase              = mkstatus(kStatusGroup_Bootloader, 2)
kStatus_Ping                        = mkstatus(kStatusGroup_Bootloader, 3)
kStatus_NoResponse                  = mkstatus(kStatusGroup_Bootloader, 4)
kStatus_NoResponseExpected          = mkstatus(kStatusGroup_Bootloader, 5)

# SB loader errors.
kStatusRomLdrSectionOverrun         = mkstatus(kStatusGroup_SBLoader, 0)
kStatusRomLdrSignature              = mkstatus(kStatusGroup_SBLoader, 1)
kStatusRomLdrSectionLength          = mkstatus(kStatusGroup_SBLoader, 2)
kStatusRomLdrUnencryptedOnly        = mkstatus(kStatusGroup_SBLoader, 3)
kStatusRomLdrEOFReached             = mkstatus(kStatusGroup_SBLoader, 4)
kStatusRomLdrChecksum               = mkstatus(kStatusGroup_SBLoader, 5)
kStatusRomLdrCrc32Error             = mkstatus(kStatusGroup_SBLoader, 6)
kStatusRomLdrUnknownCommand         = mkstatus(kStatusGroup_SBLoader, 7)
kStatusRomLdrIdNotFound             = mkstatus(kStatusGroup_SBLoader, 8)
kStatusRomLdrDataUnderrun           = mkstatus(kStatusGroup_SBLoader, 9)
kStatusRomLdrJumpReturned           = mkstatus(kStatusGroup_SBLoader, 10)
kStatusRomLdrCallFailed             = mkstatus(kStatusGroup_SBLoader, 11)
kStatusRomLdrKeyNotFound            = mkstatus(kStatusGroup_SBLoader, 12)
kStatusRomLdrSecureOnly             = mkstatus(kStatusGroup_SBLoader, 13)

# Memory interface errors.
kStatusMemoryRangeInvalid           = mkstatus(kStatusGroup_MemoryInterface, 0)
kStatusMemoryReadFailed             = mkstatus(kStatusGroup_MemoryInterface, 1)
kStatusMemoryWriteFailed            = mkstatus(kStatusGroup_MemoryInterface, 2)
kStatusMemoryCumulativeWrite        = mkstatus(kStatusGroup_MemoryInterface, 3)
kStatusMemoryAppOverlapWithExecuteOnlyRegion    = mkstatus(kStatusGroup_MemoryInterface, 4)
kStatusMemoryNotConfigured          = mkstatus(kStatusGroup_MemoryInterface, 5)   # 0x27dd
kStatusMemoryAlignmentError         = mkstatus(kStatusGroup_MemoryInterface, 6)
kStatusMemoryVerifyFailed           = mkstatus(kStatusGroup_MemoryInterface, 7)
kStatusMemoryWriteProtected         = mkstatus(kStatusGroup_MemoryInterface, 8)

# Property store errors.
kStatus_UnknownProperty             = mkstatus(kStatusGroup_PropertyStore, 0)
kStatus_ReadOnlyProperty            = mkstatus(kStatusGroup_PropertyStore, 1)
kStatus_InvalidPropertyValue        = mkstatus(kStatusGroup_PropertyStore, 2)

# Crc check errors.
kStatus_AppCrcCheckPassed           = mkstatus(kStatusGroup_AppCrcCheck, 0)
kStatus_AppCrcCheckFailed           = mkstatus(kStatusGroup_AppCrcCheck, 1)
kStatus_AppCrcCheckInactive         = mkstatus(kStatusGroup_AppCrcCheck, 2)
kStatus_AppCrcCheckInvalid          = mkstatus(kStatusGroup_AppCrcCheck, 3)
kStatus_AppCrcCheckOutOfRange       = mkstatus(kStatusGroup_AppCrcCheck, 4)

# QuadSPI driver errors
kStatus_QspiFlashSizeError          = mkstatus(kStatusGroup_QuadSPIDriver, 0)
kStatus_QspiFlashAlignmentError     = mkstatus(kStatusGroup_QuadSPIDriver, 1)
kStatus_QspiFlashAddressError       = mkstatus(kStatusGroup_QuadSPIDriver, 2)
kStatus_QspiFlashCommandFailure     = mkstatus(kStatusGroup_QuadSPIDriver, 3)
kStatus_QspiFlashUnknownProperty    = mkstatus(kStatusGroup_QuadSPIDriver, 4)
kStatus_QspiNotConfigured           = mkstatus(kStatusGroup_QuadSPIDriver, 5)
kStatus_QspiCommandNotSupported     = mkstatus(kStatusGroup_QuadSPIDriver, 6)

# Packetizer status errors.
kStatus_PacketizerStatusNoOutput    = mkstatus(kStatusGroup_Packetizer, 0)   # The name of this attribute has not been verified

# Reliable update errors.
kStatus_ReliableUpdateSuccess                     = mkstatus(kStatusGroup_ReliableUpdate, 0)
kStatus_ReliableUpdateFail                        = mkstatus(kStatusGroup_ReliableUpdate, 1)
kStatus_ReliableUpdateInactive                    = mkstatus(kStatusGroup_ReliableUpdate, 2)
kStatus_ReliableUpdateBackupApplicationInvalid    = mkstatus(kStatusGroup_ReliableUpdate, 3)
kStatus_ReliableUpdateStillInMainApplication      = mkstatus(kStatusGroup_ReliableUpdate, 4)
kStatus_ReliableUpdateSwapSystemNotReady          = mkstatus(kStatusGroup_ReliableUpdate, 5)
kStatus_ReliableUpdateBackupBootloaderNotReady    = mkstatus(kStatusGroup_ReliableUpdate, 6)
kStatus_ReliableUpdateSwapIndicatorAddressInvalid = mkstatus(kStatusGroup_ReliableUpdate, 7)

# SDP HAB mode status values.
kSDP_Status_HabEnabled = 0x12343412
kSDP_Status_HabDisabled = 0x56787856
# SDP Response status values.
kSDP_Response_WriteComplete = 0x128a8a12
kSDP_Response_WriteFileComplete = 0x88888888
kSDP_Response_HabStausFailure = 0x33333333
kSDP_Response_HabStausWarning = 0x69696969
kSDP_Response_HabStatusSuccess = 0xf0f0f0f0
kSDP_Response_OkAck = 0x900dd009

