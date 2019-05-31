import sys, os

kMcuDeviceFamily_RT500 = 'rt5xx'
kMcuDeviceFamily_RT600 = 'rt6xx'

kBootImageExecTarget_Ram      = 'RAM'
kBootImageExecTarget_XipFlash = 'External flash (XIP)'

kBootImageAuthType_Crc          = 'crc'
kBootImageAuthType_Signed       = 'Signed'
kBootImageAuthType_CryptoSigned = 'Encrypted + Signed'

kBootHeaderOffset_ImgLen      = 0x20
kBootHeaderOffset_ImgType     = 0x24
kBootHeaderOffset_CheckBlock  = 0x28
kBootHeaderOffset_ImgLoadAddr = 0x34

kBootImageTypeVal_PlainUnsigned        = 0x0000
kBootImageTypeVal_PlainSigned          = 0x0001
kBootImageTypeVal_PlainCrc             = 0x0002
kBootImageTypeVal_CryptoSigned         = 0x0003
kBootImageTypeVal_PlainSignedXip       = 0x0004
kBootImageTypeVal_PlainCrcXip          = 0x0005
kBootImageTypeVal_PlainSignedKeyStore  = 0x8001
kBootImageTypeVal_CryptoSignedKeyStore = 0x8003

kBootImageOffset_NOR_SD_EEPROM = 0x1000
