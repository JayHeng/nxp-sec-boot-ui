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

efusemapIndexDict_RT10yy = {'kEfuseIndex_START' :0x0,

                            'kEfuseIndex_LOCK' :0x0,

                            'kEfuseIndex_TESTER0' :0x1,
                            'kEfuseIndex_TESTER1' :0x2,
                            'kEfuseIndex_TESTER2' :0x3,
                            'kEfuseIndex_TESTER3' :0x4,
                            'kEfuseLocation_SecConfig0' :0x4,

                            'kEfuseIndex_BOOT_CFG0' :0x5,
                            'kEfuseIndex_BOOT_CFG1' :0x6,
                            'kEfuseLocation_SecConfig1' :0x6,
                            'kEfuseLocation_BtFuseSel' :0x6,
                            'kEfuseLocation_HwCryptoKeySel' :0x6,
                            'kEfuseIndex_BOOT_CFG2' :0x7,

                            'kEfuseIndex_OTPMK0' :0x10,
                            'kEfuseIndex_OTPMK1' :0x11,
                            'kEfuseIndex_OTPMK2' :0x12,
                            'kEfuseIndex_OTPMK3' :0x13,
                            'kEfuseIndex_OTPMK4' :0x14,
                            'kEfuseIndex_OTPMK5' :0x15,
                            'kEfuseIndex_OTPMK6' :0x16,
                            'kEfuseIndex_OTPMK7' :0x17,

                            'kEfuseIndex_SRK0' :0x18,
                            'kEfuseIndex_SRK1' :0x19,
                            'kEfuseIndex_SRK2' :0x1A,
                            'kEfuseIndex_SRK3' :0x1B,
                            'kEfuseIndex_SRK4' :0x1C,
                            'kEfuseIndex_SRK5' :0x1D,
                            'kEfuseIndex_SRK6' :0x1E,
                            'kEfuseIndex_SRK7' :0x1F,

                            'kEfuseIndex_OTFAD_KEY' :0x22,
                            'kEfuseIndex_OTFAD_CFG' :0x23,
                            'kEfuseLocation_OtfadEnable' :0x23,

                            'kEfuseIndex_SW_GP2_0' :0x29,
                            'kEfuseIndex_SW_GP2_1' :0x2A,
                            'kEfuseIndex_SW_GP2_2' :0x2B,
                            'kEfuseIndex_SW_GP2_3' :0x2C,

                            'kEfuseIndex_MISC_CONF0' :0x2D,
                            'kEfuseLocation_LpspiCfg' :0x2D,
                            'kEfuseIndex_MISC_CONF1' :0x2E,
                            'kEfuseLocation_SemcNandCfg' :0x2E,

                            'kEfuseIndex_GP4_0' :0x3C,
                            'kEfuseIndex_GP4_1' :0x3D,
                            'kEfuseIndex_GP4_2' :0x3E,
                            'kEfuseIndex_GP4_3' :0x3F,
                            }
