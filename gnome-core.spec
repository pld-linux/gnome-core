Summary:     GNOME core programs
Name:        gnome-core
Version:     0.28.1
Release:     1
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

%package devel
Summary:     GNOME core libraries, includes, etc
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Panel libraries and header files.

%package static
Summary:     GNOME core static libraries
Group:       X11/gnome
Requires:    %{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}   

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/lib/lib*.so.*.*
%config /usr/share/panelrc
%config /usr/share/default.session
/usr/share/applets
/usr/share/apps
/usr/share/gnome
/usr/share/pixmaps/*.png
/usr/share/pixmaps/*.xpm
/usr/share/pixmaps/mailcheck
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnome-core.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/gnome-core.mo
%lang(fi) /usr/share/locale/fi/LC_MESSAGES/gnome-core.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnome-core.mo
%lang(ga) /usr/share/locale/ga/LC_MESSAGES/gnome-core.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnome-core.mo
%lang(ja) /usr/share/locale/ja/LC_MESSAGES/gnome-core.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/gnome-core.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/gnome-core.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gnome-core.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/gnome-core.mo

%files devel
%defattr(644, root, root)
/usr/lib/lib*.so
/usr/lib/appletsConf.sh
/usr/include/*

%files static
%attr(644, root, root) /usr/lib/*.a

%changelog
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
