Summary:	zeiberbude
Summary(pl):	zeiberbude
Name:		zeiberbude
Version:	2.0.4
Release:	0.1
License:	GPL v2
URL:		http://zeiberbude.sourceforge.net
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/zeiberbude/%{name}-%{version}.tar.gz
# Source0-md5:	90dec3e78492989e8a3bdf89c71abe25
Patch0:		%{name}-dirs.patch
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With Zeiberbude you can control easily the access to the computer in
your internet cyber-cafe. The price is computed automatically for the
used time of the customer.

%description -l pl
todo

%prep
%setup -q -n zeiberbude
%patch0 -p1

%build
QTDIR=%{_prefix}
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
export QTDIR QMAKESPEC
qmake $RPM_BUILD_ROOT/zeiberbude.pro

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/zeiberbude
install -d $RPM_BUILD_ROOT/var/lib/zeiberbude
install zeiberbude $RPM_BUILD_ROOT%{_bindir}
install config.xml $RPM_BUILD_ROOT%{_sysconfdir}/zeiberbude
install db.xml $RPM_BUILD_ROOT/var/lib/zeiberbude

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO Authors
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/zeiberbude/config.xml
%attr(666,root,root) /var/lib/zeiberbude/db.xml
