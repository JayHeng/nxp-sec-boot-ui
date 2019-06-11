```text
  为了便于大家快速验证软件HAB加密功能，特将已开启HAB加密功能的cst工具上传至百度网盘，仅用作个人学习用途，违者后果自负。
  -- 链接: https://pan.baidu.com/s/1lcFverYPDDp0qjxCcWpkug
  -- 提取码: 3873
  使用方法：将下载到的压缩包cst_3.0.1_hab_crypto.zip解压后将其所有文件拷贝到 \NXP-MCUBootUtility\tools\cst 文件夹下即可。
```

### 1 Reason for enabling HAB encryption function 为什么要开启HAB加密功能
　　NXP-MCUBootUtility is a tool designed for NXP MCU secure encryption boot. It fully supports secure encryption boot functions (signature only, signature and encryption) based on HAB implementation. HAB related functions are based on NXP's official HAB enablement tools. Due to the restriction of export control on security product, HAB Code Signing Tool cannot be directly integrated into NXP-MCUBootUtility installation package, so if you want to enbale HAB signature and encryption function for NXP-MCUBootUtility, You need to add HAB Code Signing Tool into NXP-MCUBootUtility manually. This article teaches you how to add HAB Code Signing Tool into NXP-MCUBootUtility to activate HAB encryption function.  

　　NXP-MCUBootUtility是一个专为NXP MCU安全加密启动而设计的工具，其能完整支持基于HAB实现的安全加密启动（单签名，签名和加密），而HAB相关的功能是借助恩智浦官方的HAB Code Signing Tool工具来实现的，HAB Code Signing Tool跟安全加密有关，因为一些跟欧美出口管制有关的原因，NXP-MCUBootUtility不能够直接将HAB Code Signing Tool工具集成到软件安装包里，所以如果要在NXP-MCUBootUtility里开启HAB签名和加密功能，需要自己将HAB Code Signing Tool工具添加到NXP-MCUBootUtility里，本篇文章即教大家如何添加HAB Code Signing Tool工具进NXP-MCUBootUtility以激活HAB加密功能。  

