#!/opt/rocks/bin/python
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4.3 (Viper)
# 
# Copyright (c) 2000 - 2011 The Regents of the University of California.
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
# 	Development Team at the San Diego Supercomputer Center at the
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
# Revision 1.16  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.15  2010/09/07 23:53:14  bruno
# star power for gb
#
# Revision 1.14  2009/07/13 21:51:48  bruno
# one more tweak
#
# Revision 1.13  2009/07/10 20:32:05  bruno
# get rocks-defined metrics back in ganglia roll
#
#

import os
import sys
sys.path.append('/opt/rocks/lib/python2.4/site-packages')
import gmon.Process

def ps_handler(name):
	#
	# this is a bit twisted.
	#
	# since ganglia doesn't support dynamic number of metrics (e.g., in
	# our case, we want to send out 4 'ps' metrics on a 4-processor
	# system and only 2 'ps' metrics on a 2-processor system), then we'll
	# use this metric a 'shell' to call 'gmetric' a variable number of
	# times.
	#
	
	i = 0
	for ps in gmon.Process.ps(gmon.Process.cpus(), 1.5):
		value = "pid=%s, cmd=%s, user=%s, %%cpu=%.2f, %%mem=%.2f, size=%u, data=%u, shared=%u, vm=%u" % (ps['PID'], ps['COMMAND'], ps['USER'], ps['%CPU'], ps['%MEM'], ps['SIZE'], ps['DATA'], ps['SHARED'], ps['VM'])

		cmd = '/opt/ganglia/bin/gmetric '
		cmd += '--name="ps-%d" ' % i
		cmd += '--value="%s" ' % value
		cmd += '--type="string" '
                cmd += '--slope=zero '
                cmd += '--dmax=120 '
                os.system(cmd)

		i += 1

	return ''


def metric_init(params):
	global descriptors

	descriptors = []

	d = {
		'name': 'ps',
		'call_back': ps_handler,
		'time_max': 60,
		'value_type': 'string',
		'units': '',
		'slope': 'zero',
		'format': '%s',
		'description': 'Process Data',
		'groups': 'health'
	}

	descriptors.append(d)

	return descriptors
 
def metric_cleanup():
	'''Clean up the metric module.'''
	pass
 
#This code is for debugging and unit testing
if __name__ == '__main__':
	metric_init(None)
	for d in descriptors:
		v = d['call_back'](d['name'])
		print 'value for %s is %s' % (d['name'],  v)

