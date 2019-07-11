import sys, os

kBootImageTypeFlag_Unsigned  = '0x00'
kBootImageTypeFlag_Signed    = '0x08'
kBootImageTypeFlag_Encrypted = '0x0c'

kBootImageCsfHeaderVersion_Signed    = '4.2'
kBootImageCsfHeaderVersion_Encrypted = '4.3'

kSecKeyLengthInBits_SRK = 256
kSecKeyLengthInBits_DEK = 128

kSecFacRegionAlignedUnit_Bee   = 0x400
kSecFacRegionAlignedUnit_Otfad = 0x1000

#define NOR_EEPROM_IROM_DATA_HEADER_OFFSET      (0x400)
#define FLEXSPI_NOR_IROM_DATA_HEADER_OFFSET     (0x1000)
#define FLEXSPI_NAND_IROM_DATA_HEADER_OFFSET    (0x400)
#define SEMC_NOR_IROM_DATA_HEADER_OFFSET        (0x1000)
#define SEMC_NAND_IROM_DATA_HEADER_OFFSET       (0x400)
#define CARD_IROM_DATA_HEADER_OFFSET            (0x400)

kIvtOffset_NAND_SD_EEPROM  = 0x400
kIvtOffset_NOR             = 0x1000
kIvtOffset_RAM_FLASHLOADER = 0x0

#define SPI_NOR_EEPROM_4K_SIZE                  (4096U)
#define FLEXSPI_NOR_INIT_IMG_SIZE               (12u * 1024u)
#define FLEXSPI_NAND_4K_SIZE                    (4096U)
#define SEMC_NOR_INIT_IMG_SIZE                  (12u * 1024u)
#define SEMC_NAND_4K_SIZE                       (4096U)
#define CARD_IROM_INIT_IMAGE_SIZE               (4096U)

kInitialLoadSize_NAND_SD_EEPROM  = 0x1000
kInitialLoadSize_NOR             = 0x2000
kInitialLoadSize_RAM_FLASHLOADER = 0x200

kUserDcdFileType_Bin = 0x0
kUserDcdFileType_Cfg = 0x1

kStdDcdFilename_Bin = 'dcd.bin'
kStdDcdFilename_Cfg = 'dcd.cfg'

kSbFileType_All   = 0x0
kSbFileType_Flash = 0x1
kSbFileType_Efuse = 0x2

