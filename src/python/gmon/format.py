#!/opt/rocks/bin/python
#
# @Copyright@
#
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
#
# Copyright (c) 2000 - 2013 The Regents of the University of California.
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
# $Log: format.py,v $
# Revision 1.16  2012/11/27 00:48:58  phil
# Copyright Storm for Emerald Boa
#
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
# Revision 1.7  2006/08/10 00:10:33  mjk
# 4.2 copyright
#
# Revision 1.6  2006/01/16 06:49:07  mjk
# fix python path for source built foundation python
#
# Revision 1.5  2005/10/12 18:09:19  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:56  mjk
# updated copyright
#
# Revision 1.3  2005/08/08 21:24:58  mjk
# foundation
#
# Revision 1.2  2005/05/24 21:22:25  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:58:37  fds
# The ganglia command line client. Moved from the monolithic source tree.
#
# Revision 1.24  2004/03/25 03:15:02  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.23  2003/09/02 19:39:19  mjk
# - Print out full ipaddress when ganglia screws up on the hostname
# - Ask for CA passphrase twice for people w/ fat fingers
#
# Revision 1.22  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.21  2003/06/26 21:54:06  fds
# Fixed small misspelling
#
# Revision 1.20  2003/06/26 02:29:00  fds
# Factor out instruction set.
#
# Revision 1.19  2003/06/25 23:48:11  fds
# New StorageDevice object class
#
# Revision 1.18  2003/06/25 22:41:13  fds
# Streamlined the Sub Cluster section.
#
# Revision 1.17  2003/06/25 22:40:47  fds
# Streamlined the Sub Cluster section.
#
# Revision 1.16  2003/06/25 18:24:14  fds
# Incorporated Efstratios changes from 2003-02 into MDS2 format.
#
# Revision 1.15  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.14  2003/02/08 02:22:04  fds
# Added introspective help method.
#
# Revision 1.13  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.12  2002/08/30 23:50:01  mjk
# mds changes
#
# Revision 1.11  2002/08/24 00:01:44  mjk
# - python 2.x changes
# - finished gschedule
#
# Revision 1.10  2002/05/24 00:00:34  mjk
# checkpoint
#
# Revision 1.9  2002/04/18 17:07:19  mjk
# - Minor cleanup
# - Add gmetric.py
#
# Revision 1.8  2002/04/17 23:00:44  mdahan
# Maytal's edit of dn: for clusterData
#
# Revision 1.7  2002/04/17 20:23:46  mdahan
# Maytal Changes
#
# Revision 1.6  2002/04/17 18:29:33  mjk
# Fixes cluster name
#
# Revision 1.5  2002/04/17 18:24:28  mjk
# - added getOwner/setOwner methods to Metric class (just like Host)
# - added hostname to MDS Metric record
#
# Revision 1.4  2002/04/17 18:13:52  mdahan
# Maytal's changes to format
#
# Revision 1.3  2002/04/17 02:44:26  mjk
# second rev for MDS schema
#
# Revision 1.2  2002/04/09 05:52:57  mjk
# mds fixes
#
# Revision 1.1  2002/04/09 00:30:51  mjk
# mds changes
#

import sys
import re
import time
import types
import string
import gmon.ganglia

class Base:
	def __init__(self, ganglia, commands, args):
		self.ganglia  = ganglia
		self.commands = commands
		self.args     = args

	def format(self, hosts, metrics):
		pass

	def help(self):
		pass

	def flavors(self):
		formats = []
		for Class in globals().values():
			if type(Class) == types.ClassType:
				if issubclass(Class, Base) and Class != Base:
					formats.append(Class.__name__)
		return formats



