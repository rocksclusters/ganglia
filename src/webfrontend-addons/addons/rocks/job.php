<?php
#
# A Page to monitor the PBS parallel job scheduling queues.
# Uses the pbs.py gschedule module which publishes PBS data
# using Ganglias gmetric. Ganglia parsing code based on work
# by Matt Massie <massie@cs.berkeley.edu>.
#
# Requires ganglia >= 2.5.1 with garbage collecting.
#
$GHOME="../..";
$id = $_GET["id"];

include_once "$GHOME/class.TemplatePower.inc.php";
include_once "./get-ganglia.php";
include_once "$GHOME/functions.php";
include_once "./functions.php";

$tpl = new TemplatePower("templates/job.tpl");
$tpl->assignInclude("header", "templates/header.tpl");
$tpl->prepare();

$self="./job.php";
$state="c=" . rawurlencode($_GET[c]);

$cluster_url=rawurlencode($clustername);
$tpl->assign("self",$self);
$tpl->assign("title", "Job $id Detail");
$tpl->assign("link", "<a href=./queue.php?$state>Back to Job Queue</a>");
$tpl->assign("cluster_url",$cluster_url);
$tpl->assign("cluster",$clustername);


if (!is_numeric($id) and !$id) {
	echo "<h1>Missing a Job ID</h1>";
	return;
}

# Get metric name to graph.
$metricname = escapeshellcmd(rawurldecode($_GET["m"]));
if (!$metricname) $metricname=$default_metric;

# Parse pbs metrics.
list($jobs, $queue) = getJobs();

$job = $jobs[$id];
if (!is_array($job)) {
	echo "<h4>Job ID $id does not exist anymore</h4>";
	echo "<a href=\"./queue.php?$state\">Back to job list</a>";
	return;
}

$name = $job[name] ? "<i>$job[name]</i>" : "Job";
$tpl->assign("name",$name);
$tpl->assign("user",$job[user]);
$tpl->assign("id",$id);
$tpl->assign("now",date("r"));
$tpl->assign("P", $job[P]);

# Get the metric attributes from the first host in our cluster. 
$firsthost=key($metrics);
foreach($metrics[$firsthost] as $m=>$v) {
	if ($v[SLOPE]=="both" and $v[SOURCE]=="gmond")
		$context_metrics[] = $m;
}

# Build the list of metrics.
$metric_menu = "Metric Graph:<br>".
	"<SELECT NAME=m OnChange=\"metric_form.submit();\">\n";

sort($context_metrics);

foreach ($context_metrics as $m) {
	$metric_menu .= "<OPTION VALUE=\"". rawurlencode($m) ."\" ";
	if ($m == $metricname) 
		$metric_menu .= "SELECTED";
	$metric_menu .= ">$m\n";
}
$metric_menu .= "</SELECT>\n";
$tpl->assign("metric_menu", $metric_menu);


# Get time-in-state.
$secs_in_state = $queue[LOCALTIME] - $job[started];
$time_in_state = ($secs_in_state < 86400) ? 
	detailtime($secs_in_state) : 
	uptime($secs_in_state);

if ($job[state] == "Running") 
	{
		$tpl->assign("status","Runtime: $time_in_state");
		$running=1;
		$tpl->newBlock("running");
	}
else if ($job[state] == "Queue Wait") 
	{
		$tpl->assign("status", "Queued for: $time_in_state");

	}
else 
	$tpl->assign("status", "State: $job[state]");

if (!$running) {
	$tpl->printToScreen();
	return;
}

# I hate how we have to redefine everything inside a new block.
$tpl->assign("self",$self);
$tpl->assign("id",$id);
#
# Build a dictionary of unique compute nodes.
#
$nodes = array();

$nodelist = decode($job[nodes]);
if (is_array($nodelist))
	foreach ($nodelist as $name) {
		$nodes[$name] += 1;
	}
else
	$tpl->assign("_ROOT.error", 
		"<h2>No nodes found. Perhaps your queueing system is not well?</h2>");


# Start = the number of seconds ago this job started. 
# We make these negative for rrdtool.
$started = $secs_in_state;

# The graphing routing usually takes a range like "hour". Here we give it
# an absolute range, in seconds. One a little bigger than start.
$r = intval($started * 1.25);
$jobrange = ($started < 3600) ? -3600 : -$r ;

#
# Bring it all together.
#

$start = $jobrange;
$end = "N";
list($min, $max) = find_limits($nodes, $metricname);

$node = "";
$i=0;
$cols=3;
foreach ($nodes as $hostname => $P) {
	#echo "Name is $hostname, metric is $metricname<br>";
	$val = $metrics[$hostname][$metricname];
	$host_url=rawurlencode($hostname);

	$jobstart = time() - $started;
	$graphargs = "z=small&c=$cluster_url&h=$host_url&v=$val[VAL]".
		"&x=$max&n=$min&m=$metricname&r=job&jr=$jobrange&js=$jobstart";
	$node .= "<td>";
	$node .= "<table cellspacing=5>";
	$node .= nodebox($hostname, 2, "$P: $hostname");
	$node .= "<tr><td align=center><b>$metricname</b></td></tr>";
	$node .= "<tr><td>\n".
		"<a href=\"$GHOME/?c=$cluster_url&h=$host_url".
                "&r=job&jr=$jobrange&js=$jobstart\">".
		"<IMG SRC=\"$GHOME/graph.php?$graphargs\" ".
			"ALT=\"$hostname\" BORDER=0>".
		"</a></td></tr>\n";
	#$node .="<tr><td>$graphargs</td></tr>";
	$node .= "</table></td>\n";

	# Put $cols nodes in a row.
	$i++;
	if (!($i % $cols)) {
		$tpl->newBlock("noderow");
		$tpl->assign("node_row",$node);
		$node="";
	}
}	

# Kind of awkward to use TemplatePower for tables; here we pickup
# short rows.
if ($i % $cols) {
	$tpl->newBlock("noderow");
	$tpl->assign("node_row",$node);
}

$tpl->printToScreen();
?>
 
