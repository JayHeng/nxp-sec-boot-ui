#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

kLanguageIndex_English = 0x0
kLanguageIndex_Chinese = 0x1

kMenuPosition_File     = 0x0
kMenuPosition_Edit     = 0x1
kMenuPosition_View     = 0x2
kMenuPosition_Tools    = 0x3
kMenuPosition_Window   = 0x4
kMenuPosition_Help     = 0x5

kPanelIndex_GenSeq   = 0x0
kPanelIndex_LoadSeq  = 0x1
kPanelIndex_fuseUtil = 0x2
kPanelIndex_memView  = 0x3

kMainLanguageContentDict = {
        'menu_file':                          ['File',                                  u"文件"],
        'mItem_exit':                         ['Exit',                                  u"退出"],
        'menu_edit':                          ['Edit',                                  u"编辑"],
        'menu_view':                          ['View',                                  u"查看"],
        'menu_tools':                         ['Tools',                                 u"工具"],
        'subMenu_runMode':                    ['Run Mode',                              u"软件运行模式"],
        'mItem_runModeEntry':                 ['Entry',                                 u"入门级"],
        'mItem_runModeMaster':                ['Master',                                u"专家级"],
        'subMenu_usbDetection':               ['USB Detection',                         u"USB识别模式"],
        'mItem_usbDetectionDynamic':          ['Dynamic',                               u"动态"],
        'mItem_usbDetectionStatic':           ['Static',                                u"静态"],
        'subMenu_soundEffect':                ['Sound Effect',                          u"音效模式"],
        'mItem_soundEffectMario':             ['Mario',                                 u"马里奥"],
        'mItem_soundEffectQuiet':             ['Quiet',                                 u"静音"],
        'subMenu_genSbFile':                  ['Generate .sb file',                     u"生成.sb文件"],
        'mItem_genSbFileYes':                 ['Yes',                                   u"是"],
        'mItem_genSbFileNo':                  ['No',                                    u"否"],
        'subMenu_imageReadback':              ['Image Readback',                        u"程序回读"],
        'mItem_imageReadbackAutomatic':       ['Automatic',                             u"自动"],
        'mItem_imageReadbackManual':          ['Manual',                                u"手动"],
        'menu_window':                        ['Window',                                u"界面"],
        'menu_help':                          ['Help',                                  u"帮助"],
        'mItem_homePage':                     ['Home Page',                             u"项目主页"],
        'mItem_aboutAuthor':                  ['About Author',                          u"关于作者"],
        'mItem_contributors':                 ['Contributors',                          u"贡献者名单"],
        'mItem_specialThanks':                ['Special Thanks',                        u"特别感谢"],
        'mItem_revisionHistory':              ['Revision History',                      u"版本历史"],

        'panel_targetSetup':                  ['Target Setup',                          u"目标器件设置"],
        'sText_mcuSeries':                    ['MCU Series:',                           u"微控制器系列："],
        'sText_mcuDevice':                    ['MCU Device:',                           u"微控制器型号："],
        'sText_bootDevice':                   ['Boot Device:',                          u"启动设备类型："],
        'button_bootDeviceConfiguration':     ['Boot Device Configuration',             u"启动设备配置"],
        'button_deviceConfigurationData':     ['Device Configuration Data (DCD)',       u"DCD数据配置"],

        'panel_portSetup':                    ['Port Setup',                            u"下载接口设置"],
        'radioBtn_uart':                      ['UART',                                  u"串口"],
        'radioBtn_usbhid':                    ['USB-HID',                               u"HID设备"],
        'sText_comPort':                      ['COM Port:',                             u"端口号："],
        'sText_baudrate':                     ['Baudrate:',                             u"波特率："],
        'sText_vid':                          ['Vendor ID:',                            u"厂商识别号："],
        'sText_pid':                          ['Product ID:',                           u"产品识别号："],
        'checkBox_oneStepConnect':            ['One Step',                              u"一键连接"],
        'button_connect_black':               ['Connect to ROM',                        u"连接ROM"],
        'button_connect_yellow':              ['Connect to Flashloader',                u"连接Flashloader"],
        'button_connect_green':               ['Configure boot device',                 u"配置启动设备"],
        'button_connect_blue':                ['Reset device',                          u"复位微控制器"],
        'button_connect_red':                 ['Reconnect',                             u"重新连接"],

        'panel_deviceStatus':                 ['Device Status',                         u"目标器件状态"],

        'sText_secureBootType':               ['Secure Boot Type',                      u"安全启动模式："],
        'button_allInOneAction':              ['All-In-One Action',                     u"一键启动"],

        'panel_genSeq':                       ['Image Generation Sequence',             u"       生成可启动程序       "],
        'sText_serial':                       ['Serial (8 digits):',                    u"序列号（仅8位数字）："],
        'sText_keyPass':                      ['key_pass (text):',                      u"密钥因子（任意字符）："],
        'button_advCertSettings':             ['Advanced Cert Settings',                u"配置认证参数"],
        'sText_certFmt':                      ['Certificate Format:',                   u"证书格式："],
        'sText_hashAlgo':                     ['Hash Algorithm:',                       u"哈希算法："],
        'button_genCert':                     ['Generate Certificate,SRK',              u"生成证书和SRK"],
        'sText_appPath':                      ['Application Image File:',               u"源应用程序镜像文件："],
        'sText_appBaseAddr':                  ['Base Address for Raw Binary Image:',    u"程序链接起始地址（仅Bin格式）："],
        'sText_habCryptoAlgo':                ['HAB Encryption Algorithm:',             u"HAB加密算法："],
        'sText_enableCertForBee':             ['Enable Certificate for BEE Encryption:',u"是否为BEE加密添加认证："],
        'button_genImage_u':                  ['Generate Unsigned Bootable Image',      u"生成裸启动程序"],
        'button_genImage_c':                  ['Generate CRC Bootable Image',           u"生成含CRC的可启动程序"],
        'button_genImage_s':                  ['Generate Signed Bootable Image',        u"生成含签名的可启动程序"],
        'button_genImage_se':                 ['Generate Encrypted Bootable Image,DEK', u"生成签名加密的可启动程序和DEK"],
        'sText_keyStorageRegion':             ['Key Storage Region:',                   u"密钥存储区域："],
        'sText_availBeeEngines':              ['Max Available BEE Engines:',            u"最大可用BEE引擎数："],
        'button_advKeySettings':              ['Advanced Key Settings',                 u"配置密钥参数"],
        'sText_beeCryptoAlgo':                ['BEE Encryption Algorithm:',             u"BEE加密算法："],
        'sText_maxFacCnt':                    ['Max Protection Regions:',               u"最大可保护区域数："],
        'button_prepBee_p':                   ['Prepare For Encryption',                u"准备加密工作"],
        'button_prepBee_e':                   ['Encrypt Bootable Image',                u"加密可启动程序"],

        'panel_loadSeq':                      ['Image Loading Sequence',                u"       下载可启动程序       "],
        'sText_srk256bit':                    ['Burn below SRK data\n (256bits) into Fuse\n SRK0-7 Region:',                                  u"烧写如下SRK数据进\nFuse SRK0-7区域："],
        'button_progSrk':                     ['Burn SRK data',                         u"烧录SRK数据"],
        'sText_beeKeyInfo':                   ['Burn below user DEK\n data (128bits * n) into\n below Region for BEE:',                       u"烧写如下DEK进Fuse BEE\n密钥区域："],
        'button_operBee':                     ['Burn DEK data',                         u"烧录DEK数据"],
        'sText_showImage':                    ['Program final bootable image\n to boot device:',                                              u"下载最终可启动应用程序镜像\n文件进启动设备："],
        'button_flashImage_u':                ['Load Unsigned Image',                   u"下载裸程序"],
        'button_flashImage_c':                ['Load CRC Image',                        u"下载含CRC的程序"],
        'button_flashImage_s':                ['Load Signed Image',                     u"下载已签名程序"],
        'button_flashImage_e':                ['Load Encrypted Image',                  u"下载已加密程序"],
        'sText_habDek128bit':                 ['Use below DEK data (128bits)\n to generate keyblob and\n program it to flash for HAB:',       u"根据如下DEK动态生成KeyBlob\n并下载进启动设备："],
        'button_progDek':                     ['Enable HAB, Load KeyBlob Data',         u"使能HAB,下载KeyBlob数据"],

        'panel_fuseUtil':                     ['eFuse Operation Utility',               u"       专用eFuse烧写       "],
        'button_scan':                        ['Scan',                                  u"扫描"],
        'button_burn':                        ['Burn',                                  u"烧写"],

        'panel_memView':                      ['Boot Device Memory',                    u"       通用Flash编程       "],
        'sText_memStart':                     ['Start / Offset:',                       u"首地址/偏移："],
        'sText_memLength':                    ['Byte Length (For Read/Write):',         u"字节长度（回读/擦除）："],
        'sText_memBinFile':                   ['Bin File:',                             u"源文件："],
        'button_readMem':                     ['Read',                                  u"回读"],
        'button_eraseMem':                    ['Erase',                                 u"擦除"],
        'button_writeMem':                    ['Write (Auto Erase)',                    u"下载（含自动擦除）"],
        'button_executeApp':                  ['Execute From Start',                    u"从首地址处执行"],
        'button_viewMem':                     ['View Bootable Image',                   u"回读查看标注的程序"],
        'button_clearMem':                    ['Clear The Screen',                      u"清除屏幕显示"],
        'checkBox_saveImageData':             ['Save image/data file to',               u"将程序/数据保存到"],

        'panel_log':                          ['Log',                                   u"操作日志"],
        'button_clearLog':                    ['Clear',                                 u"清除"],
        'button_SaveLog':                     ['Save',                                  u"保存"],

}

