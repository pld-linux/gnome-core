Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gr�fico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.1.6
Release:	3
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-core/%{name}-%{version}.tar.gz
Source1:	gnome-core-Settings.order
Patch0:		gnome-core-applnk.patch
Patch1:		gnome-core-TERM.patch
Icon:		gnome-core.gif
URL:		http://www.gnome.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	gtk+ >= 1.2.5
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel >= 0.5.0
BuildRequires:	control-center-devel
BuildRequires:	XFree86-devel
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	xpm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	automake
BuildRoot:	/tmp/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_applnkdir	%{_datadir}/applnk
%define		_mandir		%{_prefix}/man

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope to
CDE and KDE, but GNOME is based completely on Open Source software.  The
gnome-core package includes the basic programs and libraries that are
needed to install GNOME.  You should install the gnome-core package if you
would like to use the GNOME desktop environment.  You'll also need to
install the gnome-libs package.  If you want to use linuxconf with a GNOME
front end, you'll also need to install the gnome-linuxconf package.

%description -l es
GNOME (Entorno de Modelos Objeto por Red de GNU) es un conjunto de
aplicaciones y herramientas amistables para el escritorio, que se usan
junto a un getionario de ventanas para el entorno X11. GNOME es similar en
su objetivo a otros entorno de escritorio como CDE o KDE, pero GNOME est�
integralmente basado en programas y bibliotecas libres. El paquete
gnome-core incluye los programas de base y bibliotecas necesarias para
instalar GNOME.

%description -l fr
GNOME (Environnement Mod�le Objet par R�seau de GNU) est un ensemble
d'applications et d'outils conviviaux pour le bureau graphique, � utiliser
conjointemment avec un gestionnaire de fen�tres X11. GNOME est similaire
dans ses buts et ses fonctionalit�s � d'autres environnements de bureau
comme CDE ou KDE, mais GNOME est integralement bas� sur des programmes et
biblioth�ques libres. Ce paquetage inclut les programmes et biblioth�ques
de base necessaires pour installer GNOME.

%description -l pl
Podstawowe programy i biblioteki, kt�re s� niezb�dne przy ka�dej instlacji
GNOME.

%description -l wa
GNOME (Evironmint di Modeles Objet pa Rantoele di GNOME) est on insemble di
programes �t d' usteyes grafikes pol scribanne, a-z eployi avou on
manaedjeu di purneas do sistinme di purneas X11. Li s�me di GNOME est l'
minme ki d' �tes evironmints di scribanne come CDE oudoben KDE, mins GNOME
est tot et�r bas� so des libes programes �t l�vreyes. Ci paketaedje chal a
les maisses programes �t l�vreyes k' i gn a dadnj� po-z astaler GNOME.

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
%patch1	-p1

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

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README \
	$RPM_BUILD_ROOT%{_mandir}/man?/*

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
%{_sysconfdir}/CORBA/servers/*
%config %{_sysconfdir}/sound/events/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/applets
%{_datadir}/control-center/*.desktop

%dir %{_datadir}/gnome/help/gnome-terminal
%lang(en) %{_datadir}/gnome/help/gnome-terminal/C
%lang(da) %{_datadir}/gnome/help/gnome-terminal/da
%lang(es) %{_datadir}/gnome/help/gnome-terminal/es
%lang(it) %{_datadir}/gnome/help/gnome-terminal/it
%lang(no) %{_datadir}/gnome/help/gnome-terminal/no

%dir %{_datadir}/gnome/help/help-browser
%lang(en) %{_datadir}/gnome/help/help-browser/C
%lang(ca) %{_datadir}/gnome/help/help-browser/ca
%lang(da) %{_datadir}/gnome/help/help-browser/da
%lang(el) %{_datadir}/gnome/help/help-browser/el
%lang(es) %{_datadir}/gnome/help/help-browser/es
%lang(et) %{_datadir}/gnome/help/help-browser/et
%lang(eu) %{_datadir}/gnome/help/help-browser/eu
%lang(fr) %{_datadir}/gnome/help/help-browser/fr
%lang(hu) %{_datadir}/gnome/help/help-browser/hu
%lang(it) %{_datadir}/gnome/help/help-browser/it
%lang(ja) %{_datadir}/gnome/help/help-browser/ja
%lang(ko) %{_datadir}/gnome/help/help-browser/ko
%lang(lt) %{_datadir}/gnome/help/help-browser/lt
%lang(no) %{_datadir}/gnome/help/help-browser/no
%lang(uk) %{_datadir}/gnome/help/help-browser/uk
%lang(wa) %{_datadir}/gnome/help/help-browser/wa

%dir %{_datadir}/gnome/help/desk-guide_applet
%lang(en) %{_datadir}/gnome/help/desk-guide_applet/C

%dir %{_datadir}/gnome/help/fish_applet
%lang(en) %{_datadir}/gnome/help/fish_applet/C

%dir %{_datadir}/gnome/help/mailcheck_applet
%lang(en) %{_datadir}/gnome/help/mailcheck_applet/C

%dir %{_datadir}/gnome/help/panel
%lang(en) %{_datadir}/gnome/help/panel/C

%dir %{_datadir}/gnome/help/tasklist_applet
%lang(en) %{_datadir}/gnome/help/tasklist_applet/C

%{_datadir}/gnome/hints
%{_datadir}/gnome-about

%dir %{_applnkdir}/Applications
%dir %{_applnkdir}/Games
%dir %{_applnkdir}/Internet
%dir %{_applnkdir}/Multimedia
%dir %{_applnkdir}/Settings
%{_applnkdir}/Settings/gmenu.desktop
%{_applnkdir}/Settings/Session
%{_applnkdir}/Settings/Desktop
%dir %{_applnkdir}/System
%{_applnkdir}/System/gnome-terminal.desktop
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
%attr(644,root,root) %{_libdir}/lib*.a
