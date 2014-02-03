#!/usr/bin/env perl

use CGI qw(:all);
my $q = new CGI;

#############################################################
#Filename: parse.cgi
#Description:
#	Parses MDS cluster data and produces web pages.
#	It breaks the mds data into multidimentional hashes and then
#	populates web pages with the data in the hashes. There are 2
#	views for the data:
#	1) Cluster View - This consists of 2 tables. The first
#	table is the information about the cluster. This includes
# 	the cluster name, local time, service (this is the service
#	that is publishing the data), and service version. It also
#	includes a drop down list that has a listing of other clusters
#	that can be viewed. The second table is a listing of the hosts
#  that the cluster has. These are links that can be clicked on
#	to go to the view of that host.
#	2) Host View - This also consists of 2 tables. The first
#	table is the host information which has the cluster the host
#	belongs to, host address, hostname, reported
#	time of the metrics on the host, the local time on the host,
#	the service publishing the data, and the version of the service
#	it also contains a drop down menu that has a list of the other host
#	names on the cluster and another drop down that has a list
#	of the clusters. The second table is the table of host metrics.
#	It contains metric name, metric value, units, metric type and source.
#	The metric table can be sorted by metric name, value, units, type
#	and source.
#
#Parameters:
#	cluster - the name of the cluster
#	host - the name of the host (if viewing a host)
#	sort_by - if sorting the metric fields (default metric name)
#	action - the action of the web page. This is either to view
#	a host or a cluster. The default is view cluster.
#
#Returns:
#	HTML
#
#Author:
#	Maytal Dahan
#	mdahan@sdsc.edu
#	SDSC Grid Portal Architecture Program Area
#
#Last Modified: April 18, 2002
#############################################################


#############################################################
########################   MAIN   ###########################
#############################################################

my $in_cluster = $q->param('cluster');
if(!$in_cluster){ $in_cluster = "slic00.sdsc.edu" }
my $in_host = $q->param('host');
if(!$in_host){ $in_host = "compute-0-7" }
my $sort_by = $q->param('sort_by');
if(!$sort_by){ $sort_by = "metric"; }
my $action = $q->param('action');
if(!$action){ $action = "view_cluster" }

if($action =~ /view_host/){
	&view_host($in_cluster, $in_host);
}elsif($action =~ /view_cluster/){
	&view_cluster($in_cluster);
}else{
	&view_cluster($in_cluster);
}
exit;

#############################################################
########################   SUBS   ###########################
#############################################################

##########################################
#Subroutine: read_data
#Description:
#	This reads the ldif data.
#	Currently it reads from a file that
#	has the mds data. It can also do
# 	a MDS query (code commented out).
#	it calles ldif_to_hashes to parse the
#	data.
#Parameters:
#	None
#Returns:
#	A hash that has all the data. This
#	is the same hash that ldif_to_hashes
#	returns.
##########################################
sub read_data{

   my @data = ();

   open(FILE, "sample_data.txt") || print "Can't open $!";
   @data = <FILE>;
   close(FILE);
   $ref = \@data;
   return &ldif_to_hashes($ref);

	##When this is mds it should change to##
	#$GLOBUS_LOCATION = $ENV{GLOBUS_LOCATION};
	#if($GLOBUS_LOCATION eq ""){
		#$GLOBUS_LOCATION = "/usr/local/apps/globus-2.0-beta";
		#$ENV{GLOBUS_LOCATION} = $GLOBUS_LOCATION;
	#$mds_path = "$GLOBUS_LOCATION/bin/grid-info-search";
	#$mds_args = " -x -LLL -b 'Mds-Host-hn=slic00.sdsc.edu,Mds-Vo-name=local, o=grid'";
	#@data = `$mds_path $mds_args 2>&1`;
   #$ref = \@data;
   #return &ldif_to_hashes($ref);

}

