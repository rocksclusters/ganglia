build:	
	gunzip -c $(ARCHIVE)-$(VERSION).tar.gz | $(TAR) -xf -
	( 							\
		cd patch-files;					\
		find . -type f | grep -v CVS | cpio -pduv 	\
			../$(ARCHIVE)-$(VERSION);		\
		cd ../$(ARCHIVE)-$(VERSION);			\
		./configure 					\
			--prefix=$(PKGROOT)			\
			--sysconfdir=/etc/ganglia		\
			--without-gmetad 			\
			--without-librrd			\
			--with-python=/opt/rocks		\
			--with-libconfuse=/opt/confuse/		\
			--with-libexpat=/usr/sfw		\
			CC=gcc					\
			CFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			CPPFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			LDFLAGS="-L/opt/rocks/lib/";		\
		$(MAKE);					\
	)
