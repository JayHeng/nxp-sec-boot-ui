#!/usr/bin/env python

# Copyright (c) 2005 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import os
import unittest

__all__ = ["align_down", "align_up", "mymkarg", "findPathListCommonPrefix", "splitPath", "rebuildPathSimple", "onlyHyphensPlease", "suite"]

def get_dict_default(d, k, default):
    if not d.has_key(k):
        return default
    else:
        return d[k]

def align_down(x, a):
    return x & ~(a - 1)

def align_up(x, a):
    return (x + a - 1) / a * a

# This is a modifed version of mkarg from commands module. It will never use single
# quoting, because the DOS shell does not like that.
def mymkarg(x):
    # XXX return empty string as quoted???
    if len(x) == 0:
        return ' ""'

    # return with whitespace prefix if all one word with no quotes
    if '"' not in x and "'" not in x and " " not in x and "\t" not in x:
        return " " + x

    # return double quoted if no double quotes
    if '"' not in x:
        return ' "' + x + '"'

    escapeChars = '\\$"`'
    if sys.platform == 'win32':
        escapeChars = r'"'

    # otherwise, return double quoted, but escape double quotes
    s = ' "'
    for c in x:
        if c in escapeChars:
            s += "\\"
        s += c
    return s + '"'

def mkcmdline(x):
    return ''.join([mymkargs(i) for i in x])

# Takes a list containing lists of the directories in paths. Returns a list
# containing the common directories between all members of the paths argument.
def findPathListCommonPrefix(paths):
    result = []
    
    if len(paths) == 0:
        return result
    
    for i in range(0, min(map(lambda p: len(p), paths))):
        pathComponent = paths[0][i]
        for thisPath in paths:
            if thisPath[i] != pathComponent:
                return result
        
        result.append(pathComponent)
    
    return result

# Returns a list containing the elements of the path argument.
def splitPath(path):
    if len(path) == 0:
        return ['']
    else:
        return os.path.normpath(path).split(os.path.sep)

#//////////////////////////////////////////////////////////////////////////////
# Finds the SOCFirmware root path, does not yet support UNC
#//////////////////////////////////////////////////////////////////////////////
def findRoot(curPath, basedir="SOCFirmware", caseSensitive=True, loop=False):
    "returns path to SOCFirmware"
    Parent, Directory = os.path.split(curPath)
    root = Parent
    if caseSensitive == True:
        if Directory != basedir:
            root = findRoot(Parent, basedir, caseSensitive, True)
    else:
        if string.upper(Directory) != string.upper(basedir):
            root = findRoot(Parent, basedir, caseSensitive, True)
    if loop == True: # is this a recursive call?
        return root
    return os.path.join(root,basedir)

# This is a not-so-smart path rebuilder. Takes "path" which is relative to
# "originalDir", and returns the same path modified so that it is relative to
# "newDir".
def rebuildPathSimple(originalDir, newDir, path):
    # just return absolute paths unchanged
    if os.path.isabs(path):
        return path
        
    absOriginal = os.path.abspath(originalDir)
    absNew = os.path.abspath(newDir)
    print "absOrig=",absOriginal
    print 'absNew=',absNew
    
    originalDirSplit = absOriginal.split(os.path.sep)
    newDirSplit = absNew.split(os.path.sep)
    commonSplit = findPathListCommonPrefix([originalDirSplit, newDirSplit])
    
    pathComponents = []
    
    newSplit = absNew.split(os.path.sep)
    stepsBack = len(newSplit) - len(commonSplit)
    if stepsBack > 0:
        backList = ['..'] * stepsBack
        pathComponents.append(os.path.join(*backList))
    
    # determine path from common to original
    originalSplit = absOriginal.split(os.path.sep)
    stepsForward = len(originalSplit) - len(commonSplit)
    if stepsForward > 0:
        forwardList = originalSplit[-stepsForward:]
        pathComponents.append(os.path.join(*forwardList))
    
    pathComponents.append(path)
    return os.path.normpath(os.path.join(*pathComponents))
    
