Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gr�fico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.4.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-core/1.4/%{name}-%{version}.tar.bz2
Source1:	%{name}-Settings.order
Source2:	%{name}-Settings.directory
Source3:	gnome-wm.1.da
Patch0:		%{name}-applnk.patch
Patch1:		%{name}-TERM.patch
Patch2:		%{name}-help_paths.patch
Patch3:		%{name}-make.patch
Patch4:		%{name}-tasklist-ugly.patch
Patch5:		%{name}-lbracket.patch
Patch6:		%{name}-am15.patch
Patch7:		%{name}-ac25.patch
Patch8:		%{name}-make2.patch
Patch9:		%{name}-help-browser.desktop.patch
Patch10:	%{name}-gnome-terminal.desktop.patch
Patch11:	%{name}-am16.patch
Patch12:	%{name}-omf.patch
Patch13:	%{name}-avoid-version.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	control-center-devel >= 1.4.0
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.7.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gtk-doc
BuildRequires:	gtkhtml-devel >= 0.2
BuildRequires:	intltool
BuildRequires:	libglade-gnome-devel >= 0.14
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	scrollkeeper
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_sysconfdir	/etc/X11/GNOME
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on Open Source software.
The gnome-core package includes the basic programs and libraries that
are needed to install GNOME. You should install the gnome-core package
if you would like to use the GNOME desktop environment. You'll also
need to install the gnome-libs package. If you want to use linuxconf
with a GNOME front end, you'll also need to install the
gnome-linuxconf package.

%description -l es
GNOME (Entorno de Modelos Objeto por Red de GNU) es un conjunto de
aplicaciones y herramientas amistables para el escritorio, que se usan
junto a un getionario de ventanas para el entorno X11. GNOME es
similar en su objetivo a otros entorno de escritorio como CDE o KDE,
pero GNOME est� integralmente basado en programas y bibliotecas
libres. El paquete gnome-core incluye los programas de base y
bibliotecas necesarias para instalar GNOME.

%description -l fr
GNOME (Environnement Mod�le Objet par R�seau de GNU) est un ensemble
d'applications et d'outils conviviaux pour le bureau graphique, �
utiliser conjointemment avec un gestionnaire de fen�tres X11. GNOME
est similaire dans ses buts et ses fonctionalit�s � d'autres
environnements de bureau comme CDE ou KDE, mais GNOME est
integralement bas� sur des programmes et biblioth�ques libres. Ce
paquetage inclut les programmes et biblioth�ques de base necessaires
pour installer GNOME.

%description -l pl
Podstawowe programy i biblioteki, kt�re s� niezb�dne przy ka�dej
instalacji GNOME.

%description -l wa
GNOME (Evironmint di Modeles Objet pa Rantoele di GNOME) est on
insemble di programes �t d' usteyes grafikes pol scribanne, a-z eployi
avou on manaedjeu di purneas do sistinme di purneas X11. Li s�me di
GNOME est l' minme ki d' �tes evironmints di scribanne come CDE
oudoben KDE, mins GNOME est tot et�r bas� so des libes programes �t
l�vreyes. Ci paketaedje chal a les maisses programes �t l�vreyes k' i
gn a dadnj� po-z astaler GNOME.

%package devel
Summary:	GNOME core libraries, includes, etc
Summary(es):	Bibliotecas, includes, etc de la base de gnome-core
Summary(fr):	Biblioth�ques, en-t�tes, etc pour la base de gnome-core
Summary(pl):	GNOME core - pliki nag��wkowe itp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc-common

%description devel
Header files for gnome-libs.

%description devel -l es
Bibliotecas y include de la base de gnome-core.

%description devel -l fr
Biblioth�ques et fichiers d'en-t�te pour la base de gnome-core.

%description devel -l pl
Pliki nag��wkowe itp. do GNOME core.

%package static
Summary:	GNOME core static libraries
Summary(pl):	Biblioteki statyczne GNOME core
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%description static -l pl
Statyczne biblioteki GNOME core.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing acinclude.m4
%{__libtoolize}
xml-i18n-toolize --copy --force
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoheader}
%{__autoconf}
%{__automake}
CFLAGS="-DHAVE_CONTROL_CENTER `gnome-config --cflags capplet` %{rpmcflags}"
CXXFLAGS="%{rpmldflags}"
%configure \
	--without-included-gettext \
	--disable-gtkhtml-help \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/da/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	HTML_DIR=%{_gtkdocdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/.order
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/.directory
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/da/man1/gnome-wm.1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README

%dir %{_sysconfdir}/CORBA
%dir %{_sysconfdir}/CORBA/servers
%{_sysconfdir}/CORBA/servers/*
%{_sysconfdir}/gnome/panel-config
%config %{_sysconfdir}/sound/events/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpanel_*.so.*.*
%attr(755,root,root) %{_libdir}/libfish_applet.so
%attr(755,root,root) %{_libdir}/libgen_util_applet.so

%{_datadir}/applets
%{_datadir}/control-center/Desktop/*.desktop
%{_datadir}/control-center/Session/*.desktop

%{_datadir}/gnome/hints
%{_datadir}/gnome/panel
%{_datadir}/gnome-about
%{_datadir}/gnome-terminal
%{_datadir}/idl/*
%{_omf_dest_dir}/%{name}
%{_applnkdir}/Settings/GNOME/.directory
%{_applnkdir}/Settings/GNOME/.order
%{_applnkdir}/Settings/GNOME/*.desktop
%{_applnkdir}/Settings/GNOME/Desktop/*.desktop
%{_applnkdir}/Settings/GNOME/Session/*.desktop
%{_applnkdir}/Terminals/gnome-terminal.desktop
%{_applnkdir}/Utilities/gnome-hint.desktop
%{_applnkdir}/Help/gnome-help.desktop

%{_pixmapsdir}/*

%config %{_datadir}/gnome/default.session
%config %{_datadir}/gnome/default.wm

%{_mandir}/man?/*
%lang(da) %{_mandir}/da/man?/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libpanel_*.so
%{_libdir}/libpanel_*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpanel_*.a
