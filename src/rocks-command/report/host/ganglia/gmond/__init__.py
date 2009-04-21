# $Id: __init__.py,v 1.1 2009/04/21 18:10:55 bruno Exp $
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
# $Log: __init__.py,v $
# Revision 1.1  2009/04/21 18:10:55  bruno
#  - converted gmond dbreport to rocks command line
#  - added supporting packages for ganglia monitor core
#
#

import rocks.commands

class Command(rocks.commands.report.host.ganglia.command):
	"""
	Report the configuration file that can be used for gmond.

	<example cmd='report host ganglia gmond'>
	Report the machines that are managed by SGE.
	</example>
	"""

	def run(self, params, args):
		hosts = self.getHostnames(args)

		#
		# only takes one host
		#
		if len(hosts) != 1:
			return

		host = hosts[0]

		#
		# all non-frontend nodes are 'deaf'
		#
		frontends = self.getHostnames( [ 'frontend' ] )

		if host in frontends:
			deaf = 'no'
		else:
			deaf = 'yes'

		#
		# Get information about the cluster.
		#
		try:
			owner = self.db.getHostAttr(host,
				'Info_CertificateOrganization')
		except:
			owner = "unspecified"

		try:
			clustername = self.db.getHostAttr(host,
				'Info_ClusterName')
		except:
			clustername = "unspecified"

		try:
			url = self.db.getHostAttr(host, 'Info_ClusterURL')
		except:
			url = "unspecified"

		try:
			latlong = self.db.getHostAttr(host,
				'Info_ClusterLatlong')
		except:
			latlong = "unspecified"

		#
		# Pick a low unassigned multicast address
		#
		mcast = '224.0.0.3'

		#
		# Get the location of the machine in the cluster.
		# The cluster is assumed to be 2 dimensional.
		#
		try:
			rack = self.db.getHostAttr(host, 'rack')
			rank = self.db.getHostAttr(host, 'rank')
			plane = 0
			location = "%u,%u,%u" % (rack, rank, plane)
		except:
			location = "unspecified"

		#
		# get the private interface. ganglia sends its traffic on
		# this interface
		#
		rows = self.db.execute("""select net.device from networks net,
			nodes n, subnets s where n.name = '%s' and
			n.id = net.node and s.name = 'private' and
			s.id = net.subnet""" % (host))

		if rows == 1:
			eth_if, = self.db.fetchone()
		else:
			eth_if = 'eth0'

		#
		# more networking info
		#
		private_network = self.db.getHostAttr(host,
			'Kickstart_PrivateNetwork')
		private_netmask = self.db.getHostAttr(host,
			'Kickstart_PrivateNetmaskCIDR')

		self.beginOutput()

		#
		# output the gmond configuration
		#
		# the globals
		#
		self.addOutput('', '/* Global Configuration */')
		self.addOutput('', """globals {
	daemonize = yes      
	setuid = yes
	user = nobody
	debug_level = 0
	max_udp_msg_len = 1472 
	mute = no
	deaf = %s 
	host_dmax = 0 /*secs */ 
	cleanup_threshold = 300 /*secs */ 
	gexec = no 
}""" % (deaf))

		self.addOutput('', "\n/* Cluster Specific attributes */")
		self.addOutput('', """cluster { 
	name = "%s" 
	owner = "%s" 
	latlong = "%s" 
	url = "%s"
}""" % (clustername, owner, latlong, url))

		self.addOutput('', "\n/* Host configuration */")
		self.addOutput('', """host {
	location="%s"
}""" % (location))

		self.addOutput('', "\n/* UDP Channels for Send and Recv */")
		self.addOutput('', """udp_recv_channel {
	mcast_join = %s
	port = 8649
}

udp_send_channel {
	mcast_join = %s
	port = 8649
}""" % (mcast, mcast))

		self.addOutput('', "\n/* TCP Accept Channel */")
		self.addOutput('', """tcp_accept_channel {
	port = 8649

	acl {
		default = "deny"

		access {
			ip = 127.0.0.1
			mask = 32
			action = "allow"
		}

		access {
			ip = %s
			mask = %s
			action = "allow"
		}
	}
}""" % (private_network, private_netmask))

		# Now this is an important part. Metrics in ganglia 3.x follow
		# the collection group style of collecting metrics. Look at the 
		# ganglia README to define your own metrics. For this we create 
		# a list with all the metrics we want to list, and then create
		# a metrics array. Finally, we assign a default value_threshold
		# of 10% to each metric. This means, data is sent every time any
		# metric increases by 10%.
		
		metric_array = [
			'location',
			'load_one',
			'mem_total',
			'cpu_intr',
			'proc_run',
			'load_five',
			'disk_free',
			'mem_cached',
			'mtu',
			'cpu_sintr',
			'pkts_in',
			'bytes_in',
			'bytes_out',
			'swap_total',
			'mem_free',
			'load_fifteen',
			'boottime',
			'cpu_idle',
			'cpu_aidle',
			'cpu_user',
			'cpu_nice',
			'sys_clock',
			'mem_buffers',
			'cpu_system',
			'part_max_used',
			'disk_total',
			'heartbeat',
			'mem_shared',
			'machine_type',
			'cpu_wio',
			'proc_total',
			'cpu_num',
			'cpu_speed',
			'pkts_out',
			'swap_free'
		]

		self.addOutput('', "\n/* Metrics Collection group */")
		self.addOutput('', """collection_group {
	collect_every = 60
	time_threshold = 300""")

		for i in metric_array:
			self.addOutput('', """	metric {
		name = "%s"
		value_threshold = 10.0
	}""" % (i.strip()))

		self.addOutput('', "}")

		self.endOutput()
