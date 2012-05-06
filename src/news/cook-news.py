#!/opt/rocks/bin/python
#
# A Cron job that cooks Ganglia gmond XML into an RSS feed.
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.5 (Mamba)
# 		         version 6.0 (Mamba)
# 
# Copyright (c) 2000 - 2012 The Regents of the University of California.
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
# $Log: cook-news.py,v $
# Revision 1.17  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.16  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.15  2010/09/07 23:53:14  bruno
# star power for gb
#
# Revision 1.14  2009/05/01 19:07:16  mjk
# chimi con queso
#
# Revision 1.13  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.12  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.11  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.10  2006/09/11 22:48:13  mjk
# monkey face copyright
#
# Revision 1.9  2006/08/10 00:10:30  mjk
# 4.2 copyright
#
# Revision 1.8  2006/01/16 06:49:04  mjk
# fix python path for source built foundation python
#
# Revision 1.7  2005/10/12 18:09:17  mjk
# final copyright for 4.1
#
# Revision 1.6  2005/09/16 01:02:53  mjk
# updated copyright
#
# Revision 1.5  2005/09/02 00:07:15  bruno
# move to foundation
#
# Revision 1.4  2005/05/24 21:22:22  mjk
# update copyright, release is not any closer
#
# Revision 1.3  2005/03/31 22:07:43  fds
# RSS stream only shows fresh items, recalculated every hour.
#
# Revision 1.2  2005/03/31 04:22:23  fds
# RSS 0.91 compliant now. Much better journalist interface. Presenting
# the RSS feed in HTML first, with a link to the XML stream.
#
# Revision 1.1  2005/03/08 00:03:31  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.4  2004/07/16 22:34:36  fds
# Now report the number of nodes in the RSS header.
#
# Revision 1.3  2004/04/14 22:01:48  fds
# Less verbose, quoting special chars in cluster name. New full-disk
# journalist inspired by lodestone.
#
# Revision 1.2  2004/04/13 20:16:05  fds
# The Ganglia RSS news prototype. 2 journalsits: MIA and load.
#
# Revision 1.1  2004/02/12 19:52:24  fds
# Ganglia XML -> RSS cooker.
#
#
# Original author: Federico Sacerdoti (fds@sdsc.edu) 2004.
#

import os
import sys
import rocks.app
import gmon.ganglia
import time
import types
import syslog

class GangliaNews(rocks.app.Application):
	"""Coordinator of news modules (journalists) that scan ganglia
	XML tree daily for any news."""


	def __init__(self, argv):
		rocks.app.Application.__init__(self,argv)
		self.usage_name = 'Ganglia News'
		self.usage_version = '@VERSION@'
		self.getopt.l.extend([
			('hello','say hi')
			])

		self.basedir = '/var/ganglia/news'
		self.journalists = {}

		# For use by all journalists
		self.fancynow = time.strftime("%a, %d %b %Y %H:%M:%S %Z")
		self.now = time.localtime()


	def parseArg(self,c):
		rocks.app.Application.parseArg(self,c)
		key,val = c
		if key == '--hello':
			print "Hi there"


	def getTime(self):
		return self.fancynow

	def getLocalTime(self):
		return self.now

	def fullImport(self, name):
		"""Imports all components of a module, from the
		Python language reference."""

		mod = __import__(name)
		components = name.split('.')
		for comp in components[1:]:
			mod = getattr(mod, comp)
		return mod
		
		
	def loadModules(self, path):
		"""Import all the python code in a directory. Path is 
		like gmon.news"""

		info = "ganglia news loading %s: " % path
		
		modules = self.fullImport(path)
		for file in os.listdir(modules.__path__[0]):
			modname, ext = os.path.splitext(file)
			if ext == '.py' and modname != '__init__':
				info = info + modname + " "

				fullmodname = "%s.%s" % (path, modname)
				#print "Importing:", fullmodname
				mod = self.fullImport(fullmodname)

				try:
					initEvents = getattr(mod, "initEvents")
				except AttributeError:
					info += "(no initEvents(), skipping) "
					continue

				# Call the entry point to get a tuple of event
				# classes.
				events = initEvents()

				if type(events) == types.TupleType:
					for event in events:
						self.register(event)
				else:
					# There is only one event in this
					# module.
					self.register(events)

		syslog.syslog(info)
		
		
	def register(self, newsclass):
		"Register a news event."
		
		if type(newsclass) == types.ClassType:
			journalist = newsclass(self)
			name = journalist.name()
			if name:
				self.journalists[name] = journalist
		
		
	def run(self):
		self.ganglia = gmon.ganglia.Ganglia()
		self.ganglia.refresh()
		
		self.loadModules('gmon.news')
		
		header = self.rssheader()
		h = open(os.path.join(self.basedir, 'header.rss'), 'w')
		h.write(header)
		h.close()
		print header

		for j in self.journalists.values():
			j.run()

		footer = self.rssfooter()
		f = open(os.path.join(self.basedir, 'footer.rss'), 'w')
		f.write(footer)
		f.close()
		print footer


	def rssheader(self):
		cluster = self.ganglia.getCluster()
		year = self.getLocalTime()[0]

		s = """<?xml version="1.0"?>
<rss version="0.91">
 <channel>
  <title>%s Cluster</title>
  <link>%s</link>
  <description>Health News from Ganglia. (Nodes up at %s: %s)
  </description>
  <language>en-us</language>
  <%s>Copyright %s %s</%s>
  <pubDate>%s</pubDate>
  <lastBuildDate>%s</lastBuildDate>
  <generator>Rocks Ganglia Cooker version %s</generator>
""" \
		% (cluster.getName(),
		cluster.getUrl(),
		time.strftime("%I:%M%p"),
		self.ganglia.clusterSize(),
		'copyright', year, cluster.getOwner(), 'copyright',
		self.getTime(),
		self.getTime(),
		self.usage_version)

		return s


	def rssfooter(self):
		s = ' </channel>\n' \
		  + '</rss>\n'

		return s



# Main
app = GangliaNews(sys.argv)
app.parseArgs()
app.run()
