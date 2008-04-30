#!/opt/rocks/bin/python
#
# A metric for Gschedule that publishes Process information
# for the node.
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		            version 5.0 (V)
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
# $Log: ps.py,v $
# Revision 1.10  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/11 22:48:12  mjk
# monkey face copyright
#
# Revision 1.7  2006/08/10 00:10:29  mjk
# 4.2 copyright
#
# Revision 1.6  2006/01/16 06:49:03  mjk
# fix python path for source built foundation python
#
# Revision 1.5  2005/10/12 18:09:16  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:53  mjk
# updated copyright
#
# Revision 1.3  2005/08/08 21:24:57  mjk
# foundation
#
# Revision 1.2  2005/05/24 21:22:22  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/08 00:26:59  fds
# Rocks Ganglia Custom Metrics for HPC
#
# Revision 1.3  2004/11/02 00:57:05  fds
# Same channel/port as gmond. For bug 68.
#
# Revision 1.2  2004/03/25 03:16:10  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.1  2004/02/18 20:21:32  fds
# Moved mpd and cluster-top metrics here from base.
#
# Revision 1.2  2003/11/17 18:55:24  fds
# Fixes from rockstar testing. Cluster top works again.
#
# Revision 1.1  2003/10/17 19:24:08  fds
# Presenting the greceptor daemon. Replaces gschedule and glisten.
#
# Revision 1.4  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.3  2003/08/04 19:57:59  fds
# Using Process.cpus() call to make things more clear.
#
# Revision 1.2  2003/08/01 22:47:31  fds
# Small changes
#
# Revision 1.1  2003/07/29 22:02:19  fds
# First design
#
#
#

import os
import time
import gmon.Process
import gmon.events
from gmon.Gmetric import publish


class PS(gmon.events.Metric):
	"Reports process usage."

	# How often we publish (in sec), on average.
	# Should not be set too low, as this metric will run on 
	# compute-bound nodes.
	freq = 60

	def __init__(self, app):
		# Schedule every few seconds on average.
		gmon.events.Metric.__init__(self, app, self.freq)

		# How many CPUs do we have?
		self.cpus = gmon.Process.cpus()


	def name(self):
		return "ps"


	def dmax(self):
		# Process data is easily perishable (needs to be fresh).
		return self.freq * 2


	# Re-implemented from our superclass. Will publish many metrics at once.
	def run(self):
		"""Reports the N top processes by CPU usage, where N is the
		number of processors we have."""

		# Provides only as many processes as we have CPUs.
		# Returns a list of dictionaries. The second arg gives the 
		# measurement window in seconds.
		processes = gmon.Process.ps(self.cpus, 1.5)

		for ps in processes:
			name = "ps-%s" % ps['PID']
			value = "cmd=%s, user=%s, %%cpu=%.2f, %%mem=%.2f, size=%u, data=%u, shared=%u, vm=%u" % \
				(ps['COMMAND'],
				ps['USER'],
				ps['%CPU'],
				ps['%MEM'],
				ps['SIZE'],
				ps['DATA'],
				ps['SHARED'],
				ps['VM'])

			self.publish(name, value)
			
			#print "Sent <%s>, <%s>" % (name, value)



def initEvents():
	return PS


# My Main. Not run if loaded as a module.
#
if __name__=="__main__":
	app=PS()
	app.run()

