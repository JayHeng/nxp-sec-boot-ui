# NXP MCU Boot Utility

[![GitHub release](https://img.shields.io/github/release/JayHeng/NXP-MCUBootUtility.svg)](https://github.com/JayHeng/NXP-MCUBootUtility/releases/latest) [![GitHub commits](https://img.shields.io/github/commits-since/JayHeng/NXP-MCUBootUtility/v1.4.0.svg)](https://github.com/JayHeng/NXP-MCUBootUtility/compare/v1.4.0...master) ![GitHub All Releases](https://img.shields.io/github/downloads/JayHeng/NXP-MCUBootUtility/total.svg) [![GitHub license](https://img.shields.io/github/license/JayHeng/NXP-MCUBootUtility.svg)](https://github.com/JayHeng/NXP-MCUBootUtility/blob/master/LICENSE)

[English](./README.md) | 中文

### 1 软件概览
#### 1.1 介绍
　　NXP-MCUBootUtility是一个专为NXP MCU安全加密启动而设计的工具，其特性与NXP MCU里BootROM功能相对应，目前主要支持i.MXRT系列MCU芯片，与NXP官方的标准安全加密配套工具集（OpenSSL, CST, sdphost, blhost, elftosb, BD, MfgTool2）相比，NXP-MCUBootUtility是一个真正的一站式工具，一个工具包含NXP官方所有加密配套工具的功能，并且是全图形用户界面操作。借助于NXP-MCUBootUtility，你可以轻松上手NXP MCU安全加密启动。  
　　NXP-MCUBootUtility主要功能如下：  

> * 支持i.MXRT全系列MCU，包含i.MXRT1015、i.MXRT1021、i.MXRT1051/1052、i.MXRT1061/1062、i.MXRT1064 SIP  
> * 支持UART和USB-HID两种串行下载方式（COM端口/USB设备自动识别）  
> * 支持五种常用格式(elf/axf/srec/hex/bin)源image文件输入并检查其链接地址的合法性  
> * 源image文件既可以是裸源image文件，也可以是含启动文件头的bootable image文件  
> * 支持将裸源image文件自动转换成i.MXRT能启动的Bootable image  
> * 支持将裸源image文件自动转换成MfgTool和RT-Flash工具能下载的.sb格式文件  
> * 支持下载Bootable image进主动启动设备 - FlexSPI接口NOR Flash  
> * 支持下载Bootable image进主动启动设备 - SEMC接口NAND Flash  
> * 支持下载Bootable image进主动启动设备 - uSDHC接口SD/eMMC卡  
> * 支持下载Bootable image进备份启动设备 - LPSPI接口NOR/EEPROM Flash  
> * 支持DCD配置功能，可用于加载image进SDRAM执行  
> * 支持用于开发阶段的非安全加密启动（未签名加密）  
> * 支持基于HAB实现的安全加密启动（单签名，签名和加密），证书自动备份  
> * 支持基于BEE实现的安全加密启动（唯一SNVS key，用户自定义key）  
> * 支持MCU芯片内部eFuse的回读和烧写操作（即专用eFuse烧写器）  
> * 支持MCU芯片内部FlexRAM的读/写/执行操作（即专用FlexRAM编程器，可用于ISP启动）  
> * 支持外部启动设备的任意读/写/擦操作（即通用Flash编程器）  
> * 支持从外部启动设备回读Bootable image，并对其组成部分（NFCB/DBBT/FDCB/EKIB/EPRDB/IVT/Boot Data/DCD/Image/CSF/DEK KeyBlob）进行标注  

#### 1.2 下载
　　NXP-MCUBootUtility完全基于Python语言开发，并且源代码全部开源，其具体开发环境为Python 2.7.15 (32bit)、wxPython 4.0.3、pySerial 3.4、pywinusb 0.4.2、bincopy 15.0.0、PyAudio 0.2.11、PyInstaller 3.3.1（或更高）。  

> * 源代码: https://github.com/JayHeng/NXP-MCUBootUtility  
> * 问题反馈: https://www.cnblogs.com/henjay724/p/10159925.html  

　　NXP-MCUBootUtility在发布时借助PyInstaller将所有的Python依赖全部打包进一个可执行文件（\NXP-MCUBootUtility\bin\NXP-MCUBootUtility.exe），因此如果不是对NXP-MCUBootUtility的二次开发，你不需要安装任何Python软件及相关库。  

> Note1: 使用NXP-MCUBootUtility之前必须先从NXP官网下载 [HAB Code Signing Tool工具](https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX_CST_TOOL&appType=file2&location=null&DOWNLOAD_ID=null&lang_cd=en)，并将其解压放在\NXP-MCUBootUtility\tools\cst\目录下，并且需要修改代码使能AES功能重新生成\NXP-MCUBootUtility\tools\cst\mingw32\bin\cst.exe，否则HAB签名以及加密相关功能无法使用。具体步骤可以参考这篇博客 [《开启NXP-MCUBootUtility工具的HAB加密功能 - cst.exe》](https://www.cnblogs.com/henjay724/p/10189593.html)。   

> Note2: 使用NXP-MCUBootUtility之前必须编译\NXP-MCUBootUtility\tools\image_enc\code下面的源文件生成image_enc.exe，并将其放置在\NXP-MCUBootUtility\tools\image_enc\win，否则BEE加密相关功能无法使用。具体步骤可以参考这篇博客 [《开启NXP-MCUBootUtility工具的BEE加密功能 - image_enc.exe》](https://www.cnblogs.com/henjay724/p/10189602.html)  

> Note3: 源代码包里的NXP-MCUBootUtility.exe是在Windows 10 x64环境下打包的，也仅在该环境下测试过，如果因系统原因无法直接使用，你需要先安装 [Python2.7.15 x86版本](https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi) （安装完成后确认\Python27\\, \Python27\Scripts\\目录被添加到系统环境变量Path里），然后在\NXP-MCUBootUtility\env\目录下点击do_setup_by_pip.bat安装开发NXP-MCUBootUtility所依赖的Python库，最后点击do_pack_by_pyinstaller.bat重新生成NXP-MCUBootUtility.exe可执行文件。  

> Note4: 必须使用Python2 x86版本去打包NXP-MCUBootUtility，因为NXP-MCUBootUtility使用了pywinusb库，该库在Python2 x64版本下无法用PyInstaller打包，pywinusb作者没有计划修复该问题。  

#### 1.3 安装
　　NXP-MCUBootUtility是一个是纯绿色免安装的工具，下载了源代码包之后，直接双击\NXP-MCUBootUtility\bin\NXP-MCUBootUtility.exe即可使用。使用NXP-MCUBootUtility没有任何软件依赖，不需要额外安装任何软件。  
　　在NXP-MCUBootUtility.exe图形界面显示之前，会首先弹出一个控制台窗口，该控制台会伴随着NXP-MCUBootUtility.exe图形界面一起工作，很多图形界面的操作都会在控制台窗口看到对应的底层命令执行，保留控制台主要是为了便于定位NXP-MCUBootUtility.exe的问题，目前NXP-MCUBootUtility尚处于早期阶段，等后期软件成熟会考虑移除控制台。  

#### 1.4 目录

　　NXP-MCUBootUtility软件目录组织如下：  
```text
\NXP-MCUBootUtility
                \apps                 --放置NXP官方评估板示例image文件
                \bin                  --放置NXP-MCUBootUtility可执行文件及用户配置文件
                \doc                  --放置NXP官方安全启动相关的参考文档
                \env                  --放置用于安装NXP-MCUBootUtility开发环境以及打包脚本
                \gen                  --放置NXP-MCUBootUtility使用过程中生成的临时文件
                      \bd_file            --根据配置动态生成的BD文件
                      \bee_crypto         --BEE加密过程中生成的文件
                      \bootable_image     --生成的bootable image文件
                      \dcd_file           --生成的DCD数据文件
                      \hab_cert           --HAB签名过程中生成的文件
                      \hab_crypto         --HAB加密过程中生成的文件
                      \log_file           --保存软件操作记录日志
                      \sb_image           --生成的.sb格式文件
                      \user_file          --软件运行过程中缓存的临时文件
                \gui                  --放置开发NXP-MCUBootUtility UI构建工程文件
                \img                  --放置NXP-MCUBootUtility使用过程中需加载的图片
                \src                  --放置开发NXP-MCUBootUtility的所有Python源代码文件
                \tools                --放置NXP-MCUBootUtility使用过程中需调用的外部程序
                      \blhost             --与Flashloader通信的上位机命令行工具
                      \cst                --HAB加密的配套命令行工具
                      \elftosb            --生成bootable image的命令行工具
                      \ide_utils          --各IDE提供的image格式转换工具
                      \image_enc          --BEE加密的配套命令行工具
                      \imgutil            --生成DCD数据的命令行工具
                      \openssl            --生成证书和秘钥的标准工具
                      \sdphost            --与ROM通信的上位机命令行工具
```

#### 1.5 界面
　　下图为NXP-MCUBootUtility工具的主界面，界面主要由六部分组成，各部分功能如下：  

![NXP-MCUBootUtility_mainWin_e](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_mainWin_e.png)

> * 【Menu Bar】：功能菜单栏，提供软件通用设置。  
> * 【Target Setup】：目标设备设置栏，提供MCU Device和Boot Device配置选项。  
> * 【Port Setup】：串行接口设置栏，选择用于连接MCU Device的接口。  
> * 【Device Status】：目标设备状态信息栏，当连接上目标设备之后，用于显示目标设备的状态。  
> * 【Secure Boot Action】：安全加密启动主界面，提供对目标设备做安全加密启动的所有操作。  
> * 【Log Info】：操作日志栏，记录软件操作日志。  

### 2 准备工作
　　在使用NXP-MCUBootUtility工具前主要有两个准备工作：一、准备好i.MXRT硬件板以及串行下载连接线（USB/UART）；二、准备好用于下载进Flash的源image文件。  
　　关于串行下载线连接，需要查看i.MXRT参考手册System Boot章节，确保连接的UART/USB引脚是BootROM指定的。  
　　关于源image文件准备，NXP-MCUBootUtility工具能够识别五种常见格式(elf/axf/srec/hex/bin)的image，源image既可以包含i.MXRT加载启动头（IVT, BootData等），也可以不包含这些i.MXRT加载启动头。如果源image中不包含这些启动头，NXP-MCUBootUtility会自动添加文件头。  
　　以NXP官方SDK为例进一步讲解源image文件的生成，注册并登录NXP官网，来到 [MCUXpresso SDK Builder](https://mcuxpresso.nxp.com/en/select) 页面，选择合适的MCU芯片以及IDE（以RT1060芯片，IAR IDE为例）并点击Download SDK后便可得到SDK_2.4.0_EVK-MIMXRT1060.zip。  
　　使用IAR打开SDK包里的\boards\evkmimxrt1060\demo_apps\led_blinky\iar\led_blinky.eww示例应用：  

![NXP-MCUBootUtility_sdkProjectBuilds_e](http://henjay724.com/image/cnblogs/nxpSecBoot_sdkProjectBuilds_e.png)

　　led_blinky应用其实包含了三个工程（ram/flexspi_nor/sdram），分别对应三个不同的linker文件（.icf），其中ram工程生成的image即是所谓的Non-XIP image，flexspi_nor工程生成的image即是所谓的XIP image。  
　　默认情况下，ram工程和flexspi_nor工程生成的image文件是无法直接为NXP-MCUBootUtility所用的，需要做一些小小的改变。  
　　ram工程需要修改linker文件如下：（推荐从0x3000开始链接中断向量表，中断向量表前面预留一段内存用于放置i.MXRT加载启动所需的文件头）。  

```text
define symbol m_interrupts_start       = 0x00003000;   // 0x00000000
define symbol m_interrupts_end         = 0x000033FF;   // 0x000003FF

define symbol m_text_start             = 0x00003400;   // 0x00000400
define symbol m_text_end               = 0x0001FFFF;

define symbol m_data_start             = 0x20000000;
define symbol m_data_end               = 0x2001FFFF;

define symbol m_data2_start            = 0x20200000;
define symbol m_data2_end              = 0x202BFFFF;
```

　　flexspi_nor工程需要修改工程配置选项里的Defined symbols如下：（将XIP_BOOT_HEADER_ENABLE设为0，即不需要生成包含i.MXRT加载启动文件头的image; 如果保持XIP_BOOT_HEADER_ENABLE为1不变，那么生成的可执行image文件会包含i.MXRT加载启动文件头）。  

![NXP-MCUBootUtility_sdkProjectOptions](http://henjay724.com/image/cnblogs/nxpSecBoot_sdkProjectOptions.PNG)

　　如果只是为了快速验证NXP-MCUBootUtility工具，在NXP-MCUBootUtility\apps文件夹下默认存放了全系列恩智浦官方i.MXRT评估板的led_blinky应用的image文件。  

### 3 软件使用
#### 3.1 设置目标设备
　　在使用NXP-MCUBootUtility时首先需要配置目标设备，目标设备包括MCU Device和Boot Device。以NXP官方开发板EVK-MIMXRT1060为例，该开发板主芯片为i.MXRT1062DVL6A，所以【MCU Device】应设为i.MXRT106x。且以最常用的FlexSPI NOR启动为例，【Boot Device】设为FLEXSPI NOR，开发板上对应的外部存储芯片为IS25WP064AJBLE，其是一颗常用的四线QSPI NOR Flash，我们需要在软件里进一步配置该Boot Device，单击【Boot Device Configuration】按钮可弹出如下新的配置页面：  

![NXP-MCUBootUtility_flexspiNorCfgWin_e](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_flexspiNorCfgWin_e.png)

　　在弹出的名为FlexSPI NOR Device Configuration页面里可以看到很多描述Multi-IO SPI NOR Flash特性的选项，比如Device Type、Query Pads等，这些选项都需要被正确地设置，以与开发板上的外部存储芯片相匹配。  
　　除此以外，页面上还有一个名为【Use Typical Device Model】的选项，NXP-MCUBootUtility软件预先定义了一些常用的Multi-IO SPI NOR Flash型号模型，如果开发板上的外部存储芯片恰好在软件预定义的型号列表里，那么你可以直接在【Use Typical Device Model】选择对应型号，而不必在Nor Option里逐一配置。  
　　EVK-MIMXRT1060开发板上的IS25WP064AJBLE芯片属于ISSI - IS25LP064A大类，因此我们只需要在【Use Typical Device Model】选择ISSI - IS25LP064A并点击【Ok】即完成了目标设备的设置。  

#### 3.2 连接目标设备
　　设置好目标设备之后，下一步便是连接目标设备，以USB-HID接口连接为例，给EVK-MIMXRT1060板子供电，并用USB Cable将PC与J9口连接起来，如果一切正常，应该可以在设备管理器找到vid,pid为0x1fc9,0x0135的HID-compliant vendor-defined device设备被枚举。如果没有发现该HID设备，请仔细检查板子SW7拨码开关是否将Boot Mode设为2'b01即Serial Downloader模式。  

![NXP-MCUBootUtility_usbhidDetected_e](http://henjay724.com/image/cnblogs/nxpSecBoot_usbhidDetected_e.png)

　　确认HID设备存在之后，在【Port Setup】选中USB-HID，然后直接点击【Connect to ROM】按钮，此时软件便会自动完成目标设备连接全过程（使用sdphost连接ROM，获取一些MCU内部寄存器信息，使用sdphost加载Flashloader并跳转过去，使用blhost连接Flashloader，获取一些eFuse信息，使用blhost去配置boot device并获取boot device meomry信息），这个过程需要大概5s的时间，如果目标设备连接正常，你可以看到指示灯变蓝，并且【Connect to ROM】按钮标签变为【Reset Device】。如果目标设备连接失败，指示灯会变红，并且【Connect to ROM】按钮标签变为【Reconnect】。  

![NXP-MCUBootUtility_connectedToDevice_e](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_connectedToDevice_e.png)

　　目标设备连接成功后可以在目标设备状态信息栏看到一些有用的设备状态信息，比如MCU芯片的UUID值、HAB状态、与启动相关的重要Fuse值，Boot Device的Page/Sector/Block大小等。  

#### 3.3 安全加密启动
　　确保菜单栏Tools/Generate .sb file选项勾选的是"No"，目标设备连接成功后便可以开始最核心的安全加密启动操作，在做安全加密启动之前先来介绍安全加密启动主界面分布：  

![NXP-MCUBootUtility_secboot0_intro_e](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot0_intro_e.png)

> * 【Image Generation Sequence】：image生成窗口，用于对源image进行加密安全处理，生成可放在Boot Device中的bootable image  
> * 【Image Loading Sequence】：image下载窗口，用于将生成的bootable image下载进Boot Device中，并且在MCU中烧录相应的Fuse值（各种Key，HAB设置等）  
> * 【eFuse Operation Utility】：eFuse回读与烧录窗口，用户可烧录自定义值进Fuse Region。  
> * 【Boot Device Memory】：image回读与标注显示窗口，用于从Boot Device回读已下载的Bootable image数据，并对数据组成各部分进行标注  
> * 【Secure Boot Type】：安全加密模式选择，选择想要安全模式（不使能安全，HAB单签名，HAB签名加密，BEE加密）。  
> * 【All-In-One Action】：一键操作，image生成窗口和image下载窗口里激活的操作自动按序执行  

##### 3.3.1 模式一：不启用任何安全措施
　　第一种模式是最简单的模式，即不启动任何安全措施，一般用于产品开发调试阶段。  
　　【Secure Boot Type】选择“DEV Unsigned Image Boot”，然后点击【Browse】按钮选择一个原始image文件（使用IDE生成的裸image文件即可，不需要包含任何i.MXRT启动所需的额外文件头），点击【All-In-One Action】按钮即可完成bootable image生成与下载所有操作。  

> Note: 软件如果设置为Auto-detect image format选项，则根据文件后缀名自动识别源文件格式。但是对于MCUXpresso或者GCC生成的axf文件，需要主动设置为".out(axf) from MCUXpresso/GCC ARM"。  

![NXP-MCUBootUtility_secboot1_unsigned](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot1_unsigned_e.png)

　　上图中Step4和Step5并不是必需操作，仅是用于确认【All-In-One Action】按钮操作是否成功，尤其是Step5操作，可以对应image下载窗口里显示的Bootable image构成图做一遍检查。  
　　一切操作无误，板子上SW7拨码开关将Boot Mode设为2'b10即Internal Boot模式，其余保持全0，重新上电便可以看到unsigned image正常执行了。  

##### 3.3.2 模式二：启用HAB签名认证
　　第二种模式是初级的安全模式，即仅对image进行签名认证，一般用于对产品安全性要求较高的场合。签名认证主要是对image合法性进行校验，检测image是否被异常破坏或篡改，如果检测发现image不合法，那么MCU便不会启动执行该image。  
　　【Secure Boot Type】选择“HAB Signed Image Boot”，然后输入serial（必须是8位数字）以及key_pass（任意长度字符）后点击【Advanced Cert Settings】按钮配置所有签名认证的参数（熟悉 [NXP官方HAB Code Signing Tool工具](https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX_CST_TOOL&appType=file2&location=null&DOWNLOAD_ID=null&lang_cd=en) 使用的朋友应该对这些设置很熟悉），再点击【Browse】按钮选择一个原始image文件，最后点击【All-In-One Action】按钮即可完成bootable image生成与下载所有操作。  

![NXP-MCUBootUtility_secboot2_signed](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot2_signed_e.png)

　　上图中Step5主要确认两点：一、HAB状态是否是Closed的（Fuse 0x460[31:0]的bit1为1'b1）；二、SRKH是否被正确烧录（Fuse 0x580 - 0x5f0，一共256bit，即sha-256算法），SRKH是最终bootable image里CSF数据里的Public RSA Key的Hash值，用于校验Public RSA Key是否合法。  
　　一切操作无误，板子上SW7拨码开关将Boot Mode设为2'b10即Internal Boot模式，其余保持全0，重新上电便可以看到HAB signed image正常执行了。  
　　因为此时MCU芯片HAB状态已经是Closed，并且SRKH已经被烧录无法更改，所以未经签名认证的image无法正常运行，在软件目录\NXP-MCUBootUtility\tools\cst\crts文件夹下存放着Private RSA Key文件，请妥善保存好，一旦遗失，那么新的image将无法被正确签名从而导致HAB认证失败无法被启动执行。  

##### 3.3.3 模式三：启用HAB签名认证与HAB加密
　　第三种模式是中级的安全模式，即对image进行签名认证以及HAB级加密，一般用于对产品安全性要求很高的场合。签名认证主要是对image合法性进行校验，而加密则可以保护image在外部Boot Device中不被非法盗用，因为在外部Boot Device中存放的是image的密文数据，即使被非法获取也无法轻易破解，并且加密是和MCU芯片绑定的，因为HAB加密过程中使用了MCU内部SNVS模块里的唯一Master Secret Key。  
　　【Secure Boot Type】选择“HAB Encrypted Image Boot”，然后配置所有签名认证的参数（如果本地已有证书，可以不用配置，软件会尝试复用），再点击【Browse】按钮选择一个原始image文件，最后点击【All-In-One Action】按钮即可完成bootable image生成与下载所有操作。  

![NXP-MCUBootUtility_secboot3_hab_encrypted](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot3_hab_encrypted_e.png)

　　上图中Step6操作之后可以看到下载进Boot Device里的image部分确实是密文，实际上HAB加密仅支持加密image区域，其他区域（比如FDCB、IVT、Boot Data等）均没有加密。  
　　一切操作无误，板子上SW7拨码开关将Boot Mode设为2'b10即Internal Boot模式，其余保持全0，重新上电便可以看到HAB signed encrypted image正常执行了。  
　　你可能会好奇，既然image是经过HAB加密的，那么密码在哪里？怎么设置的？其实image加密操作完全被HAB配套工具封装好了，HAB加密使用的AES-128算法，其对应的128bits的AES-128 Key不是由用户自定义的，而是HAB加密工具自动随机生成的，并且每一次加密操作生成的AES-128 Key都是不一样的，即使你没有更换输入的原始image。AES-128 Key保存在\NXP-MCUBootUtility\gen\hab_crypto\hab_dek.bin文件里。  
　　从上图中image下载窗口里显示的Bootable image构成图里可以看出，相比HAB单签名的方式，HAB签名加密方式最终使用的Bootable image的最后多了一个DEK KeyBlob组成部分，这个DEK KeyBlob是通过MCU芯片内部SNVS模块里的Master Secret Key对hab_dek.bin里的key数据进行动态加密生成的，因为Master Secret Key是芯片唯一的，因此DEK KeyBlob也是芯片唯一的，这是保护image不被非法盗用的关键。  
　　关于HAB加密为何不支持XIP Image，其实简单分析一下启动原理便清楚，Image在Boot Device里存储的是密文，这部分密文必须要经过HAB解密成明文才可以被CPU执行，因此必须要指定不同的存储空间去存放Image明文，Non-XIP image天然指定了明文应存放在芯片内部SRAM或者外挂SDRAM中，而XIP Image是在Boot Device中直接执行的，一般明文地址与密文地址是相同的，因此HAB加密不支持XIP Image。  

##### 3.3.4 模式四：启用单引擎BEE加密（唯一SNVS Key）
　　第四种模式是高级的安全模式，即用唯一SNVS Key对image进行单引擎BEE级加密，一般用于对产品安全性要求极高的场合。BEE加密与HAB加密的主要区别是执行解密操作的主体不同，主要有如下三点区别：  

> * HAB加密是由BootROM里的HAB将加密后的image全部解密成明文另存后再执行（静态解密），而BEE加密是由MCU芯片内部的BEE模块对加密的image进行解密后再执行（如果是XIP image，则是原地边解密边执行（动态解密）；如果是Non-XIP Image，则解密执行流程与HAB加密类似）。  
> * HAB加密仅支持Non-XIP Image（不限Boot Device），而BEE加密仅支持在FlexSPI NOR中启动的Image（不限XIP/Non-XIP）。  
> * HAB加密区域不可指定（默认全部用户Image区域），而BEE加密的区域可由用户指定。  

![NXP-MCUBootUtility_secboot4_bee_encrypted_fixed_key](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot4_bee_encrypted_fixed_key_e.png)

　　【Secure Boot Type】选择“BEE Encrypted Image Boot”，然后配置所有签名认证的参数（如果本地已有证书，可以不用配置，软件会尝试复用），再点击【Browse】按钮选择一个原始image文件（必须是XIP在FlexSPI NOR中的image），【Key Storage Region】选择“Fixed Otpmk(SNVS) Key”后点击【Advanced Key Settings】按钮配置所有BEE加密的参数，最后点击【All-In-One Action】按钮即可完成bootable image生成与下载所有操作。  
　　上图中Step6操作主要确认一点：BEE_KEY0_SEL是否设置的是From OTPMK[255:128]（Fuse 0x460[31:0]的bit13,12为2'b10）。Step7操作之后可以看到下载进Boot Deivce里的Bootable image从IVT开始全是密文，本示例仅启用一块加密区域，具体对哪些区域进行加密是在【Advanced Key Settings】里指定的，最大支持指定3块加密区域。  
　　有必要对如下使用Fixed Otpmk(SNVS) Key加密的BEE参数设置页面再做一下介绍，主要是设置Region Count以及指定Region范围，默认为0即自动对整个image区域进行加密。  

![NXP-MCUBootUtility_fixedSnvsKeyWin](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_fixedSnvsKeyWin.PNG)

　　一切操作无误，板子上SW7拨码开关将Boot Mode设为2'b10即Internal Boot模式，并且将BT_CFG[1]设为1'b1（使能Encrypted XIP），其余保持全0，重新上电便可以看到BEE encrypted image正常执行了。  
　　BEE加密相比HAB加密是要更安全的，因为HAB加密毕竟仅能静态解密，当HAB解密完成之后在SRAM/SDRAM中存储的是全部的image明文，如果此刻黑客去非法访问SRAM/SDRAM是有可能获取全部image明文的（不过也不用担心，i.MXRT可以设置JTAG访问权限）；而BEE加密可以是动态解密，CPU执行到什么地方才会去解密什么地方，任何时候都不存在完整的image明文，黑客永远无法获取全部的image明文。  

##### 3.3.5 模式五：启用双引擎BEE加密（用户自定义Key）
　　第五种模式是顶级的安全模式，即用用户自定义Key对image进行双引擎BEE级加密，跟第四种模式（单引擎）原理类似，一般用于对产品安全性要求最高的场合。单引擎BEE加密与双引擎BEE加密具体区别如下：  

> * 唯一SNVS Key单引擎BEE加密默认使用SNVS Key，芯片出厂已预先烧录，无法更改；用户自定义Key双引擎BEE加密使用的Key是由用户自己设的，需要手动烧录在Fuse SW_GP2和GP4区域。  
> * 唯一SNVS Key单引擎BEE加密只启用了BEE引擎0；用户自定义Key双引擎BEE加密可以同时启用BEE引擎0和引擎1。但需要注意的是无论启动几个BEE引擎，最大加密区域总数均是3个。  
> * 唯一SNVS Key单引擎BEE加密必须要配合HAB签名一起使用，因为只有在HAB Closed的状态下才能获取SNVS Key；用户自定义Key双引擎BEE加密不一定要使用HAB签名。  

![NXP-MCUBootUtility_secboot5_bee_encrypted_flexible_key](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_secboot5_bee_encrypted_flexible_key_e.png)

　　【Secure Boot Type】选择“BEE Encrypted Image Boot”，【Enable Certificate For BEE Encryption】选择是否要使能HAB签名，然后点击【Browse】按钮选择一个原始image文件（必须是XIP在FlexSPI NOR中的image），【Key Storage Region】选择“Flexible User Keys”后点击【Advanced Key Settings】按钮配置所有BEE加密的参数，最后点击【All-In-One Action】按钮即可完成bootable image生成与下载所有操作。  
　　上图中Step6操作主要确认两点：一、BEE_KEY0_SEL是否设置正确（Fuse 0x460[31:0]的bit13,12）和BEE_KEY1_SEL是否设置正确（Fuse 0x460[31:0]的bit15,14）；二、用户Key是否被正确烧录（SW_GP2: Fuse 0x690 - 0x6c0，GP4: Fuse 0x8c0 - 0x8f0）或锁住。  
　　有必要对如下使用Flexible User Keys加密的BEE参数设置页面再做一下介绍，首先是选择要激活的BEE引擎，可以单独激活BEE引擎0，也可以单独激活BEE引擎1，当然更可以同时激活BEE引擎0和1，本示例同时激活BEE引擎0和1。指定了BEE引擎后需要进一步为该引擎配置加密所使用的Key的存储空间以及需要用户手动输入Key（128bits）。最后还需要设置加密保护的区域，本示例共使能加密2个区域，分别为0x60001000 - 0x60001fff（由BEE引擎0保护），0x60003000 - 0x60003fff（由BEE引擎1保护）。  

![NXP-MCUBootUtility_flexibleUserKeysWin](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_flexibleUserKeysWin_e.png)

　　为了确认image是否按指定区域加密，你可以打开\NXP-MCUBootUtility\gen\bootable_image\文件夹下面生成的未加密bootable image文件与image回读窗口里的内容进行比对。  
　　一切操作无误，板子上SW7拨码开关将Boot Mode设为2'b10即Internal Boot模式，并且将BT_CFG[1]设为1'b1（使能Encrypted XIP），其余保持全0，重新上电便可以看到BEE encrypted image正常执行了。  
　　双引擎BEE加密是将用户自定义的Key烧录进了Fuse SW_GP2/GP4区域里，但该区域的Fuse内容是可以回读的，如果黑客拿到Key，还是有可能破解存在外部Boot Device里的image密文，有没有对Fuse SW_GP2/GP4区域进行保护的方法？当然有，你可以对指定的Fuse区域进行加锁，可设置Fuse区域访问权限（读保护，写保护，覆盖保护），具体后面有单独章节详细介绍。NXP-MCUBootUtility工具为了安全考虑，直接将SW_GP2/GP4区域锁了起来。  
　　双引擎BEE加密相比单引擎BEE加密，从破解角度来说难度加倍，毕竟可以启用两组不同的Key来共同保护image不被非法获取。  

#### 3.4 生成.sb格式文件
　　在菜单栏Tools/Generate .sb file选项里勾选"Yes"，此时点击【All-In-One Action】按钮便会在\NXP-MCUBootUtility\gen\sb_image\目录下生成.sb格式的文件，该文件可用于MfgTool或者RT-Flash工具中。注意此时【All-In-One Action】按钮并不会在MCU上真正地执行3.3节里的各种操作，而只是将所有命令操作记录在\NXP-MCUBootUtility\gen\bd_file\imx_application_sb_gen.bd里，最终用于生成.sb格式文件。  

![NXP-MCUBootUtility_setGenerateSbFile](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_2_0_setGenerateSbFile.PNG)

> Note1: .sb格式文件生成有一个限制，即每次生成新.sb文件均需要重新连接，点击【Reset device】按钮后回到初始连接状态，然后点击【Connect to ROM】按钮。  
> Note2: 当.sb文件中包含必要的efuse操作时，会一次性生成3个.sb格式文件，其中application_device.sb包含全部的操作（flash+efuse操作），application_device_flash.sb仅包含flash操作，application_device_efuse.sb仅包含efuse操作，这样做的目的是为了方便工厂量产。  
> Note3: 对于NOR Flash（FlexSPI NOR、LPSPI NOR）型的启动设备生成.sb文件而言，既可连接板子在线操作（推荐），也可以不用连接板子离线操作。  
> Note4: eFuse Operation Utility窗口里的【Scan】、【Burn】按钮可用于生成仅含自定义efuse操作的.sb文件，需要先点【Scan】按钮，然后填入想烧写的efuse值，最后再点【Burn】按钮便可在\NXP-MCUBootUtility\gen\sb_image\下生成burn_efuse.sb文件。  

### 4 软件进阶
　　NXP-MCUBootUtility软件打开默认工作在Entry Mode下，可通过功能菜单栏Tools->Option选择进入Master Mode，在Master模式下开放了一些高级功能，适用于对NXP MCU芯片以及Boot ROM非常熟悉的用户。  

![NXP-MCUBootUtility_setToolRunMode](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_2_0_setToolRunMode.PNG)

#### 4.1 分步连接设备
　　进入Master模式下，可以不勾选One Step选项，这样可以单步去连接目标设备，单步连接的主要意义在于，可以在不配置Boot Device的情况下仅连接到Flashloader去实现eFuse操作。  

![NXP-MCUBootUtility_nonOneStepConnection](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_nonOneStepConnection.png)

#### 4.2 专用eFuse烧写器
　　进入Master模式下，可以看到eFuse全部区域都开放了，你可以任意烧写指定的eFuse区域。eFuse操作是按bit一次性的（类似熔丝烧断），只能将0烧写成1，烧录成1之后便无法更改，所以eFuse的操作需要特别谨慎。  

![NXP-MCUBootUtility_fuseUnderMasterMode](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_0_0_fuseUnderMasterMode.PNG)

　　在上一章节安全加密启动过程中，我们会烧录SRKH(0x580 - 0x5f0)、SW_GP2(0x690 - 0x6c0)、GP4(0x8c0 - 0x8f0)，这些区域一经烧录便不得更改，甚至我们希望这些区域不仅不能被更改，也要不能被回读。  

![NXP-MCUBootUtility_fuseLockerBits](http://henjay724.com/image/cnblogs/nxpSecBoot_fuseLockerBits.PNG)

　　从上图可知eFuse 0x400即是各Fuse功能区域的Locker，我们可以通过烧录eFuse 0x400来锁住SW_GP2, GP4区域。那么如何烧录呢？其实非常简单，直接在各eFuse框内填写想要烧录的值，点击【Burn】按钮即可。  

　　对于一些混合功能的eFuse区域，除了可以在对应框内直接填写想要烧录的值外，也可以点击索引按钮，在弹出的界面里编辑：  

![NXP-MCUBootUtility_fuseViewer](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_4_0_fuseViewer.PNG)

#### 4.3 专用FlexRAM编程器
　　进入Master模式下，可以点击【Read】、【Write】、【Execute】按钮实现FlexRAM的任意读/写/执行操作，这样可以将NXP-MCUBootUtility工具当做专用FlexRAM编程器。  

![NXP-MCUBootUtility_flexramProgrammer](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_5_0_flexramProgrammer_e.png)

#### 4.4 通用Flash编程器
　　进入Master模式下，可以点击【Read】、【Erase】、【Write】按钮实现已配置Flash的任意读/擦/写操作，这样可以将NXP-MCUBootUtility工具当做通用Flash编程器。  

![NXP-MCUBootUtility_flashProgrammer](http://henjay724.com/image/cnblogs/nxpSecBoot_v1_5_0_flashProgrammer_e.png)