class mymkargUnitTest(unittest.TestCase):
    def test_mymkarg(self):
        self.assertEqual(mymkarg("foo"), ' foo')
        self.assertEqual(mymkarg(""), ' ""')
        self.assertEqual(mymkarg('he "said"'), r' "he \"said\""')
        if sys.platform == 'win32':
            self.assertEqual(mymkarg('$10.00'), r' $10.00')
        else:
            self.assertEqual(mymkarg('$10.00'), r' $10.00')

# Unit test for findPathListCommonPrefix() function.
class FindPathListCommonPrefixUnitTest(unittest.TestCase):
    def split(self, path):
        return splitPath(path)
        
    def test_empty(self):
        prefix = findPathListCommonPrefix([])
        self.assertEqual(len(prefix), 0)
    
    def test_single(self):
        path = self.split("/Library/Widgets")
        prefix = findPathListCommonPrefix([path])
        self.assertEqual(prefix, path)
    
    def test_multiple_equal(self):
        path = self.split("/usr/local/apache/include/httpd.h")

        prefix = findPathListCommonPrefix([path, path])
        self.assertEqual(prefix, path)

        prefix = findPathListCommonPrefix([path, path, path])
        self.assertEqual(prefix, path)

        prefix = findPathListCommonPrefix([path, path, path, path, path, path, path])
        self.assertEqual(prefix, path)
    
    def test_not_equal(self):
        path1 = self.split("foo/bar")
        path2 = self.split("baz/buz")
        prefix = findPathListCommonPrefix([path1, path2])
        self.assertEqual(prefix, [])
    
    def test_complex(self):
        path1 = self.split("/usr/local/apache/include/httpd.h")
        path2 = self.split("/usr/local/apache/conf/httpd.conf")
        path3 = self.split("/usr/local/bin/python")
        path4 = self.split("/System/Library/Frameworks")
        
        prefix = findPathListCommonPrefix([path1, path2])
        self.assertEqual(prefix, self.split("/usr/local/apache"))
        
        prefix = findPathListCommonPrefix([path1, path2, path3])
        self.assertEqual(prefix, self.split("/usr/local"))
        
        prefix = findPathListCommonPrefix([path1, path2, path3, path4])
        self.assertEqual(prefix, self.split(""))

class rebuildPathSimpleUnitTest(unittest.TestCase):
    def test_rebuild(self):
        pass


def onlyHyphensPlease( argList ):
    """
    argList is a list of strings, such as the argv of a
    Python script.  This function searches in argList for the
    presence of em- or en-dashes.  If any are found, they are
    converted to hyphens.

    Return:
    True if found
    False if none found
    """

    bReplaced = False
    for i in range(len(argList)):
        if (argList[i].find('\x97') >= 0) or (argList[i].find('\x96') >= 0) :
            bReplaced = True
            arg         = argList[i].replace('\x97','-')    # Replace em-dashes with hyphens.
            argList[i]  = arg.replace('\x96','-')           # Replace en-dashes with hyphens.

    return bReplaced

class onlyHyphensPleaseUnitTest( unittest.TestCase ):
    def test_hyphens(self):
        em_dash    = "kung\x97fu"
        en_dash    = "kung\x96fu"
        argList    = [ em_dash, en_dash ] 
        hyphen     = "kung-fu"
        onlyHyphensPlease( argList )
        self.assertEqual( argList[0] , hyphen )
        self.assertEqual( argList[1] , hyphen )

def suite():
    argSuite = unittest.makeSuite(mymkargUnitTest)
    pathListSuite = unittest.makeSuite(FindPathListCommonPrefixUnitTest)
    rebuildSuite = unittest.makeSuite(rebuildPathSimpleUnitTest)
    hyphenSuite = unittest.makeSuite(onlyHyphensPleaseUnitTest)
    suite = unittest.TestSuite()
    suite.addTests((argSuite, pathListSuite, rebuildSuite, hyphenSuite))
    return suite

# Run unit tests when this source file is executed directly from the command
# line.
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
