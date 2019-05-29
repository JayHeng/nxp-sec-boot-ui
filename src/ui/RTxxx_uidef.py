import wx
import sys, os

kMcuDevice_iMXRT500  = 'i.MXRT595'
kMcuDevice_iMXRT500S = 'i.MXRT595S'
kMcuDevice_iMXRT600  = 'i.MXRT685'
kMcuDevice_iMXRT600S = 'i.MXRT685S'

kMcuDevice_v2_0_0 = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600]
kMcuDevice_Latest = kMcuDevice_v2_0_0

kBootDevice_FlexspiNor     = 'FLEXSPI NOR'
kBootDevice_QuadspiNor     = 'QUADSPI NOR'
kBootDevice_UsdhcSd        = 'uSDHC SD'
kBootDevice_UsdhcMmc       = 'uSDHC MMC'
kBootDevice_FlexcommSpiNor = 'FLEXCOMM SPI NOR/EEPROM'

kBootDevice_v2_0_0 = [kBootDevice_FlexspiNor]
kBootDevice_Latest = kBootDevice_v2_0_0
