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

import os
import sys
import stat
import exceptions
import unittest
from os.path import abspath

__all__ = ["copyfileobj","copyfile","copymode","copystat","copy","copy2",
   		"copytree","move","rmtree","Error"]

class Error(exceptions.EnvironmentError):
	pass

# Make a file executable for user, group, and other.
def makeExecutable(path):
    s = os.stat(path)
    m = s.st_mode
    m |= stat.S_IXGRP | stat.S_IXOTH | stat.S_IXUSR
    os.chmod(path, m)

def copyfileobj(fsrc, fdst, length=16*1024):
	"""copy data from file-like object fsrc to file-like object fdst"""
	while 1:
		buf = fsrc.read(length)
		if not buf:
			break
		fdst.write(buf)

def _samefile(src, dst):
	# Macintosh, Unix.
	if hasattr(os.path,'samefile'):
		try:
			return os.path.samefile(src, dst)
		except OSError:
			return False

	# All other platforms: check for same pathname.
	return (os.path.normcase(os.path.abspath(src)) ==
			os.path.normcase(os.path.abspath(dst)))

def copyfile(src, dst):
	"""Copy data from src to dst"""
	if _samefile(src, dst):
		raise Error, "`%s` and `%s` are the same file" % (src, dst)

	fsrc = None
	fdst = None
	try:
		fsrc = open(src, 'rb')
		fdst = open(dst, 'wb')
		copyfileobj(fsrc, fdst)
	finally:
		if fdst:
			fdst.close()
		if fsrc:
			fsrc.close()

def copymode(src, dst):
	"""Copy mode bits from src to dst"""
	if hasattr(os, 'chmod'):
		st = os.stat(src)
		mode = stat.S_IMODE(st.st_mode)
		os.chmod(dst, mode)

def copystat(src, dst, forceMode=None):
	"""Copy all stat info (mode bits, atime and mtime) from src to dst"""
	st = os.stat(src)
	mode = stat.S_IMODE(st.st_mode)
	if forceMode != None:
		mode = forceMode
	if hasattr(os, 'utime'):
		os.utime(dst, (st.st_atime, st.st_mtime))
	if hasattr(os, 'chmod'):
		os.chmod(dst, mode)


def copy(src, dst):
	"""Copy data and mode bits ("cp src dst").

	The destination may be a directory.

	"""
	if os.path.isdir(dst):
		dst = os.path.join(dst, os.path.basename(src))
	copyfile(src, dst)
	copymode(src, dst)

def copy2(src, dst, forceMode=None):
	"""Copy data and all stat info ("cp -p src dst").

	The destination may be a directory.

	"""
	if os.path.isdir(dst):
		dst = os.path.join(dst, os.path.basename(src))
	copyfile(src, dst)
	copystat(src, dst, forceMode)


def copytree(src, dst, symlinks=False, mode=None):
	"""Recursively copy a directory tree using copy2().

	The destination directory must not already exist.
	If exception(s) occur, an Error is raised with a list of reasons.

	If the optional symlinks flag is true, symbolic links in the
	source tree result in symbolic links in the destination tree; if
	it is false, the contents of the files pointed to by symbolic
	links are copied.
	
	The mode argument, if not None, is the mode to which all copied files
	and directories will be set.

	XXX Consider this example code rather than the ultimate tool.

	"""
	names = os.listdir(src)
	if os.path.exists(dst) and not os.path.isdir(dst):
		raise Exception, "destination directory is a file"
	
	dstMode = 0777
	if hasattr(os, "chmod"):
		if mode == None:
			st = os.stat(src)
			dstMode = stat.S_IMODE(st.st_mode)
		else:
			dstMode = mode
	os.mkdir(dst, dstMode)
		
	errors = []
	for name in names:
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			if symlinks and os.path.islink(srcname):
				linkto = os.readlink(srcname)
				os.symlink(linkto, dstname)
			elif os.path.isdir(srcname):
				copytree(srcname, dstname, symlinks, mode)
			else:
				copy2(srcname, dstname)
				
				if mode != None and hasattr(os, 'chmod'):
					os.chmod(dstname, mode)
					
			# XXX What about devices, sockets etc.?
		except (IOError, os.error), why:
			errors.append((srcname, dstname, why))
	if errors:
		raise Error, errors

def rmtree(path, ignore_errors=False, onerror=None, force=False):
	"""Recursively delete a directory tree.

	If ignore_errors is set, errors are ignored; otherwise, if onerror
	is set, it is called to handle the error with arguments (func,
	path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
	path is the argument to that function that caused it to fail; and
	exc_info is a tuple returned by sys.exc_info().  If ignore_errors
	is false and onerror is None, an exception is raised.

	"""
	if ignore_errors:
		def onerror(*args):
			pass
	elif onerror is None:
		def onerror(*args):
			raise
	names = []
	try:
		names = os.listdir(path)
	except os.error, err:
		onerror(os.listdir, path, sys.exc_info())
	for name in names:
		fullname = os.path.join(path, name)
		try:
			mode = os.lstat(fullname).st_mode
		except os.error:
			mode = 0
		if stat.S_ISDIR(mode):
			rmtree(fullname, ignore_errors, onerror)
		else:
			try:
				os.remove(fullname)
			except os.error, err:
				onerror(os.remove, fullname, sys.exc_info())
	try:
		os.rmdir(path)
	except os.error:
		onerror(os.rmdir, path, sys.exc_info())

def move(src, dst):
	"""Recursively move a file or directory to another location.

	If the destination is on our current filesystem, then simply use
	rename.  Otherwise, copy src to the dst and then remove src.
	A lot more could be done here...  A look at a mv.c shows a lot of
	the issues this implementation glosses over.

	"""

	try:
		os.rename(src, dst)
	except OSError:
		if os.path.isdir(src):
			if destinsrc(src, dst):
				raise Error, "Cannot move a directory '%s' into itself '%s'." % (src, dst)
			copytree(src, dst, symlinks=True)
			rmtree(src)
		else:
			copy2(src,dst)
			os.unlink(src)

def destinsrc(src, dst):
	return abspath(dst).startswith(abspath(src))

class CopyFileUnitTest(unittest.TestCase):
	def test_it(self):
		pass

def suite():
	suite = unittest.makeSuite(CopyFileUnitTest)
	return suite

if __name__ == "__main__":
	unittest.TextTestRunner(verbosity=2).run(suite())
