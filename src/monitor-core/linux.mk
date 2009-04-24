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
			CFLAGS="-I/opt/rocks/include/"		\
			CPPFLAGS="-I/opt/rocks/include/"	\
			LDFLAGS="-L/opt/rocks/lib/";		\
		$(MAKE);					\
	)

install::
GMOND_INIT	= gmond/gmond.init
GMETAD_INIT	= gmetad/gmetad.init
install::
	mkdir -p $(ROOT)/$(INIT_SCRIPTS_DIR)
	$(INSTALL) -m 0755 $(GMOND_INIT)		\
		$(ROOT)/$(INIT_SCRIPTS_DIR)/gmond
	$(INSTALL) -m 0755 $(GMETAD_INIT) 		\
		$(ROOT)/$(INIT_SCRIPTS_DIR)/gmetad
