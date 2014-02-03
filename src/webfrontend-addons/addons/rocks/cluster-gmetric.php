<?php
/* $Id: cluster-gmetric.php,v 1.2 2008/04/24 12:33:22 bruno Exp $ */

$clustername = escapeshellcmd(rawurldecode($_GET["c"]));
$search = rawurldecode($_GET["search"]);
$sortby = $_GET["sortby"];
$sortorder = $_GET["sortorder"];
$context = "cluster";

$GHOME="../..";
include_once "$GHOME/conf.php";
include_once "$GHOME/ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";
include_once "$GHOME/get_ganglia.php";
include_once "$GHOME/class.TemplatePower.inc.php";

$tpl = new TemplatePower("templates/cluster-gmetric.tpl");
$tpl->prepare();

$self="./cluster-gmetric.php";
$tpl->assign("self",$self);
$tpl->assign("cluster", $clustername);
$tpl->assign("search", $search);

if (!$sortby) $sortby="TN";
if (!$sortorder) $sortorder="up";
$tpl->assign("sortby",$sortby);
$tpl->assign("sortorder",$sortorder);
$tpl->assign("sortvars","sortby=$sortby&sortorder=$sortorder");


if($hosts_up)
      $tpl->assign("node_msg", "This host is up and running.");
else
      $tpl->assign("node_msg", "This host is down.");

$cluster_url=rawurlencode($clustername);
$tpl->assign("cluster_url", $cluster_url);

# For the node view link.
$tpl->assign("cluster_view","$GHOME/?c=$cluster_url");

# Sorting
$columns=array("TN","TMAX","DMAX","HOST","NAME","VALUE");

foreach ($columns as $c) {
        $name = $c;
        if ($sortby==$c)
                $tpl->assign("${c}_SortLink",$name);
        else
                $tpl->assign("${c}_SortLink", "<a href=$self?".
                  "c=$cluster_url&search=$search&sortby=$c&sortorder=$sortorder>".
                  "$name</a>");
}

$orders=array("up","down");
foreach ($orders as $o) {
        $name=ucfirst($o);
        if ($sortorder==$o)
                $tpl->assign("${o}_SortOrder",$name);
        else
                $tpl->assign("${o}_SortOrder", "<a href=$self?".
                  "c=$cluster_url&search=$search&sortby=$sortby&sortorder=$o>".
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

foreach ($metrics as $hostname => $metric) {
        foreach ($metric as $name => $v)
           {
              # Show only user defined metrics.
              if ($v[SOURCE] == "gmetric") {
                 $key = "$hostname-$name";
                 $g_metrics[$key] = $v;
                 $g_metrics[$key][HOST] = $hostname;
              }
           }
}

# Show gmetrics
if (is_array($g_metrics))
   {
      # Very simple sorting
      uasort($g_metrics, "cmp");
      foreach ($g_metrics as $key => $v) {
              $name = $v[NAME];
              if ($search and strpos($name, $search) === false)
                   continue;
              #  echo "Adding gmetric name $name<br>";
              $tpl->newBlock("g_metric_info");
              $tpl->assign("color",rowStyle());
              $tpl->assign("name", $name);
              $tpl->assign("tn", $v[TN]);
              $tpl->assign("tmax", $v[TMAX]);
              $tpl->assign("dmax", $v[DMAX]);
              $tpl->assign("host", $v[HOST]);
              if( $v[TYPE]=="timestamp" or $always_timestamp[$name])
                   {
                      $tpl->assign("value", date("r", $v[VAL]));
                   }
                else
                   {
                      $tpl->assign("value", "$v[VAL] $v[UNITS]");
                   }
      }
   }

$tpl->printToScreen();
?>
