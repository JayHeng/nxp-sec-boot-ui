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

efuse_0xc70_flexramPartion512KB = {'Default_FlexRAM_Partion':['000000 - 256KB ITCM, 256KB DTCM,   0KB OCRAM',
                                                              '000001 - 320KB ITCM, 192KB DTCM,   0KB OCRAM',
                                                              '000010 - 384KB ITCM, 128KB DTCM,   0KB OCRAM',
                                                              '000011 - 448KB ITCM,  64KB DTCM,   0KB OCRAM',
                                                              '000100 - 512KB ITCM,   0KB DTCM,   0KB OCRAM',
                                                              '000101 - 192KB ITCM, 320KB DTCM,   0KB OCRAM',
                                                              '000110 - 128KB ITCM, 384KB DTCM,   0KB OCRAM',
                                                              '000111 -  64KB ITCM, 448KB DTCM,   0KB OCRAM',
                                                              '001000 -   0KB ITCM, 512KB DTCM,   0KB OCRAM',
                                                              '001001 - 256KB ITCM, 192KB DTCM,  64KB OCRAM',
                                                              '001010 - 320KB ITCM, 128KB DTCM,  64KB OCRAM',
                                                              '001011 - 384KB ITCM,  64KB DTCM,  64KB OCRAM',
                                                              '001100 - 448KB ITCM,   0KB DTCM,  64KB OCRAM',
                                                              '001101 - 192KB ITCM, 256KB DTCM,  64KB OCRAM',
                                                              '001110 - 128KB ITCM, 320KB DTCM,  64KB OCRAM',
                                                              '001111 -  64KB ITCM, 384KB DTCM,  64KB OCRAM',
                                                              '010000 -   0KB ITCM, 448KB DTCM,  64KB OCRAM',
                                                             ]}

efusemapIndexDict_RT10yy = {'kEfuseIndex_START' :0x0,

                            'kEfuseIndex_LOCK'  :0x0,
                            'kEfuseIndex_LOCK2' :None,

                            'kEfuseIndex_TESTER0' :0x1,
                            'kEfuseIndex_TESTER1' :0x2,
                            'kEfuseIndex_TESTER2' :0x3,
                            'kEfuseIndex_TESTER3' :0x4,
                            'kEfuseLocation_SecConfig0' :0x4,

                            'kEfuseIndex_BOOT_CFG0' :0x5,
                            'kEfuseIndex_BOOT_CFG1' :0x6,
                            'kEfuseLocation_SecConfig1'     :0x6,
                            'kEfuseLocation_BtFuseSel'      :0x6,
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
                            'kEfuseLocation_LpspiCfg'    :0x2D,
                            'kEfuseIndex_MISC_CONF1' :0x2E,
                            'kEfuseLocation_SemcNandCfg' :0x2E,

                            'kEfuseIndex_GP4_0' :0x3C,
                            'kEfuseIndex_GP4_1' :0x3D,
                            'kEfuseIndex_GP4_2' :0x3E,
                            'kEfuseIndex_GP4_3' :0x3F,

                            'kEfuseEntryModeRegion0IndexStart' :0x01,
                            'kEfuseEntryModeRegion0IndexEnd'   :0x02,
                            'kEfuseEntryModeRegion1IndexStart' :0x05,
                            'kEfuseEntryModeRegion1IndexEnd'   :0x07,
                            'kEfuseEntryModeRegion2IndexStart' :0x18,
                            'kEfuseEntryModeRegion2IndexEnd'   :0x1F,
                            'kEfuseEntryModeRegion3IndexStart' :0x29,
                            'kEfuseEntryModeRegion3IndexEnd'   :0x2E,
                            'kEfuseEntryModeRegion4IndexStart' :0x4C,
                            'kEfuseEntryModeRegion4IndexEnd'   :0x4F,
                            'kEfuseEntryModeRegion5IndexStart' :None,
                            'kEfuseEntryModeRegion5IndexEnd'   :None,
                            }

efusemapDefnDict_RT10yy = {
                           'kEfuseMask_HwCryptoKey0Sel' :0x00003000,
                           'kEfuseMask_HwCryptoKey1Sel' :0x0000C000,
                           'kEfuseShift_HwCryptoKey0Sel' :12,
                           'kEfuseShift_HwCryptoKey1Sel' :14,

                           'kEfuseMask_OtfadKeyScrambleAlign'   :0x000000FF,
                           'kEfuseShift_OtfadKeyScrambleAlign'  :0,
                           'kEfuseMask_OtfadEnable'             :0x00000100,
                           'kEfuseShift_OtfadEnable'            :8,
                           'kEfuseMask_OtfadKeyblobEnable'      :0x00000200,
                           'kEfuseShift_OtfadKeyblobEnable'     :9,
                           'kEfuseMask_OtfadKeyScrambleEnable'  :0x00000400,
                           'kEfuseShift_OtfadKeyScrambleEnable' :10,
                           'kEfuseMask_OtfadKeyblobCrcEnable'   :0x00001000,
                           'kEfuseShift_OtfadKeyblobCrcEnable'  :12,

                           'kEfuseMask_SecConfig0'   :0x00000002,
                           'kEfuseMask_SecConfig1'   :0x00000002,
                           'kEfuseShift_SecConfig0'  :1,
                           'kEfuseShift_SecConfig1'  :1,

                           'kEfuseMask_BtFuseSel'    :0x00000010,
                           'kEfuseShift_BtFuseSel'   :4,

                           'kEfuseMask_DefaultFlexramPart'    :0x000F0000,
                           'kEfuseShift_DefaultFlexramPart'   :16,
                           'kEfuseMask_EepromEnable'          :0x01000000,
                           'kEfuseShift_EepromEnable'         :24,
                           'kEfuseMask_LpspiIndex'            :0x06000000,
                           'kEfuseShift_LpspiIndex'           :25,
                           'kEfuseMask_SpiAddressing'         :0x08000000,
                           'kEfuseShift_SpiAddressing'        :27,
                           'kEfuseMask_LpspiSpeed'            :0x30000000,
                           'kEfuseShift_LpspiSpeed'           :28,

                           'kEfuseMask_RawNandPortSize'   :0x00000008,
                           'kEfuseShift_RawNandPortSize'  :3,
                           'kEfuseMask_RawNandEccEdoSet'  :0x00000010,
                           'kEfuseShift_RawNandEccEdoSet' :4,
                           'kEfuseMask_RawNandEccStatus'  :0x01000000,
                           'kEfuseShift_RawNandEccStatus' :24,
                            }

