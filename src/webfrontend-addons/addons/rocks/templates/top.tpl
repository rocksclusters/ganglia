<!-- INCLUDE BLOCK : header -->

<center>
<table cellspacing=10>
<tr>
 <td colspan=6 align=center>
  <form action="{self}" method=GET>
   Show only processes by user:&nbsp;
   <input type=text size=10 maxlength=32 name=user value="{user}">
   <input type=submit value="Go">
   <input type=hidden name="sortby" value="{sortby}">
   <input type=hidden name="sortorder" value="{sortorder}">
   <input type=hidden name=c value="{cluster_url}">
  </form>
 </td>
</tr>
<tr>
 <th>{TN_SortLink}</th>
 <th>{HOST_SortLink}</th>
 <th>{PID_SortLink}</th>
 <th>{USER_SortLink}</th>
 <th>{CMD_SortLink}</th>
 <th>{%CPU_SortLink}</th>
 <th>{%MEM_SortLink}</th>
 <th>{SIZE_SortLink}</th>
 <th>{DATA_SortLink}</th>
 <th>{SHARED_SortLink}</th>
 <th>{VM_SortLink}</th>
 <td>{up_SortOrder} | {down_SortOrder}</td>
</tr>

<!-- START BLOCK : ps -->
<tr class={color}>
 <td align=center><small>{TN}</small></td>
 <td align=left>{HOST}</td>
 <td align=left>{PID}</td>
 <td align=left>{USER}</td>
 <td align=left>{CMD}</td>
 <td align=center>{%CPU}</td>
 <td align=center>{%MEM}</td>
 <td align=center>{SIZE}</td>
 <td align=center>{DATA}</td>
 <td align=center>{SHARED}</td>
 <td align=center>{VM}</td>
</tr>
<!-- END BLOCK : ps -->
</table>
</center>

  </TD>
 </TR>
</TABLE>

<HR>
<font size=-1>
Legend<br>
<ul>
 <li><i>TN:</i> Seconds since fresh data arrived.
 <li><i>SIZE:</i> Program text size (KB).
 <li><i>DATA:</i> Resident - Shared (KB). Roughly the size of 
 the Heap + Stack. <br>
 Includes text segment if there are no children.
 <li><i>SHARED:</i> Shared memory (KB). Dynamically loaded libraries live here.
 <li><i>VM:</i> Total virtual memory size used by the process (KB).
</ul>
Each host reports its top <i>P</i> processes by %CPU usage approximately 
every 60s, where P is <br> the number of CPUs on the host. 
</font>

</body>
</html>