kSubLanguageContentDict = {
        #cert
        'cert_title':                         ['Advanced Certificate Settings',         u"配置认证参数"],
        'panel_certOpt':                      ['Certificate Option',                    u"证书选项"],
        'sText_cstVersion':                   ['CST Version:',                          u"CST版本："],
        'sText_useExistingCaKey':             ['Use Existing CA Key:',                  u"复用已有CA密钥："],
        'sText_useEcc':                       ['Use Elliptic Curve Crypto:',            u"采用椭圆曲线加密："],
        'sText_pkiTreeKeyLen':                ['Key Length for PKI Tree (bits):',       u"PKI密钥比特长度："],
        'sText_pkiTreeDuration':              ['PKI Tree Duration (years):',            u"PKI保密时间（年）："],
        'sText_SRKs':                         ['Super Root Keys:',                      u"SRK密码组数："],
        'sText_caFlagSet':                    ['SRK Cert to have CA flag Set:',         u"证书CA标志选项："],
        'button_cert_ok':                     ['Ok',                                    u"确定"],
        'button_cert_cancel':                 ['Cancel',                                u"取消"],

        #dcd
        'dcd_title':                          ['Device Configuration Data',             u"配置DCD参数"],
        'panel_dcdOpt':                       ['DCD Option',                            u"DCD选项"],
        'sText_dcdSource':                    ['DCD Source:',                           u"DCD来源："],
        'sText_dcdBinFile':                   ['DCD bin file:',                         u"DCD bin文件："],
        'sText_dcdCfgFile':                   ['DCD cfg file:',                         u"DCD cfg文件："],
        'sText_dcdPurpose':                   ['DCD Purpose:',                          u"DCD用途："],
        'sText_sdramBase':                    ['SDRAM Base:',                           u"SDRAM基址："],
        'panel_dcdDesc':                      ['DCD Descriptor',                        u"DCD描述代码"],
        'sText_dcdModel':                     ['Device Model:',                         u"设备模型："],
        'button_dcd_ok':                      ['Ok',                                    u"确定"],
        'button_dcd_cancel':                  ['Cancel',                                u"取消"],

        #flexspinor/quadspinor
        'flexspinor_title':                   ['FlexSPI NOR Device Configuration',      u"配置FlexSPI接口NOR Flash启动设备"],
        'quadspinor_title':                   ['QuadSPI NOR Device Configuration',      u"配置QuadSPI接口NOR Flash启动设备"],
        'sText_deviceModel':                  ['Use Typical Device Model:',             u"使用典型设备型号："],
        'panel_norOpt0':                      ['Nor Option0',                           u"NOR选项0"],
        'sText_deviceType':                   ['Device Type:',                          u"设备类型："],
        'sText_queryPads':                    ['Query Pads:',                           u"查询管脚数："],
        'sText_cmdPads':                      ['Cmd Pads:',                             u"命令管脚数："],
        'sText_quadModeSetting':              ['Quad Mode Setting:',                    u"四路模式设置："],
        'sText_miscMode':                     ['Misc Mode:',                            u"Misc模式："],
        'sText_maxFrequency':                 ['Max Frequency:',                        u"最大频率："],
        'sText_hasOption1':                   ['Has Option1:',                          u"是否有NOR选项1："],
        'panel_norOpt1':                      ['Nor Option1',                           u"NOR选项1"],
        'sText_flashConnection':              ['Flash Connection:',                     u"Flash连接方式："],
        'sText_driveStrength':                ['Drive Strength:',                       u"Pin驱动强度："],
        'sText_dqsPinmuxGroup':               ['DQS Pinmux Group:',                     u"DQS Pinmux组："],
        'sText_enableSecondPinmux':           ['Enable Second Pinmux:',                 u"使能第二组Pinmux："],
        'sText_statusOverride':               ['Status Override:',                      u"状态位覆盖："],
        'sText_dummyCycles':                  ['Dummy Cycles:',                         u"冗余周期数："],
        'button_flexspinor_ok':               ['Ok',                                    u"确定"],
        'button_flexspinor_cancel':           ['Cancel',                                u"取消"],

        #lpspinor
        'lpspinor_title':                     ['LPSPI NOR/EEPROM Device Configuration', u"配置LPSPI接口NOR/EEPROM启动设备"],
        'panel_memOpt':                       ['Memory Option',                         u"存储器选项"],
        'sText_deviceType':                   ['Device Type:',                          u"设备类型："],
        'sText_pageSize':                     ['Page Size (Bytes):',                    u"页大小(B)："],
        'sText_sectorSize':                   ['Sector Size (KBytes):',                 u"扇区大小（KB）："],
        'sText_totalSize':                    ['Total Size (KBytes):',                  u"总容量（KB）："],
        'panel_spiOpt':                       ['Spi Option',                            u"SPI选项"],
        'sText_spiIndex':                     ['Spi Index:',                            u"Spi编号："],
        'sText_spiPcs':                       ['Spi Pcs:',                              u"Spi片选："],
        'sText_spiSpeed':                     ['Spi Speed:',                            u"Spi速度："],
        'button_lpspinor_ok':                 ['Ok',                                    u"确定"],
        'button_lpspinor_cancel':             ['Cancel',                                u"取消"],

        #semcnand
        'semcnand_title':                     ['SEMC NAND Device Configuration',        u"配置SEMC接口NAND Flash启动设备"],
        'panel_nandOpt':                      ['Nand Option',                           u"Nand选项"],
        'sText_onfiVersion':                  ['ONFI Version:',                         u"ONFI版本："],
        'sText_onfiTimingMode':               ['ONFI Timing Mode:',                     u"ONFI速度模式："],
        'sText_edoMode':                      ['EDO Mode:',                             u"EDO模式："],
        'sText_ioPortSize':                   ['I/O Port Size:',                        u"I/O端口宽度："],
        'sText_pcsPort':                      ['PCS Port:',                             u"片选端口："],
        'sText_eccType':                      ['ECC Type:',                             u"ECC类型："],
        'sText_eccStatus':                    ['Initial ECC status:',                   u"初始ECC状态："],
        'panel_fcbOpt':                       ['FCB Option',                            u"FCB选项"],
        'sText_searchCount':                  ['Search Count:',                         u"搜索次数："],
        'sText_searchStride':                 ['Search Stride:',                        u"搜索步长："],
        'sText_imageCopies':                  ['Image Copies:',                         u"程序总备份数："],
        'panel_imageInfo':                    ['Image Info',                            u"程序信息"],
        'sText_blockIndex':                   ['Block Index:',                          u"所在块索引："],
        'sText_blockCount':                   ['Block Count:',                          u"所占块个数："],
        'button_semcnand_ok':                 ['Ok',                                    u"确定"],
        'button_semcnand_cancel':             ['Cancel',                                u"取消"],

        #usdhcsd
        'usdhcsd_title':                      ['uSDHC SD Device Configuration',         u"配置uSDHC接口SD卡启动设备"],
        'panel_sdOpt':                        ['SD Option',                             u"SD卡选项"],
        'sText_busWidth':                     ['Bus Width:',                            u"总线宽度："],
        'sText_timingInterface':              ['Timing Interface:',                     u"总线时序模式："],
        'sText_enablePowerCycle':             ['Enable Power Cycle:',                   u"使能供电时序："],
        'sText_powerPolarity':                ['Power Polarity:',                       u"供电极性"],
        'sText_powerUpTime':                  ['Power Up Time:',                        u"上电时间："],
        'sText_powerDownTime':                ['Power Down Time:',                      u"掉电时间："],
        'button_usdhcsd_ok':                  ['Ok',                                    u"确定"],
        'button_usdhcsd_cancel':              ['Cancel',                                u"取消"],

        #usdhcmmc
        'usdhcmmc_title':                     ['uSDHC (e)MMC Device Configuration',     u"配置uSDHC接口MMC卡启动设备"],
        'panel_mmcOpt0':                      ['MMC Option0',                           u"MMC卡选项0"],
        'sText_partitionAccess':              ['Partition Access:',                     u"分割访问权限："],
        'sText_enableBootConfig':             ['Enable Boot Config:',                   u"使能启动配置："],
        'sText_bootBusWidth':                 ['Boot Bus Width:',                       u"启动总线宽度："],
        'sText_bootMode':                     ['Boot Mode:',                            u"启动模式："],
        'sText_enableBootPartition':          ['Enable Boot Partition:',                u"使能启动分割："],
        'sText_enableBootAck':                ['Enable Boot Ack:',                      u"使能启动确认："],
        'sText_resetBootBusConditions':       ['Reset Boot Bus Conditions:',            u"复位启动总线条件："],
        'panel_mmcOpt1':                      ['MMC Option1',                           u"MMC卡选项1"],
        'sText_enable1V8':                    ['Enable 1.8V:',                          u"使能1.8V："],
        'button_usdhcmmc_ok':                 ['Ok',                                    u"确定"],
        'button_usdhcmmc_cancel':             ['Cancel',                                u"取消"],

        #otpmk
        'otpmkKey_title':                     ['Advanced Key Settings - Fixed OTPMK',   u"配置预设OTPMK密钥参数"],
        'panel_encryptionOpt':                ['Encryption Option',                     u"加密选项"],
        'sText_keySource':                    ['Key Source:',                           u"密钥源："],
        'sText_aesMode':                      ['AES Mode:',                             u"AES模式："],
        'sText_regionCnt':                    ['Region Count:',                         u"加密区域总数："],
        'panel_regionInfo':                   ['Encrypted Region Info',                 u"加密区域信息"],
        'sText_regionStart':                  ['Region Start:',                         u"区域首地址："],
        'sText_regionLength':                 ['Region Length:',                        u"区域长度："],
        'button_otpmkkey_ok':                 ['Ok',                                    u"确定"],
        'button_otpmkkey_cancel':             ['Cancel',                                u"取消"],

        #user key
        'userKey_title':                      ['Advanced Key Settings - Flexible User', u"配置灵活用户密钥参数"],
        'panel_encryptionOpt':                ['Encryption Option',                     u"加密选项"],
        'sText_engineSel':                    ['Engine Selection:',                     u"引擎选择："],
        'sText_beeEngKeySel':                 ['BEE Engine Key Selection:',             u"BEE引擎密钥选择："],
        'sText_imageType':                    ['Image Type:',                           u"程序类型："],
        'sText_xipBaseAddr':                  ['XIP Base Address:',                     u"XIP基址："],
        'panel_engine0Info':                  ['BEE Engine 0 Info',                     u"BEE引擎0信息"],
        'sText_engine0keySource':             ['Key Source:',                           u"密钥源："],
        'sText_engine0UserKeyData':           ['User Key Data:',                        u"用户密钥："],
        'sText_engine0AesMode':               ['AES Mode:',                             u"AES模式："],
        'sText_engine0FacCnt':                ['Protected Region Count:',               u"受保护区域个数："],
        'sText_engine0Fac0Start':             ['Protected Region 0 Start:',             u"受保护区域0首地址："],
        'sText_engine0Fac0Length':            ['Protected Region 0 Length:',            u"受保护区域0长度："],
        'sText_engine0Fac1Start':             ['Protected Region 1 Start:',             u"受保护区域1首地址："],
        'sText_engine0Fac1Length':            ['Protected Region 1 Length:',            u"受保护区域1长度："],
        'sText_engine0Fac2Start':             ['Protected Region 2 Start:',             u"受保护区域2首地址："],
        'sText_engine0Fac2Length':            ['Protected Region 2 Length:',            u"受保护区域2长度："],
        'sText_engine0AccessPermision':       ['Access Permision:',                     u"访问权限："],
        'sText_engine0Lock':                  ['Region Lock:',                          u"区域锁定："],
        'panel_engine1Info':                  ['BEE Engine 1 Info',                     u"BEE引擎1信息"],
        'sText_engine1keySource':             ['Key Source:',                           u"密钥源："],
        'sText_engine1UserKeyData':           ['User Key Data:',                        u"用户密钥："],
        'sText_engine1AesMode':               ['AES Mode:',                             u"AES模式："],
        'sText_engine1FacCnt':                ['Protected Region Count:',               u"受保护区域个数："],
        'sText_engine1Fac0Start':             ['Protected Region 0 Start:',             u"受保护区域0首地址："],
        'sText_engine1Fac0Length':            ['Protected Region 0 Length:',            u"受保护区域0长度："],
        'sText_engine1Fac1Start':             ['Protected Region 1 Start:',             u"受保护区域1首地址："],
        'sText_engine1Fac1Length':            ['Protected Region 1 Length:',            u"受保护区域1长度："],
        'sText_engine1Fac2Start':             ['Protected Region 2 Start:',             u"受保护区域2首地址："],
        'sText_engine1Fac2Length':            ['Protected Region 2 Length:',            u"受保护区域2长度："],
        'sText_engine1AccessPermision':       ['Access Permision:',                     u"访问权限："],
        'sText_engine1Lock':                  ['Region Lock:',                          u"区域锁定："],
        'button_userkeys_genRandomKey':       ['Generate Random User Key',              u"产生随机密钥"],
        'button_userkeys_ok':                 ['Ok',                                    u"确定"],
        'button_userkeys_cancel':             ['Cancel',                                u"取消"],
}

