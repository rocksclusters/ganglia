#!/opt/rocks/bin/python
#
# $Id: ganglia.py,v 1.16 2012/11/27 00:48:57 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 		         version 7.0 (Manzanita)
# 
# Copyright (c) 2000 - 2017 The Regents of the University of California.
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
# $Log: ganglia.py,v $
# Revision 1.16  2012/11/27 00:48:57  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.15  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.14  2011/07/23 02:31:00  phil
# Viper Copyright
#
# Revision 1.13  2010/09/07 23:53:17  bruno
# star power for gb
#
# Revision 1.12  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.11  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:35  mjk
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
# Revision 1.5  2005/10/12 18:09:18  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:55  mjk
# updated copyright
#
# Revision 1.3  2005/07/26 19:30:25  bruno
# make more ganglia python functions use the rocks foundation
#
# Revision 1.2  2005/05/24 21:22:24  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:58:36  fds
# The ganglia command line client. Moved from the monolithic source tree.
#
# Revision 1.17  2004/08/09 06:40:16  fds
# Added --dead flag that lists dead nodes.
#
# Revision 1.16  2004/03/25 03:15:01  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.15  2003/11/03 23:50:13  fds
# The cmd-line ganglia naming confused me today. This error msg should make it clearer.
#
# Revision 1.14  2003/09/04 17:39:18  fds
# Return code reflects output for --alive test
#
# Revision 1.13  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.12  2003/07/21 23:56:32  fds
# Catching getopt errors.
#
# Revision 1.11  2003/07/21 23:49:27  fds
# Better error handling
#
# Revision 1.10  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.9  2003/02/10 19:22:33  fds
# Fixed --xml option.
#
# Revision 1.8  2003/02/08 02:20:13  fds
# Added more help, and host/port options.
#
# Revision 1.7  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.6  2002/09/26 22:27:29  mjk
# *** empty log message ***
#
# Revision 1.5  2002/09/25 16:34:00  mjk
# move to /opt/ganglia
#
# Revision 1.4  2002/08/24 00:01:44  mjk
# - python 2.x changes
# - finished gschedule
#
# Revision 1.3  2002/04/09 00:30:51  mjk
# mds changes
#
# Revision 1.2  2002/04/07 02:41:34  mjk
# added Host and Metric clases
#
# Revision 1.1  2002/02/25 21:14:22  mjk
# Moved out of our patched version of ganglia and into its own RPM.
#
# Revision 1.2  2002/01/26 01:02:32  bruno
# now ganglia class builds a list rather than just prints out the info
#
# Revision 1.1  2002/01/14 19:49:31  bruno
# changes for 2.0.0 command line support
#
# Revision 1.1  2002/01/12 01:58:52  bruno
# goodies for new ganglia
#
#

import os
import sys
import types
import getopt
from gmon.ganglia import GangliaError


class App:

	def __init__(self, argv):

		# Append package library to the default python path

		sys.path.append(os.path.join(os.path.dirname(argv[0]),
			'..', 'lib', 'python'))

		self.formatter     = 'Default'
		self.formatterArgs = None
		self.selector      = 'Default'
		self.selectorArgs  = None
		self.inputFile     = None
		self.doClustersize = 0
		self.isAlive       = None
		self.showDead      = 0


	def help(self, formats, selects):

		print 'Usage: ganglia [options] metric [metric ...]'
		print \
"""where options are:
\t --format=[name] \t Output format: %s
\t --select=[name] \t Query processor: %s
\t --host=[host] \t\t Gmond host (default: localhost)
\t --port=[port] \t\t Gmond port (default: 8649)
\t --input=[input file] \t Read from an XML file instead of a gmond.
\t --xml \t\t\t Show full ganglia XML tree.
\t --clustersize \t\t Print the number of live hosts in the cluster.
\t --alive=[hostname] \t\t Returns 1 if host is alive
\t --dead \t\t Lists dead nodes
""" % (formats, selects)


	def main(self):

		# We have to import here to make sure the library path
		# is correct.

		import gmon.ganglia
		import gmon.select
		import gmon.format

		self.ganglia = gmon.ganglia.Ganglia()

		doHelp = 0
		try:
			opts, args = getopt.getopt(sys.argv[1:], 'h',
					    ["help",
					     "format=",
					     "formatargs=",
					     "input=",
					     "select=",
					     "selectargs=",
					     "host=",
					     "port=",
						 "clustersize",
						 "alive=",
						 "dead",
					     "xml"
					     ])
		except getopt.error:
			self.help("", "")
			sys.exit(1)

		for c in opts:
			if c[0] in ('-h', '--help'):
				doHelp = 1
			elif c[0] == '--format':
				self.formatter = c[1]
			elif c[0] == '--formatargs':
				self.formatterArgs = c[1]
			elif c[0] == '--input':
				self.inputFile = c[1]
			elif c[0] == '--select':
				self.selector = c[1]
			elif c[0] == '--selectargs':
				self.selectorArgs = c[1]
			elif c[0] == '--host':
				self.ganglia.setHost(c[1])
			elif c[0] == '--port':
				self.ganglia.setPort(c[1])
			elif c[0] == '--xml':
				self.ganglia.connect()
				print self.ganglia.getXML()
				sys.exit(0)
			elif c[0] == '--clustersize':
				self.doClustersize = 1
			elif c[0] == '--alive':
				self.isAlive = c[1]
			elif c[0] == '--dead':
				self.showDead = 1

		# Connect to the ganglia service if not already
		# connected.  The --input flag allow us to read XML
		# from a file rather than the ganglia daemon.

		if not self.ganglia.isConnected():
			self.ganglia.connect(self.inputFile)

		if self.doClustersize:
			print self.ganglia.clusterSize()
			return

		if self.isAlive:
			h = self.ganglia.getCluster().getHost(self.isAlive)
			if h:
				isalive = h.alive()
				print isalive
				# Return 0 if alive, 1 otherwise
				# as per UNIX convention.
				sys.exit(not isalive)
			else:
				raise GangliaError, 'cannot find host %s. Did you give the full domain name too?' % self.isAlive

		# Does not make sense to format a list of dead nodes,
		# since there will be no valid metrics. Be simple.

		if self.showDead:
			for h in self.ganglia.getCluster().getHosts():
				if not h:
					continue
				if not h.alive():
					print h.getName().split('.')[0]
			return


		# Instantiate the selector object.  This object will
		# determine the hosts and metrics to be passed to the
		# formatter object.

		try:
			factory = eval('gmon.select.' + self.selector)
		except AttributeError:
			raise GangliaError, 'cannot load %s' % self.selector

		selector = factory(self.ganglia, args, self.selectorArgs)

		# Instantiate the formatter object.  This objects will
		# produce a report in the desired format.  For example
		# this could be the old ganglia 1.0 format, or LDIF
		# format for publishing metrics into MDS.

		try:
			factory = eval('gmon.format.' + self.formatter)
		except AttributeError:
			raise GangliaError, 'cannot load %s' % self.formatter

		formatter = factory(self.ganglia, args, self.formatterArgs)

		if doHelp:
			formats = formatter.flavors()
			selects = selector.flavors()
			self.help(formats, selects)
			formatter.help()
			selector.help()
			sys.exit(0)

		formatter.format(selector.hosts(), selector.metrics())


app = App(sys.argv)
try:
	app.main()
except GangliaError, msg:
	print 'ERROR:', msg
	sys.exit(-1)