##########################################
#Subroutine: ldif_to_hashes
#Description:
#	Breaks the ldif data into hashes for each
#	object. The hash looks like this:
#	$DATA{$index}{$key} = $val;
#	Index is incremented for each object.
#	There are also 2 additional global hashes:
#	1) %HOST_HASH - this is a hash that has
#	host information for each host. It looks
#	like this:
#	$HOST_HASH{$cluster_name}{$host_name}{$key} = $val
#	2) %<CLUSTER_NAME> - there is a hash for each
#	cluster named after the cluster name. It contains
#	the cluster specific information like localtime,
#	service and service version.
#Parameters:
#	A reference to an array that
#	has all the ldif data.
#Returns: One hash that has all the data.
##########################################

sub ldif_to_hashes{

	$array_ref = $_[0];
	%data_hash = {};

   ##This is a reference to the array that has the ldif data
	@ldif_data = @$array_ref;

   ## read the entire file
	$length = @ldif_data;

	my $index = 0;
	my %PARSE = {};

   for($i=0;$i<$length;$i++){
      chomp;
      if($ldif_data[$i] eq ""){ next;}

      ##THIS IS THE FIRST ELEMENT SO PARSE UNTIL
		##YOU GET TO A NEW ELEMENT
      if($ldif_data[$i] =~ /MDS-service=/ &&  $ldif_data[$i]=~ /hn=/){
         ($service, $hn, $junk) = split(/\,/,$ldif_data[$i],3);
         ($label, $CLUSTER) = split(/=/,$hn);
			$PARSE{$index}{cluster} = $CLUSTER;

			$i++;

			while($ldif_data[$i] !~ /service=/ &&  $ldif_data[$i] !~ /hn=/ && $i < $length){

      		if($ldif_data[$i] eq ""){ next;}

         	($key, $value) = split(/:/,$ldif_data[$i],2);
				chomp $value;
				chomp $key;
				$key =~ s/^\s+//;
				$value =~ s/^\s+//;
				if($key ne ""){
					$PARSE{$index}{$key}= $value;
				}

				$i++
			}
			##Check if this is the cluster information object##
			if($PARSE{$index}{objectclass} =~ /clusterData/){
				my $cluster_name = $PARSE{$index}{'cluster-name'};
				#make a hash that is the cluster name
				%$cluster_name = ();
				$$cluster_name{cluster_service} = $PARSE{$index}{service};
				$$cluster_name{service_version} = $PARSE{$index}{'service-version'};
				$$cluster_name{localtime} = $PARSE{$index}{localtime};
			}

			##Check if this is the host information object##
			if($PARSE{$index}{objectclass} =~ /hostData/){
				my $cluster_name = $PARSE{$index}{'cluster-name'};
				my $hostname = $PARSE{$index}{'hostname'};
				#make a hash that is the cluster name
				$HOST_HASH{$cluster_name}{$hostname}{address} = $PARSE{$index}{'address'};
				$HOST_HASH{$cluster_name}{$hostname}{reportedtime} = $PARSE{$index}{'reportedtime'};
			}
			$index++;
			$i--;

		}else{
			print "ERROR SHOULD BE FIRST ITEM, INSTEAD $ldif_data[$i]";
      }
   }

	##MAKE A HASH $HASH{CLUSTER}{HOST}{INDEX_NUM}{KEY} = {VALUE};
	#Now make the hashes into a 3D hash#
	my $index = 0;
	foreach $num (keys %PARSE){

		$CLUSTER = $PARSE{$num}{cluster};
		$HOST = $PARSE{$num}{hostname};

		if($data_hash{$CLUSTER}{$HOST}{$index}){
			$index++;
		}
		foreach $key (keys %{ $PARSE{$num} }){
			$data_hash{$CLUSTER}{$HOST}{$index}{$key} = $PARSE{$num}{$key};

		}
	}

	@m = %data_hash;
   return %data_hash;
}


