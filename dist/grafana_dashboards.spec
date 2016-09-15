Summary: Grafana dashboards developed for SIMP
Name: grafana-dashboards-simp
Version: 0.0.1
Release: Alpha
License: Apache-2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch

Prefix: %{_var}/lib/grafana/dashboards

#Requires: grafana >= 3.0.0 
#Requires: grafana < 4.0.0 

%description
Dashboards developed with SIMP in mind, but may be useful for other grafana
users.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{prefix}
# Need to set ownership
install -p -m 640 -D src/*.json %{buildroot}%{prefix}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,grafana,grafana,-)
%config %{prefix}

%post
# Post installation stuff

%postun
# Post uninstall stuff

%changelog
* Mon Sep 12 2016 Ralph Wright <ralph.wright@onyxpoint.com> - 0.0.1-Alpha
  - Initial Grafana dashboards
