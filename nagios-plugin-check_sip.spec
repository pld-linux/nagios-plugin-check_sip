Summary:	Nagios plugin to check SIP server/device
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania urządzeń i serwerów SIP
Name:		nagios-plugin-check_sip
Version:	1.3
Release:	2
License:	GPL
Group:		Networking
Source0:	http://www.bashton.com/downloads/nagios-check_sip-%{version}.tar.gz
# Source0-md5:	6bccc1b1fcd481df7065c6285aadbe25
URL:		http://www.bashton.com/content/nagiosplugins
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	nagios-core
Requires:	nagios-plugins-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%define		_noautoreq_perl utils

%description
This plugin will test a SIP server/device for availability and
response time.

%description -l pl.UTF-8
Wtyczka Nagios-a testująca dostępność i czas odpowiedzi z urządzeń i
serwerów SIP.

%prep
%setup -q -n nagios-check_sip-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}

sed -e 's,@plugindir@,%{_plugindir},' check_sip > $RPM_BUILD_ROOT%{_plugindir}/check_sip
chmod +x $RPM_BUILD_ROOT%{_plugindir}/check_sip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_plugindir}/*
