build:	
	gunzip -c $(ARCHIVE)-$(VERSION).tar.gz | $(TAR) -xf -
	( 							\
		cd patch-files;					\
		find . -type f | grep -v CVS | 			\
			cpio -pduv ../$(ARCHIVE)-$(VERSION);	\
		cd ../$(ARCHIVE)-$(VERSION);			\
		./configure 					\
			--prefix=$(PKGROOT)			\
			--with-gmetad 				\
			--with-libconfuse=/opt/confuse/		\
			--with-librrd=/opt/rocks/lib/		\
			CFLAGS="-I/opt/rocks/include/ -DROCKS"	\
			CPPFLAGS="-I/opt/rocks/include/"	\
			LDFLAGS="-L/opt/rocks/lib/";		\
		$(MAKE);					\
	)


install::
GMOND_INIT	= $(ARCHIVE)-$(VERSION)/gmond/gmond.init
GMETAD_INIT	= $(ARCHIVE)-$(VERSION)/gmetad/gmetad.init
install::
	mkdir -p $(ROOT)/$(INIT_SCRIPTS_DIR)
	$(INSTALL) -m 0755 $(GMOND_INIT)		\
		$(ROOT)/$(INIT_SCRIPTS_DIR)/gmond
	$(INSTALL) -m 0755 $(GMETAD_INIT) 		\
		$(ROOT)/$(INIT_SCRIPTS_DIR)/gmetad
