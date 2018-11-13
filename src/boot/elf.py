#!/usr/bin/env python
import struct

# ELF object file reader
# (C) 2003 cliechti@gmx.net
# Python license

#            size  alignment
# Elf32_Addr    4  4  Unsigned program address
# Elf32_Half    2  2  Unsigned medium integer
# Elf32_Off     4  4  Unsigned file offset
# Elf32_Sword   4  4  Signed large integer
# Elf32_Word    4  4  Unsigned large integer
# unsignedchar  1  1  Unsigned small integer

#define EI_NIDENT 16
#~ typedef struct{
    #~ unsigned char e_ident[EI_NIDENT];
    #~ Elf32_Half e_type;
    #~ Elf32_Half e_machine;
    #~ Elf32_Word e_version;
    #~ Elf32_Addr e_entry;
    #~ Elf32_Off  e_phoff;
    #~ Elf32_Off  e_shoff;
    #~ Elf32_Word e_flags;
    #~ Elf32_Half e_ehsize;
    #~ Elf32_Half e_phentsize;
    #~ Elf32_Half e_phnum;
    #~ Elf32_Half e_shentsize;
    #~ Elf32_Half e_shnum;
    #~ Elf32_Half e_shstrndx;
#~ } Elf32_Ehdr;


#Section Header
#~ typedef struct {
    #~ Elf32_Word sh_name;
    #~ Elf32_Word sh_type;
    #~ Elf32_Word sh_flags;
    #~ Elf32_Addr sh_addr;
    #~ Elf32_Off  sh_offset;
    #~ Elf32_Word sh_size;
    #~ Elf32_Word sh_link;
    #~ Elf32_Word sh_info;
    #~ Elf32_Word sh_addralign;
    #~ Elf32_Word sh_entsize;
#~ } Elf32_Shdr; 

#~ typedef struct {
    #~ Elf32_Word p_type;
    #~ Elf32_Off  p_offset;
    #~ Elf32_Addr p_vaddr;
    #~ Elf32_Addr p_paddr;
    #~ Elf32_Word p_filesz;
    #~ Elf32_Word p_memsz;
    #~ Elf32_Word p_flags;
    #~ Elf32_Word p_align;
#~ } Elf32_Phdr;

# struct Elf32_Sym
# {
#   Elf32_Word st_name;     //!< Index into file's string table.
#   Elf32_Addr st_value;    //!< Value associated with the symbol. Depends on context.
#   Elf32_Word st_size;     //!< Size associated with symbol. 0 if the symbol has no size or an unknown size.
#   unsigned char st_info;  //!< Specified the symbol's type and binding attributes.
#   unsigned char st_other; //!< Currently 0 (reserved).
#   Elf32_Half st_shndx;    //!< Section header table index for this symbol.
# };


class ELFException(Exception): pass

class ELFSymbol:
    Elf32_Sym = "<IIIBBH"
    
    STB_LOCAL = 0,  # Local symbol not visible outside the object file.
    STB_GLOBAL = 1  # Symbol is visible to all object files being linked together.
    STB_WEAK = 2    # Like global symbols, but with lower precedence.
    STB_LOPROC = 13
    STB_HIPROC = 15
    
    STT_NOTYPE = 0  # The symbol's type is not specified.
    STT_OBJECT = 1  # The symbol is associated with a data object, such as a variable or array.
    STT_FUNC = 2    # The symbol is associated with a function or other executable code.
    STT_SECTION = 3 # The synmbol is associated with a section. Primarily used for relocation.
    STT_FILE = 4    # A file symbol has STB_LOCAL binding, its section index is SHN_ABS, and it precedes the other STB_LOCAL symbols for the file, if it is present.
    STT_LOPROC = 13 # Low bound of processor-specific symbol types.
    STT_HIPROC = 15 # High bound of processor-specific symbol types.

    ARM_SEQUENCE_MAPSYM = "$a"
    DATA_SEQUENCE_MAPSYM = "$d"
    THUMB_SEQUENCE_MAPSYM = "$t"

    THUMB_BL_TAGSYM = "$b"
    FN_PTR_CONST_TAGSYM = "$f"
    INDIRECT_FN_CALL_TAGSYM = "$p"
    MAPPING_SYMBOL_COUNT_TAGSYM = "$m"
    
    def __init__(self):
        (self.st_name, self.st_value, self.st_size, self.st_info,
            self.st_other, self.st_shndx, self.st_bind, self.st_type) = [0] * 8
        self.name = None
    
    def fromString(self, s):
        (self.st_name, self.st_value, self.st_size, self.st_info,
            self.st_other, self.st_shndx) = struct.unpack(self.Elf32_Sym, s)
        self.st_bind = (self.st_info >> 4) & 0x0f
        self.st_type = self.st_info & 0x0f
    
    def __repr__(self):
        return "%s(%s, st_value=0x%08x, st_size=%d, st_bind=%d, st_type=%d, st_shndx=%d)" % (
            self.__class__.__name__,
            self.name is not None and "%r" % self.name or "st_name=%s" % self.st_name,
            self.st_value, self.st_size, self.st_bind, self.st_type, self.st_shndx)
    