efusemapIndexDict_RT11yy = {'kEfuseIndex_START' :0x0,

                            'kEfuseIndex_LOCK'  :0x8,
                            'kEfuseIndex_LOCK2' :0x9,

                            'kEfuseLocation_SecConfig0'     :0xE,
                            'kEfuseLocation_SecConfig1'     :0x16,
                            'kEfuseLocation_BtFuseSel'      :0x16,

                            'kEfuseLocation_HwCryptoKeySel'     :0xE,
                            'kEfuseIndex_OTFAD_CFG'   :0x47,
                            'kEfuseLocation_OtfadEnable'        :0x47,
                            'kEfuseLocation_LpspiCfg'           :0x47,
                            'kEfuseIndex_OTFAD_KEY'   :0x84,

                            'kEfuseLocation_SemcNandCfg'        :0x48,

                            'kEfuseIndex_USER_KEY5_0' :0x80,
                            'kEfuseIndex_USER_KEY5_1' :0x81,
                            'kEfuseIndex_USER_KEY5_2' :0x82,
                            'kEfuseIndex_USER_KEY5_3' :0x83,

                            'kEfuseEntryModeRegion0IndexStart' :0x10,
                            'kEfuseEntryModeRegion0IndexEnd'   :0x1B,
                            'kEfuseEntryModeRegion1IndexStart' :0x2E,
                            'kEfuseEntryModeRegion1IndexEnd'   :0x2E,
                            'kEfuseEntryModeRegion2IndexStart' :0x30,
                            'kEfuseEntryModeRegion2IndexEnd'   :0x3F,
                            'kEfuseEntryModeRegion3IndexStart' :0x47,
                            'kEfuseEntryModeRegion3IndexEnd'   :0x4A,
                            'kEfuseEntryModeRegion4IndexStart' :0x60,
                            'kEfuseEntryModeRegion4IndexEnd'   :0x87,
                            'kEfuseEntryModeRegion5IndexStart' :0xB0,
                            'kEfuseEntryModeRegion5IndexEnd'   :0x10F,
                            }

efusemapDefnDict_RT11yy = {
                           'kEfuseMask_HwCryptoKey0Sel' :0x00000010,
                           'kEfuseMask_HwCryptoKey1Sel' :0x00000040,
                           'kEfuseShift_HwCryptoKey0Sel' :4,
                           'kEfuseShift_HwCryptoKey1Sel' :6,

                           'kEfuseMask_OtfadKeyScrambleEnable'  :0x00000001,
                           'kEfuseShift_OtfadKeyScrambleEnable' :0,
                           'kEfuseMask_OtfadKeyblobEnable'      :0x00000002,
                           'kEfuseShift_OtfadKeyblobEnable'     :1,
                           'kEfuseMask_OtfadKeyblobCrcEnable'   :0x00000008,
                           'kEfuseShift_OtfadKeyblobCrcEnable'  :3,
                           'kEfuseMask_Otfad2KeyScrambleEnable' :0x00000010,
                           'kEfuseShift_Otfad2KeyScrambleEnable':4,
                           'kEfuseMask_Otfad2KeyblobEnable'     :0x00000020,
                           'kEfuseShift_Otfad2KeyblobEnable'    :5,
                           'kEfuseMask_Otfad2KeyblobCrcEnable'  :0x00000080,
                           'kEfuseShift_Otfad2KeyblobCrcEnable' :7,

                           'kEfuseMask_SecConfig0'   :0x00000002,
                           'kEfuseMask_SecConfig1'   :0x00000002,
                           'kEfuseShift_SecConfig0'  :1,
                           'kEfuseShift_SecConfig1'  :1,

                           'kEfuseMask_BtFuseSel'    :0x00000010,
                           'kEfuseShift_BtFuseSel'   :4,

                           'kEfuseMask_DefaultFlexramPart'    :0x003F0000,
                           'kEfuseShift_DefaultFlexramPart'   :16,
                           'kEfuseMask_EepromEnable'          :0x01000000,
                           'kEfuseShift_EepromEnable'         :24,
                           'kEfuseMask_LpspiIndex'            :0x06000000,
                           'kEfuseShift_LpspiIndex'           :25,
                           'kEfuseMask_SpiAddressing'         :0x00000000,  # Tricky
                           'kEfuseShift_SpiAddressing'        :None,
                           'kEfuseMask_LpspiSpeed'            :0x18000000,
                           'kEfuseShift_LpspiSpeed'           :27,

                           'kEfuseMask_RawNandPortSize'   :0x00000008,
                           'kEfuseShift_RawNandPortSize'  :3,
                           'kEfuseMask_RawNandEccEdoSet'  :0x00000010,
                           'kEfuseShift_RawNandEccEdoSet' :4,
                           'kEfuseMask_RawNandEccStatus'  :0x01000000,
                           'kEfuseShift_RawNandEccStatus' :24,
                            }
