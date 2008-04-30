<!-- INCLUDE BLOCK : header -->

<table cellspacing=10>
<tr>
 <th align=left>
Name: {name}<br>
Procs: {P}<br>
User: {user}<br>
{status}
 </th>
 <th colspan=2 valign=center align=center>
  <form action="{self}" method=GET name="metric_form">
   {metric_menu}
   <input type=hidden name=id value={id}>
   <input type=hidden name=c value="{cluster_url}">
  </form>
 </th>
</tr>
<!-- START BLOCK : running -->
<!-- START BLOCK : noderow -->
<tr>
{node_row}
</tr>
<!-- END BLOCK : noderow -->

</table>

<HR>
<font size=-1>
<b>Legend:</b><br>
<ul>
<li>The red vertical line in the graphs show approximately when this job began.
<li>Runninng time is <tt>hrs:min:sec</tt>.
<li>Node box is <tt>Job CPUs: hostname [1-min load]</tt>.

</ul>
</font>

<!-- END BLOCK : running -->
<p>

</body>
</html>
