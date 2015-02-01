%global cartridgedir %{_libexecdir}/openshift/cartridges/squid

Name: 		openshift-origin-cartridge-squid
Version:	3.1.10
Release:	1%{?dist}
Summary:	Squid is a proxy server and web cache daemon

Group:		Development/Languages
License:	GPLv2
URL:	 	http://blub.com	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64

Requires:	squid

%define _unpackaged_files_terminate_build 0


%description
Squid is a proxy server and web cache daemon packaged as cartridge for Openshift 2.

%prep
%setup -q


%build


%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{cartridgedir}
%__cp -r * %{buildroot}/%{cartridgedir}

%clean
rm -rf %{buildroot}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/errors
%{cartridgedir}/icons
%{cartridgedir}/template
%{cartridgedir}/metadata
%{cartridgedir}




%changelog

