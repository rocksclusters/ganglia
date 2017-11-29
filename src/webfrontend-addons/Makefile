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
# Revision 1.24  2012/11/27 00:48:59  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.23  2012/05/31 00:46:26  clem
# ganglia 3.3.7 updated betaversion
#
# Revision 1.22  2012/05/06 05:49:08  phil
# Copyright Storm for Mamba
#
# Revision 1.21  2011/07/27 22:52:36  anoop
# Disable addons for the current release
#
# Revision 1.20  2011/07/23 02:31:00  phil
# Viper Copyright
#
# Revision 1.19  2010/09/07 23:53:19  bruno
# star power for gb
#
# Revision 1.18  2009/07/10 22:04:29  bruno
# add 'Rocks Tools' back
#
# Revision 1.17  2009/06/15 23:46:00  bruno
# don't include the rocks tools links (job queue, cluster top, etc.) for this
# release
#
# Revision 1.16  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.15  2009/04/28 23:28:09  bruno
# fixes
#
# Revision 1.14  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.13  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.12  2008/03/06 23:41:52  mjk
# copyright storm on
#
# Revision 1.11  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.10  2007/04/28 00:17:14  anoop
# WEBSERVER_ROOT variable necessary to distinguish solaris webserver root
# and linux apache webserver root.
#
# Revision 1.9  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.8  2006/12/02 01:04:59  anoop
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
# Revision 1.7  2006/09/11 22:48:17  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:33  mjk
# 4.2 copyright
#
# Revision 1.5  2005/12/30 19:15:42  mjk
# removed spec files
#
# Revision 1.4  2005/10/12 18:09:20  mjk
# final copyright for 4.1
#
# Revision 1.3  2005/09/16 01:02:57  mjk
# updated copyright
#
# Revision 1.2  2005/05/24 21:22:26  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/08 00:03:34  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.11  2004/03/25 03:15:07  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.10  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.9  2003/08/04 22:09:18  fds
# Auto discover domain name.
#
# Revision 1.8  2003/07/24 17:48:16  fds
# Added new 'extra' extensions.
#
# Revision 1.7  2003/06/02 05:10:27  fds
# Back to release 1
#
# Revision 1.6  2003/05/14 18:01:58  fds
# Added RPM to enable access to the Rocks Monitoring Grid
#
# Revision 1.5  2003/02/17 18:43:04  bruno
# updated copyright to 2003
#
# Revision 1.4  2003/02/03 17:42:41  fds
# A link to maintain backwards compatibility with 2.3.0.
#
# Revision 1.3  2002/10/18 21:33:25  mjk
# Rocks 2.3 Copyright
#
# Revision 1.2  2002/10/16 16:34:18  bruno
# moved files to /var/www/html
#
# Revision 1.1  2002/10/15 22:29:47  fds
# Original design for RPM-building spec file. Using makefile logic heavily.
#
#

PKGROOT = $(WEBSERVER_ROOT)/ganglia

#ADDONS = addons/rocks
#PHP = $(wildcard $(ADDONS)/*.php)
#IMAGES = $(wildcard $(ADDONS)/images/*jpg)
#TEMPLATES = $(wildcard $(ADDONS)/templates/*tpl)

# Extensions to the standard Ganglia Rocks template.
EXTRAS = $(wildcard templates/default/*.tpl)
IMAGES = $(wildcard templates/default/images/*.png)


REDHAT.ROOT = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

install::
	mkdir -p $(ROOT)/$(PKGROOT)/$(ADDONS)/templates
	mkdir -p $(ROOT)/$(PKGROOT)/$(ADDONS)/images

	#$(INSTALL) -m644 $(PHP) $(ROOT)/$(PKGROOT)/$(ADDONS)
	#$(INSTALL) -m644 $(ADDONS)/styles.css $(ROOT)/$(PKGROOT)/$(ADDONS)
	#$(INSTALL) -m644 $(IMAGES) $(ROOT)/$(PKGROOT)/$(ADDONS)/images
	#$(INSTALL) -m644 $(TEMPLATES) $(ROOT)/$(PKGROOT)/$(ADDONS)/templates
	#$(INSTALL) -m644 conf.php $(ROOT)/$(PKGROOT)/

	# For backwards compatibility with 2.3.0
	#-(cd $(ROOT)/$(PKGROOT)/rocks/; ln -sf queue.php pbs.php)

	# Extend the standard Ganglia 'Rocks' template.
	mkdir -p $(ROOT)/$(PKGROOT)/templates/default
	mkdir -p $(ROOT)/$(PKGROOT)/templates/default/images
	$(INSTALL) -m644 $(EXTRAS) $(ROOT)/$(PKGROOT)/templates/default
	$(INSTALL) -m644 $(IMAGES) $(ROOT)/$(PKGROOT)/templates/default/images

build:

clean::
	rm -f $(NAME).spec.in
