<?php
/* $Id: temp_view.php,v 1.6 2008/04/24 12:33:22 bruno Exp $ */
#
# Displays the cluster temperature in a physical view.
# Nodes are located by Rack, Rank, and Plane in the physical
# cluster.
#
# Originally written by Federico Sacerdoti <fds@sdsc.edu>
# Part of the Ganglia Project, All Rights Reserved.
#

# Called from index.php, so cluster and xml tree vars
# ($metrics, $clusters, $hosts) are set, and header.php
# already called.

$GHOME="../..";
include_once "$GHOME/class.TemplatePower.inc.php";
include_once "./get-ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";

$tpl = new TemplatePower("templates/temp_view.tpl");
$tpl->assignInclude("header", "templates/header.tpl");
$tpl->prepare();

$cluster_url = rawurlencode($clustername);
$self="./temp_view.php";
$state="c=" . rawurlencode($_GET[c]);

$tpl->assign("self",$self);
$tpl->assign("title", "Temperature View");
$tpl->assign("link", "<a href=$GHOME/?$state>Back to Cluster View</a>");
$tpl->assign("cluster_url",$cluster_url);
$tpl->assign("cluster",$clustername);
$tpl->assign("now",date("r"));

#-------------------------------------------------------------------------------
# Converts Celsius to Farenheight
function CtoF($t)
{
	if (!$t) return 0;
	return intval(($t*(9/5.0)) + 32);
}

$aveTempC = sprintf("%.1f", cluster_sum("temp", $metrics) / 
	floatval(count($hosts_up) + count($hosts_down)));
$tpl->assign("aveTempC",$aveTempC);
$tpl->assign("aveTempF",CtoF($aveTempC));


#-------------------------------------------------------------------------------
#
# Generates the colored Node cell HTML. Used in Physical
# view and others. Intended to be used to build a table, output
# begins with "<tr><td>" and ends the same.
function tempbox($hostname, $temp, $title="", $extrarow="")
{
   global $cluster, $clustername, $metrics, $hosts_up, $GHOME;

   if (!$title) $title = $hostname;

   # An array of [NAME|VAL|TYPE|UNITS|SOURCE].
   $m=$metrics[$hostname];
   $up = $hosts_up[$hostname] ? 1 : 0;

   #
   # The nested tables are to get the formatting. Insane.
   # We have three levels of verbosity. At L3 we show
   # everything; at L1 we only show name and load.
   #
   $rowclass = $up ? rowStyle() : "down";
   $host_url=rawurlencode($hostname);
   $cluster_url=rawurlencode($clustername);
   
   $row1 = "<tr><td class=$rowclass>\n".
      "<table width=100% cellpadding=1 cellspacing=0 border=0><tr>".
      "<td><a href=\"$GHOME/?c=$cluster_url&h=$host_url\">".
      "$title</a>&nbsp;<br>\n";

   # Scalar helps choose a load color. The lower it is, the easier to get red.
   # The highest level occurs at a load of (loadscalar*10).
   $loadscalar=2.8;

   #
   # Load box. Colors range from 1 to 10. Temp ranges from 10 to 40C
   #
   $mintemp = 10;
   if (!$cpu_num) $cpu_num=1;
   $loadindex = intval(($temp-$mintemp)/$loadscalar);
   # 10 is currently the highest allowed load index.
   if (!$temp) {
   	$load_class = "Lunknown";
	$temp = 0;
   }
   elseif ($loadindex > 10)
   	$load_class = "L10";
   elseif ($loadindex < 0)
   	$load_class = "L0";
   else
   	$load_class = "L$loadindex";
   $status = "${temp}C ". CtoF($temp) ."F";
   $row1 .= "</td><td align=right valign=top>".
      "<table cellspacing=1 cellpadding=3 border=0><tr>".
      "<td class=$load_class align=right><small>$status</small>".
      "</td></tr></table>".
      "</td></tr>\n";

   # Construct cell.
   $cell = $row1;

   $cell .= "</td></tr></table>\n";
   $cell .= "</td></tr>\n";

   return $cell;
}

#-------------------------------------------------------------------------------
# Displays a rack and all its nodes.
function showrack($ID)
{
   global $racks, $metrics;
   global $tpl;

   if ($ID>=0) {
      $tpl->assign("RackID","<tr><th>Rack $ID</th></tr>");
   }

   # A string of node HTML for the template.
   $nodes="";

   foreach ($racks[$ID] as $name)
   {
      $nodes .= tempbox($name, $metrics[$name]['temp']['VAL']);
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
$i=1;
$hostcols = 4;
foreach ($racks as $rack=>$v)
   {
      $tpl->newBlock("racks");

      $racknodes = showrack($rack);

      $tpl->assign("nodes", $racknodes);

      if (! ($i++ % $hostcols)) {
         $tpl->assign("tr","</tr><tr>");
      }
   }

$tpl->printToScreen();

?>
