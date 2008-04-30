install::
GMOND_INIT	= gmond/gmond.init.solaris
GMETAD_INIT	= gmetad/gmetad.init.solaris
install::
	mkdir -p $(ROOT)/$(PKGROOT)/share/ganglia/
	$(INSTALL) gmetad.xml $(ROOT)/$(PKGROOT)/share/ganglia/gmetad.xml
	$(INSTALL) gmond.xml $(ROOT)/$(PKGROOT)/share/ganglia/gmond.xml