kRevision_1_0_0_en =  "【v1.0.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT1021, i.MXRT1051/1052, i.MXRT1061/1062, i.MXRT1064 SIP \n" + \
                      "     2. Support both UART and USB-HID serial downloader modes \n" + \
                      "     3. Support various user application image file formats (elf/axf/srec/hex/bin) \n" + \
                      "     4. Can validate the range and applicability of user application image \n" + \
                      "     5. Support for converting bare image into bootable image \n" + \
                      "     6. Support for loading bootable image into FlexSPI NOR and SEMC NAND boot devices \n" + \
                      "     7. Support for loading bootable image into LPSPI NOR/EEPROM recovery boot device \n" + \
                      "     8. Support DCD which can help load image to SDRAM \n" + \
                      "     9. Support development boot case (Unsigned) \n" + \
                      "    10. Support HAB encryption secure boot case (Signed only, Signed and Encrypted) \n" + \
                      "    11. Can back up certificate with time stamp \n" + \
                      "    12. Support BEE encryption secure boot case (SNVS Key, User Keys) \n" + \
                      "    13. Support common eFuse memory operation \n" + \
                      "    14. Support common boot device memory operation \n" + \
                      "    15. Support for reading back and marking bootable image(NFCB/DBBT/FDCB/EKIB/EPRDB/IVT/Boot Data/DCD/Image/CSF/DEK KeyBlob) from boot device \n\n"
