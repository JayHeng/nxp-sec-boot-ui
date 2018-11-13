#! /usr/bin/env python
import sys
import os
import uidef

g_flexspiNandOpt = None
g_flexspiNandFcbOpt = None
g_flexspiNandKeyBlob = None

g_semcNorOpt = None
g_semcNorSetting = None

g_semcNandOpt = None
g_semcNandFcbOpt = None
g_semcNandImageInfo = None

g_usdhcSDOpt = None

g_UsdhcMmcOpt = None


def initVar():
    global g_flexspiNandOpt
    global g_flexspiNandFcbOpt
    global g_flexspiNandKeyBlob
    g_flexspiNandOpt = 0xD0010101
    g_flexspiNandFcbOpt = 0x00010601
    g_flexspiNandKeyBlob = [None] * 8
    g_flexspiNandKeyBlob[0] = 0x00020001

    global g_semcNorOpt
    global g_semcNorSetting
    g_semcNorOpt = 0xD0010101
    g_semcNorSetting = 0x00010601

    global g_semcNandOpt
    global g_semcNandFcbOpt
    global g_semcNandImageInfo
    g_semcNandOpt = 0xD0010101
    g_semcNandFcbOpt = 0x00010601
    g_semcNandImageInfo = [None] * 8
    g_semcNandImageInfo[0] = 0x00020001

    global g_usdhcSDOpt
    g_usdhcSDOpt = 0xD0010101

    global g_UsdhcMmcOpt
    g_UsdhcMmcOpt = 0xD0010101





def getVar( group ):
    if group == uidef.kBootDevice_FlexspiNor:
        pass
    elif group == uidef.kBootDevice_FlexspiNand:
        global g_flexspiNandOpt
        global g_flexspiNandFcbOpt
        global g_flexspiNandKeyBlob
        return g_flexspiNandOpt, g_flexspiNandFcbOpt, g_flexspiNandKeyBlob
    elif group == uidef.kBootDevice_SemcNor:
        global g_semcNorOpt
        global g_semcNorSetting
        return g_semcNorOpt, g_semcNorSetting
    elif group == uidef.kBootDevice_SemcNand:
        global g_semcNandOpt
        global g_semcNandFcbOpt
        global g_semcNandImageInfo
        return g_semcNandOpt, g_semcNandFcbOpt, g_semcNandImageInfo
    elif group == uidef.kBootDevice_UsdhcSd:
        global g_usdhcSDOpt
        return g_usdhcSDOpt
    elif group == uidef.kBootDevice_UsdhcMmc:
        global g_UsdhcMmcOpt
        return g_UsdhcMmcOpt
    elif group == uidef.kBootDevice_LpspiNor:
        pass
    else:
        pass

def setVar( group, *args ):
    if group == uidef.kBootDevice_FlexspiNor:
        pass
    elif group == uidef.kBootDevice_FlexspiNand:
        global g_flexspiNandOpt
        global g_flexspiNandFcbOpt
        global g_flexspiNandKeyBlob
        g_flexspiNandOpt = args[0]
        g_flexspiNandFcbOpt = args[1]
        g_flexspiNandKeyBlob = args[2]
    elif group == uidef.kBootDevice_SemcNor:
        global g_semcNorOpt
        global g_semcNorSetting
        g_semcNorOpt = args[0]
        g_semcNorSetting = args[1]
    elif group == uidef.kBootDevice_SemcNand:
        global g_semcNandOpt
        global g_semcNandFcbOpt
        global g_semcNandImageInfo
        g_semcNandOpt = args[0]
        g_semcNandFcbOpt = args[1]
        g_semcNandImageInfo = args[2]
    elif group == uidef.kBootDevice_UsdhcSd:
        global g_usdhcSDOpt
        g_usdhcSDOpt = args[0]
    elif group == uidef.kBootDevice_UsdhcMmc:
        global g_UsdhcMmcOpt
        g_UsdhcMmcOpt = args[0]
    elif group == uidef.kBootDevice_LpspiNor:
        pass
    else:
        pass


global_count = {}
global_count[1] = 0
global_count[2] = 0
global_count[3] = 0
global_count[4] = 0
global_count[5] = 0
global_count[6] = 0
global_count[7] = 0


