build::
OS.CPPFLAGS = "-I/usr/sfw/include -I/usr/sfw/include/freetype2/freetype -I/opt/rocks/include"
LDFLAGS = -L/usr/sfw/lib/ -L/opt/rocks/lib/ 
export OS.CPPFLAGS LDFLAGS
build::
	gunzip -c $(BASENAME).tar.gz | $(TAR) -xf -
	(\
		cd $(BASENAME);		\
		./configure --enable-perl-site-install --disable-python --prefix=$(PKGROOT) CPPFLAGS=$(OS.CPPFLAGS);\
		$(MAKE);			\
	)	