class ELFSection:
    """read and store a section"""
    Elf32_Shdr = "<IIIIIIIIII"          #header format
    
    #section types
    SHT_NULL        = 0
    SHT_PROGBITS    = 1
    SHT_SYMTAB      = 2
    SHT_STRTAB      = 3
    SHT_RELA        = 4
    SHT_HASH        = 5
    SHT_DYNAMIC     = 6
    SHT_NOTE        = 7
    SHT_NOBITS      = 8
    SHT_REL         = 9
    SHT_SHLIB       = 10
    SHT_DYNSYM      = 11
    SHT_LOPROC      = 0x70000000L
    SHT_HIPROC      = 0x7fffffffL
    SHT_LOUSER      = 0x80000000L
    SHT_HIUSER      = 0xffffffffL
    #section attribute flags
    SHF_WRITE       = 0x1
    SHF_ALLOC       = 0x2
    SHF_EXECINSTR   = 0x4
    SHF_MASKPROC    = 0xf0000000

    def __init__(self):
        """creat a new empty section object"""
        (self.sh_name, self.sh_type, self.sh_flags, self.sh_addr,
         self.sh_offset, self.sh_size, self.sh_link, self.sh_info,
         self.sh_addralign, self.sh_entsize) = [0]*10
        self.name = None
        self.data = None
        self.lma =  None

    def fromString(self, s):
        """get section header from string"""
        (self.sh_name, self.sh_type, self.sh_flags, self.sh_addr,
         self.sh_offset, self.sh_size, self.sh_link, self.sh_info,
         self.sh_addralign, self.sh_entsize) = struct.unpack(self.Elf32_Shdr, s)
         
    def __repr__(self):
        """pretty print for debug..."""
        return "%s(%s, sh_type=%s, sh_flags=%s, "\
               "sh_addr=0x%04x, sh_offset=0x%04x, sh_size=%s, sh_link=%s, "\
               "sh_info=%s, sh_addralign=%s, sh_entsize=%s, lma=0x%04x)" % (
            self.__class__.__name__,
            self.name is not None and "%r" % self.name or "sh_name=%s" % self.sh_name,
            self.sh_type, self.sh_flags, self.sh_addr,
            self.sh_offset, self.sh_size, self.sh_link, self.sh_info,
            self.sh_addralign, self.sh_entsize, self.lma)

class ELFProgramHeader:
    """Store and parse a program header"""
    Elf32_Phdr = "<IIIIIIII"            #header format
    
    #segmet types
    PT_NULL         = 0
    PT_LOAD         = 1
    PT_DYNAMIC      = 2
    PT_INTERP       = 3
    PT_NOTE         = 4
    PT_SHLIB        = 5
    PT_PHDR         = 6
    PT_LOPROC       = 0x70000000L
    PT_HIPROC       = 0x7fffffffL
    
    #segment flags
    PF_R            = 0x4       #segment is readable
    PF_W            = 0x2       #segment is writable
    PF_X            = 0x1       #segment is executable
     
    def __init__(self):
        """create a new, empty segment/program header"""
        (self.p_type, self.p_offset, self.p_vaddr, self.p_paddr,
            self.p_filesz, self.p_memsz, self.p_flags, self.p_align) = [0]*8
        self.data = None

    def fromString(self, s):
        """parse header info from string"""
        (self.p_type, self.p_offset, self.p_vaddr, self.p_paddr,
            self.p_filesz, self.p_memsz, self.p_flags,
            self.p_align) = struct.unpack(self.Elf32_Phdr, s)

    def __repr__(self):
        """pretty print for debug..."""
        return "%s(p_type=%s, p_offset=0x%04x, p_vaddr=0x%04x, p_paddr=0x%04x, "\
            "p_filesz=%s, p_memsz=%s, p_flags=%s, "\
            "p_align=%s)" % (
            self.__class__.__name__,
            self.p_type, self.p_offset, self.p_vaddr, self.p_paddr,
            self.p_filesz, self.p_memsz, self.p_flags,
            self.p_align)

