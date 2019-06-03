import sys, os

kUartSpeed_Blhost = ['115200', '57600', '19200', '9600', '4800']
kUartSpeed_Sdphost = ['115200']

kBootDeviceMemId_QuadspiNor   = 0x1
kBootDeviceMemId_SemcNor      = 0x8
kBootDeviceMemId_FlexspiNor   = 0x9
kBootDeviceMemId_SpifiNor     = 0xa
kBootDeviceMemId_SemcNand     = 0x100
kBootDeviceMemId_FlexspiNand  = 0x101
kBootDeviceMemId_SpiNor       = 0x110
kBootDeviceMemId_UsdhcSd      = 0x120
kBootDeviceMemId_UsdhcMmc     = 0x121

#----------------FlexSPI NOR---------------------
kFlexspiNorCfgTag_Flexspi = 0x42464346  # 'FCFB'

kFlexspiNorCfgInfo_StartAddr = 0x0
kFlexspiNorCfgInfo_Length    = 0x400
kFlexspiNorCfgInfo_Notify    = 0xF000000F

kXspiNorCfgInfo_StartAddr    = 0x400
kXspiNorCfgInfo_Length       = 0x400

kFlexspiNorCfgOffset_FlexspiTag     = 0x000
kFlexspiNorCfgOffset_PageByteSize   = 0x1c0
kFlexspiNorCfgOffset_SectorByteSize = 0x1c4
kFlexspiNorCfgOffset_BlockByteSize  = 0x1d0
