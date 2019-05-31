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