class Default(Base):
	def format(self, hosts, metrics):
		cols = []
		for host in hosts:

			# Split off the domainname from the hostname.
			# If the result is numeric ganglia screwed up
			# and is just reporting ip address.  In this
			# case use the full IP address.

			hostname = string.split(host.getName(), '.')[0]
			try:
				int(hostname)
				hostname = host.getName()
			except ValueError:
				pass
			row = [ hostname ]
			for metric in host.getMetric(metrics):
				if metric:
					row.append(metric.getValue())
				else:
					row.append('')
			cols.append(row)
		self.display(cols)


	def display(self, cols):

		# Create the maxCols list which represents the max
		# length of each row element.

		maxCols = []
		for i in range(0, len(cols[0])):
			maxCols.append(0)
		for row in cols:
			for i in range(0, len(row)):
				if len(row[i]) > maxCols[i]:
					maxCols[i] = len(row[i])

		# Print the table using maxCols list to force all
		# columns in the rows to line up.  The first column
		# (hostname) is left justified, and the subsequent
		# columns are right justified.

		for row in cols:
			for i in range(0, len(row)):
				if i == 0:
					print string.ljust(row[i], maxCols[i]),
				else:
					print string.rjust(row[i], maxCols[i]),
				if i < len(row)-1:
					print '\t',
			print



