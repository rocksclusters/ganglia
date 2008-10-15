# $Id: Makefile,v 1.15 2008/10/15 20:13:03 mjk Exp $
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
# $Log: Makefile,v $
# Revision 1.15  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.14  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.13  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.12  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.11  2006/12/02 01:04:58  anoop
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
# Revision 1.10  2006/09/11 22:48:13  mjk
# monkey face copyright
#
# Revision 1.9  2006/08/10 00:10:30  mjk
# 4.2 copyright
#
# Revision 1.8  2005/12/30 19:15:40  mjk
# removed spec files
#
# Revision 1.7  2005/10/12 18:09:17  mjk
# final copyright for 4.1
#
# Revision 1.6  2005/09/19 18:34:57  bruno
# added ganglia news back
#
# Revision 1.5  2005/09/16 01:02:53  mjk
# updated copyright
#
# Revision 1.4  2005/05/24 21:22:22  mjk
# update copyright, release is not any closer
#
# Revision 1.3  2005/03/31 22:07:43  fds
# RSS stream only shows fresh items, recalculated every hour.
#
# Revision 1.2  2005/03/31 04:22:23  fds
# RSS 0.91 compliant now. Much better journalist interface. Presenting
# the RSS feed in HTML first, with a link to the XML stream.
#
# Revision 1.1  2005/03/08 00:03:31  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.4  2004/04/16 00:26:51  fds
# News on first boot.
#
# Revision 1.3  2004/04/13 20:16:05  fds
# The Ganglia RSS news prototype. 2 journalsits: MIA and load.
#
# Revision 1.2  2004/03/25 19:14:57  fds
# Tweaks
#
# Revision 1.1  2004/03/25 16:55:05  fds
# Quick add to give a valid rpm target.
#
#


PKGROOT = /opt/ganglia
SCRIPTS = cook-news 
PYLIB = $(wildcard gmon/*py)
CGI = $(wildcard www/*cgi)
JOURNALISTS = $(wildcard gmon/news/*.py)

REDHAT.ROOT = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
-include $(ROCKSROOT)/etc/python.mk
include python.mk


build:

install:: $(SCRIPTS)
	mkdir -p $(ROOT)/$(PKGROOT)/bin
	$(INSTALL) -m0555 $(SCRIPTS) $(ROOT)/$(PKGROOT)/bin

	mkdir -p $(ROOT)/$(PY.ROCKS)/gmon/news
	touch $(ROOT)/$(PY.ROCKS)/gmon/news/__init__.py
	$(INSTALL) -m 0444 $(PYLIB) $(ROOT)/$(PY.ROCKS)/gmon
	$(INSTALL) -m 0444 $(JOURNALISTS) $(ROOT)/$(PY.ROCKS)/gmon/news/

	mkdir -p $(ROOT)/var/www/html/rss/ganglia
	$(INSTALL) -m0555 www/{*cgi,*php,*tpl,*css} \
		$(ROOT)/var/www/html/rss/ganglia

	mkdir -p $(ROOT)/var/www/html/images
	$(INSTALL) -m0444 www/images/*png $(ROOT)/var/www/html/images

	mkdir -p $(ROOT)/etc/rc.d/rocksconfig.d
	$(INSTALL) -m0555 post-50-news.sh \
		$(ROOT)/etc/rc.d/rocksconfig.d/post-50-news

	mkdir -p $(ROOT)/var/ganglia/news

clean::
	rm -f $(SCRIPTS)
	rm -f $(NAME).spec.in

