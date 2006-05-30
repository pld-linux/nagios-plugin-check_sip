%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check SIP server/device
Summary(pl):	Wtyczka Nagiosa do sprawdzania urz±dzeñ i serwerów SIP
Name:		nagios-plugin-check_sip
Version:	1.01
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.bashton.com/downloads/nagios-check_sip-%{version}.tar.gz
# Source0-md5:	c8f43a177d8127c58aaa53c47fc2ea1e
URL:		http://www.bashton.com/content/nagiosplugins
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%define		_noautoreq 'perl(utils)'

%description
This plugin will test a SIP server/device for availability and
response time.

%description -l pl
Wtyczka Nagios-a testuj±ca dostêpno¶æ i czas odpowiedzi z urz±dzeñ i
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
