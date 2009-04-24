install::
	$(INSTALL) -m0755 sunos/gmond/gmond.init.solaris   $(ROOT)/$(INIT_SCRIPTS_DIR)/gmond
	$(INSTALL) -m0755 sunos/gmetad/gmetad.init.solaris $(ROOT)/$(INIT_SCRIPTS_DIR)/gmetad
	$(INSTALL) -m0644 sunos/gmond.xml  $(ROOT)/$(PKGROOT)/share/ganglia/gmond.xml
	$(INSTALL) -m0644 sunos/gmetad.xml $(ROOT)/$(PKGROOT)/share/ganglia/gmetad.xml
