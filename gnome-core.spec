Summary:	GNOME core programs
Summary(pl):	Programy podstawowe GNOME'a 
Name:		gnome-core
Version:	1.0.5
Release:	2
Copyright:	LGPL
Group:		X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnome-core-DESTDIR.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root
BuildPrereq:	gnome-libs-devel
BuildPrereq:	gtk+ >= 1.2.0
BuildPrereq:	XFree86-devel
BuildPrereq:	ORBit-devel
BuildPrereq:	gettext
Obsoletes:	gnome

%description
Basic programs and libraries that are virtually required for any GNOME
installation.

GNOME is the GNU Network Object Model Environment.  That's a fancy name but
really GNOME is a nice GUI desktop environment.  It makes using your
computer easy, powerful, and easy to configure.

%description -l pl
Podstawowe programy i biblioteki, które s± niezbêdne przy ka¿dej instlacji
GNOME.

%package devel
Summary:	GNOME core libraries, includes, etc
Summary(pl):	GNOME core - pliki nag³ówkowe, etc
Group:		X11/GNOME
Requires:	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l pl devel
Pliki nag³ówkowe etc do GNOME core.

%package static
Summary:	GNOME core static libraries
Summary(pl):	Biblioteki statyczne GNOME core
Group:		X11/GNOME
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="-DHAVE_CONTROL_CENTER $RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--without-included-gettext \
	--with-window-manager=enlightenment

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%dir /etc/X11/GNOME/CORBA
%dir /etc/X11/GNOME/CORBA/servers
%config /etc/X11/GNOME/CORBA/servers/*
%config /etc/X11/GNOME/sound/events/panel.soundlist

%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

/usr/X11R6/share/applets
/usr/X11R6/share/mc
%dir /usr/X11R6/share/xmodmap
%lang(be) /usr/X11R6/share/xmodmap/xmodmap.be
%lang(bg) /usr/X11R6/share/xmodmap/xmodmap.bg
%lang(ch) /usr/X11R6/share/xmodmap/xmodmap.ch
%lang(ch) /usr/X11R6/share/xmodmap/xmodmap.cz
%lang(de) /usr/X11R6/share/xmodmap/xmodmap.de
%lang(dk) /usr/X11R6/share/xmodmap/xmodmap.dk
/usr/X11R6/share/xmodmap/xmodmap.dvorak
%lang(es) /usr/X11R6/share/xmodmap/xmodmap.es
%lang(fi) /usr/X11R6/share/xmodmap/xmodmap.fi
%lang(fr) /usr/X11R6/share/xmodmap/xmodmap.fr*
%lang(gr) /usr/X11R6/share/xmodmap/xmodmap.gr
%lang(hu) /usr/X11R6/share/xmodmap/xmodmap.hu*
%lang(il) /usr/X11R6/share/xmodmap/xmodmap.il
%lang(is) /usr/X11R6/share/xmodmap/xmodmap.is
%lang(it) /usr/X11R6/share/xmodmap/xmodmap.it
%lang(la) /usr/X11R6/share/xmodmap/xmodmap.la
%lang(nl) /usr/X11R6/share/xmodmap/xmodmap.nl
%lang(no) /usr/X11R6/share/xmodmap/xmodmap.no
%lang(pl) /usr/X11R6/share/xmodmap/xmodmap.pl
%lang(pt) /usr/X11R6/share/xmodmap/xmodmap.pt*
%lang(qc) /usr/X11R6/share/xmodmap/xmodmap.qc
%lang(ru) /usr/X11R6/share/xmodmap/xmodmap.ru
%lang(se) /usr/X11R6/share/xmodmap/xmodmap.se
%lang(sf) /usr/X11R6/share/xmodmap/xmodmap.sf
%lang(sg) /usr/X11R6/share/xmodmap/xmodmap.sg
%lang(si) /usr/X11R6/share/xmodmap/xmodmap.si
%lang(sk) /usr/X11R6/share/xmodmap/xmodmap.sk
%lang(th) /usr/X11R6/share/xmodmap/xmodmap.th
%lang(tr) /usr/X11R6/share/xmodmap/xmodmap.tr*
%lang(uk) /usr/X11R6/share/xmodmap/xmodmap.uk
%lang(us) /usr/X11R6/share/xmodmap/xmodmap.us*
%lang(yu) /usr/X11R6/share/xmodmap/xmodmap.yu

%dir /usr/X11R6/share/gnome/help/gnome-intro
/usr/X11R6/share/gnome/help/gnome-intro/C

%dir /usr/X11R6/share/gnome/help/gnome-terminal
/usr/X11R6/share/gnome/help/gnome-terminal/C
%lang(no) /usr/X11R6/share/gnome/help/gnome-terminal/no

%dir /usr/X11R6/share/gnome/help/help-browser
/usr/X11R6/share/gnome/help/help-browser/C
%lang(es) /usr/X11R6/share/gnome/help/help-browser/es
%lang(fr) /usr/X11R6/share/gnome/help/help-browser/fr
%lang(hu) /usr/X11R6/share/gnome/help/help-browser/hu
%lang(it) /usr/X11R6/share/gnome/help/help-browser/it
%lang(ko) /usr/X11R6/share/gnome/help/help-browser/ko
%lang(no) /usr/X11R6/share/gnome/help/help-browser/no

%dir /usr/X11R6/share/gnome/help/mini-commander_applet
/usr/X11R6/share/gnome/help/mini-commander_applet/C

/usr/X11R6/share/pixmaps/*xpm
/usr/X11R6/share/pixmaps/*png
/usr/X11R6/share/pixmaps/fish
/usr/X11R6/share/pixmaps/mailcheck
/usr/X11R6/share/pixmaps/mini-commander
/usr/X11R6/share/pixmaps/tiles

%dir /usr/X11R6/share/pixmaps/gkb
%lang(at) /usr/X11R6/share/pixmaps/gkb/at.xpm
%lang(be) /usr/X11R6/share/pixmaps/gkb/be.xpm
%lang(bg) /usr/X11R6/share/pixmaps/gkb/bg.xpm
%lang(ca) /usr/X11R6/share/pixmaps/gkb/ca.xpm
%lang(ch) /usr/X11R6/share/pixmaps/gkb/ch.xpm
%lang(cz) /usr/X11R6/share/pixmaps/gkb/cz.xpm
%lang(de) /usr/X11R6/share/pixmaps/gkb/de.xpm
%lang(dk) /usr/X11R6/share/pixmaps/gkb/dk.xpm
%lang(es) /usr/X11R6/share/pixmaps/gkb/es.xpm
%lang(fi) /usr/X11R6/share/pixmaps/gkb/fi.xpm
%lang(fr) /usr/X11R6/share/pixmaps/gkb/fr.xpm
%lang(gb) /usr/X11R6/share/pixmaps/gkb/gb.xpm
%lang(gr) /usr/X11R6/share/pixmaps/gkb/gr.xpm
%lang(hu) /usr/X11R6/share/pixmaps/gkb/hu.xpm
%lang(il) /usr/X11R6/share/pixmaps/gkb/il.xpm
%lang(is) /usr/X11R6/share/pixmaps/gkb/is.xpm
%lang(it) /usr/X11R6/share/pixmaps/gkb/it.xpm
%lang(jp) /usr/X11R6/share/pixmaps/gkb/jp.xpm
%lang(nl) /usr/X11R6/share/pixmaps/gkb/nl.xpm
%lang(no) /usr/X11R6/share/pixmaps/gkb/no.xpm
%lang(pl) /usr/X11R6/share/pixmaps/gkb/pl.xpm
%lang(pt) /usr/X11R6/share/pixmaps/gkb/pt.xpm
%lang(qc) /usr/X11R6/share/pixmaps/gkb/qc.xpm
%lang(ru) /usr/X11R6/share/pixmaps/gkb/ru.xpm
%lang(se) /usr/X11R6/share/pixmaps/gkb/se.xpm
%lang(si) /usr/X11R6/share/pixmaps/gkb/si.xpm
%lang(sk) /usr/X11R6/share/pixmaps/gkb/sk.xpm
%lang(th) /usr/X11R6/share/pixmaps/gkb/th.xpm
%lang(tr) /usr/X11R6/share/pixmaps/gkb/tr.xpm
%lang(us) /usr/X11R6/share/pixmaps/gkb/us.xpm
%lang(yu) /usr/X11R6/share/pixmaps/gkb/yu.xpm

%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/gnome-core.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-core.mo
%lang(ga)    /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-core.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/gnome-core.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-core.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-core.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-core.mo
%lang(nl)    /usr/X11R6/share/locale/nl/LC_MESSAGES/gnome-core.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-core.mo
%lang(pl)    /usr/X11R6/share/locale/pl/LC_MESSAGES/gnome-core.mo
%lang(pt)    /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-core.mo
%lang(ru)    /usr/X11R6/share/locale/ru/LC_MESSAGES/gnome-core.mo
%lang(sv)    /usr/X11R6/share/locale/sv/LC_MESSAGES/gnome-core.mo
%lang(wa)    /usr/X11R6/share/locale/wa/LC_MESSAGES/gnome-core.mo

%config /usr/X11R6/share/panelrc
%config /usr/X11R6/share/gnome/default.session
%config /usr/X11R6/share/gnome/default.wm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/lib/*.sh
/usr/X11R6/share/idl
/usr/X11R6/include/*

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.0.5-2]
- compiled on rpm 3
- replacement in %%files

* Tue Apr 13 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.5-1]
- gzipping %doc,
- more complex %files but %files %lang description is full.

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.1-1]
- added LDFLAGS="-s" to ./configure enviroment,
- more locales (ca, da, es_DO, es_GT, es_HN, es_MX, es_PA, es_PE, es_SV,
  hu, pl, ru),
- changed Requires "gtk+ >= 1.1.11, glib = 1.1.11",
- added --with-included-gettext to configure parameters.

* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-1]
- added /usr/X11R6/share/control-center to main,
- added Requires "gtk+ >= 1.1.2, glib >= 1.1.3".

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-3]
- added package Icon,
- changed prefix to /usr/X11R6.

* Mon Aug 31 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.28-2]
- added pl translation.

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-1]
- more .mo files (sv, pt, ja, fi),
- added package icon,
- added %{_datadir}/default.session %config file in main package,
- added /usr/lib/appletsConf.sh to devel,
- added static subpackage.

* Fri Jul 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.20-3]
- added -q %setup parameter,
- added %lang macros to %{_datadir}/locale/cs/LC_MESSAGES/*/gnome-core.mo
  files,
- added dependences to main package "Requires: gtk+ >= 1.0.0",
- added using %%{name} and %%{version} macros in Source,
- added using $RPM_OPT_FLAGS in CXXFLAGS,
- removed COPYING file from %doc (copyright statment is in Copyright field),
- removed "Prereq: /sbin/install-info" fron main and devel subpackage
  desription,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- changes in registering files from %{_datadir} (not all files an directores
  explicite are from package),
- Buildroot changed to /tmp/%{name}-%%{version}-root,
- added stripping binaries and shared libs,
- removed /usr/lib/<soname> symlink from main package,
- changed permisiion for shared libs to 755,
- removed /usr/lib/*.la from devel,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-core CVS source tree