class ELFObject:
    """Object to read and handle an LEF object file"""
    #header information
    Elf32_Ehdr = "<16sHHIIIIIHHHHHH"
    
    #offsets within e_ident
    EI_MAG0         = 0     #File identification
    EI_MAG1         = 1     #File identification
    EI_MAG2         = 2     #File identification
    EI_MAG3         = 3     #File identification
    EI_CLASS        = 4     #File class
    EI_DATA         = 5     #Data encoding
    EI_VERSION      = 6     #File version
    EI_PAD          = 7     #Start of padding bytes
    EI_NIDENT       = 16    #Size of e_ident[]
    #elf file type flags
    ET_NONE         = 0     #No file type
    ET_REL          = 1     #Relocatable file
    ET_EXEC         = 2     #Executable file
    ET_DYN          = 3     #Shared object file
    ET_CORE         = 4     #Core file
    ET_LOPROC       = 0xff00 #Processor-specific
    ET_HIPROC       = 0xffff #Processor-specific
    #ELF format
    ELFCLASSNONE    = 0     #Invalid class
    ELFCLASS32      = 1     #32-bit objects
    ELFCLASS64      = 2     #64-bit objects
    #encoding
    ELFDATANONE     = 0     #Invalid data encoding
    ELFDATA2LSB     = 1     #See below
    ELFDATA2MSB     = 2     #See below

    def __init__(self):
        """create a new elf object"""
        (self.e_ident, self.e_type, self.e_machine, self.e_version,
        self.e_entry, self.e_phoff, self.e_shoff,
        self.e_flags, self.e_ehsize, self.e_phentsize, self.e_phnum,
        self.e_shentsize, self.e_shnum, self.e_shstrndx) = [0]*14

    def fromFile(self, fileobj):
        """read all relevant data from fileobj.
        the file must be seekable"""
        fileobj.seek(0)
        
        #get file header
        (self.e_ident, self.e_type, self.e_machine, self.e_version,
        self.e_entry, self.e_phoff, self.e_shoff,
        self.e_flags, self.e_ehsize, self.e_phentsize, self.e_phnum,
        self.e_shentsize, self.e_shnum, self.e_shstrndx) = struct.unpack(
            self.Elf32_Ehdr, fileobj.read(struct.calcsize(self.Elf32_Ehdr)))
        #verify if its a known format and realy an ELF file
        if self.e_ident[0:4]             != '\x7fELF' and\
           self.e_ident[self.EI_CLASS]   != self.ELFCLASS32 and\
           self.e_ident[self.EI_DATA]    != self.ELFDATA2LSB and\
           self.e_ident[self.EI_VERSION] != 1:
                raise ELFException("Not a valid ELF file")

        #load programm headers
        self.programmheaders = []
        if self.e_phnum:
            #load program headers
            fileobj.seek(self.e_phoff)
            for sectionnum in range(self.e_phnum):
                shdr = (fileobj.read(self.e_phentsize) + '\0'* struct.calcsize(ELFProgramHeader.Elf32_Phdr))[0:struct.calcsize(ELFProgramHeader.Elf32_Phdr)]
                psection = ELFProgramHeader()
                psection.fromString(shdr)
                if psection.p_offset:   #skip if section has invalid offset in file
                    self.programmheaders.append(psection)
            #~ #get the segment data from the file for each prg header
            #~ for phdr in self.programmheaders:
                #~ fileobj.seek(phdr.p_offset)
                #~ phdr.data = fileobj.read(phdr.p_filesz)
                #~ #pad if needed
                #~ if phdr.p_filesz < phdr.p_memsz:
                    #~ phdr.data = phdr.data + '\0' * (phdr.p_memsz-phdr.p_filesz)

        #load sections
        self.sections = []
        fileobj.seek(self.e_shoff)
        for sectionnum in range(self.e_shnum):
            shdr = (fileobj.read(self.e_shentsize) + '\0'* struct.calcsize(ELFSection.Elf32_Shdr))[0:struct.calcsize(ELFSection.Elf32_Shdr)]
            elfsection = ELFSection()
            elfsection.fromString(shdr)
            self.sections.append(elfsection)
        
        #load data for all sections
        for section in self.sections:
            fileobj.seek(section.sh_offset)
            data = fileobj.read(section.sh_size)
            section.data = data
            if section.sh_type == ELFSection.SHT_STRTAB:
                section.values = data.split('\0')
            section.lma = self.getLMA(section)
        
        #get section names
        for section in self.sections:
