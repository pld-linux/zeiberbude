Summary:	zeiberbude - controlling access to the computer in Internet cyber-cafe
Summary(pl):	zeiberbude - kontrola dostêpu do komputera w kawiarniach internetowych
Name:		zeiberbude
Version:	2.0.4
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/zeiberbude/%{name}-%{version}.tar.gz
# Source0-md5:	90dec3e78492989e8a3bdf89c71abe25
Patch0:		%{name}-dirs.patch
URL:		http://zeiberbude.sourceforge.net/
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With Zeiberbude you can control easily the access to the computer in
your Internet cyber-cafe. The price is computed automatically for the
used time of the customer.

%description -l pl
Za pomoc± Zeiberbude mo¿na ³atwo kontrolowaæ dostêp do komputera we
w³asnej kawiarni internetowej. Dla ka¿dego klienta jest automatycznie
wyliczana cena us³ugi na podstawie czasu korzystania.

%prep
%setup -q -n %{name}
%patch0 -p1

# needed for gcc 3.3 (multi-line string issue)
sed -e '2,281s/$/\\n\\/' src/copying.h > copying.h.tmp
mv -f copying.h.tmp src/copying.h

%build
QTDIR=%{_prefix}
QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
export QTDIR QMAKESPEC
qmake

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -W -DVERSION=\\\"2.0.4\\\" -DZEIBERBUDE_RC=\\\"/etc/zeiberbude/config.xml\\\" -DZEIBERBUDE_DB=\\\"/var/lib/zeiberbude/db.xml\\\" -DQT_NO_DEBUG"

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
