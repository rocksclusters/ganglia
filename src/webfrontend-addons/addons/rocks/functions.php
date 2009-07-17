<?php
#
# Some helpful functions common to two or more php scripts in this
# directory.
#

# Decodes mpd-style encoded name lists (4*compute-0-%d:4-7).
function decode($nodes, $dn="")
{
	$namelist = explode(" ", $nodes);

	if (!count($namelist)) return;

	$domain = $dn ? ".$dn" : "." . domain();

	foreach ($namelist as $name) {
		$a = strpos($name, "*");
		$b = strpos($name, "%d");
		if (!is_integer($b))
			continue;
		if (!is_integer($a)) {
			$prefix = substr($name, 0, $b);
			$count = 1;
			}
		else {
			$prefix = substr($name, $a+1, $b-$a-1);
			$count = intval(substr($name, 0, $a));
		}
		$ranges_str = substr($name, $b+3, strlen($name));
		$ranges = explode(",", $ranges_str);
		foreach ($ranges as $range) {
			list($low,$high) = explode("-",$range);

			foreach (range(intval($low),intval($high)) as $n) {
				$hostname = "$prefix$n";

				foreach (range(1,$count) as $i) {
					$wholelist[] = "$hostname$domain";
					#echo "Adding $Name<br>";
				}
			}
		}
	  }
	  return $wholelist;
}


#
# Pull out "queue-job-N" and "queue-state" metrics from a cluster.
# Leverages the standard Ganglia PHP XML parser. Assumes 
# the standard Ganglia parser has already been run.
#
function getJobs()
{
	global $hosts_up, $cluster, $metrics;

	# A 2-key array: job id" / "Attribute name" = Attribute value;
	$jobs=array();
	$queue=array();
	
	$queue['LOCALTIME'] = $cluster['LOCALTIME'];

	foreach ($hosts_up as $hostname=>$v)
	{
		#echo "Examining host $hostname<br>";
		foreach ($metrics[$hostname] as $metricname=>$v)
		{
			# Strpos is faster than strstr, but needs the triple
			# === since it can return FALSE (and FALSE==0). Dumb
			# language.
			if (strpos($metricname, "queue-job") === 0)
			{
				# Ignore dead metrics. Detect and mask failures.
				if ($v[TN] > ($v[TMAX] * 2)) continue;

				$jobid=0;
				sscanf($v[NAME], "queue-job-%d", $jobid);
				#echo "Adding job $jobid<br>";

				# Note explode is faster than split.
				$fields = explode(", ", $v[VAL]);
				foreach ($fields as $f)
				{
					$l=explode("=",$f);
					$key = $l[0];
					$jobs[$jobid][$key] = $l[1];
				}
				$jobs[$jobid][id] = $jobid;
				$jobs[$jobid][TN] = $v[TN];
			}
			else if ($metricname=="queue-state")
			{
				$fields = explode(",", $v[VAL]);
				foreach ($fields as $f) {
					$l=explode("=",$f);
					$key = $l[0];
					$queue[$key]=$l[1];
				}
			}
		}
	}
	return array($jobs, $queue);
}


#
# Pull out "ps-PID" metrics from a cluster.
# Assumes the standard Ganglia parser has already been run.
#
function getPS()
{
	global $hosts_up, $cluster, $metrics;

	# A 2-key array: "hostname-PID" / "Attribute name" = Attribute value;
	$ps=array();
	
	foreach ($hosts_up as $hostname=>$hostattrs)
	{
		#echo "Examining host $hostname<br>";
		foreach ($metrics[$hostname] as $metricname=>$v)
		{
			if (strpos($metricname, "ps-") === 0)
			{
				# ignore dead metrics
				if ($v[TN] > ($v[TMAX] * 2)) continue;

				$pid=0;
				sscanf($v[NAME], "ps-%d", $pid);
				#echo "Adding ps $pid<br>";

				# Primary key pair.
				$pkey = "$hostname-$pid";

				# Note explode is faster than split.
				$fields = explode(", ", $v[VAL]);
				foreach ($fields as $f)
				{
					$l=explode("=",$f);
					$key = strtoupper($l[0]);
					$ps[$pkey][$key] = $l[1];
				}
				$ps[$pkey][HOST] = $hostname;
				$ps[$pkey][TN] = $v[TN];
			}
		}
	}
	return $ps;
}


# Turns a time interval (in seconds) into a "2days 3:15:49" string, like the
# uptime command.
function detailtime($uptimeS)
{
   if (!$uptimeS) return "";

   $uptimeD=intval($uptimeS/86400);
   $uptimeS=$uptimeD ? $uptimeS % ($uptimeD*86400) : $uptimeS;
   $uptimeH=intval($uptimeS/3600);
   $uptimeS=$uptimeH ? $uptimeS % ($uptimeH*3600) : $uptimeS;
   $uptimeM=intval($uptimeS/60);
   $uptimeS=$uptimeM ? $uptimeS % ($uptimeM*60) : $uptimeS;

   $s = ($uptimeD!=1) ? "s" : "";
   if ($uptimeD>0)
     return "$uptimeD day$s, $uptimeH:$uptimeM:$uptimeS";
   else
     return "$uptimeH:$uptimeM:$uptimeS";
}


# Guesses at the domain name of hosts in the cluster.
function domain()
{
	global $metrics;

	# Default domain name.
	$domain = "local";

	# Assumes all hostnames have the same domain name.
	$firsthost = key($metrics);

	$namelist = explode(".", $firsthost);
	if (count($namelist) > 1)
		$domain = array_pop($namelist);
	
	return $domain;
}

?>
