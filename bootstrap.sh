#!/bin/sh
#
# This file should remain OS independent
#
# $Id: bootstrap.sh,v 1.13 2010/09/07 23:53:13 bruno Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4 (Maverick)
# 
# Copyright (c) 2000 - 2010 The Regents of the University of California.
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
# $Log: bootstrap.sh,v $
# Revision 1.13  2010/09/07 23:53:13  bruno
# star power for gb
#
# Revision 1.12  2009/12/10 00:06:37  bruno
# more junk
#
# Revision 1.11  2009/12/09 22:19:00  bruno
# new
#
# Revision 1.10  2009/05/01 19:07:15  mjk
# chimi con queso
#
# Revision 1.9  2008/10/18 00:56:07  mjk
# copyright 5.1
#
# Revision 1.8  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.7  2008/03/06 23:41:50  mjk
# copyright storm on
#
# Revision 1.6  2007/06/23 04:03:34  mjk
# mars hill copyright
#
# Revision 1.5  2006/09/11 22:48:10  mjk
# monkey face copyright
#
# Revision 1.4  2006/08/23 20:36:46  anoop
# Upgraded Ganglia from 2.5.7 to 3.0.3
# Upgraded RRD Tool from 1.0.38 to 1.2.15
#
# Changes to the roll to adapt the roll to the upgrades.
#
# Revision 1.3  2006/08/10 00:10:27  mjk
# 4.2 copyright
#
# Revision 1.2  2006/06/19 18:02:16  bruno
# also need rrdtool-devel
#
# Revision 1.1  2006/06/19 17:23:58  bruno
# bootstrap file for ganglia
#
#

. $ROLLSROOT/etc/bootstrap-functions.sh

if [ `./_os` == "linux" ]; then
	compile_and_install rrdtool
fi

compile_and_install confuse

if [ `./_os` == "sunos" ]; then
	compile_and_install apr
	compile_and_install apr-util
fi

