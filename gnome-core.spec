Summary:	The core programs for the GNOME GUI desktop environment
Summary(es):	Los programas de base del entorno gráfico de Gnome
Summary(fr):	Les programmes de base de l'environnement graphique Gnome
Summary(pl):	Programy podstawowe GNOME'a
Summary(wa):	Les maisses programes do scribanne grafike Gnome
Name:		gnome-core
Version:	1.0.53
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
Source1:	gnome-core-Settings.order
Patch0:		gnome-core-asclock.patch
Patch1:		gnome-core-smallfont.patch
Patch2:		gnome-core-nodisc.patch
Patch3:		gnome-core-applnk.patch
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
objetivo a otros entorno de escritorio como CDE o KDE, pero GNOME está
integralmente basado en programas y bibliotecas libres. El paquete
gnome-core incluye los programas de base y bibliotecas necesarias para
instalar GNOME.

%description -l fr
GNOME (Environnement Modèle Objet par Réseau de GNU) est un ensemble
d'applications et d'outils conviviaux pour le bureau graphique, à utiliser
conjointemment avec un gestionnaire de fenêtres X11. GNOME est similaire
dans ses buts et ses fonctionalités à d'autres environnements de bureau
comme CDE ou KDE, mais GNOME est integralement basé sur des programmes et
bibliothèques libres. Ce paquetage inclut les programmes et bibliothèques de
base necessaires pour installer GNOME.

%description -l pl
Podstawowe programy i biblioteki, które s± niezbêdne przy ka¿dej instlacji
GNOME.

%description -l wa
GNOME (Evironmint di Modeles Objet pa Rantoele di GNOME) est on insemble di
programes èt d' usteyes grafikes pol scribanne, a-z eployi avou on manaedjeu
di purneas do sistinme di purneas X11. Li såme di GNOME est l' minme ki d'
ôtes evironmints di scribanne come CDE oudoben KDE, mins GNOME est tot etîr
basé so des libes programes èt lîvreyes. Ci paketaedje chal a les maisses
programes èt lîvreyes k' i gn a dadnjî po-z astaler GNOME.

%package devel
Summary:	GNOME core libraries, includes, etc
Summary(es):	Bibliotecas, includes, etc de la base de gnome-core
Summary(fr):	Bibliothèques, en-têtes, etc pour la base de gnome-core
Summary(pl):	GNOME core - pliki nag³ówkowe, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
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
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/gnome/apps/Settings/.order

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
%dir %{_datadir}/xmodmap
%lang(be) %{_datadir}/xmodmap/xmodmap.be
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch
%lang(ch) %{_datadir}/xmodmap/xmodmap.cz
%lang(de) %{_datadir}/xmodmap/xmodmap.de
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(es) %{_datadir}/xmodmap/xmodmap.es
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%lang(gr) %{_datadir}/xmodmap/xmodmap.gr
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(il) %{_datadir}/xmodmap/xmodmap.il
%lang(is) %{_datadir}/xmodmap/xmodmap.is
%lang(it) %{_datadir}/xmodmap/xmodmap.it
%lang(la) %{_datadir}/xmodmap/xmodmap.la
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl
%lang(no) %{_datadir}/xmodmap/xmodmap.no
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(qc) %{_datadir}/xmodmap/xmodmap.qc
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru
%lang(se) %{_datadir}/xmodmap/xmodmap.se
%lang(sf) %{_datadir}/xmodmap/xmodmap.sf
%lang(sg) %{_datadir}/xmodmap/xmodmap.sg
%lang(si) %{_datadir}/xmodmap/xmodmap.si
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk
%lang(th) %{_datadir}/xmodmap/xmodmap.th
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk
%lang(us) %{_datadir}/xmodmap/xmodmap.us*
%lang(yu) %{_datadir}/xmodmap/xmodmap.yu

%dir %{_datadir}/gnome/help/gnome-intro
%{_datadir}/gnome/help/gnome-intro/C

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

%dir %{_datadir}/gnome/help/mini-commander_applet
%{_datadir}/gnome/help/mini-commander_applet/C

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
%{_datadir}/pixmaps/mini-commander
%{_datadir}/pixmaps/tiles

%dir %{_datadir}/pixmaps/gkb
%lang(at) %{_datadir}/pixmaps/gkb/at.xpm
%lang(be) %{_datadir}/pixmaps/gkb/be.xpm
%lang(bg) %{_datadir}/pixmaps/gkb/bg.xpm
%lang(ca) %{_datadir}/pixmaps/gkb/ca.xpm
%lang(ch) %{_datadir}/pixmaps/gkb/ch.xpm
%lang(cz) %{_datadir}/pixmaps/gkb/cz.xpm
%lang(de) %{_datadir}/pixmaps/gkb/de.xpm
%lang(dk) %{_datadir}/pixmaps/gkb/dk.xpm
%lang(es) %{_datadir}/pixmaps/gkb/es.xpm
%lang(fi) %{_datadir}/pixmaps/gkb/fi.xpm
%lang(fr) %{_datadir}/pixmaps/gkb/fr.xpm
%lang(gb) %{_datadir}/pixmaps/gkb/gb.xpm
%lang(gr) %{_datadir}/pixmaps/gkb/gr.xpm
%lang(hu) %{_datadir}/pixmaps/gkb/hu.xpm
%lang(il) %{_datadir}/pixmaps/gkb/il.xpm
%lang(is) %{_datadir}/pixmaps/gkb/is.xpm
%lang(it) %{_datadir}/pixmaps/gkb/it.xpm
%lang(jp) %{_datadir}/pixmaps/gkb/jp.xpm
%lang(nl) %{_datadir}/pixmaps/gkb/nl.xpm
%lang(no) %{_datadir}/pixmaps/gkb/no.xpm
%lang(pl) %{_datadir}/pixmaps/gkb/pl.xpm
%lang(pt) %{_datadir}/pixmaps/gkb/pt.xpm
%lang(qc) %{_datadir}/pixmaps/gkb/qc.xpm
%lang(ru) %{_datadir}/pixmaps/gkb/ru.xpm
%lang(se) %{_datadir}/pixmaps/gkb/se.xpm
%lang(si) %{_datadir}/pixmaps/gkb/si.xpm
%lang(sk) %{_datadir}/pixmaps/gkb/sk.xpm
%lang(th) %{_datadir}/pixmaps/gkb/th.xpm
%lang(tr) %{_datadir}/pixmaps/gkb/tr.xpm
%lang(us) %{_datadir}/pixmaps/gkb/us.xpm
%lang(yu) %{_datadir}/pixmaps/gkb/yu.xpm

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