##########################################
#Subroutine: view_host
#Description: Produces html that is the view
#	of a host.
#Parameters:
#	cluster - the name of the cluster the
#	host belongs to..
#	host - the name of the host to view.
#Returns:
#	Prints HTML
##########################################

sub view_host{

	my $cluster = $_[0];
	my $hostname = $_[1];

	my %INFO = {};
	%INFO = &read_data;

	my @CLUSTER_LIST = ();
	#Get a listing of all the clusters and hostnames
	foreach my $other_clus (sort keys %INFO){
		if($other_clus ne $cluster){
			push(@CLUSTER_LIST, $other_clus);
		}
	}

	@HOST_LIST = ();
	#Get a listing of all the clusters and hostnames
	foreach my $host (sort keys %{ $INFO{$cluster} }){
		if($host ne $hostname && $host ne ""){
			push(@HOST_LIST, $host);
		}
	}

	foreach $k (keys %CLUSTER_HASH){
		print "ANOTHER CLUSTER KEY $k<br>";
		foreach $m (keys %{ $CLUSTER_HASH{$k} }){
			print "KEY: $m VAL: $CLUSTER_HASH{$k}{$m}<br>";
		}
	}

	print header;
	print qq(<HTML><HEAD><TITLE>Host Information For $hostname</TITLE>
	<STYLE type="text/css">
	<!--
	.DataCell {background-color: #FFFFFF}
	-->
	</STYLE></HEAD>
	<BODY BGCOLOR=#FFFFFF>);

	&begin_shadow_table("380","#CCCCCC");

	$c = "class=DataCell";
	print qq(
	<TABLE bgcolor=#660000 border=0 cellpadding=4 cellspacing=0>
	<TR><TD><FONT color=#FFFFFF><b>Cluster: $cluster</font></TD>
	<TD><FONT color=#FFFFFF><b>Host: $hostname</font></TD></TR>
	<TR><TD colspan=2>
	<TABLE width=380 bgcolor=#CCCCCC border=0 cellpadding=2 cellspacing=1>
		<TR><TD class=DataCell>Host Address: </TD>
		<TD class=DataCell colspan=2>$HOST_HASH{$cluster}{$hostname}{address}&nbsp;</TD></TR>
		<TR><TD class=DataCell>Reported Time: </TD>
		<TD class=DataCell colspan=2>$HOST_HASH{$cluster}{$hostname}{reportedtime}&nbsp;</TD></TR>
		<TR><TD $c>Local Time: </TD>
		<TD $c colspan=2>$$cluster{localtime}</TD></TR>
		<TR><TD $c>Service: </TD>
		<TD $c colspan=2>$$cluster{cluster_service}</TD></TR>
		<TR><TD $c>Service Version: </TD>
		<TD $c colspan=2>$$cluster{service_version}</TD></TR>
		<TR><form method=post>
		<TD $c>Host Names: </TD><TD $c><SELECT name=host>
		<OPTION selected value=$hostname>$hostname
	);
	foreach (@HOST_LIST){
		print "<OPTION value=$_>$_";
	}
	print "</SELECT><INPUT type=hidden name=cluster value=$cluster>
	<input type=hidden name=action value=view_host></TD>
	<TD $c><input type=submit value=Update></TD></form></TR>
	<TR><form method=post><TD $c>Cluster Names: </TD><TD $c><select name=cluster>
	<OPTION selected value=$cluster>$cluster";
	foreach (@CLUSTER_LIST){
		print "<OPTION value=$_>$_";
	}
	print "</SELECT><input type=hidden name=action value=view_cluster></TD>
	<TD $c><input type=submit value=Update></TD></form></TR>";
	print "</TABLE></TD></TR></TABLE>";

	&end_shadow_table();

	print "<p>";
	&begin_shadow_table("380","#CCCCCC");

	print "<TABLE BGCOLOR=#660000 BORDER=0 CELLPADDING=4 CELLSPACING=0>
	<TR><TD><FONT color=#FFFFFF><b>$hostname Metric Information </font></TD></TR>
	<TR><TD>
	<TABLE width=380 bgcolor=#CCCCCC border=0 cellpadding=2 cellspacing=1>
	<TR><TD $c><B>
	<a href=parse.cgi?cluster=$cluster&host=$hostname&sort_by=metric&action=view_host>Metric</a>
		</B></TD>
	<TD $c><B>
	<a href=parse.cgi?cluster=$cluster&host=$hostname&sort_by=value&action=view_host>Value</a>
	</B></TD>
	<TD $c>
	<B><a href=parse.cgi?cluster=$cluster&host=$hostname&sort_by=units&action=view_host>Units</a>
	</B></TD>
	<TD $c>
	<B><a href=parse.cgi?cluster=$cluster&host=$hostname&sort_by=type&action=view_host>Type</a>
	</B></TD>
	<TD $c>
	<B><a href=parse.cgi?cluster=$cluster&host=$hostname&sort_by=source&action=view_host>Source</a>
	</B></TD></TR>";

	foreach $i (keys %{ $INFO{$cluster}{$hostname} }){
		$m = $INFO{$cluster}{$hostname}{$i}{metric};
		$v = $INFO{$cluster}{$hostname}{$i}{value};
		$u = $INFO{$cluster}{$hostname}{$i}{units};
		$t = $INFO{$cluster}{$hostname}{$i}{metrictype};
		$s = $INFO{$cluster}{$hostname}{$i}{source};
		#SORT BY METRIC
		$METRICS{$m}{value} = $v;
		$METRICS{$m}{units} = $u;
		$METRICS{$m}{source} = $s;
		$METRICS{$m}{type} = $t;
	}
	if($sort_by =~ /metric/){
		foreach $metric (sort keys %METRICS){
			print "<TR><TD $c><B>$metric</B></TD>";
			print "<TD $c>$METRICS{$metric}{value}</TD>";
			print "<TD $c>$METRICS{$metric}{units}</TD>";
			print "<TD $c>$METRICS{$metric}{type}</TD>";
			print "<TD $c>$METRICS{$metric}{source}</TD>";
			print "</TR>";
		}
	}elsif($sort_by =~ /value/){
		for(sort {$METRICS{$b}{$sort_by} <=> $METRICS{$a}{$sort_by} } keys %METRICS){
			print "<TR><TD $c><B>$_</B></TD>";
			print "<TD $c>$METRICS{$_}{value}</TD>";
			print "<TD $c>$METRICS{$_}{units}</TD>";
			print "<TD $c>$METRICS{$_}{type}</TD>";
			print "<TD $c>$METRICS{$_}{source}</TD>";
			print "</TR>";
		}
	}else{
		for(sort {$METRICS{$b}{$sort_by} cmp $METRICS{$a}{$sort_by} } keys %METRICS){
			print "<TR><TD $c><B>$_</B></TD>";
			print "<TD $c>$METRICS{$_}{value}</TD>";
			print "<TD $c>$METRICS{$_}{units}</TD>";
			print "<TD $c>$METRICS{$_}{type}</TD>";
			print "<TD $c>$METRICS{$_}{source}</TD>";
			print "</TR>";
		}
	}

	print "</TABLE></TD></TR></TABLE>";
	&end_shadow_table;
	print "</BODY></HTML>";
}

##########################################
#Subroutine: view_cluster
#Description:
#	Produces html that is the view of a cluster.
#Parameters:
#	cluster - the name of the cluster to view.
#Returns:
#	Prints HTML
##########################################

sub view_cluster{

	$cluster = $_[0];

	my %INFO = {};
	%INFO = &read_data;

	my @metricCLUSTER_LIST = ();
	#Get a listing of all the clusters and hostnames
	foreach my $other_clus (sort keys %INFO){
		if($other_clus ne $cluster){
			push(@CLUSTER_LIST, $other_clus);
		}
	}
	print header;

	#a:link {color: blue; text-decoration: none;}
	#a:active {color: red; background-color: #ffffcc;}
	#a:visited {color: purple; text-decoration: none;}

	print qq(
	<HTML><HEAD><TITLE>Cluster Information For $cluster</TITLE></HEAD>
	<STYLE type="text/css">
	<!--
	.DataCell { background-color: #FFFFFF }
	BODY {background-color: #FFFFFF;}
	-->
	</STYLE>
	<BODY>
	);

	###START HEADER TABLE##
	&begin_shadow_table("380","#CCCCCC");

	print qq(
	<TABLE BGCOLOR=#660000 BORDER=0 CELLSPACING=0 CELLPADDING=4>
	<TR><TD><FONT color=#FFFFFF><B>Cluster: $cluster</B></FONT></TD></TR>
	<TR><TD>
	<TABLE width=380 bgcolor=#cccccc BORDER=0 CELLPADDING=2 CELLSPACING=1>
		<TR><TD class=DataCell>Local Time: </TD>
		<TD class=DataCell colspan=2>$$cluster{localtime}&nbsp;</TD></TR>
		<TR><TD class=DataCell>Service: </TD>
		<TD class=DataCell colspan=2>$$cluster{cluster_service}&nbsp;</TD></TR>
		<TR><TD class=DataCell>Service Version: </TD>
		<TD class=DataCell colspan=2>$$cluster{service_version}&nbsp;</TD></TR>
		<TR><form method=post>
		<TD class=DataCell>Other Clusters: </TD>
		<TD class=DataCell><SELECT name=cluster>
		<OPTION selected value=$cluster>$cluster
	);
	foreach (@CLUSTER_LIST){
		print "<OPTION value=$_>$_";
   }
   print "</SELECT><input type=hidden name=action value=view_cluster></TD>
   <TD class=dataCell><input type=submit value=Update></TD></form></TR>
   </TABLE></TD></TR></TABLE>";
	&end_shadow_table();
	###END HEADER_TABLE##

   print "<p>";

	###START HOST TABLE##
   &begin_shadow_table("150","#CCCCCC");

   print "<TABLE bgcolor=#660000 BORDER=0 CELLPADDING=4 CELLSPACING=0>
	<TR><TD align=center><font color=#FFFFFF ><b>Cluster Hostnames</font></td></tr>
   <tr><td>
   <TABLE width=150 bgcolor=#CCCCCC BORDER=0 CELLPADDING=2 CELLSPACING=1>
   ";

	foreach my $h (sort keys %{ $INFO{$cluster} }){
   	print "<TR><TD align=center class=DataCell>
		<a href=parse.cgi?cluster=$cluster&host=$h&action=view_host>$h</a></TD></TR>";
	}
	print "</TABLE></TD></TR></TABLE>";
	&end_shadow_table;
	print "</BODY></HTML>";
}

sub begin_shadow_table {
   my $table_width = $_[0];
   my $bgcolor = $_[1];
   if(!$table_width) { $table_width="100%"; }
   if(!$bgcolor) { $bgcolor="#FFFFFF"; }
	print qq(<table border=0 cellpadding=0 cellspacing=0 width=$table_width>
   	<tr><td background="images/shad_l.gif" width=2 valign=top><img src="images/shad_tl.gif" width=2 height=4></td>
   	<td bgcolor="$bgcolor">
	);
}
sub end_shadow_table {
	print qq(
		</td><td valign=top width=8 background="images/shad_r.gif">
		<img src="images/shad_tr.gif" width=8 height=8></td>
   	</tr><tr><td colspan=2 height=8 background="images/shad_bot.gif" align=left><img src="images/shad_bl_corn.gif" width=8 height=8></td>
   	<td width=8 height=8><img src="images/shad_br_corner.gif" width=8 height=8></td></tr></table>
	);
}
