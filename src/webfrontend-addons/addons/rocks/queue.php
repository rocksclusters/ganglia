<?php
#
# A Page to monitor the PBS parallel job scheduling queues.
# Uses the pbs.py gschedule module which publishes PBS data
# using Ganglia's gmetric. Ganglia parsing code based on work
# by Matt Massie <massie@cs.berkeley.edu>.
#
# Requires ganglia >= 2.5.1 with garbage collecting.
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
# $Log: queue.php,v $
# Revision 1.15  2010/09/07 23:53:19  bruno
# star power for gb
#
# Revision 1.14  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.13  2009/04/27 17:58:26  bruno
# fixes
#
# Revision 1.12  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.11  2008/04/24 12:33:22  bruno
# fix for job detail page -- thanks to Graham Inggs for the fix.
#
# Revision 1.10  2008/03/06 23:41:52  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:36  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/18 21:45:49  anoop
# Small changes to ganglia and SGE roll.
# sge.py now parses the date in the right format.
# queue.py does not report a running time if the job not yet started.
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
# Revision 1.14  2004/10/06 00:50:02  fds
# Cluster name may have special characters in it.
#
# Revision 1.13  2004/10/04 19:07:04  fds
# New Cluster Gmetric inspector. General support for Grid access to Top
# and Job queue: you can see a cluster Queue for a on meta monitor. (Wilfred
# should be pleased).
#
# Revision 1.12  2004/09/07 23:43:48  fds
# Fixed bad time reporting, 80-col code.
#
# Revision 1.11  2004/04/13 02:58:11  fds
# Tested with both SGE and PBS schedulers. New Update button gives instant
# new information about queues.
#
#
$GHOME="../..";
$update = 1;
$sortby = $_GET["sortby"];
$sortorder = $_GET["sortorder"];
$user = $_GET["user"];
$update = $_GET["update"];

include_once "$GHOME/class.TemplatePower.inc.php";
include_once "./get-ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";

if ($update) {
	# Refresh metrics explicitly.

	$base = "/opt/ganglia/lib/python/gmon/metrics";
	if (file_exists("$base/sge.py")) {
		echo "Refreshing SGE, please wait...<br>\n";
		$SGE_ROOT="/opt/gridengine";
		$SGE_ARCH=exec("$SGE_ROOT/util/arch");
		$ENV="SGE_ROOT=$SGE_ROOT PATH=$SGE_ROOT/bin/$SGE_ARCH";
		exec("$ENV /opt/rocks/bin/grunner gmon/metrics/sge.py");
	}
	else {
		echo "Refreshing PBS, please wait...<br>\n";
		$ENV = "PATH=/opt/maui/bin:/opt/torque/bin:/opt/torque/sbin";
		system("$ENV /opt/rocks/bin/grunner gmon/metrics/pbs.py");
	}

	# Reload main page.
	$me = "$_SERVER[PHP_SELF]"
	 ."?user=$user&sortby=$sortby&sortorder=$sortorder";
	echo "<html><head>\n";
	echo "<meta http-equiv=\"Refresh\" content=\"0; URL=$me\">\n";
	echo "<meta http-equiv=\"Pragma\" content=\"no-cache\">\n";
	echo "</head></html>";
	exit;
}

$tpl = new TemplatePower("templates/queue.tpl");
$tpl->assignInclude("header", "templates/header.tpl");
$tpl->prepare();

$self="./queue.php";
$state="c=" . rawurlencode($_GET[c]);

$tpl->assign("self",$self);
$tpl->assign("title", "Job Queue");
$tpl->assign("link", 
   "<a href=./assignments.php?$state>Physical Job Assignments</a>");

if (!$sortby) $sortby="id";
if (!$sortorder) $sortorder="up";
$tpl->assign("sortby",$sortby);
$tpl->assign("sortorder",$sortorder);
$tpl->assign("sortvars","sortby=$sortby&sortorder=$sortorder");
$tpl->assign("cluster_url",rawurlencode($clustername));
$tpl->assign("cluster",$clustername);
$tpl->assign("user",$user);
$tpl->assign("now",date("r"));

#
# Some templatePower tricks to set the sortby links.
#
$columns=array("id","user","processors","state","name","runtime","TN");
foreach ($columns as $c) {
	$name=ucfirst($c);
	if ($sortby==$c) 
		$tpl->assign("${c}SortLink",$name);
	else 
		$tpl->assign("${c}SortLink",
		 "<a href=$self?$state&sortby=$c&sortorder=$sortorder>".
                 "$name</a>");
}

$orders=array("up","down");
foreach ($orders as $o) {
	$name=ucfirst($o);
	if ($sortorder==$o) 
		$tpl->assign("${o}SortOrder",$name);
	else
		$tpl->assign("${o}SortOrder",
			"<a href=$self?$state&sortby=$sortby&sortorder=$o>".
                        "$name</a>");
}

function cmp($a,$b)
{
	global $sortby, $sortorder;
	if ($a[$sortby] == $b[$sortby]) return 0;
	if ($sortorder=="up") 
		return ($a[$sortby] > $b[$sortby]) ? 1 : -1;
	else
		return ($a[$sortby] < $b[$sortby]) ? 1 : -1;
}

# Parse queue metrics.
list($jobs, $queue) = getJobs();

# The number of active nodes, according to scheduler
$activeP=0;
$activeJobs=0;

#
# Display the set of jobs in the queue.
#
if (is_array($jobs)) {
	uasort($jobs, "cmp");
	foreach ($jobs as $id=>$job) {
		$tpl->newBlock("job");
		$tpl->assign("color",rowStyle());
		if ($user and $user!=$job[user]) 
			$tpl->assign("color","inactive");
		$tpl->assign("id",$job[id]);
                $tpl->assign("joblink","./job.php?$state&id=$id");
		$tpl->assign("user",$job[user]);
		$tpl->assign("processors",$job[P]);
		$tpl->assign("state",$job[state]);
		$tpl->assign("name",$job[name]);

		$started = $job[started];

		if ( $started == 0 )
			$secs_in_state = 0;
		else
			$secs_in_state = $queue['LOCALTIME'] - $started;

		if ($secs_in_state < 0)
			$time_in_state = "??";
		elseif ($secs_in_state < 86400)
			$time_in_state = detailtime($secs_in_state);
		else
			$time_in_state = uptime($secs_in_state);

		if ($job[state] == "Running") {
			$activeP += $job[P];
			$activeJobs++;
		}
		$tpl->assign("runtime",$time_in_state);
		$tpl->assign("TN",$job[TN]);
	}
}

# The total number of processors, according to the scheduler.
$totalP = $queue[P];
if ($activeP > $totalP) $activeP = $totalP;

if ($totalP) {
	# Mask the case when gmond hasn't yet
	# deleted the metric of a finished job.
	if ($activeP > $totalP) $activeP = $totalP;

	$percentUsed = sprintf("%.2f",($activeP/$totalP)*100);
}
else
	$percentUsed = "0.00";

$s = ($activeJobs!=1) ? "s" : "";
$summary = "$activeJobs Active Job$s. ".
	"$activeP of $totalP Processors Active ($percentUsed%)";

# See FAQ:1 on the template power site for why we need "_ROOT".
$tpl->assign("_ROOT.summary",$summary);

# Only show 'update' button if the webserver is running on the queue
# submit host (frontend). Otherwise it has no meaning.
if (!$_GET["c"])
   $tpl->newBlock("local");

$tpl->printToScreen();
?>
 
