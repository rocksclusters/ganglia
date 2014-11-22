#!/opt/rocks/bin/python
#
# The base classe for Ganglia news journalists.
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
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
# $Log: journalist.py,v $
# Revision 1.17  2012/11/27 00:48:57  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.16  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.15  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.14  2010/09/07 23:53:14  bruno
# star power for gb
#
# Revision 1.13  2009/05/01 19:07:16  mjk
# chimi con queso
#
# Revision 1.12  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.11  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.10  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.9  2006/09/11 22:48:15  mjk
# monkey face copyright
#
# Revision 1.8  2006/08/10 00:10:31  mjk
# 4.2 copyright
#
# Revision 1.7  2006/01/16 06:49:04  mjk
# fix python path for source built foundation python
#
# Revision 1.6  2005/10/12 18:09:17  mjk
# final copyright for 4.1
#
# Revision 1.5  2005/09/19 18:34:58  bruno
# added ganglia news back
#
# Revision 1.4  2005/09/16 01:02:54  mjk
# updated copyright
#
# Revision 1.3  2005/05/24 21:22:23  mjk
# update copyright, release is not any closer
#
# Revision 1.2  2005/03/31 04:22:24  fds
# RSS 0.91 compliant now. Much better journalist interface. Presenting
# the RSS feed in HTML first, with a link to the XML stream.
#
# Revision 1.1  2005/03/08 00:03:32  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.2  2004/04/14 22:01:49  fds
# Less verbose, quoting special chars in cluster name. New full-disk
# journalist inspired by lodestone.
#
# Revision 1.1  2004/04/13 20:16:05  fds
# The Ganglia RSS news prototype. 2 journalsits: MIA and load.
#
#

import os
import sys
import syslog
import time
import urllib


class Journalist:
	"""The base class for all ganglia news collectors."""

	def __init__(self, app):
		self.app = app
		self.items = ''

		self.today = time.strftime("%d-%b")

	def name(self):
		"""The name of a Ganglia Journalist"""
		return self.__class__.__name__

	def run(self):
		pass

	def getGanglia(self):
		return self.app.ganglia

	def getTime(self):
		return self.app.getTime()

	def getLocalTime(self):
		return self.app.getLocalTime()

	def getDate(self):
		return self.today

	def getHostPage(self, cluster, host, physical=0):
		"Gives a URL to a Ganglia Host page."

		link = '%s/ganglia/?c=%s&amp;h=%s' \
			% (cluster.getUrl(),
			urllib.quote(cluster.getName()),
			host.getName())

		if physical:
			link += '&amp;p=1'

		return link


	def debug(self, msg):
		mesg = "gevent debug: %s" % (msg)
		syslog.syslog(mesg)
		print mesg

	def info(self,msg):
		mesg = "gevent info: %s" % (msg)
		syslog.syslog(mesg)
		print mesg

	def warning(self, msg):
		mesg = "gevent warning: %s" % (msg)
		syslog.syslog(syslog.LOG_WARNING, mesg)
		print mesg


	def uptime(self, seconds):
		"""Returns a nicely formatted time from a seconds figure."""

		try:
			secs = int(seconds)
		except:
			return ''

		days = secs/86400
		if days:
			secs = secs % (days*86400)
		hours = secs/3600
		if hours:
			secs = secs % (hours*3600)
		mins = secs/60
		if mins:
			secs = secs % (mins*60)

		s = ''
		if days != 1:
			s = 's'
		if days > 0:
			return "%s day%s, %s:%s:%s" % \
				(days, s, hours, mins, secs)
		else:
			return "%s:%s:%s" % (hours,mins,secs)


	def newItem(self, id, title, description, link, date=None):

		if not date:
			date=self.getTime()

		s = ('  <item>\n'
   		    +'   <title>%s</title>\n' % title
		    +'   <description>%s</description>\n' % description
		    +'   <link>%s</link>\n' % link
		    +'   <pubDate>%s</pubDate>\n' % date
		    +'  </item>\n')

		print s

  		self.recordItem(id, s)


	def recordItem(self, id, item):
		"""Places an RSS snippet of an item in the appropriate
		place in the filesystem."""

		year, month, day = self.getLocalTime()[:3]

		# We want one item per host, per month, per journalist.

		todaysNews = os.path.join(self.app.basedir,
			"%s" % year,
			"%02d" % month,
			self.name())

		os.system('mkdir -p %s' % todaysNews)

		i = open(os.path.join(todaysNews, "%s.rss" % id), 'w')
		i.write(item)
		i.close()