### 2 Enable HAB signature function first 首先开启HAB签名功能
　　First, you need to refer to [《开启NXP-MCUBootUtility工具的HAB签名功能 - CST》](https://www.cnblogs.com/henjay724/p/10189593.html), This article teaches you to add the CST tool into NXP-MCUBootUtility and activates the HAB signature function, the prerequisite for activating HAB encryption function is to enable HAB signature function.  

　　首先参照 [《开启NXP-MCUBootUtility工具的HAB签名功能 - CST》](https://www.cnblogs.com/henjay724/p/10189593.html) 这篇文章教你将CST工具添加进NXP-MCUBootUtility里并激活HAB签名功能，激活HAB加密的前提是使能HAB签名。  

### 3 Regenerate cst.exe with AES encryption function 重新生成含AES加密功能的cst.exe
　　The signature and encryption functions of NXP-MCUBootUtility are implemented by calling \NXP-MCUBootUtility\tools\cst\mingw32\bin\cst.exe. The cs.exe in the CST package downloaded from NXP's official website does not include AES encryption function by default. So we need to recompile and generate cst.exe with AES encryption function.  

　　NXP-MCUBootUtility的签名和加密功能均是通过调用\NXP-MCUBootUtility\tools\cst\mingw32\bin\cst.exe实现的，从恩智浦官网下载的CST包里的cst.exe默认没有开启AES加密功能，因此我们需要重新编译生成含AES加密功能的cst.exe。  

#### 3.1 Install gcc under MSYS2 在MSYS2下安装gcc
　　First, you need to download the msys2 installation package on the website [http://www.msys2.org/](http://www.msys2.org/) and select the appropriate installation package according to your system (x86_64 is for 64bit system, i686 is for 32bit systems), We choose msys2-x86_64-20180531.exe here. After the installation is complete, open the MSYS2 MSYS console from the Start menu.  

　　首先在网站 [http://www.msys2.org/](http://www.msys2.org/) 下载msys2的安装包，根据你的系统选择合适的安装包（x86_64适用于64bit系统，i686适用于32bit系统），这里选择的是msys2-x86_64-20180531.exe，安装完成后从开始菜单里打开MSYS2 MSYS控制台。  

![msys2StartMenuMysy](http://henjay724.com/image/cnblogs/nxpSecBoot_msys2StartMenuMysy.PNG)

　　Execute the following four commands in sequence, and just input y when encountering ":: Proceed with installation? [Y/n]" questions. Note that you may need to close the console and reopen after the first command is executed. After successful execution of all commands, the basic configuration of MSYS2 and the installation of standard packages and gcc for compilation are completed.  

　　依次执行如下四条命令，遇到":: Proceed with installation? [Y/n]"询问全部输入y，注意第一条命令执行后可能需要关闭控制台重新打开。所有命令正常执行结束后便完成了MSYS2的基础更新配置以及用于编译的标准包和gcc的安装。  

> jay@pc MSYS ~
> <font style="font-weight:bold;" color="Blue">$ pacman -Syu</font>
> <font style="font-weight:bold;" color="Blue">$ pacman -Su</font>
> <font style="font-weight:bold;" color="Blue">$ pacman -S –-needed base-devel</font>
> <font style="font-weight:bold;" color="Blue">$ pacman -S mingw-w64-i686-gcc</font>

#### 3.2 Compile openssl under MinGW 在MinGW下编译openssl
　　Then download the openssl source package on the website [https://www.openssl.org/](https://www.openssl.org/), it is recommended to select the 1.0.x version (1.1.x version seems to  have issues). We choose openssl-1.0.2q.tar.gz here. After downloading, decompress it and place it in the \NXP-MCUBootUtility\tools\openssl\ directory. Open the MSYS2 MinGW 32-bit console from the Start menu.  

　　然后在网站 [https://www.openssl.org/](https://www.openssl.org/) 下载openssl的源码包，推荐选择1.0.x版本（1.1.x版本经测试有问题），这里选择的是openssl-1.0.2q.tar.gz，下载完成后将其解压放置到\NXP-MCUBootUtility\tools\openssl\目录下，从开始菜单里打开MSYS2 MinGW 32-bit控制台。  

![msys2StartMenuMingw32](http://henjay724.com/image/cnblogs/nxpSecBoot_msys2StartMenuMingw32.PNG)

　　Use the cd command to checkout to the \NXP-MCUBootUtility\tools\openssl\openssl-1.0.2q directory and execute the following three commands in sequence. Note that the second command takes a little longer time (about 10 minutes). Please be patient.  

　　使用cd命令切换到\NXP-MCUBootUtility\tools\openssl\openssl-1.0.2q目录下，依次执行如下三条命令，注意第二条命令执行时间稍长（大约10分钟），请耐心等待。  

> jay@pc MINGW32 /d/NXP-MCUBootUtility/tools/openssl/openssl-1.0.2q
> <font style="font-weight:bold;" color="Blue">$ ./config</font>
> <font style="font-weight:bold;" color="Blue">$ make</font>
> <font style="font-weight:bold;" color="Blue">$ cp ms/applink.c include/openssl/</font>

#### 3.3 Generate cst.exe under MinGW 在MinGW下生成cst.exe
　　Use the cd command to checkout to the \NXP-MCUBootUtility\tools\cst\code\back_end\src directory and execute the following two commands in sequence.  

　　继续在MSYS2 MinGW 32-bit控制台下操作，使用cd命令切换到\NXP-MCUBootUtility\tools\cst\code\back_end\src目录下，依次执行如下两条命令。  

> jay@pc MINGW32 /d/NXP-MCUBootUtility/tools/cst/code/back_end/src
> <font style="font-weight:bold;" color="Blue">$ gcc *.c -o cst.exe -I ../hdr -I ../../../../openssl/openssl-1.0.2q/include/ -L ../../../mingw32/lib/ -L ../../../../openssl/openssl-1.0.2q -lfrontend -lcrypto -lgdi32 -static </font>
> <font style="font-weight:bold;" color="Blue">$ cp cst.exe ../../../mingw32/bin/</font>

　　At this point, the HAB encryption function is also activated. Open the NXP-MCUBootUtility and select the "HAB Encrypted Image Boot" mode in the Secure Boot Type and then enjoy it.  

　　至此NXP-MCUBootUtility的HAB加密功能也被激活了，打开NXP-MCUBootUtility软件，在Secure Boot Type里选择"HAB Encrypted Image Boot"模式试试吧。  

![enableHabEncryptFunc](http://henjay724.com/image/cnblogs/nxpSecBoot_enableHabEncryptFunc.PNG)
