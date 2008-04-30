<!-- INCLUDE BLOCK : header -->

<table cellspacing=20>
<tr>
<!-- START BLOCK : racks -->
   <td valign=top align=center>
      <table cellspacing=5 border=0>
         {RackID}
         {nodes}
      </table>
   </td>
   {tr}
<!-- END BLOCK : racks -->
<tr>

<td colspan=3 valign=top>
<hr>
Click the job button to only see nodes for that job.

<form name="selectjob" action="{self}" method=GET>
<input type=radio name="onejob" 
   value="" OnClick="selectjob.submit()"> All Jobs<br>
<input type=hidden name=c value="{cluster_url}">

<!-- START BLOCK : jobs -->
{button} {summary}<br>
<!-- END BLOCK : jobs -->

<p>
<input type=submit value="View Job">
</form>

</td>

<td colspan=3 valign=top>
<hr>
Click the user button to only see nodes for that user.

<form name="selectuser" action="{self}" method=GET>
<input type=radio name="oneuser" value="" 
   OnClick="selectuser.submit()"> All Users<br>
<input type=hidden name=c value="{cluster_url}">

<!-- START BLOCK : users -->
{button} {user}<br>
<!-- END BLOCK : users -->

<p>
<input type=submit value="View User">
</form>

</td>

</tr>
<tr>

<td colspan=4>
<font size=-1>
Legend<br>
<ul>
 <li>Job line is <i>id: name (user): CPUs/Nodes</i>
</ul>
 
 </td>
</tr>
</table>

</TD></TR></TABLE>

</BODY>
</HTML>