class MDS(Base):

	def __init__(self, ganglia, commands, args):
		self.name = None
		self.vo   = None
		self.schemaVersion = (1, 1)
		Base.__init__(self, ganglia, commands, args)

	def format(self, hosts, metrics):
		if self.args:
			index = self.args
		else:
			index = ('machine_type', 'os_name', 'os_release')
			subclusters = self.partitionCluster(hosts, index)
		if not subclusters:
			return

		dn = 'mds-vo-name=local, o=grid'
		dn = self.createEDTTopRecord(dn)
		dn = self.createClusterTopRecord(dn, hosts[0].getOwner())

		i = 1
		for id in subclusters.keys():
			subcluster = subclusters[id]
			self.createSubClusterRecord(dn, "sub%s" % i, id, subcluster)
			i = i + 1

		return


	def createEDTTopRecord(self, dn):
		print 'dn:', dn
		print 'objectclass: GlueTop'
		print 'objectclass: GlueGeneralTop'
		print 'GlueSchemaVersionMajor:', self.schemaVersion[0]
		print 'GlueSchemaVersionMinor:', self.schemaVersion[1]
		print # end of record
		return dn

	def createClusterTopRecord(self, dn, cluster):
		dn = 'cl=datatag-CNAF, %s' % dn
		print 'dn:', dn
		print 'objectclass: GlueClusterTop'
		print 'objectclass: GlueCluster'
		print 'GlueClusterName:', cluster.getID()
		print 'GlueClusterUniqueID:', cluster.getUniqueID()
		# Depricated.
		#print 'GlueClusterService: compute'
		print # end of record
		return dn

	def createSubClusterRecord(self, dn, name, id, hosts):
		"""Generates a Sub-Cluster record. ID is assumed to be
		<os-name>--<os_release> from ganglia."""

		if not len(hosts): return

		dn = 'scl=%s, %s' % (name, dn)

		# Get a representative host from sub-cluster.
		host = hosts[0]

		os = host.getMetricValue('os_name')
		os_release = host.getMetricValue('os_release')
		# Assuming a redhat RPM style 'os_release' metric: version-release.
		version, release = string.split(os_release,"-")

		print 'dn:', dn
		print 'objectclass: GlueClusterTop'
		print 'objectclass: GlueSubCluster'
		print 'GlueSubClusterName: %s' % name
		print 'GlueSubClusterUniqueID: %s' % id
		print 'objectclass: GlueHostOperatingSystem'
		print 'GlueHostOperatingSystemName:', os
		print 'GlueHostOperatingSystemVersion:', version
		print 'GlueHostOperatingSystemRelease:', release
		print 'objectclass: GlueHostProcessor'
		print 'GlueHostProcessorInstructionSet:', \
		      host.getMetricValue('machine_type')
		print # end of record

		for host in hosts:
			self.createHostRecord(dn, host)

		return dn

	def createHostRecord(self, dn, host):
		dn = 'host=%s, %s' % (host.getName(), dn)
		print 'dn:', dn

		# Host
		print 'objectclass: GlueHost'
		print 'GlueHostName:', host.getName()
		id = '%s-%s'  % (host.getOwner().getUniqueID(), host.getName())
		print 'GlueHostUniqueID:', id

		# HostArchitecture
		print 'objectclass: GlueHostArchitecture'
		try:
			arch = "%s-%s" % \
				(host.getMetricValue("machine_type"),
				host.getMetricValue("os_name"))
			print 'GlueHostArchitecturePlatformType:', arch
		except:
			pass

		print 'GlueHostArchitectureSMPSize:', \
		      host.getMetricValue('cpu_num')

		# HostProcessor
		print 'objectclass: GlueHostProcessor'
		print 'GlueHostProcessorClockSpeed:', \
		      host.getMetricValue('cpu_speed')

		# HostMainMemory
		print 'objectclass: GlueHostMainMemory'
		print 'GlueHostMainMemoryRAMSize:', \
		      host.getMetricValue('mem_total')
		print 'GlueHostMainMemoryRAMAvailable:', \
		      host.getMetricValue('mem_free')

		# NetworkAdapter
		print 'objectclass: GlueHostNetworkAdapter'
		print 'GlueHostNetworkAdapterName:', host.getName()
		print 'GlueHostNetworkAdapterIPAddress:', host.getIP()
		print 'GlueHostNetworkAdapterMTU:', \
				host.getMetricValue('mtu')
		print 'GlueHostNetworkAdapterOutboundIP: 1'
		print 'GlueHostNetworkAdapterInboundIP: 1'

		# ProcessorLoad
		print 'objectclass: GlueHostProcessorLoad'
		print 'GlueHostProcessorLoadLast1Min:', \
				host.getMetricValue('load_one')
		print 'GlueHostProcessorLoadLast5Min:', \
				host.getMetricValue('load_five')
		print 'GlueHostProcessorLoadLast15Min:', \
				host.getMetricValue('load_fifteen')

		# SMPLoad (same as ProcessorLoad but only if we are SMP)
		smp = host.getMetric('cpu_num')
		if smp:
			print 'objectclass: GlueHostSMPLoad'
			print 'GlueHostSMPLoadLast1Min:', \
				host.getMetricValue('load_one')
			print 'GlueHostSMPLoadLast5Min:', \
				host.getMetricValue('load_five')
			print 'GlueHostSMPLoadLast15Min:', \
				host.getMetricValue('load_fifteen')

		# HostStorageDevice. Note, we group local and remote
		# filesystems into these.
		print 'objectclass: GlueHostStorageDevice'
		try:
			size = host.getMetricValue('disk_total')
			bytes = float(size) * 1e6
			print 'GlueHostStorageDeviceSize:', int(bytes)
			size = host.getMetricValue('disk_free')
			bytes = float(size) * 1e6
			print 'GlueHostStorageDeviceAvailableSpace:', int(bytes)
		except:
			pass
		print 'GlueHostStorageDeviceType: disk'

		print # end of record
		return dn


	def partitionCluster(self, hosts, metricNames):
		"""Returns a list of lists: each list is a 'homogenous'
		set of hosts in the cluster. Hosts grouped by their
		values for all metrics given in metricNames."""

		subclusters = {}
		for host in hosts:

			# If the node has not reported the metric we
			# are using to partition the cluster then skip
			# the node.  Since we don't know what the
			# value is there isn't any reasonable way to
			# handle this.  Hopefully the node will start
			# reporting and can join a subclusters.

			value_list = []
			for name in metricNames:
				metric = host.getMetric(name)
				if metric:
					value_list.append(metric.getValue())
			if not value_list:
				continue

			values = string.join(value_list,"-")

			if not subclusters.has_key(values):
				subclusters[values] = []
			subclusters[values].append(host)

		return subclusters
