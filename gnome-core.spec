Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gráfico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.2.4
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-core/%{name}-%{version}.tar.gz
Source1:	%{name}-Settings.order
Patch0:		%{name}-applnk.patch
Patch1:		%{name}-TERM.patch
Patch2:		%{name}-help_paths.patch
Patch3:		%{name}-applet-docs.make.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	gtk+ >= 1.2.5
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	control-center-devel
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	automake
BuildRequires:	bzip2-devel >= 1.0.1
# BuildRequires:	gtkhtml-static >= 0.2
# BuildRequires:	gnome-print-static
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man

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
pero GNOME está integralmente basado en programas y bibliotecas
libres. El paquete gnome-core incluye los programas de base y
bibliotecas necesarias para instalar GNOME.

%description -l fr
GNOME (Environnement Modèle Objet par Réseau de GNU) est un ensemble
d'applications et d'outils conviviaux pour le bureau graphique, à
utiliser conjointemment avec un gestionnaire de fenêtres X11. GNOME
est similaire dans ses buts et ses fonctionalités à d'autres
environnements de bureau comme CDE ou KDE, mais GNOME est
integralement basé sur des programmes et bibliothèques libres. Ce
paquetage inclut les programmes et bibliothèques de base necessaires
pour installer GNOME.

%description -l pl
Podstawowe programy i biblioteki, które s± niezbêdne przy ka¿dej
instlacji GNOME.

%description -l wa
GNOME (Evironmint di Modeles Objet pa Rantoele di GNOME) est on
insemble di programes èt d' usteyes grafikes pol scribanne, a-z eployi
avou on manaedjeu di purneas do sistinme di purneas X11. Li såme di
GNOME est l' minme ki d' ôtes evironmints di scribanne come CDE
oudoben KDE, mins GNOME est tot etîr basé so des libes programes èt
lîvreyes. Ci paketaedje chal a les maisses programes èt lîvreyes k' i
gn a dadnjî po-z astaler GNOME.

%package devel
Summary:	GNOME core libraries, includes, etc
Summary(es):	Bibliotecas, includes, etc de la base de gnome-core
Summary(fr):	Bibliothèques, en-têtes, etc pour la base de gnome-core
Summary(pl):	GNOME core - pliki nag³ówkowe, etc
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l es devel
Bibliotecas y include de la base de gnome-core.

%description -l fr devel
Bibliothèques et fichiers d'en-tête pour la base de gnome-core.

%description -l pl devel
Pliki nag³ówkowe etc do GNOME core.

%package static
Summary:	GNOME core static libraries
Summary(pl):	Biblioteki statyczne GNOME core
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1 
%patch1	-p1
%patch2	-p1
%patch3	-p1

%build
gettextize --copy --force
autoheader
automake
autoconf
CFLAGS="-DHAVE_CONTROL_CENTER %{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"
%configure \
	--without-included-gettext \
	--disable-gtkhtml-help

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/.order

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README \
	$RPM_BUILD_ROOT%{_mandir}/man?/*

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

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

%{_applnkdir}/Settings/gmenu.desktop
%{_applnkdir}/Settings/.order
%{_applnkdir}/Settings/Session
%{_applnkdir}/Settings/Desktop
%{_applnkdir}/System/gnome-terminal.desktop
%{_applnkdir}/Utilities/gnome-hint.desktop
%{_applnkdir}/gnome-help.desktop

%{_datadir}/pixmaps/*xpm
%{_datadir}/pixmaps/*png
%{_datadir}/pixmaps/fish
%{_datadir}/pixmaps/mailcheck
%{_datadir}/pixmaps/tiles
%{_datadir}/pixmaps/splash

%config %{_datadir}/panelrc
%config %{_datadir}/gnome/default.session
%config %{_datadir}/gnome/default.wm

%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_datadir}/idl
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
