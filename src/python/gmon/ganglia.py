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
# $Log: ganglia.py,v $
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
# Revision 1.21  2004/03/25 03:15:02  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.20  2004/02/12 19:06:04  fds
# Added CLUSTER attributes for RSS.
#
# Revision 1.19  2003/09/04 17:39:51  fds
# Put error object close to top of file for clarity
#
# Revision 1.18  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.17  2003/07/21 23:55:30  fds
# New cluster size support and alive host oracle.
#
# Revision 1.16  2003/02/25 23:17:11  fds
# Removed some debugging commands.
#
# Revision 1.15  2003/02/25 23:02:28  fds
# Fixed memleak in xml.sax constructor.
#
# Revision 1.14  2003/02/25 20:48:46  fds
# Added new attributes to metric.
#
#

import socket
import string
import sys
import xml.sax
from xml.sax import handler
import xml.sax.saxutils


class GangliaError(Exception):
	"""Ganglia Python Error"""
	pass


class Root:
	def __init__(self, version, source):
		self.version  = version
		self.source   = source
		self.clusters = {}

	def __del__(self):
		self.clusters = {}

	def flush(self):
		"A deep delete to remove references to self."
		for c in self.getClusters():
			c.flush()
		self.clusters = {}

	def addCluster(self, cluster):
		self.clusters[cluster.getName()] = cluster

	def getCluster(self, name):
		return self.clusters[name]

	def getClusters(self):
		return self.clusters.values()

	def getClusterNames(self):
		list = self.clusters.keys()
		list.sort()
		return list

	def getVersion(self):
		return self.version

	def getSource(self):
		return self.source


class Cluster:
	def __init__(self, name, owner, localtime, url, latlong):
		self.name      = name
		self.owner     = owner
		self.url       = url
		self.latlong   = latlong
		self.localtime = float(localtime)
		self.hosts     = {}

	def __del__(self):
		self.hosts = {}

	def flush(self):
		"A deep delete to remove reference counts to self"
		for h in self.getHosts():
			h.flush()
		self.hosts = {}

	def addHost(self, host):
		host.setOwner(self)
		self.hosts[host.getName()] = host

	def getHosts(self):
		return self.hosts.values()

	def getName(self):
		return self.name

	def getID(self):
		return string.join(string.split(self.name), '_')

	def getUniqueID(self):
		return '%s-%s' % (string.join(string.split(self.name), '_'),
				  string.join(string.split(self.owner), '_'))

	def getOwner(self):
		return self.owner

	def getLocalTime(self):
		return self.localtime

	def getUrl(self):
		return self.url

	def getLatlong(self):
		return self.latlong

	def getHostNames(self):
		list = []
		for host in self.getHosts():
			list.append(host.getName())
		list.sort()
		return list

	def getHost(self, name):
		"""Returns a single host if present. Fastest to do this
		lookup here, in our dictionary."""

		if self.hosts.has_key(name):
			return self.hosts[name]
		else:
			return None


class Host:
	def __init__(self, name, ip, tn=None, tmax=None, time=None):
		self.name    = name
		self.ip      = ip
		self.time    = float(time)
		self.metrics = {}
		self.owner   = None
		self.tn      = int(tn)
		self.tmax    = int(tmax)

	def __del__(self):
		self.metrics = {}

	def __repr__(self):
		list = []
		list.append('%s at %s' % (self.name, self.time))
		for key in self.metrics.keys():
			list.append(self.metrics[key].__repr__())
		return string.join(list, '\n')

	def flush(self):
		"A deep delete to remove reference counts to self"
		self.metrics = {}

	def getName(self):
		return self.name

	def getIP(self):
		return self.ip

	def getTimestamp(self):
		return self.time

	def getTn(self):
		"""Returns the age of this host: seconds since we have heard a
		heartbeat."""
		return self.tn

	def getTmax(self):
		"""Returns the expected frequency of the host's heartbeat."""
		return self.tmax

	def getMetricNames(self):
		list = []
		for name in self.metrics.keys():
			list.append(name)
		list.sort()
		return list

	def getMetric(self, name):
		"""Lookup a list of metrics. Do not use this for long-lived
		processes, as it will leave reference counts around. Only
		return metric names/values, not objects."""

		if type(name) == type([]):
			list = []
			for e in name:
				try:
					list.append(self.metrics[e])
				except KeyError:
					list.append(None)
			return list

		# Only one metric requested
		try:
			return self.metrics[name]
		except:
			return None

	def getMetricValue(self, name):
		if type(name) == type([]) or type(name) == type(()):
			list = []
			for metric in self.getMetric(name):
				if metric:
					list.append(metric.getValue())
				else:
					list.append('unknown')
			return list
		else:
			metric = self.getMetric(name)
			if metric:
				return metric.getValue()
			else:
				return 'unknown'


	def getMetrics(self):
		"Return a list with all our metrics."
		return self.metrics.values()


	def addMetric(self, metric):
		metric.setOwner(self)
		self.metrics[metric.getName()] = metric

	def setOwner(self, cluster):
		self.owner = cluster

	def getOwner(self):
		return self.owner

	def alive(self):
		"""Returns 1 if alive, 0 if dead. Life is defined the same way
		as in gmetad: if we have not heard from this host in 4 heartbeats."""

		return self.tn <= (self.tmax * 4)



