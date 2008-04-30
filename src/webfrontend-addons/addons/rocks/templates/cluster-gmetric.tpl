<HTML>
<HEAD>
 <TITLE>{cluster} user-defined metrics</TITLE>
 <META http-equiv="Content-type" content="text/html; charset=utf-8">
 <META http-equiv="refresh" content="300">
 <LINK rel="stylesheet" href="./styles.css" type="text/css"
</HEAD>
<BODY>

<TABLE BORDER="0" WIDTH="100%">
<TR>
  <TD COLSPAN="2" BGCOLOR="#EEEEEE" ALIGN="CENTER">
  <FONT SIZE="+2">{cluster} User Metrics (gmetrics)</FONT>
  </TD>
</TR>

<TR>
 <TD ALIGN="LEFT" VALIGN="TOP" WIDTH=70%>

<FORM ACTION="{self}" METHOD=GET>
<INPUT TYPE=HIDDEN NAME=c VALUE="{cluster_url}">
Show only gmetrics containing:&nbsp;
<input type=text size=20 maxlength=48 name=search value="{search}">
<input type=hidden name="sortby" value="{sortby}">
<input type=hidden name="sortorder" value="{sortorder}">
<input type=submit value="Go">
</FORM>

 </TD>
 <TD ALIGN=left>
<a href={cluster_view}>Back to Cluster View</a>
 </TD>
</TR>

<TABLE BORDER="0" WIDTH="100%">
<TR>
<TH>{TN_SortLink}</TH>
<TH>{TMAX_SortLink}</TH>
<TH>{DMAX_SortLink}</TH>
<TH>{HOST_SortLink}</TH>
<TH>{NAME_SortLink}</TH>
<TH>{VALUE_SortLink}</TH>
<TD>{up_SortOrder} | {down_SortOrder}</TD>
</TR>

<!-- START BLOCK : g_metric_info -->
<TR CLASS={color}>
 <TD CLASS=footer>{tn}</TD><TD CLASS=footer>{tmax}</TD><TD CLASS=footer>{dmax}</TD>
 <TD CLASS=footer>{host}</TD>
 <TD>{name}</TD><TD>{value}</TD>
</TR>
<!-- END BLOCK : g_metric_info -->
</TABLE>

 </TD>
</TR>
</TABLE>

</BODY>
</HTML>
