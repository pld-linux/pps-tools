Summary:	LinuxPPS user-space tools
Summary(pl.UTF-8):	Narzędzia LinuxPPS przestrzeni użytkownika
Name:		pps-tools
Version:	1.0.3
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/redlab-i/pps-tools/tags
Source0:	https://github.com/redlab-i/pps-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9b18c55efe020d02c26cd8c759ac258d
URL:		https://github.com/redlab-i/pps-tools
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinuxPPS user-space tools.

%description -l pl.UTF-8
Narzędzia LinuxPPS przestrzeni użytkownika.

%package devel
Summary:	LinuxPPS PPS API header file
Summary(pl.UTF-8):	Plik nagłówkowy PPS API projektu LinuxPPS
Group:		Development/Libraries
BuildArch:	noarch

%description devel
LinuxPPS PPS API (RFC-2783) header file.

%description devel -l pl.UTF-8
Plik nagłówkowy PPS API (RFC-2783) projektu LinuxPPS.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ppsctl
%attr(755,root,root) %{_bindir}/ppsfind
%attr(755,root,root) %{_bindir}/ppsldisc
%attr(755,root,root) %{_bindir}/ppstest
%attr(755,root,root) %{_bindir}/ppswatch

%files devel
%defattr(644,root,root,755)
%{_includedir}/sys/timepps.h
