%define name	wmakerconf
%define version	2.12
%define release	%mkrel 3
%define Summary	WMakerConf : a configuration utility for WindowMaker

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Graphical desktop/WindowMaker
URL:		https://wmakerconf.sourceforge.net
Source0:	http://garr.dl.sourceforge.net/sourceforge/wmakerconf/wmakerconf-2.12.tar.bz2
Patch0:		wmakerconf.src.error.c.patch
Patch1:		wmakerconf.configure.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	libwraster-devel
BuildRequires:	windowmaker-devel
BuildRequires:	WindowMaker-static-devel
BuildRequires:	windowmaker

%description
WMakerConf (short for Window Maker Configurator) is a configuration
utility for the Window Maker window manager. Unlike the WPrefs.app program
included with Window Maker, WMakerConf uses the GTK+ graphics library. 

%prep
%setup -q
# force use of stdarg.h 
%patch0 -p0
# suppresss imlib support : broken. it's force to use gtk+1.2
%patch1 -p0
# the configure file seems to be really broken

%build
# that is nasty and must be fixed but makes it compile smoothly
export CPPFLAGS=`pkg-config --cflags gtk+-2.0`
export LDFLAGS=`pkg-config --libs gtk+-2.0`
%configure
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
# create missing directories
mkdir -p %{buildroot}%{_datadir}/{icons,doc/%{name}}
# move stuff at the right place
mv %{buildroot}%{_datadir}/%{name}/%{name}.xpm %{buildroot}%{_datadir}/icons/
for docfile in README ABOUT-NLS AUTHORS COPYING ChangeLog MANUAL NEWS NLS-TEAM1
do
mv %{buildroot}%{_datadir}/%{name}/$docfile %{buildroot}%{_datadir}/doc/%{name}
done

# fix the desktop file
sed -i -e 's/^Icon=.*$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*.desktop
sed -i -e 's/^Categories=*.$/Categories=GTK;Settings;X-MandrivaLinux-System-Configuration-Other;/g' %{buildroot}%{_datadir}/applications/*.desktop

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(0755,root,root,0755)
%{_bindir}/*
%{_mandir}/man1/*
%{_iconsdir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%doc README ABOUT-NLS AUTHORS COPYING ChangeLog MANUAL NEWS NLS-TEAM1
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/%{name}.mo
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/%{name}-data.mo
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/%{name}.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/%{name}-data.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%lang(es_ES) %{_datadir}/locale/es_ES/LC_MESSAGES/%{name}-data.mo
%lang(es_ES) %{_datadir}/locale/es_ES/LC_MESSAGES/%{name}.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/%{name}.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/%{name}-data.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/%{name}-data.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/%{name}-data.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/%{name}.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/%{name}.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/%{name}-data.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}-data.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/%{name}-data.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/%{name}.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
