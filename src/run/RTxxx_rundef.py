import sys, os

kActionFrom_AllInOne = 0x0
kActionFrom_BurnOtp = 0x1

kBootDeviceMemBase_FlexspiNor     = 0x08000000
kBootDeviceMemBase_FlexcommSpiNor = 0x0
kBootDeviceMemBase_UsdhcSd        = 0x0
kBootDeviceMemBase_UsdhcMmc       = 0x0

kBootDeviceMemXipSize_FlexspiNor   = 0x08000000 #128MB
kBootDeviceMemXipSize_QuadspiNor   = 0x08000000 #128MB

kRamFreeSpaceStart_LoadCommOpt        = 0x0010c000
kRamFreeSpaceStart_LoadCfgBlock       = 0x0010d000