kRevision_1_0_0_zh = u"【v1.0.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持i.MXRT全系列MCU，包含i.MXRT1021、i.MXRT1051/1052、i.MXRT1061/1062、i.MXRT1064 SIP \n" + \
                     u"     2. 支持UART和USB-HID两种串行下载方式（COM端口/USB设备自动识别） \n" + \
                     u"     3. 支持五种常用格式(elf/axf/srec/hex/bin)裸源image文件输入并检查其链接地址的合法性 \n" + \
                     u"     4. 能够检查用户源image文件的适用性与合法性 \n" + \
                     u"     5. 支持将裸源image文件自动转换成i.MXRT能启动的Bootable image \n" + \
                     u"     6. 支持下载Bootable image进主动启动设备 - FlexSPI NOR、SEMC NAND接口Flash \n" + \
                     u"     7. 支持下载Bootable image进备份启动设备 - LPSPI接口NOR/EEPROM Flash \n" + \
                     u"     8. 支持DCD配置功能，可用于加载image进SDRAM执行 \n" + \
                     u"     9. 支持用于开发阶段的非安全加密启动（未签名加密） \n" + \
                     u"    10. 支持基于HAB实现的安全加密启动（单签名，签名和加密） \n" + \
                     u"    11. 能够自动备份证书并用时间戳记录 \n" + \
                     u"    12. 支持基于BEE实现的安全加密启动（唯一SNVS key，用户自定义key） \n" + \
                     u"    13. 支持MCU芯片内部eFuse的回读和烧写操作（即专用eFuse烧写器） \n" + \
                     u"    14. 支持外部启动设备的任意读写擦操作（即通用Flash编程器） \n" + \
                     u"    15. 支持从外部启动设备回读Bootable image，并对其组成部分（NFCB/DBBT/FDCB/EKIB/EPRDB/IVT/Boot Data/DCD/Image/CSF/DEK KeyBlob）进行标注 \n\n"
