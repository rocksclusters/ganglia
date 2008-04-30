<?php
#
# Parses the ganglia XML tree and pulls out the pbs metrics.
# Assumes we have a $GHOME variable that points to ganglia, 
# usually "../..".
#
include_once "$GHOME/conf.php";
include_once "$GHOME/ganglia.php";

# Collect cluster name from the command line if it exists.
if ($_GET["c"])
{
	$clustername = escapeshellcmd(rawurldecode($_GET["c"]));

	# Get data from gmetad (just like main webpage) if we are querying
	# from a remote machine.
	$context = "cluster";
	$rc=Gmetad();
}
else
{
	# Try querying gmond if we are on the local machine - more responsive.
	# This change in behavior is not very obvious, however.
	$rc=Gmetad($ganglia_ip, 8649);
}

if (!rc)
{
	print "<H4>There was an error collecting ganglia data ".
		"($ganglia_ip:$ganglia_port): $error</H4>\n";
	exit;
}

# We should have a cluster name specified. 
if (!$clustername)
	$clustername = $cluster[NAME];

?>
