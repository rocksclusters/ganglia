#!/opt/rocks/bin/python
#
# Flags full disks.
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		           version 5.1  (VI)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
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
# $Log: full.py,v $
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
# Revision 1.2  2004/04/20 04:30:44  fds
# Not as stupid. Will give more than one news item if necessary.
#
# Revision 1.1  2004/04/14 22:01:49  fds
# Less verbose, quoting special chars in cluster name. New full-disk
# journalist inspired by lodestone.
#
#

import os
import sys
import gmon.journalist

class Full(gmon.journalist.Journalist):
	"""A news collector that detects full disk partitions."""

	fullthresh = 95.0

	def run(self):
	
		c = self.getGanglia().getCluster()
		for h in c.getHosts():
			try:
				f = float(h.getMetricValue('part_max_used'))
			except:
				continue
			if f > self.fullthresh:
				self.item(c, h, f)


	def item(self, cluster, host, fullest):
		"Write a new news alert"
		
		title = 'Node %s has a full disk' % host.getName()

		descr = ('Node %s has a disk which is %d%% full. ' 
				% (host.getName(), fullest)
			+'(Threshold is %d%%)' 
				% self.fullthresh)

		link = self.getHostPage(cluster, host)

		self.newItem(host.getIP(), title, descr, link)

		
		
def initEvents():
	return Full

