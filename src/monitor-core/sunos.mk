build:	
	gunzip -c $(ARCHIVE)-$(VERSION).tar.gz | $(TAR) -xf -
	( 							\
		cd patch-files;					\
		find . -type f | grep -v CVS | cpio -pduv 	\
			../$(ARCHIVE)-$(VERSION);		\
		cd ../$(ARCHIVE)-$(VERSION);			\
		./configure 					\
			--prefix=$(PKGROOT)			\
			--with-gmetad 				\
			--with-libconfuse=/opt/confuse/		\
			--with-libexpat=/usr/sfw		\
			CFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			CPPFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			LDFLAGS="-L/opt/rocks/lib/";		\
		$(MAKE);					\
	)

install::
GMOND_INIT	= gmond/gmond.init.solaris
GMETAD_INIT	= gmetad/gmetad.init.solaris
install::
	mkdir -p $(ROOT)/$(PKGROOT)/share/ganglia/
	$(INSTALL) gmetad.xml $(ROOT)/$(PKGROOT)/share/ganglia/gmetad.xml
	$(INSTALL) gmond.xml $(ROOT)/$(PKGROOT)/share/ganglia/gmond.xml
