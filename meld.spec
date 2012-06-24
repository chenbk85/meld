Summary:	Visual diff and merge tool
Summary(pl):	Wizualne narz�dzie do ogl�dania i w��czania zmian (diff)
Name:		meld
Version:	0.9.0
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sf.net/meld/%{name}-%{version}.tgz
# Source0-md5:	ade97f490ff61f2a5b85a3cc6d885232
Patch0:		%{name}-desktop.patch
URL:		http://meld.sf.net/
BuildRequires:	python-pyorbit-devel >= 1.99.7
BuildRequires:	python-gnome-devel >= 1.99.18
BuildRequires:	python-pygtk-devel >= 1.99.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%description -l pl
Meld to przeznaczone dla GNOME 2 wizualne narz�dzie do ogl�dania i
w��czania zmian (w formacie diff). Integruje si� szczeg�lnie dobrze z
CVS. Przegl�darka r�nic pozwala modyfikowa� pliki w miejscu
(dynamicznie uaktualnia�), a �rodkowa kolumna pokazuje szczeg�owe
zmiany i pozwala na w��czanie. Na marginesach jest pokazane po�o�enie
zmian w celu �atwej nawigacji. Jest dost�pny tak�e interfejs z
zak�adkami, pozwalaj�cy na otwieranie wielu plik�w diff naraz.

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/meld/glade2/pixmaps,%{_desktopdir},%{_pixmapsdir}}

install %{name} *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install glade2/*.glade* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2
install glade2/pixmaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2/pixmaps
install glade2/pixmaps/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/meld.png
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

echo "exec %{_datadir}/%{name}/%{name}" >$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO.txt changelog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/glade2
%{_desktopdir}/*
%{_pixmapsdir}/*
