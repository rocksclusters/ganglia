#!/opt/rocks/bin/python
#
# $RCSfile: gmond.py,v $
#
# Script to generate the /etc/gmond.conf file from the Rocks MySQL database.
#
# This script must have access to the MySQL server on a Rocks Frontend node.
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
# $Log: gmond.py,v $
# Revision 1.20  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.19  2008/06/27 21:45:36  bruno
# need to allow access to private network too
#
# Revision 1.18  2008/06/27 21:29:11  bruno
# new access control that doesn't cause gmond to seg fault
#
# Revision 1.17  2008/06/16 19:19:46  bruno
# block all gmetad requests by default
#
# Revision 1.16  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.15  2007/10/31 00:29:54  anoop
# removes the mcast_if line. Temporary fix for solaris. Will be changed
# in the future.
#
# Revision 1.14  2007/10/17 00:28:27  bruno
# in order for the location (rack, rank, plane) to be reported, it must be
# listed as a metric.
#
# Revision 1.13  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.12  2007/06/08 14:58:18  anoop
# Stupid syntax error fixed. I reaaly should remember this correctly from
# now on.
#
# Revision 1.11  2007/04/28 00:15:56  anoop
# Private interface is now not always eth0. The value is taken from the database
# as necessary. This is useful for solaris
#
# Revision 1.10  2006/09/11 22:48:12  mjk
# monkey face copyright
#
# Revision 1.9  2006/08/23 20:36:47  anoop
# Upgraded Ganglia from 2.5.7 to 3.0.3
# Upgraded RRD Tool from 1.0.38 to 1.2.15
#
# Changes to the roll to adapt the roll to the upgrades.
#
# Revision 1.8  2006/08/10 00:10:28  mjk
# 4.2 copyright
#
# Revision 1.7  2006/01/16 06:49:03  mjk
# fix python path for source built foundation python
#
# Revision 1.6  2005/10/12 18:09:16  mjk
# final copyright for 4.1
#
# Revision 1.5  2005/09/16 01:02:52  mjk
# updated copyright
#
# Revision 1.4  2005/07/26 18:54:24  bruno
# move gmond.py into the rocks foundation
#
# Revision 1.3  2005/05/24 21:22:21  mjk
# update copyright, release is not any closer
#
# Revision 1.2  2005/05/23 20:10:01  fds
# Tweaks
#
# Revision 1.1  2005/05/18 04:52:39  fds
# Moved gmon dbreport into ganglia roll.
#
# Revision 1.1  2005/03/01 02:02:46  mjk
# moved from core to base
#
# Revision 1.10  2004/11/02 01:39:53  fds
# Converge faster by increasing load on frontend papache server (suggesion by phil).
#
# Revision 1.9  2004/07/14 23:53:35  fds
# ClusterOwner has been replaced by CertificateOrganization
#
# Revision 1.8  2004/03/25 03:15:35  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.7  2003/08/15 22:34:46  mjk
# 3.0.0 copyright
#
# Revision 1.6  2003/07/16 19:44:45  fds
# Reporting fully-qualified domain names in all cases.
#
# Revision 1.5  2003/05/22 16:39:27  mjk
# copyright
#
# Revision 1.4  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.3  2002/10/18 21:33:26  mjk
# Rocks 2.3 Copyright
#
# Revision 1.2  2002/10/12 16:52:07  fds
# Added rowcount() method to detect sucessful queries.
#
# Revision 1.1  2002/10/02 20:44:16  fds
# Original design of gmond database report
#

import sys
import os
import rocks.reports.base

class Report(rocks.reports.base.ReportBase):
      
	def run(self):
		if not len(self.args):
			print "/* Error - I need a node name argument. */"
			return
		name = self.args[0]
		eth_if = "eth0"
		# Get only the first part of the host name. 
		#Otherwise database query will fail
		name = name.split('.')[0]

		# Find out whether its a frontend or compute
		# If it doesn't exist in the database quit
		self.execute('select memberships.Compute from memberships,nodes '
				'where memberships.ID=nodes.Membership '
				'and nodes.Name="%s"' % (name))

		if not self.rowcount():
			print "/* Error - Cannot find node in Database. */"
			return
		# Get the membership of the node. If node is compute, which
		# is what the above SQL query returns, then make the node deaf.
		deaf = self.fetchone()

		# Get information about the cluster. Such as name owner, url and
		# the latitude and longitude.
		try:
			owner = self.sql.getGlobalVar('Info','CertificateOrganization')
			clustername = self.sql.getGlobalVar('Info','ClusterName')
			url = self.sql.getGlobalVar('Info','ClusterURL')
			latlong = self.sql.getGlobalVar('Info','ClusterLatlong')
		except:
			clustername=owner=url=latlong="unspecified" 

		# Get the multicast address of the cluster. If it's not in the
		# database, just choose some random one. It's all randomly generated anyway
		try:
			mcast = self.sql.getGlobalVar('Kickstart','Multicast')
		except:
			mcast = '239.2.11.171'

		# Get the location of the machine in the cluster.
		# The cluster is assumed to be 2 dimensional.
		self.execute('select rack, rank from nodes '
			'where name="%s" and site=0 limit 1' % name)
		if self.rowcount():
			rack, rank = self.fetchone()
			plane = 0
			location = "%u,%u,%u" % (rack, rank, plane)
		else:
			location="unspecified"
		
		self.execute('select device from networks '
			'where name="%s"' % name)
		if self.rowcount():
			eth_if = self.fetchone()[0]
			
		private_network = self.sql.getGlobalVar('Kickstart',
			'PrivateNetwork')
		private_netmask = self.sql.getGlobalVar('Kickstart',
			'PrivateNetmaskCIDR')
		
		# Finally start printing out the gmond configuration
		# The comments in the gmond configuration file are C-style
		# comments. 
		print "/*"
		print "Ganglia gmond configuration file for %s" % (name)
		print "DO NOT EDIT - Automatically generated by dbreport"
		print "*/"
		# Print out the globals. This is an important section.
		print ""
		print "/* Global Configuration */"
		print """
globals {
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
}""" % (deaf)
		print ""
		print "/* Cluster Specific attributes */"
		print """

cluster { 
  name = "%s" 
  owner = "%s" 
  latlong = "%s" 
  url = "%s"
}""" % (clustername,owner,latlong,url) 

		print ""
		print "/* Host configuration */"
		print """
host {
	location="%s"
}""" % (location)

		print ""
		print "/* UDP Channels for Send and Recv */"
		print """
udp_recv_channel {
	mcast_join = %s
	port = 8649
}

udp_send_channel {
	mcast_join = %s
	port = 8649
}""" % (mcast,mcast)

		print ""
		print "/* TCP Accept Channel */"
		print """
tcp_accept_channel {
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
}""" % (private_network, private_netmask)

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

		print ""
		print "/* Metrics Collection group */"
		print """
collection_group {
  collect_every = 60
  time_threshold = 300"""
		for i in metric_array:
			print """
   metric {
	name = "%s"
	value_threshold = 10.0
     }""" % (i.strip())

		print "}"
