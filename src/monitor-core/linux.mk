build:
	gunzip -c $(ARCHIVE)-$(VERSION).tar.gz | $(TAR) -xf -
	( 							\
		cd $(ARCHIVE)-$(VERSION);			\
		if [ -f ../$(ARCHIVE)-$(VERSION).patch ]; then	\
			patch -p1 < ../$(ARCHIVE)-$(VERSION).patch;\
		fi;						\
		./configure 					\
			--prefix=$(PKGROOT)			\
			--with-gmetad 				\
			--with-libconfuse=/opt/confuse		\
			--with-librrd=/opt/rocks/lib		\
			--sysconfdir=/etc/ganglia		\
			CFLAGS="-I/opt/rocks/include -DROCKS"	\
			CPPFLAGS="-I/opt/rocks/include"		\
			LDFLAGS="-L/opt/rocks/lib -L/opt/confuse/lib"\
			LIBS="-lm -lutil"	;		\
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