class Metric:
	def __init__(self, name, val, type=None, units=None, source=None,
			tn=None, tmax=None, dmax=None):
		self.name   = name
		self.val    = val
		self.type   = type
		self.units  = units
		self.source = source
		self.tn     = int(tn)
		self.tmax   = int(tmax)
		self.dmax   = int(dmax)
		self.owner  = None

	def __del__(self):
		pass

	def __repr__(self):
		if self.units:
			type  = '%s(%s)' % (self.type, self.units)
		else:
			type = self.type
		return '%s %s::%s=%s' % (type, self.source, \
					 self.name, self.val)

	def getName(self):
		return self.name

	def getValue(self):
		return self.val

	def getType(self):
		return self.type

	def getUnits(self):
		return self.units

	def getSource(self):
		return self.source

	def getTn(self):
		"Returns the age of this metric (sec)."
		return self.tn

	def getTmax(self):
		"""Returns the maximum age of this metric. If metric is older than this,
		host may be dead."""
		return self.tmax

	def getDmax(self):
		"Returns the deletion time of this metric. Zero indicates immortality."
		return self.dmax

	def setOwner(self, host):
		self.owner = host

	def getOwner(self):
		return self.owner


class Ganglia(handler.ContentHandler,
              handler.DTDHandler,
              handler.EntityResolver,
              handler.ErrorHandler):

	def __init__(self, host='localhost', port=8649):
		handler.ContentHandler.__init__(self)
		self.root       = None
		self.svchost    = host
		self.svcport    = port
		self.xml        = ''

		self.parser = xml.sax.make_parser()
		self.parser.setContentHandler(self)


	def __repr__(self):
		list = []
		for host in self.root.getHosts():
			list.append(host.__repr__())
		return string.join(list, '\n')

	def setHost(self, host):
		"Will point to another gmond. Takes effect on the next refresh."
		self.svchost = host

	def setPort(self, port):
		"Will point this app to another port."
		self.svcport = port

	def isConnected(self):
		if self.xml:
			return 1
		else:
			return 0

	def connect(self, file=None):
		if file:
			try:
				fin = open(file, 'r')
			except:
				raise GangliaError, 'cannot open file %s' % file

			fin = open(file, 'r')
			self.parser.parse(fin)
			fin.close()
			self.xml = 1
		else:
			self.refresh()


	def refresh(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((self.svchost, self.svcport))
		except:
			raise GangliaError, 'cannot connect to ganglia server (gmond) [%s:%s]' \
				% (self.svchost, self.svcport)

		# Clear old tree from memory. Reassignment will call
		# __del__ methods. Careful to set refcounts to 0.
		self.cluster = None
		self.host = None
		sys.last_traceback = None
		sys.exc_traceback = None

		if (self.root): self.root.flush()
		self.root = None
		self.xml = ""

		while 1:
			data = sock.recv(1024)
			if not data:
				break
			self.xml = self.xml + data

		self.parser.reset()
		self.parser.feed(self.xml)
		sock.shutdown(2)

	#
	# XML parsing code
	#

	def startElement(self, name, attrs):
		try:
			eval('self.startElement_%s(name, attrs)' % name)
		except AttributeError:
			pass

	def endElement(self, name):
		try:
			eval('self.endElement_%s(name)' % name)
		except AttributeError:
			pass


	# <GANGLIA_XML>

	def startElement_GANGLIA_XML(self, name, attrs):
		self.root = Root(attrs.get('VERSION'),
				 attrs.get('SOURCE'))

	# <ClUSTER>

	def startElement_CLUSTER(self, name, attrs):
		self.cluster = Cluster(attrs.get('NAME'),
				       attrs.get('OWNER'),
				       attrs.get('LOCALTIME'),
				       attrs.get('URL'),
				       attrs.get('LATLONG'))


	def endElement_CLUSTER(self, name):
		self.root.addCluster(self.cluster)

	# <HOST>

	def startElement_HOST(self, name, attrs):
		self.host = Host(attrs.get('NAME'),
				 attrs.get('IP'),
				 attrs.get('TN'),
				 attrs.get('TMAX'),
				 attrs.get('REPORTED'))


	def endElement_HOST(self, name):
		self.cluster.addHost(self.host)


	# <METRIC>

	def startElement_METRIC(self, name, attrs):
		self.host.addMetric(Metric(attrs.get('NAME'),
					   attrs.get('VAL'),
					   attrs.get('TYPE'),
					   attrs.get('UNITS'),
					   attrs.get('SOURCE'),
					   attrs.get('TN'),
					   attrs.get('TMAX'),
					   attrs.get('DMAX')))

	#
	# Access Methods
	#

	def getXML(self):
		return self.xml

	def getVersion(self):
		return self.root.getVersion()

	def getSource(self):
		return self.root.getSource()

	def getClustersNames(self):
		return self.root.getClusterNames()

	def getCluster(self, name=None):
		clusters = self.root.getClusterNames()
		if not name:
			if len(clusters) == 1:
				return self.root.getCluster(clusters[0])
			else:
				raise GangliaError, 'cannot handle multiple clusters'
		else:
			return self.root.getCluster(name)


	def clusterSize(self):
		"""Returns the number of hosts ganglia thinks are present
		and alive in this cluster."""

		if not self.isConnected():
			self.connect()

		hosts = 0
		for h in self.getCluster().getHosts():
			if h.alive():
				hosts = hosts + 1

		return hosts


	def getMetricNames(self):
		list = []
		for cluster in self.root.getClusters():
			for host in cluster.getHosts():
				for name in host.getMetricNames():
					if name not in list:
						list.append(name)
		list.sort()
		return list
