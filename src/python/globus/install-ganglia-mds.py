#! /opt/rocks/bin/python
#
# Install the hooks required for the Ganglia MDS monitoring schema.
# This should be installed in $GLOBUS_LOCATION/etc and run after
# configuring globus.
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
# $Log: install-ganglia-mds.py,v $
# Revision 1.15  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.14  2011/07/23 02:31:00  phil
# Viper Copyright
#
# Revision 1.13  2010/09/07 23:53:18  bruno
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
# Revision 1.1  2005/03/12 00:58:37  fds
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
# Revision 1.1  2002/07/19 21:07:43  mjk
# bite me!
#

import os
import sys
import getopt
import string


def getHostname(path):

	print 'Determining Hostname (based on Globus config)'

	# Determines the hostname based on how it was setup in the
	# grid-info.conf file.  This is safer than just calling
	# hostname().
	
	hostname = None
	file = open(os.path.join(path, 'grid-info.conf'))
	for line in file.readlines():
		fields = string.split(line[:-1], '=')
		if len(fields) == 2:
			if fields[0] == 'hostname':
				hostname = fields[1]
	file.close()
	return hostname[:-1]

def patchLdif(path, hostname):
	filename = os.path.join(path, 'grid-info-resource-ldif.conf')
	print 'patching', filename


	# Read the config file into core

	file = open(filename)
	text = file.readlines()
	file.close()

	text2 = []
	state = 0
	for line in text:
		fields = string.split(line[:-1], ':')
		if fields[0] == 'dn':
			if string.find(fields[1], 'cmMetricData') != -1:
				state = 1
			else:
				state = 0
		if not state:
			text2.append(line)

	# Write the config file back out to disk

	file = open(filename, 'w')
	for line in text2:
		file.write(line)
	file.write('\n')
	file.write('dn: MDS-service=cmMetricData, Mds-Host-hn=%s, ' % hostname)
	file.write('Mds-Vo-name=local, o=grid\n')
	file.write('objectclass: GlobusTop\n')
	file.write('objectclass: GlobusActiveObject\n')
	file.write('objectclass: GlobusActiveSearch\n')
	file.write('type: exec\n')
	file.write('path: /usr/sbin\n')
	file.write('base: ganglia\n')
	file.write('args: --format=MDS --select=All\n')
	file.write('cachetime: 0\n')
	file.write('timelimit: 20\n')
	file.write('sizelimit: 0\n')
	file.close()


	
def patchSlapd(path):
	filename = os.path.join(path, 'grid-info-slapd.conf')
	print 'Patching', filename

	# Read the config file into core
	
	file = open(filename)
	text = file.readlines()
	file.close()

	# Patch the in core copy of the file.  Add the desired
	# configuration and nuke any existing installation.

	text2 = []
	text2.append('schemacheck on\n')
	text2.append('sizelimit 1000\n')
	text2.append('include %s\n' % os.path.join(globusLocation, 'etc',
						   'monitoring.schema'))
    
	for line in text:
		keep = 1
		for s in [ 'sizelimit', 'schemacheck', 'monitoring.schema']:
			if string.find(line, s) != -1:
				keep = 0
		if keep:
			text2.append(line)

	# Write the config file back out to disk

	file = open(filename, 'w')
	for line in text2:
		file.write(line)
	file.close()



globusLocation = os.path.join(os.sep, 'usr', 'local', 'apps', 'globus-2.0')

opts, args = getopt.getopt(sys.argv[1:], '', ['globus-location='])
for c in opts:
	if c[0] == '--globus-location':
		globusLocation = c[1]

globusEtc = os.path.join(globusLocation, 'etc')

hostname = getHostname(globusEtc)
patchSlapd(globusEtc)
patchLdif(globusEtc, hostname)