kRevision_1_1_0_en =  "【v1.1.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT1015 \n" + \
                      "     2. Add Language option in Menu/View and support Chinese\n" + \
                      "  Improvement: \n" + \
                      "     1. USB device auto-detection can be disabled \n" + \
                      "     2. Original image can be a bootable image (with IVT&BootData/DCD) \n" + \
                      "     3. Show boot sequence page dynamically according to action \n" + \
                      "  Interest: \n" + \
                      "     1. Add sound effect (Mario) \n\n"
kRevision_1_1_0_zh = u"【v1.1.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持i.MXRT1015 \n" + \
                     u"     2. 支持界面中文显示\n" + \
                     u"  改进: \n" + \
                     u"     1. USB自动识别的功能可以禁掉 \n" + \
                     u"     2. 用户输入的源程序文件可以包含i.MXRT启动头 (IVT&BootData/DCD) \n" + \
                     u"     3. 根据操作过程自动跟随显示操作页面 \n" + \
                     u"  个性: \n" + \
                     u"     1. 增加马里奥音效 \n\n"
kRevision_1_2_0_en =  "【v1.2.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Can generate .sb file by all-in-one action for MfgTool and RT-Flash \n" + \
                      "     2. Can show cost time along with gauge \n" + \
                      "  Improvement: \n" + \
                      "     1. Non-XIP image can also be supported for BEE Encryption case \n" + \
                      "     2. Display guage in real time \n" + \
                      "  Bugfix: \n" + \
                      "     1. Region count cannot be set more than 1 for Fixed OTPMK Key case \n" + \
                      "     2. Option1 field is not implemented for FlexSPI NOR configuration \n\n"
kRevision_1_2_0_zh = u"【v1.2.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持生成.sb格式的应用程序(通过all-in-one按钮)，可用于MfgTool和RT-Flash \n" + \
                     u"     2. 可以实时显示操作消耗的时间，随着进度条同步更新 \n" + \
                     u"  改进: \n" + \
                     u"     1. BEE加密模式下也能支持Non-XIP应用程序 \n" + \
                     u"     2. 进度条可以实时更新，更新速度由快到慢 \n" + \
                     u"  修复: \n" + \
                     u"     1. 使用Fixed OTPMK Key的BEE加密模式下，加密区域不能被设超过1 \n" + \
                     u"     2. FlexSPI NOR启动设备配置界面，Option1不能被有效设置 \n\n"
kRevision_1_3_0_en =  "【v1.3.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Can generate .sb file by actions in efuse operation utility window \n" + \
                      "  Improvement: \n" + \
                      "     1. HAB signed mode should not appliable for FlexSPI/SEMC NOR device Non-XIP boot with RT1020/1015 ROM \n" + \
                      "     2. HAB encrypted mode should not appliable for FlexSPI/SEMC NOR device boot with RT1020/1015 ROM \n" + \
                      "     3. Multiple .sb files(all, flash, efuse) should be generated if there is efuse operation in all-in-one action \n" + \
                      "     4. Can generate .sb file without board connection when boot device type is NOR \n" + \
                      "     5. Automatic image readback can be disabled to save operation time \n" + \
                      "     6. The text of language option in menu bar should be static and easy understanding \n" + \
                      "  Bugfix: \n" + \
                      "     1. Cannot generate bootable image when original image (hex/bin) size is larger than 64KB \n" + \
                      "     2. Cannot download large image file (eg 6.8MB) in some case \n" + \
                      "     3. There is language switch issue with some dynamic labels \n" + \
                      "     4. Some led demos of RT1050 EVKB board are invalid \n\n"
kRevision_1_3_0_zh = u"【v1.3.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持生成仅含自定义efuse烧写操作(在efuse operation windows里指定)的.sb格式文件 \n" + \
                     u"  改进: \n" + \
                     u"     1. HAB签名模式在i.MXRT1020/1015下应不支持从FlexSPI NOR/SEMC NOR启动设备中Non-XIP启动 \n" + \
                     u"     2. HAB加密模式在i.MXRT1020/1015下应不支持从FlexSPI NOR/SEMC NOR启动设备中启动 \n" + \
                     u"     3. 当All-In-One操作中包含efuse烧写操作时，会生成3个.sb文件(全部操作、仅flash操作、仅efuse操作) \n" + \
                      "     4. 当启动设备是NOR型Flash时，可以不用连接板子直接生成.sb文件 \n" + \
                     u"     5. 一键操作下的自动程序回读可以被禁掉，用以节省操作时间 \n" + \
                     u"     6. 菜单栏里的语言选项标签应该是静态且易于理解的(中英双语同时显示) \n" + \
                     u"  修复: \n" + \
                     u"     1. 当输入的源image文件格式为hex或者bin且其大小超过64KB时，生成可启动程序会失败 \n" + \
                     u"     2. 当输入的源image文件非常大时(比如6.8MB)，下载可能会超时失败 \n" + \
                     u"     3. 当切换显示语言时，有一些控件标签(如Connect按钮)不能实时更新 \n" + \
                     u"     4. /apps目录下RT1050 EVKB板子的一些LED demo是无效的 \n\n"
kRevision_1_4_0_en =  "【v1.4.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support for loading bootable image into uSDHC SD/eMMC boot device  \n" + \
                      "     2. Provide friendly way to view and set mixed eFuse fields  \n" + \
                      "  Improvement: \n" + \
                      "     1. Set default FlexSPI NOR device to align with  NXP EVK boards \n" + \
                      "     2. Enable real-time gauge for Flash Programmer actions \n\n"
kRevision_1_4_0_zh = u"【v1.4.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持下载Bootable image进主动启动设备 - uSDHC接口SD/eMMC卡 \n" + \
                     u"     2. 支持更直观友好的方式去查看/设置某些混合功能的eFuse区域 \n" + \
                     u"  改进: \n" + \
                     u"     1. 默认FlexSPI NOR device应与恩智浦官方EVK板卡相匹配 \n" + \
                     u"     2. 为通用Flash编程器里的操作添加实时进度条显示 \n\n"
