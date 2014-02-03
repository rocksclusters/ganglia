<?php
#
# Cluster Top. This page shows cluster-wide process table.
# PS information comes from the 'ps' gmetric (by gschedule),
# so we cannot adjust the refresh interval.
#
# Copyright 2003 Federico Sacerdoti and UC regents.
#
# @Copyright@
#
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
#
# Copyright (c) 2000 - 2013 The Regents of the University of California.
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
$GHOME="../..";
$sortby = $_GET["sortby"];
$sortorder = $_GET["sortorder"];
$user = $_GET["user"];

include_once "$GHOME/class.TemplatePower.inc.php";
include_once "./get-ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";

$tpl = new TemplatePower("templates/top.tpl");
$tpl->assignInclude("header", "templates/header.tpl");
$tpl->prepare();

$self="./top.php";
$state="c=" . rawurlencode($_GET[c]);

$tpl->assign("self",$self);
$tpl->assign("title", "Cluster Top");
$tpl->assign("link",
   "<a href=./assignments.php?$state>Physical Job Assignments</a>");

if (!$sortby) $sortby="%CPU";
if (!$sortorder) $sortorder="down";
$tpl->assign("sortby",$sortby);
$tpl->assign("sortorder",$sortorder);
$tpl->assign("sortvars","sortby=$sortby&sortorder=$sortorder");
$tpl->assign("cluster_url",rawurlencode($clustername));
$tpl->assign("cluster",$clustername);
$tpl->assign("user",$user);
$tpl->assign("now",date("r"));

#
# Some templatePower tricks to set the sortby links. The column names
# must match attribute names for our ps array.
#
$columns=array("TN","HOST","PID","USER","CMD","%CPU","%MEM","SIZE",
   "DATA", "SHARED", "VM");

foreach ($columns as $c) {
	$name=ucfirst($c);
	if ($sortby==$c)
		$tpl->assign("${c}_SortLink",$name);
	else
		$tpl->assign("${c}_SortLink",
			"<a href=$self?$state&sortby=$c&sortorder=$sortorder>".
                        "$name</a>");
}

$orders=array("up","down");
foreach ($orders as $o) {
	$name=ucfirst($o);
	if ($sortorder==$o)
		$tpl->assign("${o}_SortOrder",$name);
	else
		$tpl->assign("${o}_SortOrder",
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

$ps = getPS();

#
# Display the set of active processes on the cluster.
#
if (is_array($ps)) {
 	uasort($ps, "cmp");
	foreach ($ps as $key=>$p) {
		$tpl->newBlock("ps");
		if ($user and $user!=$p[USER])
			$tpl->assign("color","inactive");
		else
			$tpl->assign("color",rowStyle());

		foreach ($columns as $c)
		{
			$tpl->assign($c, $p[$c]);
		}
	}
}

$tpl->printToScreen();

?>
