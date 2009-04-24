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
