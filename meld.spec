Summary:	Visual diff and merge tool
Name:		meld
Version:	0.8.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sf.net/meld/%{name}-%{version}.tgz
# Source0-md5:	463553f70bda8c400843fd34270de2fd
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

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/meld/glade2/pixmaps}

install %{name} *.py $RPM_BUILD_ROOT%{_datadir}/%{name}/
install glade2/*.glade* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2/
install glade2/pixmaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2/pixmaps/

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