kRevision_2_0_0_en =  "【v2.0.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT5xx A0, i.MXRT6xx A0 \n" + \
                      "     2. Support i.MXRT1011, i.MXRT117x A0 \n" + \
                      "     3. [RTxxx] Support both UART and USB-HID ISP modes \n" + \
                      "     4. [RTxxx] Support for converting bare image into bootable image \n" + \
                      "     5. [RTxxx] Original image can be a bootable image (with FDCB) \n" + \
                      "     6. [RTxxx] Support for loading bootable image into FlexSPI/QuadSPI NOR boot device \n" + \
                      "     7. [RTxxx] Support development boot case (Unsigned, CRC) \n" + \
                      "     8. Add Execute action support for memory programmer \n" + \
                      "     9. [RTyyyy] Can show FlexRAM info in device status  \n" + \
                      "  Improvement: \n" + \
                      "     1. [RTyyyy] Improve stability of USB connection of i.MXRT105x board \n" + \
                      "     2. Can write/read RAM via memory programmer \n" + \
                      "  Bugfix: \n" + \
                      "     1. [RTyyyy] Sometimes tool will report error \"xx.bat file cannot be found\" \n" + \
                      "     2. [RTyyyy] Editing mixed eFuse fields is not working as expected \n\n"
kRevision_2_0_0_zh = u"【v2.0.0】 \n" + \
                     u"  特性: \n" + \
                     u"     1. 支持i.MXRT5xx A0, i.MXRT6xx A0 \n" + \
                     u"     2. 支持i.MXRT1011, i.MXRT117x A0 \n" + \
                     u"     3. [RTxxx] 支持UART和USB-HID两种串行编程方式（COM端口/USB设备自动识别） \n" + \
                     u"     4. [RTxxx] 支持将裸源image文件自动转换成i.MXRT能启动的Bootable image \n" + \
                     u"     5. [RTxxx] 用户输入的源程序文件可以包含i.MXRT启动头 (FDCB) \n" + \
                     u"     6. [RTxxx] 支持下载Bootable image进主动启动设备 - FlexSPI/QuadSPI NOR接口Flash \n" + \
                     u"     7. [RTxxx] 支持用于开发阶段的非安全加密启动（未签名，CRC校验） \n" + \
                     u"     8. 在通用Flash编程器模式下增加执行(跳转)操作 \n" + \
                     u"     9. [RTyyyy] 支持在device status里显示当前FlexRAM配置情况 \n" + \
                     u"  改进: \n" + \
                     u"     1. [RTyyyy] 提高i.MXRT105x目标板USB连接稳定性 \n" + \
                     u"     2. 通用Flash编程器里也支持读写RAM \n" + \
                     u"  修复: \n" + \
                     u"     1. [RTyyyy] 有时候生成证书时会提示bat文件无法找到，导致证书无法生成 \n" + \
                     u"     2. [RTyyyy] 可视化方式去编辑混合eFuse区域并没有生效 \n\n"

