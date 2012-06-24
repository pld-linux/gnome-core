Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gr�fico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.4.0.4
Release:	39
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-core/%{name}-%{version}.tar.bz2
Source1:	%{name}-Settings.order
Patch0:		%{name}-applnk.patch
Patch1:		%{name}-TERM.patch
Patch2:		%{name}-help_paths.patch
Patch3:		%{name}-make.patch
Patch4:		%{name}-tasklist-ugly.patch
Patch5:		%{name}-gettext.patch
Patch6:		%{name}-clockicon.patch
Patch7:		%{name}-am15.patch
Patch8:		%{name}-ac25.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	control-center-devel >= 1.4.0
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	xml-i18n-tools
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gtkhtml-devel >= 0.2
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	scrollkeeper
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
Summary(pl):	GNOME core - pliki nag��wkowe itp.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l es devel
Bibliotecas y include de la base de gnome-core.

%description -l fr devel
Biblioth�ques et fichiers d'en-t�te pour la base de gnome-core.

%description -l pl devel
Pliki nag��wkowe itp. do GNOME core.

%package static
Summary:	GNOME core static libraries
Summary(pl):	Biblioteki statyczne GNOME core
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%description -l pl static
Statyczne biblioteki GNOME core.

%prep
%setup -q
%patch0 -p1 
%patch1	-p1
%patch2	-p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
xml-i18n-toolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoheader
autoconf
automake -a -c --foreign
CFLAGS="-DHAVE_CONTROL_CENTER %{rpmcflags}"
CXXFLAGS="%{rpmldflags}"
%configure \
	--without-included-gettext \
	--disable-gtkhtml-help

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/.order

gzip -9nf AUTHORS ChangeLog NEWS README

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
%doc {AUTHORS,NEWS,README}.gz

%dir %{_sysconfdir}/CORBA
%dir %{_sysconfdir}/CORBA/servers
%{_sysconfdir}/CORBA/servers/*
%config %{_sysconfdir}/sound/events/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/applets
%{_datadir}/control-center/Desktop
%{_datadir}/control-center/Session/*.desktop

%{_datadir}/gnome/hints
%{_datadir}/gnome-about
%{_datadir}/gnome-terminal
%{_omf_dest_dir}/omf/%{name}
%{_applnkdir}/Settings/GNOME
%{_applnkdir}/System/gnome-terminal.desktop
%{_applnkdir}/Utilities/gnome-hint.desktop
%{_applnkdir}/gnome-help.desktop

%{_pixmapsdir}/*xpm
%{_pixmapsdir}/*png
%{_pixmapsdir}/fish
%{_pixmapsdir}/mailcheck
%{_pixmapsdir}/tiles
%{_pixmapsdir}/splash

%config %{_datadir}/gnome/default.session
%config %{_datadir}/gnome/default.wm

%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_datadir}/idl
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
