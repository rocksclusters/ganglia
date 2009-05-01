#! /opt/rocks/bin/python
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 5.2 (Chimichanga)
# 
# Copyright (c) 2000 - 2009 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: build-schema.py,v $
# Revision 1.12  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.11  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/11 22:48:16  mjk
# monkey face copyright
#
# Revision 1.7  2006/08/10 00:10:32  mjk
# 4.2 copyright
#
# Revision 1.6  2006/01/16 06:49:06  mjk
# fix python path for source built foundation python
#
# Revision 1.5  2005/10/12 18:09:19  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:55  mjk
# updated copyright
#
# Revision 1.3  2005/08/08 21:24:58  mjk
# foundation
#
# Revision 1.2  2005/05/24 21:22:24  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:58:36  fds
# The ganglia command line client. Moved from the monolithic source tree.
#
# Revision 1.5  2004/03/25 03:15:02  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.4  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.3  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.2  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.1  2002/05/24 00:00:34  mjk
# checkpoint
#

import sys
import string
import xml.sax
import xml.sax.saxutils


class Handler(xml.sax.saxutils.DefaultHandler):

	def __init__(self):
		xml.sax.saxutils.DefaultHandler.__init__(self)
		self.prefix = 'cm'


	#
	# XML parsing code
	#
	
	def startElement(self, name, attrs):
		try:
			self.text = ''
			eval('self.startElement_%s(name, attrs)' % name)
		except AttributeError:
			pass

	def endElement(self, name):
		try:
			eval('self.endElement_%s(name)' % name)
		except AttributeError:
			pass

	def characters(self, s):
		self.text = self.text + s

	# <schema>
        
	def startElement_schema(self, name, attrs):
            	self.oid         = attrs.get('oid')
		self.objectIndex = 0
		print '# MDS Cluster Monitoring Schema'
		print '#'
		print '# base oid = ', self.oid
		print


	# <object>

	def startElement_object(self, name, attrs):
		self.objectName  = '%s%s' % (self.prefix, attrs.get('name'))
		self.objectIndex = self.objectIndex + 1
		self.attrIndex   = 0
		self.objectAttributes         = {}
		self.objectAttributes['must'] = []
		self.objectAttributes['may']  = []
		print '#'
		print '#', self.objectName
		print '#'

	def endElement_object(self, name):
		oid = '%s.%d' % (self.oid, self.objectIndex)
		print "objectclass ( %s" % oid
		print "\tNAME '%s'" % self.objectName
		attrs = self.objectAttributes['must']
		if attrs:
			print "\tMUST (%s)" % string.join(attrs, ' $ ')
		attrs = self.objectAttributes['may']
		if attrs:
			print "\tMAY  (%s)" % string.join(attrs, ' $ ')
		print " )"
		print


	# <attribute>

	def startElement_attribute(self, name, attrs):
		self.attrIndex   = self.attrIndex + 1
		self.attrName    = '%s%s' % (self.prefix, attrs.get('name'))
		self.attrRequire = attrs.get('require')
		self.objectAttributes[self.attrRequire].append(self.attrName)

	def endElement_attribute(self, name):
		oid = '%s.%d.%d' % (self.oid, self.objectIndex, self.attrIndex)
		print "attributetype ( %s" % oid
		print "\tNAME     '%s'" % self.attrName
		print "\tDESC     '%s'" % self.attrDesc
		print "\tEQUALITY", self.attrEquality
		print "\tORDERING", self.attrOrdering
		print "\tSUBSTR  ", self.attrSubstr
		print "\tSYNTAX  ", self.attrSyntax
		print " )"
		print

	# <desc>

	def endElement_desc(self, name):
		self.attrDesc = string.strip(self.text)

	# <syntax>

	def endElement_syntax(self, name):
		self.attrSyntax = string.strip(self.text)

	# <equality>

	def endElement_equality(self, name):
		self.attrEquality = string.strip(self.text)

	# <ordering>

	def endElement_ordering(self, name):
		self.attrOrdering = string.strip(self.text)
		
	# <substr>

	def endElement_substr(self, name):
		self.attrSubstr = string.strip(self.text)

	
		

parser  = xml.sax.make_parser()
handler = Handler()
parser.setContentHandler(Handler())
parser.parse(sys.stdin)
