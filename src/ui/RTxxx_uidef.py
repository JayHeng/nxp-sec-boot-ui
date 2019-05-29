import wx
import sys, os

kConnectStep_Fast   = 2
kConnectStep_Normal = 1

kMcuDevice_iMXRT500  = 'i.MXRT5xx'
kMcuDevice_iMXRT500S = 'i.MXRT5xxS'
kMcuDevice_iMXRT600  = 'i.MXRT6xx'
kMcuDevice_iMXRT600S = 'i.MXRT6xxS'

kMcuDevice_v2_0_0 = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600]
kMcuDevice_Latest = kMcuDevice_v2_0_0

kBootDevice_FlexspiNor     = 'FLEXSPI NOR'
kBootDevice_QuadspiNor     = 'QUADSPI NOR'
kBootDevice_UsdhcSd        = 'uSDHC SD'
kBootDevice_UsdhcMmc       = 'uSDHC MMC'
kBootDevice_FlexcommSpiNor = 'FLEXCOMM SPI NOR/EEPROM'

kBootDevice_v2_0_0 = [kBootDevice_FlexspiNor]
kBootDevice_Latest = kBootDevice_v2_0_0
