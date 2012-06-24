Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gr�fico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.1.0
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-core/%{name}-%{version}.tar.gz
Source1:	gnome-core-Settings.order
Patch0:		gnome-core-applnk.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root
BuildRequires:	gnome-libs-devel
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	gtk+ >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_applnkdir	%{_datadir}/applnk

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope to
CDE and KDE, but GNOME is based completely on Open Source software.  The
gnome-core package includes the basic programs and libraries that are needed
to install GNOME.

You should install the gnome-core package if you would like to use the GNOME
desktop environment.  You'll also need to install the gnome-libs package. 
If you want to use linuxconf with a GNOME front end, you'll also need to
install the gnome-linuxconf package.

%description -l es
GNOME (Entorno de Modelos Objeto por Red de GNU) es un conjunto de
aplicaciones y herramientas amistables para el escritorio, que se usan junto
a un getionario de ventanas para el entorno X11. GNOME es similar en su
objetivo a otros entorno de escritorio como CDE o KDE, pero GNOME est�
integralmente basado en programas y bibliotecas libres. El paquete
gnome-core incluye los programas de base y bibliotecas necesarias para
instalar GNOME.

%description -l fr
GNOME (Environnement Mod�le Objet par R�seau de GNU) est un ensemble
d'applications et d'outils conviviaux pour le bureau graphique, � utiliser
conjointemment avec un gestionnaire de fen�tres X11. GNOME est similaire
dans ses buts et ses fonctionalit�s � d'autres environnements de bureau
comme CDE ou KDE, mais GNOME est integralement bas� sur des programmes et
biblioth�ques libres. Ce paquetage inclut les programmes et biblioth�ques de
base necessaires pour installer GNOME.

%description -l pl
Podstawowe programy i biblioteki, kt�re s� niezb�dne przy ka�dej instlacji
GNOME.

%description -l wa
GNOME (Evironmint di Modeles Objet pa Rantoele di GNOME) est on insemble di
programes �t d' usteyes grafikes pol scribanne, a-z eployi avou on manaedjeu
di purneas do sistinme di purneas X11. Li s�me di GNOME est l' minme ki d'
�tes evironmints di scribanne come CDE oudoben KDE, mins GNOME est tot et�r
bas� so des libes programes �t l�vreyes. Ci paketaedje chal a les maisses
programes �t l�vreyes k' i gn a dadnj� po-z astaler GNOME.

%package devel
Summary:	GNOME core libraries, includes, etc
Summary(es):	Bibliotecas, includes, etc de la base de gnome-core
Summary(fr):	Biblioth�ques, en-t�tes, etc pour la base de gnome-core
Summary(pl):	GNOME core - pliki nag��wkowe, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l es devel
Bibliotecas y include de la base de gnome-core.

%description -l fr devel
Biblioth�ques et fichiers d'en-t�te pour la base de gnome-core.

%description -l pl devel
Pliki nag��wkowe etc do GNOME core.

%package static
Summary:	GNOME core static libraries
Summary(pl):	Biblioteki statyczne GNOME core
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1

%build

gettextize --copy --force
CFLAGS="-DHAVE_CONTROL_CENTER $RPM_OPT_FLAGS"
CXXFLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-s"
export CFLAGS CXXFLAGS LDFLAGS
automake
%configure \
	--without-included-gettext \
	--with-window-manager=enlightenment

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/.order

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%dir %{_sysconfdir}/CORBA
%dir %{_sysconfdir}/CORBA/servers
%config %{_sysconfdir}/CORBA/servers/*
%config %{_sysconfdir}/sound/events/panel.soundlist

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/applets
%{_datadir}/mc

%dir %{_datadir}/gnome/help/gnome-terminal
%{_datadir}/gnome/help/gnome-terminal/C
%lang(no) %{_datadir}/gnome/help/gnome-terminal/no

%dir %{_datadir}/gnome/help/help-browser
%{_datadir}/gnome/help/help-browser/C
%lang(es) %{_datadir}/gnome/help/help-browser/es
%lang(fr) %{_datadir}/gnome/help/help-browser/fr
%lang(hu) %{_datadir}/gnome/help/help-browser/hu
%lang(it) %{_datadir}/gnome/help/help-browser/it
%lang(ko) %{_datadir}/gnome/help/help-browser/ko
%lang(no) %{_datadir}/gnome/help/help-browser/no

%dir %{_applnkdir}/Applications
%dir %{_applnkdir}/Games
%dir %{_applnkdir}/Internet
%dir %{_applnkdir}/Multimedia
%dir %{_applnkdir}/Settings
%dir %{_applnkdir}/System
%dir %{_applnkdir}/Utilities
%{_applnkdir}/.order
%{_applnkdir}/gnome-help.desktop
%{_applnkdir}/*/.directory
%{_applnkdir}/*/.order

%{_datadir}/pixmaps/*xpm
%{_datadir}/pixmaps/*png
%{_datadir}/pixmaps/fish
%{_datadir}/pixmaps/mailcheck
%{_datadir}/pixmaps/tiles

%config %{_datadir}/panelrc
%config %{_datadir}/gnome/default.session
%config %{_datadir}/gnome/default.wm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_datadir}/idl
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