kMsgLanguageContentDict = {
        'homePage_title':                     ['Home Page',                             u"项目主页"],
        'homePage_info':                      ['https://github.com/JayHeng/NXP-MCUBootUtility.git \n',                             u"https://github.com/JayHeng/NXP-MCUBootUtility.git \n"],
        'aboutAuthor_title':                  ['About Author',                          u"关于作者"],
        'aboutAuthor_author':                 [u"Author:  痞子衡 \n",                   u"作者：痞子衡 \n"],
        'aboutAuthor_email1':                 ['Email:     jie.heng@nxp.com \n',        u"邮箱：jie.heng@nxp.com \n"],
        'aboutAuthor_email2':                 ['Email:     hengjie1989@foxmail.com \n', u"邮箱：hengjie1989@foxmail.com \n"],
        'aboutAuthor_blog':                   [u"Blog:      痞子衡嵌入式 https://www.cnblogs.com/henjay724/ \n",                   u"博客：痞子衡嵌入式 https://www.cnblogs.com/henjay724/ \n"],
        'contributors_title':                 ['Contributors',                          u"贡献者名单"],
        'contributors_info':                  [u"李嘉奕Joyeee、祁凯Kelvin \n",          u"李嘉奕Joyeee、祁凯Kelvin \n"],
        'specialThanks_title':                ['Special Thanks',                        u"特别感谢"],
        'specialThanks_info':                 [u"Special thanks to 周小朋Clare、杨帆、刘华东Howard、沈浩杰Jayson \n",              u"特别感谢我亲爱的同事们：周小朋Clare、杨帆、刘华东Howard、沈浩杰Jayson \n"],
        'revisionHistory_title':              ['Revision History',                      u"版本历史"],
        'revisionHistory_v1_0_0':             [kRevision_1_0_0_en,                      kRevision_1_0_0_zh],
        'revisionHistory_v1_1_0':             [kRevision_1_1_0_en,                      kRevision_1_1_0_zh],
        'revisionHistory_v1_2_0':             [kRevision_1_2_0_en,                      kRevision_1_2_0_zh],
        'revisionHistory_v1_3_0':             [kRevision_1_3_0_en,                      kRevision_1_3_0_zh],
        'revisionHistory_v1_4_0':             [kRevision_1_4_0_en,                      kRevision_1_4_0_zh],
        'revisionHistory_v2_0_0':             [kRevision_2_0_0_en,                      kRevision_2_0_0_zh],

        'bootDeviceInfo_hasOnchipSerialNor':  ['MCU has on-chip QSPI NOR Flash (4MB, 133MHz), so you don\'t need to configure this boot device!',
                                              u"微控制器内置4MB的QSPI NOR Flash，所以无需配置该启动设备！"],
        'connectError_cannotSetOneStep':      ['One Step mode cannot be set under Entry Mode, Please switch to Master Mode and try again!',
                                              u"在软件入门级模式下，[一键连接]模式不可改，请切换到软件专家级模式下再试！"],
        'connectError_failToJumpToFl':        ['MCU has entered ROM SDP mode but failed to jump to Flashloader, Please reset board and try again!',
                                              u"微控制器已成功进入ROM SDP模式，但是未能跳转进入Flashloader，请复位板子再试！"],
        'connectError_doubleCheckBmod':       ['Make sure that you have put MCU in SDP (Serial Downloader Programming) mode (BMOD[1:0] pins = 2\'b01)!',
                                              u"请检查BMOD[1:0]引脚状态是否为2\'b01以确认微控制器处于ROM SDP模式！"],
        'connectError_failToPingFl':          ['Failed to ping Flashloader, Please reset board and consider updating flashloader.srec file under /src/targets/ then try again!',
                                              u"微控制器未能与Flashloader建立连接，请复位板子并考虑更新/src/targets/目录下相应的flashloader.srec文件再试！"],
        'connectError_failToCfgBootDevice':   ['MCU has entered Flashloader but failed to configure external memory, Please reset board and set proper boot device then try again!',
                                              u"微控制器已与Flashloader建立连接，但是未能识别启动设备。请复位板子并配置正确的启动设备再试！"],
        'connectError_hasnotCfgBootDevice':   ['Please configure boot device via Flashloader first!',
                                              u"请先借助Flashloader去完成启动设备的配置！"],
        'connectError_hasnotEnterFl':         ['Please connect to Flashloader first!',
                                              u"请先连接到Flashloader！"],
        'certGenError_notEnabledForBee':      ['Certificate is not enabled for BEE, You can enable it then try again!',
                                              u"当前BEE加密启动模式下没有使能认证，请先使能认证再试！"],
        'certGenError_noNeedToSetForUnsigned':['No need to set certificate option when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要配置认证参数！"],
        'certGenError_noNeedToGenForUnsigned':['No need to generate certificate when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要生成证书！"],
        'certGenInfo_reuseOldCert':           ["There is available certificate, Do you want to reuse existing certificate? \n",
                                              u"当前目录下已有证书文件，你想复用已有的证书吗？"],
        'certGenInfo_haveNewCert':            ["New certificate will be different even you don’t change any settings, Do you really want to have new certificate? \n",
                                              u"即使不改任何认证参数，新证书也会不同于已有证书，你依旧想生成新证书吗？"],
        'keyGenError_onlyForBee':             ['Key setting is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"配置密钥参数仅在BEE加密启动模式下有效！"],
        'operHabError_notAppliableDevice':    ['HAB encryption is not appliable for FlexSPI NOR/SEMC NOR device under selected MCU device!',
                                              u"HAB加密操作在选中的微控制器型号下不支持FlexSPI NOR/SEMC NOR启动设备！"],
        'operBeeError_onlyForBee':            ['BEE encryption is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"BEE加密操作仅在BEE加密启动模式下有效！"],
        'operBeeError_onlyForFlexspiNor':     ['Action is not available because BEE encryption boot is only designed for FlexSPI NOR device!',
                                              u"在软件入门级模式下，单步操作不被支持，请直接使用[一键启动]！"],
        'operBeeError_failToPrepareForSnvs':  ['Failed to prepare for fixed OTPMK SNVS encryption, Please reset board and try again!',
                                              u"未能准备好OTPMK SNVS加密，请复位板子再试！！"],
        'operKeyError_srkNotForUnsigned':     ['No need to burn SRK data when booting unsigned image!',
                                              u"当前裸启动开发模式下不需要烧写SRK！"],
        'operKeyError_dekOnlyForBee':         ['BEE DEK Burning is only available when booting BEE encrypted image in FlexSPI NOR device!',
                                              u"烧写DEK操作仅在BEE加密启动模式下有效！"],
        'operKeyError_dekNotForSnvs':         ['No need to burn BEE DEK data as OTPMK key is selected!',
                                              u"当前选择OTPMK SNVS区域存储密钥下不需要烧写DEK！"],
        'operMemError_notAvailUnderEntry':    ['Common memory operation is not available under Entry Mode, Please switch to Master Mode and try again!',
                                              u"在软件入门级模式下，通用Flash操作没有使能，请切换到软件专家级模式下再试！"],
        'separActnError_notAvailUnderEntry':  ['Separated action is not available under Entry Mode, You should use All-In-One Action!',
                                              u"在软件入门级模式下，单步操作不被支持，请直接使用[一键启动]！"],
        'operImgError_failToFlashImage':      ['Failed to flash bootable image into external memory, Please reset board and try again!',
                                              u"未能将应用程序下载进启动设备，请复位板子再试！！"],
        'operImgError_keyBlobOnlyForHab':     ['KeyBlob loading is only available when booting HAB encrypted image!',
                                              u"下载KeyBlob操作仅在HAB加密启动模式下有效！"],
        'operImgError_hasnotFlashImage':      ['Please flash image into boot device first!',
                                              u"请先将应用程序下载进启动设备！"],

        'inputError_illegalFormat':           ['Illegal input detected! You should input like this format: 0x5000',
                                              u"检测到非法输入!参考合法格式示例为: 0x5000（十六进制）"],

        'inputError_serial':                  ['Serial must be 8 digits!',
                                              u"序列号必须是8位数字!"],
        'inputError_keyPass':                 ['You forget to set key_pass!',
                                              u"密钥因子没有设置正确！"],
        'genImgError_formatNotValid':         ['Cannot recognise/convert the format of image file: ',
                                              u"无法识别/转换该程序文件格式: "],
        'genDcdError_failToGen':              ['DCD binary is not generated successfully! Check your DCD descriptor file and make sure you don\'t put the tool in path with blank space!',
                                              u"DCD文件未成功生成!检查DCD描述符文件, 并确保NXP-MCUBootUtility工具的路径中没有空格!"],
        'srcImgError_invalidVector':          ['Invalid vector address found in image file: ',
                                              u"该程序文件起始链接地址是无效的:"],
        'srcImgError_invalidNonXipRange':     ['Non-XIP Application is detected but it is not in the range of ITCM/DTCM/OCRAM/SDRAM!',
                                              u"检测到非XIP应用程序,但它没有链接到ITCM/DTCM/OCRAM/SDRAM范围内!"],
        'srcImgError_nonXipNotAppliable':     ['Non-XIP Application is detected but it is not appliable for HAB Signed image boot when boot device is FlexSPI/SEMC NOR under selected MCU device!',
                                              u"Non-XIP应用程序被检测到, 但它在选中的微控制器型号以及FlexSPI/SEMC NOR启动设备下不适用于HAB签名启动!"],
        'srcImgError_xipNotForHabCrypto':     ['XIP Application is detected but it is not appliable for HAB Encrypted image boot!',
                                              u"XIP应用程序被检测到, 但它不适用于HAB加密启动!"],
        'srcImgError_nonXipNotForBeeCrypto':  ['Non-XIP Application is detected but it is not appliable for BEE Encrypted image boot!',
                                              u"检测到非XIP应用程序, 但它不适用于BEE加密启动!"],
        'srcImgError_notFound':               ['You should first specify a source image file (.elf/.axf/.srec/.hex/.bin)!',
                                              u"请首先选定一个程序文件 (. elf/. axf/. srec/. srec/. hacn)!"],
        'srcImgError_xipSizeTooLarge':        ['XIP Application is detected but the size exceeds maximum XIP size ',
                                              u"XIP应用程序被检测到, 但其大小超过最大XIP范围 "],
        'operCertError_notGen':               ['You should first generate certificates, or make sure you don\'t put the tool in path with blank space!',
                                              u"请首先生成证书, 或者确保NXP-MCUBootUtility工具存放的路径中没有空格!"],
        'srcImgError_failToGen':              ['Bootable image is not generated successfully! Make sure you don\'t put the tool in path with blank space!',
                                              u"可启动的程序文件未成功生成!请确保NXP-MCUBootUtility工具存放的路径中没有空格!"],
        'srcImgError_failToGenSb':            ['.sb image is not generated successfully! Make sure you don\'t put the tool in path with blank space!',
                                              u".sb格式程序文件未成功生成!请确保NXP-MCUBootUtility工具存放的路径中没有空格!"],
        'srcImgError_invalidFl':              ['Default Flashloader image file is not usable!',
                                              u"默认的Flashloader程序文件不适用!"],
        'operCertError_notGen1':              ['You should first generate certificates!',
                                              u"请首先生成证书！"],
        'burnFuseError_failToBurnSrk':        ['Fuse SRK Regions were not burned successfully!',
                                              u"SRK数据未成功烧录进Fuse SRK0-7区域!"],
        'burnFuseError_srkHasBeenBurned':     ['Fuse SRK Regions have been burned, it is program-once!',
                                              u"Fuse SRK区域已经被烧录过，它只可被烧写一次！"],
        'certGenError_srkNotGen':             ['Super Root Keys hasn\'t been generated!',
                                              u"SRK数据文件还没有生成！"],
        'burnFuseError_failToBurnSwgp2Lock':  ['Fuse LOCK SW_GP2 region was not burned successfully!',
                                              u"Fuse SW_GP2区域的Lock位未成功烧录!"],
        'burnFuseError_failToBurnGp4Lock':    ['Fuse LOCK GP4 region was not burned successfully!',
                                              u"Fuse GP4区域的Lock位未成功烧录!"],
        'burnFuseError_failToBurnSwgp2':      ['Fuse SW_GP2 Regions were not burned successfully!',
                                              u"Fuse SW_GP2区域未成功烧录!"],
        'burnFuseError_swgp2HasBeenBurned':   ['Fuse SW_GP2 Regions have been burned/locked, it is program-once!',
                                              u"Fuse SW_GP2区域已经被烧录过或锁定，它只可被烧写一次！"],
        'burnFuseError_failToBurnGp4':        ['Fuse GP4 Regions were not burned successfully!',
                                              u"Fuse GP4区域未成功烧录!"],
        'burnFuseError_gp4HasBeenBurned':     ['Fuse GP4 Regions have been burned/locked, it is program-once!',
                                              u"Fuse GP4区域已经被烧录过或锁定，它只可被烧写一次！"],
        'burnFuseError_miscConf1HasBeenBurned': ['Fuse MISC_CONF1[31:0] has been burned, it is program-once!',
                                                u"Fuse MISC_CONF1[31:0]区域已经被烧录过，它只可被烧写一次！"],
        'burnFuseError_failToBurnMiscConf1':  ['Fuse MISC_CONF1[31:0] region was not burned successfully!',
                                              u"Fuse MISC_CONF1[31:0]区域未成功烧录！"],
        'burnFuseError_miscConf0HasBeenBurned': ['Fuse MISC_CONF0[28:24] LPSPI_EEPROM has been burned, it is program-once!',
                                                u"Fuse MISC_CONF0[28:24]已经被烧录，它只可被烧写一次！"],
        'burnFuseError_failToBurnMiscConf0':  ['Fuse MISC_CONF0[28:24] LPSPI EEPROM region was not burned successfully!',
                                              u"Fuse MISC_CONF0[28:24]区域未成功烧录！"],
        'burnFuseError_beeKey0SelHasBeenBurned': ['Fuse BOOT_CFG1[5:4] BEE_KEY0_SEL has been burned, it is program-once!',
                                                 u"Fuse BOOT_CFG1[5:4] BEE_KEY0_SEL位已经被烧录过，它只可被烧写一次！"],
        'burnFuseError_beeKey1SelHasBeenBurned': ['Fuse BOOT_CFG1[7:6] BEE_KEY1_SEL has been burned, it is program-once!',
                                                 u"Fuse BOOT_CFG1[7:6] BEE_KEY1_SEL位已经被烧录过，它只可被烧写一次！"],
        'burnFuseError_failToBurnBeeKeyxSel': ['Fuse BOOT_CFG1[7:4] BEE_KEY0/1_SEL region was not burned successfully!',
                                              u"Fuse BOOT_CFG1[7:4] BEE_KEY0/1_SEL位未成功烧录！"],
        'certGenError_dekNotGen':             ['Dek file hasn\'t been generated!',
                                              u"DEK数据文件还没有生成!"],
        'burnFuseError_failToBurnSecConfig1': ['Fuse BOOT_CFG1[1] SEC_CONFIG[1] region was not burned successfully!',
                                              u"Fuse BOOT_CFG1[1] SEC_CONFIG[1]位未成功烧录！"],

        'burnFuseError_cannotBurnSrkLock':    ['Fuse 0x400[14] - SRK_LOCK is not allowed to be set, because SRK will be OP+RP+WP if SRK_LOCK is set and then ROM cannot get SRK!',
                                              u"Fuse 0x400[14] - SRK_LOCK位不允许被烧写成1，如果SRK_LOCK被置1，SRK区域将会被保护(覆盖&读&写)，导致ROM不能得到SRK数据!"],

        'operImgError_hasnotProgImage':       ['You should program your image first!',
                                              u"请首先下载image文件！"],
        'operImgError_notInRam':              ['Your specified area is not in the range of RAM, Please double check!',
                                              u"当前指定的访问区域超出有效RAM范围，请仔细检查！"],

        'connectError_doubleCheckIsp':        ['Make sure that you have put MCU in ISP (In-System Programming) modes (ISP[2:0] pins = 3\'b010 (USB) or 3\'b110 (UART))!',
                                              u"请检查ISP[2:0]引脚状态是否为3\'b010 (USB)或3\'b110 (UART)以确认微控制器处于ROM ISP模式！"],

}