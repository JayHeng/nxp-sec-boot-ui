```text
  为了便于大家快速验证软件HAB签名功能，特将已开启HAB签名功能的cst工具上传至百度网盘，仅用作个人学习用途，违者后果自负。
  -- 链接: https://pan.baidu.com/s/15kFA3qwwFyY4BuL3ZpDqSQ
  -- 提取码: rivb
  使用方法：将下载到的压缩包cst_3.0.1_hab_auth.zip解压后将其所有文件拷贝到 \NXP-MCUBootUtility\tools\cst 文件夹下即可。
```

### 1 Reason for enabling HAB signature function 为什么要开启HAB签名功能
　　NXP-MCUBootUtility is a tool designed for NXP MCU secure encryption boot. It fully supports secure encryption boot functions (signature only, signature and encryption) based on HAB implementation. HAB related functions are based on NXP's official HAB enablement tools. Due to the restriction of export control on security product, HAB Code Signing Tool cannot be directly integrated into NXP-MCUBootUtility installation package, so if you want to enbale HAB signature and encryption function for NXP-MCUBootUtility, You need to add HAB Code Signing Tool into NXP-MCUBootUtility manually. This article teaches you how to add HAB Code Signing Tool into NXP-MCUBootUtility to activate HAB signature function.  

　　NXP-MCUBootUtility是一个专为NXP MCU安全加密启动而设计的工具，其能完整支持基于HAB实现的安全加密启动（单签名，签名和加密），而HAB相关的功能是借助恩智浦官方的HAB Code Signing Tool工具来实现的，HAB Code Signing Tool跟安全加密有关，因为一些跟欧美出口管制有关的原因，NXP-MCUBootUtility不能够直接将HAB Code Signing Tool工具集成到软件安装包里，所以如果要在NXP-MCUBootUtility里开启HAB签名和加密功能，需要自己将HAB Code Signing Tool工具添加到NXP-MCUBootUtility里，本篇文章即教大家如何添加HAB Code Signing Tool工具进NXP-MCUBootUtility以激活HAB签名功能。  

### 2 Download the HAB Code Signing Tool 下载HAB CST包
　　First, you need to download [HAB Code Signing Tool](https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX_CST_TOOL&appType=file2&location=null&DOWNLOAD_ID=null&lang_cd=en) from the NXP official website. before downloading, The following web page will pop up, click 'I Accept' and then you can download cst-3.1.0.tgz (downloaded at 2018.12, the version may change over time).　

　　首先需要从NXP官网下载 [HAB CST工具](https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX_CST_TOOL&appType=file2&location=null&DOWNLOAD_ID=null&lang_cd=en)，下载前会弹出如下界面，点击'I Accept'后便可以下载到cst-3.1.0.tgz（下载于2018.12，随着时间推移，版本会有所变化）。  

![agreementToDownloadCST](http://henjay724.com/image/cnblogs/nxpSecBoot_agreementToDownloadCST.PNG)

　　This Agreement clause must be read through and agreed, This step must be done. This is one of the reasons why CST tool can not be directly put into NXP-MCUBootUtility package.  

　　这个Agreement条款必须要通读并且要同意才可以下载CST工具，这一步是必须要做的，这也是NXP-MCUBootUtility不直接将CST工具放到软件包里的原因之一。  

### 3 Placed in the \NXP-MCUBootUtility\tools\cst\ directory 放置于\NXP-MCUBootUtility\tools\cst\目录下
　　After downloading the cst-3.1.0.tgz package, unzip it into \NXP-MCUBootUtility\tools\cst \ directory as shown below:  

　　下载到cst-3.1.0.tgz包后将其解压（需要2次解压才能看到\cst-3.1.0\cst-3.1.0\release里的内容）放在\NXP-MCUBootUtility\tools\cst\目录下即可，如下图所示：  

![putCstIntoFolder](http://henjay724.com/image/cnblogs/nxpSecBoot_putCstIntoFolder.PNG)

### 4 Change the hab4_pki_tree.bat script 改动hab4_pki_tree.bat脚本
　　The HAB signature certificate generation function in NXP-MCUBootUtility is implemented by calling the \NXP-MCUBootUtility\tools\cst\keys\hab4_pki_tree.bat script. You need to make the following minor changes to this script to use it for NXP-MCUBootUtility.  

　　NXP-MCUBootUtility里的HAB签名证书生成功能是调用\NXP-MCUBootUtility\tools\cst\keys\hab4_pki_tree.bat脚本实现的，需要对该脚本做如下轻微改动才可以为NXP-MCUBootUtility所用。  

　　First, You need to comment the following 6 lines of code：  

　　首先需要注释如下6行代码：  
```bash
:: Comment line 72 注释第72行
::set /P existing_ca="Do you want to use an existing CA key (y/n)?: "
:: Comment line 80 注释第80行
::set /P use_ecc="Do you want to use Elliptic Curve Cryptography (y/n)?: "
:: Comment line 104 注释第104行
::set /P kl="Enter key length in bits for PKI tree: "
:: Comment line 115 注释第115行
::set /P duration="Enter PKI tree duration (years): "
:: Comment line 121 注释第121行
::set /P num_srk="How many Super Root Keys should be generated? "
:: Comment line 133 注释第133行
::set /P srk_ca="Do you want the SRK certificates to have the CA flag set? (y/n)?: "
```

　　Then you need to add the following 6 lines of code starting from line 2.：  

　　然后需要从第2行开始添加如下6行代码：  

```bash
@echo off

:: Add below codes 如下为新增代码
set existing_ca=%1
set use_ecc=n
set kl=%2
set duration=%3
set num_srk=%4
set srk_ca=%5
```

　　At this point, the HAB signature function of NXP-MCUBootUtility is activated. Open the NXP-MCUBootUtility and select the "HAB Signed Image Boot" mode in the Secure Boot Type and then enjoy it. If you want to go on activating the HAB encryption function of the NXP-MCUBootUtility, please refer to [《开启NXP-MCUBootUtility工具的HAB加密功能 - CST》](https://www.cnblogs.com/henjay724/p/10219459.html).  

　　至此NXP-MCUBootUtility的HAB签名功能便被激活了，打开NXP-MCUBootUtility软件，在Secure Boot Type里选择"HAB Signed Image Boot"模式试试吧。如果要继续激活NXP-MCUBootUtility软件的HAB加密功能，请继续参考 [《开启NXP-MCUBootUtility工具的HAB加密功能 - CST》](https://www.cnblogs.com/henjay724/p/10219459.html)  

![enableHabSignFunc](http://henjay724.com/image/cnblogs/nxpSecBoot_enableHabSignFunc.PNG)
