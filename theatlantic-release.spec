Name:           theatlantic-release
Version:        7
Release:        1
Summary:        The Atlantic's custom yum repository

Group:          System Environment/Base
License:        GPLv2

URL:            http://dev.theatlantic.com/repo/el/7/
Source0:        theatlantic.repo

BuildArch:     noarch
Requires:      redhat-release >=  %{version}

%description
This package contains The Atlantic's custom yum repository.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Wed Jan 18 2017 Frankie Dintino <fdintino@theatlantic.com> - 7-1
- Initial build.
