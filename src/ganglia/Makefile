#
# Rocks Ganglia Custom Metrics for HPC.
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
# $Log: Makefile,v $
# Revision 1.33  2012/11/27 00:48:56  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.32  2012/05/06 05:49:05  phil
# Copyright Storm for Mamba
#
# Revision 1.31  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.30  2010/09/07 23:53:14  bruno
# star power for gb
#
# Revision 1.29  2009/10/05 17:40:08  bruno
# build fix
#
# Revision 1.28  2009/07/13 20:20:30  bruno
# restart gmond on all nodes after the frontend boots
#
# Revision 1.27  2009/07/10 21:05:18  bruno
# make 80 column friendly
#
# Revision 1.26  2009/07/10 20:32:04  bruno
# get rocks-defined metrics back in ganglia roll
#
# Revision 1.25  2009/05/01 19:07:15  mjk
# chimi con queso
#
# Revision 1.24  2009/04/24 22:07:49  anoop
# Moved the solaris specific startup scripts to ganglia-hpc package
#
# Revision 1.23  2009/04/21 18:10:54  bruno
#  - converted gmond dbreport to rocks command line
#  - added supporting packages for ganglia monitor core
#
# Revision 1.22  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.21  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.20  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.19  2007/08/13 19:37:50  bruno
# moved profile.d/ganglia-binaries.*sh to ganglia roll
#
# Revision 1.18  2007/08/13 19:22:41  bruno
# moved ganglia-save-rrds.cron to the ganglia roll
#
# Revision 1.17  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.16  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.15  2006/12/02 01:04:58  anoop
# Ridiculously big ass commit.
# Also known as the week after thanksgiving 2006. Or "The day Anoop
# broke Rocks".
#
# Main Changes.
#
# 1. Added a roll-profile.mk file. This is meant as a makefile for building
# the profile rpm containing all the XML files meant for the roll. This is a
# breakaway from the spec.in file method of building the profile RPM.
#
# 2. The variable PWD is now changed to CURDIR. The main reason for this is
# PWD is supplied by the shell. CURDIR is the variable supplied by gmake itself.
# This means we can have a slightly more platform independant way of doing things.
# Also Solaris was failing to set PWD correctly in the source directories, wreaking
# havoc on the location of the BUILD and PKG directories.
#
# Revision 1.14  2006/11/30 01:15:31  bruno
# moved ganglia-restore-rrds into the base roll
#
# also configured the service to be enabled on boot
#
# Revision 1.13  2006/09/11 22:48:12  mjk
# monkey face copyright
#
# Revision 1.12  2006/08/10 00:10:28  mjk
# 4.2 copyright
#
# Revision 1.11  2005/12/30 19:15:40  mjk
# removed spec files
#
# Revision 1.10  2005/10/12 18:09:15  mjk
# final copyright for 4.1
#
# Revision 1.9  2005/09/16 01:02:52  mjk
# updated copyright
#
# Revision 1.8  2005/09/02 00:07:15  bruno
# move to foundation
#
# Revision 1.7  2005/07/26 18:54:23  bruno
# move gmond.py into the rocks foundation
#
# Revision 1.6  2005/05/24 21:22:21  mjk
# update copyright, release is not any closer
#
# Revision 1.5  2005/05/23 20:10:01  fds
# Tweaks
#
# Revision 1.4  2005/05/18 04:52:39  fds
# Moved gmon dbreport into ganglia roll.
#
# Revision 1.3  2005/03/17 22:20:57  fds
# Path tweaks
#
# Revision 1.2  2005/03/08 00:34:38  fds
# Moved hpc-ganglia metrics from hpc roll. Insert-ethers plugin for ganglia.
#
# Revision 1.1  2005/03/08 00:26:58  fds
# Rocks Ganglia Custom Metrics for HPC
#
# Revision 1.2  2004/03/25 03:16:09  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.1  2004/02/18 20:21:31  fds
# Moved mpd and cluster-top metrics here from base.
#
# Revision 1.1  2004/02/18 19:46:51  fds
# Added Ganglia Monitoring of PBS.
#
#

PKGROOT = /opt/ganglia
PLUGINDIR = /opt/rocks/var/plugins/insertethers
PLUGINS = $(wildcard plugins/*.py)
REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

-include $(ROCKSROOT)/etc/python.mk
include python.mk

build:

install::
	mkdir -p $(ROOT)/$(PKGROOT)/$(LIBARCH)/ganglia/python_modules
	mkdir -p $(ROOT)/$(PKGROOT)/etc/conf.d
	# Install insert-ethers plugins
	mkdir -p $(ROOT)/$(PLUGINDIR)
	$(INSTALL) -m 0444 $(PLUGINS) $(ROOT)/$(PLUGINDIR)
	# Install ganglia-restore-rrds scripts
	mkdir -p $(ROOT)/$(INIT_SCRIPTS_DIR)
	$(INSTALL) -m 0755 init.d/ganglia-restore-rrds \
		$(ROOT)/$(INIT_SCRIPTS_DIR)
	# Install cron job that works saves ganglia data
	mkdir -p $(ROOT)/etc/cron.weekly
	$(INSTALL) -m 0755 cron.weekly/ganglia-save-rrds.cron \
		$(ROOT)/etc/cron.weekly
	# Install the ganglia profile scripts
	mkdir -p $(ROOT)/etc/profile.d
	$(INSTALL) -m 0755 profile.d/*sh $(ROOT)/etc/profile.d

clean::
