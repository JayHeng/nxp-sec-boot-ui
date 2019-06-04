set peripheral=-p com4,115200
blhost %peripheral% -- efuse-program-once  0x000000A9  55020103
blhost %peripheral% -- efuse-program-once  0x000000AA  130171d9
blhost %peripheral% -- efuse-program-once  0x000000AB  4400F240
blhost %peripheral% -- efuse-program-once  0x000000AC  0400F6C0
blhost %peripheral% -- efuse-program-once  0x000000AD  47709400
blhost %peripheral% -- efuse-program-once  0x000000AE  55020103
blhost %peripheral% -- efuse-program-once  0x000000AF  1301720b
blhost %peripheral% -- efuse-program-once  0x000000B0  4400F240
blhost %peripheral% -- efuse-program-once  0x000000B1  0400F6C0
blhost %peripheral% -- efuse-program-once  0x000000B2  47709400

::alias KBL-4586 
blhost %peripheral% -- efuse-program-once  0x000000B3  55020106
blhost %peripheral% -- efuse-program-once  0x000000B4  13011815
blhost %peripheral% -- efuse-program-once  0x000000B5  F64F9901
blhost %peripheral% -- efuse-program-once  0x000000b6  F6CE72FF
blhost %peripheral% -- efuse-program-once  0x000000b7  EA0172FF
blhost %peripheral% -- efuse-program-once  0x000000b8  F04F0102
blhost %peripheral% -- efuse-program-once  0x000000b9  91010204
blhost %peripheral% -- efuse-program-once  0x000000ba  47709202 

::spi KBL-4189 

blhost %peripheral% -- efuse-program-once  0x000000bb  55020102 
blhost %peripheral% -- efuse-program-once  0x000000bc  13002941 
blhost %peripheral% -- efuse-program-once  0x000000bd  90002007 
blhost %peripheral% -- efuse-program-once  0x000000be  47704770 

::emmc KBL-4662

blhost %peripheral% -- efuse-program-once  0x000000bf  55020104 
blhost %peripheral% -- efuse-program-once  0x000000c0  13018637 
blhost %peripheral% -- efuse-program-once  0x000000c1  F2426820 
blhost %peripheral% -- efuse-program-once  0x000000c2  4A017110 
blhost %peripheral% -- efuse-program-once  0x000000c3  47704710 
blhost %peripheral% -- efuse-program-once  0x000000c4  130196E3 

::EMMC KBL-4661 
blhost %peripheral% -- efuse-program-once  0x000000c5  55020107 
blhost %peripheral% -- efuse-program-once  0x000000c6  1301796B 
blhost %peripheral% -- efuse-program-once  0x000000c7  BF1C2E00 
blhost %peripheral% -- efuse-program-once  0x000000c8  47709600 
blhost %peripheral% -- efuse-program-once  0x000000c9  0040980D 
blhost %peripheral% -- efuse-program-once  0x000000ca  6D21BF42 
blhost %peripheral% -- efuse-program-once  0x000000cb  7180F441 
blhost %peripheral% -- efuse-program-once  0x000000cc  96006521 
blhost %peripheral% -- efuse-program-once  0x000000cd  47704770 

::emmc fastboot  KBL-4718  
blhost %peripheral% -- efuse-program-once  0x000000CE  55010001
blhost %peripheral% -- efuse-program-once  0x000000CF  13018a69
blhost %peripheral% -- efuse-program-once  0x000000D0  e01670f5
pause