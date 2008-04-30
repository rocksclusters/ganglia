<?php
#
# A Page that shows the job placements or assignments in the
# cluster. Similar to the physical view ganglia page. Inspired
# by ideas from Dave Pierce at Scripps Institute of Oceanography.
#
# Uses the pbs.py gschedule module which publishes PBS data
# using Ganglia's gmetric. 
# Ganglia parsing code based on work by Matt Massie <massie@cs.berkeley.edu>.
#
# Requires ganglia >= 2.5.1 with garbage collecting.
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
# $Log: assignments.php,v $
# Revision 1.10  2008/04/24 12:33:22  bruno
# fix for job detail page -- thanks to Graham Inggs for the fix.
#
# Revision 1.9  2008/03/06 23:41:52  mjk
# copyright storm on
#
# Revision 1.8  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.7  2006/09/11 22:48:18  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:34  mjk
# 4.2 copyright
#
# Revision 1.5  2005/10/12 18:09:20  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:57  mjk
# updated copyright
#
# Revision 1.3  2005/05/24 21:22:26  mjk
# update copyright, release is not any closer
#
# Revision 1.2  2005/04/21 22:03:06  fds
# Fix a 3.3.0 bug that affected Cluster Top/Queue sorting when the cluster name
# had spaces in it. (Pointed out by Caroline Papadopoulos)
#
# Revision 1.1  2005/03/08 00:03:35  fds
# The Ganglia Roll. Moved all relevant source from rocks/src/ganglia here.
# Uses Ganglia v2.5.x.
#
# Revision 1.16  2004/10/04 19:07:04  fds
# New Cluster Gmetric inspector. General support for Grid access to Top
# and Job queue: you can see a cluster Queue for a on meta monitor. (Wilfred
# should be pleased).
#
# Revision 1.15  2004/04/13 19:55:07  fds
# Some attention to physical job view.
#
#

$onejob = $_GET["onejob"];
$oneuser = $_GET["oneuser"];

$GHOME="../..";
include_once "$GHOME/class.TemplatePower.inc.php";
include_once "./get-ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";

$tpl = new TemplatePower("templates/assignments.tpl");
$tpl->assignInclude("header", "templates/header.tpl");
$tpl->prepare();

$self="./assignments.php";
$state="c=" . rawurlencode($_GET[c]);

$tpl->assign("self",$self);
$tpl->assign("title", "Physical Job Assignments");
$tpl->assign("link", "<a href=./queue.php?$state>Back to Job Queue</a>");
$tpl->assign("cluster_url",rawurlencode($clustername));
$tpl->assign("cluster",$clustername);
$tpl->assign("now",date("r"));

list($jobs, $queue) = getJobs();

#
# Make suitable assignments data structures.
#
$assignments = array();
$jobnodes = array();
$nodeusers = array();

if (is_array($jobs)) 
{
	foreach ($jobs as $id=>$job)
	{
		#echo "Looking at job $id<br>";
		if (!$job[nodes]) continue;

		$nodelist = decode($job[nodes]);
		foreach ($nodelist as $name) 
		{
			# Track usage by node name.
			$assignments[$name][jobs][$id] += 1;
			$assignments[$name][P] += 1;
			# To count how many unique nodes this job runs on.
			$jobnodes[$id][$name] = 1;
			# To count how many nodes are used by whom (which user).
			$nodeusers[$job[user]][$name] = 1;
		}
	}
}

#-------------------------------------------------------------------------------
# Displays a rack and all its nodes.
function showrack($ID)
{
	global $racks, $clustername, $tpl, $assignments; 
	global $onejob, $oneuser, $jobnodes, $nodeusers;
	global $state;

	if ($ID>=0) {
		$tpl->assign("RackID","<tr><th>Rack $ID</th></tr>");
	}

	# A string of node HTML for the template.
	$nodes="";

	foreach ($racks[$ID] as $name) {

		if ($onejob and !$jobnodes[$onejob][$name]) 
			continue;
		if ($oneuser and !$nodeusers[$oneuser][$name]) 
			continue;

		$P = $assignments[$name][P];
		$jobsizes = $assignments[$name][jobs];

		if (!count($jobsizes)) 
			$jobrow = "";
		else 
		{
			$class = $P ? "job" : "";
			$jobrow = "<tr><td colspan=2 class=$class>";
			#
			# Show who is using what processors on this node.
			#
			foreach ($jobsizes as $id=>$P) {
				if (!$id) continue;
				$job = $jobs[$id];
				$jobrow .= "$P: $job[user] <a href=./job.php?"
					."$state&id=$id>$id</a> ";
			}
			$jobrow .= "</td></tr>";
		}
	
		# Use the standard ganglia node box function.
		$nodes .= nodebox($name, 1, "<i>$name</i>", $jobrow);
	}

	return $nodes;
}
#-------------------------------------------------------------------------------

#
# My Main
#

# 2Key = "Rack ID / Rank (order in rack)" = [hostname, UP|DOWN]
$racks = physical_racks();

# Make a $cols-wide table of Racks.
$cols=5;
$i=1;
foreach ($racks as $rack=>$v) 
{
	$tpl->newBlock("racks");

	$racknodes = showrack($rack);

	$tpl->assign("nodes",$racknodes);

	if (! ($i++ % $cols))
		$tpl->assign("tr","</tr><tr>");
}

#
# Summarize the jobs on the cluser.
#
if (is_array($jobs)) {
	foreach ($jobs as $id=>$job) 
	{
		if ($job[state] != "Running") continue;
		$tpl->newBlock("jobs");
		$checked = ($onejob==$id) ? $checked="checked" : "";
		$tpl->assign("button",
		 "<input type=radio name=onejob value=$id "
		 ."OnClick=\"selectjob.submit()\" $checked>");
		$n = count($jobnodes[$id]);
		$s = $n>1 ? "s" : "";
		$Ps = $job[P]>1 ? "s" : "";
		$tpl->assign("summary",
			"<a href=\"./job.php?$state&id=$id\">$id.</a> "
			."$job[name] ($job[user]): "
			."$job[P]/$n ");
	}
	foreach ($nodeusers as $user=>$nodes) 
	{
		$tpl->newBlock("users");
		$checked = ($oneuser==$user) ? "checked" : "";
		$tpl->assign("button",
		 "<input type=radio name=oneuser value=\"$user\" "
		 ."OnClick=\"selectuser.submit()\" $checked>");
		$n = count($nodes);
		$s = $n>1 ? "s" : "";
		$tpl->assign("user","$user ($n node$s)");
	}
}

$tpl->printToScreen();

?>
