# 
# $Id: Makefile,v 1.15 2008/10/15 20:13:04 mjk Exp $
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
# Revision 1.15  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.14  2008/03/06 23:41:52  mjk
# copyright storm on
#
# Revision 1.13  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.12  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.11  2006/12/02 01:04:59  anoop
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
# Revision 1.10  2006/09/15 02:03:44  mjk
# builds
#
# Revision 1.9  2006/09/11 22:48:17  mjk
# monkey face copyright
#
# Revision 1.8  2006/08/10 00:10:33  mjk
# 4.2 copyright
#
# Revision 1.7  2005/12/30 19:15:41  mjk
# removed spec files
#
# Revision 1.6  2005/10/18 20:20:32  bruno
# automatically set the copyright date
#
# Revision 1.5  2005/10/12 18:09:20  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:57  mjk
# updated copyright
#
# Revision 1.3  2005/05/24 21:22:25  mjk
# update copyright, release is not any closer
#
# Revision 1.2  2005/04/05 20:45:35  nadya
# move logic of creating rocks.dsl, rocks.css and stylesheet-images to Rules.mk
# Add target predoc in order to make docs in a local directory
#
# Revision 1.1  2005/03/08 00:03:34  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.2  2005/01/18 16:28:09  fds
# Normalized stylesheets and stylesheet-images: no longer is rocks.dsl
# repeated for every roll by default. The pdf and html targets perform better
# when used on their own (for testing).
#
# Revision 1.1  2004/11/30 01:42:10  fds
# Normalize! This usersguide has a DOCROOT make var that pulls stylesheet-images
# and rocks.css, rocks.dsl from a central location in CVS. These are currently
# copied in several locations, namely rocks/src/roll/grid/src/usersguide, and
# rocks/src/roll/condor/src/usersguide among others.
#

PKGROOT = /var/www/html/roll-documentation/ganglia/$(VERSION)

REDHAT.ROOT = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

default: $(NAME).spec 

html: predoc
	jw --backend html --dsl $(CURDIR)/rocks.dsl#html index.sgml

pdf: predoc
	jw --backend pdf --dsl $(CURDIR)/rocks.dsl#print index.sgml

build: html pdf

install:: build
	mkdir -p $(ROOT)/$(PKGROOT)/images
	mkdir -p $(ROOT)/$(PKGROOT)/stylesheet-images
	$(INSTALL) -m 0444 index.pdf		$(ROOT)/$(PKGROOT)/$(NAME).pdf
	$(INSTALL) -m 0444 *.html    	$(ROOT)/$(PKGROOT)/
	$(INSTALL) -m 0444 images/*.png	$(ROOT)/$(PKGROOT)/images/
	$(INSTALL) -m 0444 stylesheet-images/{*.gif,*.png} \
		$(ROOT)/$(PKGROOT)/stylesheet-images/
	$(INSTALL) -m 0444 rocks.css $(ROOT)/$(PKGROOT)/

clean::
	rm -f *.html
	rm -f index.pdf

