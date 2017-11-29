#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWindwer)
# 		         version 7.0 (Manzanita)
# 
# Copyright (c) 2000 - 2017 The Regents of the University of California.
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
# Revision 1.20  2012/11/27 00:48:57  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.19  2012/05/06 05:49:07  phil
# Copyright Storm for Mamba
#
# Revision 1.18  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.17  2010/09/07 23:53:17  bruno
# star power for gb
#
# Revision 1.16  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.15  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.14  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.13  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.12  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.11  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.10  2006/12/02 01:04:59  anoop
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
# Revision 1.9  2006/09/11 22:48:16  mjk
# monkey face copyright
#
# Revision 1.8  2006/08/10 00:10:32  mjk
# 4.2 copyright
#
# Revision 1.7  2005/12/30 19:15:41  mjk
# removed spec files
#
# Revision 1.6  2005/10/12 18:09:18  mjk
# final copyright for 4.1
#
# Revision 1.5  2005/09/16 01:02:55  mjk
# updated copyright
#
# Revision 1.4  2005/09/02 00:07:16  bruno
# move to foundation
#
# Revision 1.3  2005/07/26 19:30:25  bruno
# make more ganglia python functions use the rocks foundation
#
# Revision 1.2  2005/05/24 21:22:24  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:58:36  fds
# The ganglia command line client. Moved from the monolithic source tree.
#
# Revision 1.25  2004/03/25 03:15:01  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.24  2003/10/21 20:40:26  fds
# Gschedule is dead. Replaced by greceptor.
#
# Revision 1.23  2003/10/06 18:40:21  fds
# Some features to make this package play nice outside of Rocks.
# -Symbolic link in package to make 'gmon' python modules visible.
# -Man page put in a central location.
# These changes were suggested by Jaegermann (michal@harddata.com), but
# I like the links to be part of the RPM file list so they are correctly
# removed on update.
#
# Revision 1.22  2003/09/16 00:35:05  fds
# Made python version handling cleaner.
#
# Revision 1.21  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.20  2003/08/04 19:57:59  fds
# Using Process.cpus() call to make things more clear.
#
# Revision 1.19  2003/07/15 23:51:15  fds
# Added glisten initscript, and improved the glisten daemon.
#
# Revision 1.18  2003/07/11 23:06:19  fds
# Doing the Multicast dance from within python.
#
# Revision 1.17  2003/03/10 18:11:53  fds
# Compiling and installing python extension modules correctly.
#
# Revision 1.16  2003/03/10 17:57:48  fds
# Making python extention modules.
#
# Revision 1.15  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.14  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.13  2002/10/15 17:14:35  fds
# Gschedule package ready, and daemon tested.
#
# Revision 1.12  2002/10/15 00:05:29  fds
# Making the RPM with most logic in the makefile.
#
# Revision 1.11  2002/10/04 17:00:54  mjk
# *** empty log message ***
#
# Revision 1.10  2002/10/03 23:06:08  mjk
# futzed with CVS repository structure
#
# Revision 1.9  2002/09/26 22:30:21  mjk
# typo
#
# Revision 1.8  2002/09/26 22:27:29  mjk
# *** empty log message ***
#
# Revision 1.7  2002/09/25 17:01:38  mjk
# more path fixes
#
# Revision 1.6  2002/09/25 16:34:00  mjk
# move to /opt/ganglia
#
# Revision 1.5  2002/07/19 21:10:30  bruno
# changed version to 2.3
#
# Revision 1.4  2002/05/24 00:00:34  mjk
# checkpoint
#
# Revision 1.3  2002/04/18 17:06:49  mjk
# Adding gschedule
#
# Revision 1.2  2002/04/09 00:30:51  mjk
# mds changes
#
# Revision 1.1  2002/02/25 21:14:22  mjk
# Moved out of our patched version of ganglia and into its own RPM.
#

SCRIPTS = ganglia
PKGROOT = /opt/ganglia
MANROOT = /usr/share/man
PYLIB   = $(wildcard gmon/*.py)


REDHAT.ROOT = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

-include $(ROCKSROOT)/etc/python.mk
include python.mk


install:: $(SCRIPTS)
	mkdir -p $(ROOT)/$(PKGROOT)/bin/
	$(INSTALL) -m 0555 $(SCRIPTS)  $(ROOT)/$(PKGROOT)/bin/

	mkdir -p $(ROOT)/$(PKGROOT)/etc/
	$(INSTALL) -m 0444 etc/glue.schema $(ROOT)/$(PKGROOT)/etc/

	# Drop the man page in a friendly spot.
	mkdir -p $(ROOT)/usr/share/man/man1
	gzip -c $(ROOT)/$(PKGROOT)/man/man1/ganglia.1 > \
		$(ROOT)/$(MANROOT)/man1/ganglia.1.gz

	mkdir -p $(ROOT)/$(PY.ROCKS)/gmon
	$(INSTALL) -m 0444 $(PYLIB)	   $(ROOT)/$(PY.ROCKS)/gmon


build:


clean::
	rm -f $(SCRIPTS)
	rm -f *.pyc gmon/*.pyc
	rm -f $(NAME).spec.in
