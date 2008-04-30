<!-- INCLUDE BLOCK : header -->

<center>
<table cellspacing=10>
<tr>
 <td colspan=6 align=center>
  <form action="{self}" method=GET>
   Show only jobs for user:&nbsp;
   <input type=text size=10 maxlength=32 name=user value="{user}">
   <input type=submit value="Go">
   <input type=hidden name="sortby" value="{sortby}">
   <input type=hidden name="sortorder" value="{sortorder}">
   <input type=hidden name=c value="{cluster_url}">
  </form>
 </td>
 <td>
  <form action="{self}" method=GET>
   <input type=hidden name="sortby" value="{sortby}">
   <input type=hidden name="sortorder" value="{sortorder}">
   <input type=hidden name="update" value="1">
<!-- START BLOCK : local -->
   <input type=submit value="Update">
<!-- END BLOCK : local -->
  </form>
 </td>

</tr>
<tr>
 <th>{idSortLink}</th>
 <th>{userSortLink}</th>
 <th>{processorsSortLink}</th>
 <th>{stateSortLink}</th>
 <th>{nameSortLink}</th>
 <th>{runtimeSortLink}</th>
 <th>{TNSortLink}</th>
 <td>{upSortOrder} | {downSortOrder}</td>
</tr>

<!-- START BLOCK : job -->
<tr class={color}>
 <td align=center><font size="+1"><a href="{joblink}">{id}</font></td>
 <td align=center>{user}</td>
 <td align=center>{processors}</td>
 <td align=center><a href="{joblink}">{state}</a></td>
 <td align=center>{name}</td>
 <td align=center>{runtime}</td>
 <td align=center><small>{TN}</small></td>
</tr>
<!-- END BLOCK : job -->
<tr>
 <td colspan=7 align=center>
  {summary}
 </td>
</tr>
</table>
</center>

  </TD>
 </TR>
</TABLE>

<p>
<hr>
<font size=-1>
<ul>
<li>Click on a column header to sort by that field.
<li>Click on a job id for its nodes and history.
<li>TN is how old (in sec) the job information is.
<li>Note: Update button only shown if webserver is also the queue submit host.
</ul>
</font>

</body>
</html>
