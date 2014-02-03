build:
	gunzip -c $(ARCHIVE)-$(VERSION).tar.gz | $(TAR) -xf -
	( 							\
		cd patch-files;					\
		find . -type f | grep -v CVS | cpio -pduv 	\
			../$(ARCHIVE)-$(VERSION);		\
	)
	for i in `find ganglia-$(VERSION) -type f -name Makefile.\*`; do \
			sed -e "/[\t ]*pod2/s/pod2html/-pod2html/g" \
			-e "/[\t ]*pod2/s/pod2text/-pod2text/g"     \
			-e "/[\t ]*pod2/s/pod2man/-pod2man/g" $$i > $${i}.tmp; \
			mv $${i}.tmp $$i; \
		done
		(						\
		cd $(ARCHIVE)-$(VERSION);			\
		./configure 					\
			--prefix=$(PKGROOT)			\
			--sysconfdir=/etc/ganglia		\
			--without-gmetad 			\
			--without-librrd			\
			--with-python=/opt/rocks		\
			--with-libconfuse=/opt/confuse/		\
			--with-libexpat=/usr/sfw		\
			CFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			CPPFLAGS="-I/opt/rocks/include/ -I/usr/sfw"\
			LDFLAGS="-L/opt/rocks/lib/";		\
		$(MAKE);					\
	)
