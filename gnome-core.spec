Summary:     GNOME core programs
Summary(pl): Programy podstawowe GNOME'a 
Name:        gnome-core
Version:     0.28.1
Release:     3
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome
Icon:        foot.gif
URL:         http://www.gnome.org/
Requires:    gtk+ >= 1.1.1
Requires:    xscreensaver, xlockmore

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

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6/ \
	datadir=$RPM_BUILD_ROOT/usr/X11R6/share

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*.so.*.*}   

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/X11R6/bin/*
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%config /usr/X11R6/share/panelrc
%config /usr/X11R6/share/default.session
/usr/X11R6/share/applets
/usr/X11R6/share/apps
/usr/X11R6/share/gnome
/usr/X11R6/share/pixmaps/*.png
/usr/X11R6/share/pixmaps/*.xpm
/usr/X11R6/share/pixmaps/mailcheck
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-core.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-core.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/gnome-core.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-core.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-core.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-core.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-core.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-core.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-core.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-core.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/gnome-core.mo

%files devel
%defattr(644, root, root)
/usr/X11R6/lib/lib*.so
/usr/X11R6/lib/appletsConf.sh
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/*.a

%changelog
* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-3]
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
- added striping binaries and shared libs,
- removed /usr/lib/<soname> symlink from main package,
- changed permisiion for shared libs to 755,
- removed /usr/lib/*.la from devel,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-core CVS source tree
