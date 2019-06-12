import wx
import sys, os

kEfuseFieldColor_Valid  = wx.Colour( 141, 180, 226 )

efuse_temp_reserved1 = {'Reserved':['x - N/A']}
efuse_temp_reserved2 = {'Reserved':['xx - N/A']}
efuse_temp_reserved3 = {'Reserved':['xxx - N/A']}
efuse_temp_reserved4 = {'Reserved':['xxxx - N/A']}
efuse_temp_reserved5 = {'Reserved':['xxxxx - N/A']}
efuse_temp_reserved6 = {'Reserved':['xxxxxx - N/A']}
efuse_temp_reserved7 = {'Reserved':['xxxxxxx - N/A']}
efuse_temp_reserved8 = {'Reserved':['xxxxxxxx - N/A']}

efuse_0x6d0_flexramPartion128KB = {'Default_FlexRAM_Partion':['0000 -  32KB ITCM,  32KB DTCM,  64KB OCRAM',
                                                              '0001 -  32KB ITCM,  64KB DTCM,  32KB OCRAM',
                                                              '0010 -   0KB ITCM,  64KB DTCM,  64KB OCRAM',
                                                              '0011 -  16KB ITCM,  64KB DTCM,  48KB OCRAM',
                                                              '0100 -  64KB ITCM,  32KB DTCM,  32KB OCRAM',
                                                              '0101 -   0KB ITCM,  96KB DTCM,  32KB OCRAM',
                                                              '0110 -  16KB ITCM,  32KB DTCM,  80KB OCRAM',
                                                              '0111 -   0KB ITCM,  32KB DTCM,  96KB OCRAM',
                                                              '1000 -  32KB ITCM,  16KB DTCM,  80KB OCRAM',
                                                              '1001 -  64KB ITCM,  16KB DTCM,  48KB OCRAM',
                                                              '1010 -  80KB ITCM,  16KB DTCM,  32KB OCRAM',
                                                              '1011 -   0KB ITCM,  16KB DTCM, 112KB OCRAM',
                                                              '1100 -  64KB ITCM,   0KB DTCM,  64KB OCRAM',
                                                              '1101 -  16KB ITCM,  16KB DTCM,  96KB OCRAM',
                                                              '1110 -  96KB ITCM,   0KB DTCM,  32KB OCRAM',
                                                              '1111 -   0KB ITCM,   0KB DTCM, 128KB OCRAM',
                                                             ]}

efuse_0x6d0_flexramPartion256KB = {'Default_FlexRAM_Partion':['0000 -  64KB ITCM,  64KB DTCM,  128KB OCRAM',
                                                              '0001 -  64KB ITCM, 128KB DTCM,  64KB OCRAM',
                                                              '0010 -   0KB ITCM, 128KB DTCM, 128KB OCRAM',
                                                              '0011 -  32KB ITCM, 128KB DTCM,  96KB OCRAM',
                                                              '0100 - 128KB ITCM,  64KB DTCM,  64KB OCRAM',
                                                              '0101 -   0KB ITCM, 192KB DTCM,  64KB OCRAM',
                                                              '0110 -  32KB ITCM,  64KB DTCM, 160KB OCRAM',
                                                              '0111 -   0KB ITCM,  64KB DTCM, 192KB OCRAM',
                                                              '1000 -  64KB ITCM,  32KB DTCM, 160KB OCRAM',
                                                              '1001 - 128KB ITCM,  32KB DTCM,  96KB OCRAM',
                                                              '1010 - 160KB ITCM,  32KB DTCM,  64KB OCRAM',
                                                              '1011 -   0KB ITCM,  32KB DTCM, 224KB OCRAM',
                                                              '1100 - 128KB ITCM,   0KB DTCM, 128KB OCRAM',
                                                              '1101 -  32KB ITCM,  32KB DTCM, 192KB OCRAM',
                                                              '1110 - 192KB ITCM,   0KB DTCM,  64KB OCRAM',
                                                              '1111 -   0KB ITCM,   0KB DTCM, 256KB OCRAM',
                                                             ]}

efuse_0x6d0_flexramPartion512KB = {'Default_FlexRAM_Partion':['0000 - 128KB ITCM, 128KB DTCM, 256KB OCRAM',
                                                              '0001 -  64KB ITCM, 128KB DTCM, 320KB OCRAM',
                                                              '0010 - 256KB ITCM, 128KB DTCM, 128KB OCRAM',
                                                              '0011 -  32KB ITCM, 128KB DTCM, 352KB OCRAM',
                                                              '0100 - 128KB ITCM,  64KB DTCM, 320KB OCRAM',
                                                              '0101 -  64KB ITCM,  64KB DTCM, 384KB OCRAM',
                                                              '0110 - 256KB ITCM,  64KB DTCM, 192KB OCRAM',
                                                              '0111 - 442KB ITCM,   0KB DTCM,  64KB OCRAM',
                                                              '1000 - 128KB ITCM, 256KB DTCM, 128KB OCRAM',
                                                              '1001 -  64KB ITCM, 256KB DTCM, 192KB OCRAM',
                                                              '1010 - 256KB ITCM, 192KB DTCM,  64KB OCRAM',
                                                              '1011 -   0KB ITCM, 448KB DTCM,  64KB OCRAM',
                                                              '1100 - 128KB ITCM,   0KB DTCM, 384KB OCRAM',
                                                              '1101 -  32KB ITCM,  32KB DTCM, 448KB OCRAM',
                                                              '1110 - 256KB ITCM,   0KB DTCM, 256KB OCRAM',
                                                              '1111 -   0KB ITCM,   0KB DTCM, 512KB OCRAM',
                                                             ]}