#             start = self.sections[self.e_shstrndx].data[section.sh_name:]
#             section.name = start.split('\0')[0]
            section.name = self.getString(self.e_shstrndx, section.sh_name)

        # Load symbols.
        symtab = self.getSection('.symtab')
        symsize = symtab.sh_entsize
        self.symbolCount = symtab.sh_size / symsize
        self.symbols = []
        self.symbolDict = {}
        for symnum in range(self.symbolCount):
            # Compute range
            start = symnum * symsize
            end = start + symsize
            
            # Create symbol
            sym = ELFSymbol()
            sym.fromString(symtab.data[start:end])
            
            # Read symbol name string
            sym.name = self.getString(symtab.sh_link, sym.st_name)
            
            # Add to symbol list
            self.symbols.append(sym)
            self.symbolDict[sym.name] = sym
        
    def getString(self, table, index):
        start = self.sections[table].data[index:]
        return start.split('\0')[0]
    
    def getSection(self, name):
        """get section by name"""
        for section in self.sections:
            if section.name == name:
                return section
    
    def getSymbol(self, name):
        return self.symbolDict[name]
    
    def getProgrammableSections(self):
        """get all program headers that are marked as executable and
        have suitable attributes to be code"""
        res = []
        for p in self.programmheaders:
            #~ print p
            #~ if section.sh_flags & self.SHF_ALLOC and section.name not in ('.data', '.data1', '.bss'):
            #~ if p.p_type == ELFProgramHeader.PT_LOAD:# and p.p_paddr == p.p_vaddr and p.p_flags & ELFProgramHeader.PF_X:
            if p.p_type == ELFProgramHeader.PT_LOAD:
                res.append(p)
        return res

    def getLMA(self, section):
        #magic load memory address calculation ;-)
        for p in self.programmheaders:
            if (p.p_paddr != 0 and \
                p.p_type == ELFProgramHeader.PT_LOAD and \
                p.p_vaddr != p.p_paddr and \
                p.p_vaddr <= section.sh_addr and \
                (p.p_vaddr + p.p_memsz >= section.sh_addr + section.sh_size) \
                    and (not (section.sh_flags & ELFSection.SHF_ALLOC and section.sh_type != ELFSection.SHT_NOBITS) \
                    or  (p.p_offset <= section.sh_offset \
                    and (p.p_offset + p.p_filesz >= section.sh_offset + section.sh_size)))):
                return section.sh_addr + p.p_paddr - p.p_vaddr
        return section.sh_addr

    def getSections(self):
        """get sections relevant for the application"""
        res = []
        for section in self.sections:
            if section.sh_flags & ELFSection.SHF_ALLOC and section.sh_type != ELFSection.SHT_NOBITS:
                res.append(section)
        return res

    def __repr__(self):
        """pretty print for debug..."""
        return "%s(self.e_type=%r, self.e_machine=%r, self.e_version=%r, sections=%r)" % (
            self.__class__.__name__, 
            self.e_type, self.e_machine, self.e_version,
            [section.name for section in self.sections])


if __name__ == '__main__':
    print "This is only a module test!"
    elf = ELFObject()
    elf.fromFile(open("test.elf"))
    if elf.e_type != ELFObject.ET_EXEC:
        raise Exception("No executable")
    print elf

    #~ print repr(elf.getSection('.text').data)
    #~ print [(s.name, hex(s.sh_addr)) for s in elf.getSections()]
    print "-"*20
    for p in elf.sections: print p
    print "-"*20
    for p in elf.getSections(): print p
    print "-"*20
    for p in elf.getProgrammableSections(): print p
