Summary:     GNOME core programs
Summary(pl): Programy podstawowe GNOME'a 
Name:        gnome-core
Version:     0.99.2
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/%{name}-%{version}.tar.gz
Patch0:      gnome-core.patch
Icon:        gnome-core.gif
Requires:    gnome-libs = 0.99.2, esound = 0.2.7, libgtop = 0.99.1,
Requires:    gtk+ = 1.1.12, glib = 1.1.12
URL:         http://www.gnome.org/
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

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
Summary:     GNOME core libraries, includes, etc
Summary(pl): GNOME core - pliki nag³ówkowe, etc
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l pl devel
Pliki nag³ówkowe etc do GNOME core.

%package static
Summary:     GNOME core static libraries
Summary(pl): Biblioteki statyczne GNOME core
Group:       X11/gnome
Requires:    %{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

#%clean
#rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README

%dir /etc/X11/GNOME/CORBA
%dir /etc/X11/GNOME/CORBA/servers
%config /etc/X11/GNOME/CORBA/servers/*
%config /etc/X11/GNOME/sound/events/panel.soundlist

%config /usr/X11R6/share/panelrc
%config /usr/X11R6/share/default.session

%attr(755, root, root) /usr/X11R6/bin/*
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*

/usr/X11R6/share/applets
/usr/X11R6/share/apps
/usr/X11R6/share/gnome/help/*

/usr/X11R6/share/pixmaps/*

%lang(ca)    /usr/X11R6/share/locale/ca/LC_MESSAGES/gnome-core.mo
%lang(cs)    /usr/X11R6/share/locale/cs/LC_MESSAGES/gnome-core.mo
%lang(da)    /usr/X11R6/share/locale/da/LC_MESSAGES/gnome-core.mo
%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-core.mo
%lang(es)    /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-core.mo
%lang(es_DO) /usr/X11R6/share/locale/es_DO/LC_MESSAGES/gnome-core.mo
%lang(es_GT) /usr/X11R6/share/locale/es_GT/LC_MESSAGES/gnome-core.mo
%lang(es_HN) /usr/X11R6/share/locale/es_HN/LC_MESSAGES/gnome-core.mo
%lang(es_MX) /usr/X11R6/share/locale/es_MX/LC_MESSAGES/gnome-core.mo
%lang(es_PA) /usr/X11R6/share/locale/es_PA/LC_MESSAGES/gnome-core.mo
%lang(es_PE) /usr/X11R6/share/locale/es_PE/LC_MESSAGES/gnome-core.mo
%lang(es_SV) /usr/X11R6/share/locale/es_SV/LC_MESSAGES/gnome-core.mo
%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/gnome-core.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-core.mo
%lang(ga)    /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-core.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/gnome-core.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-core.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-core.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-core.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-core.mo
%lang(pl)    /usr/X11R6/share/locale/pl/LC_MESSAGES/gnome-core.mo
%lang(pt)    /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-core.mo
%lang(ru)    /usr/X11R6/share/locale/ru/LC_MESSAGES/gnome-core.mo
%lang(sv)    /usr/X11R6/share/locale/sv/LC_MESSAGES/gnome-core.mo

%files devel
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/lib/lib*.so
%attr(755, root, root) /usr/X11R6/lib/*.sh
/usr/X11R6/share/idl
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
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
- added /usr/share/default.session %config file in main package,
- added /usr/lib/appletsConf.sh to devel,
- added static subpackage.

* Fri Jul 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.20-3]
- added -q %setup parameter,
- added %lang macros to /usr/share/locale/cs/LC_MESSAGES/*/gnome-core.mo
  files,
- added dependences to main package "Requires: gtk+ >= 1.0.0",
- added using %%{name} and %%{version} macros in Source,
- added using $RPM_OPT_FLAGS in CXXFLAGS,
- removed COPYING file from %doc (copyright statment is in Copyright field),
- removed "Prereq: /sbin/install-info" fron main and devel subpackage
  desription,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- changes in registering files from /usr/share (not all files an directores
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
