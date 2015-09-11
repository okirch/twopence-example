#
# spec file for package twopence-example
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/


# norootforbuild

%define baseversion 0.1
%define snapshot 20150911-5b2ac60

%define testsuite_dir /var/lib/slenkins

Name:           twopence-example
BuildRequires:  susetest
License:        GPL-2.0
Group:          QA
URL:		https://github.com/okirch/twopence-example
Summary:        Example twopence scripts
Version:        %{baseversion} 
Release:        0
Requires:	susetest-python python-twopence
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{snapshot}.tar.bz2
BuildArch:	noarch

%package control
Summary:	Integration of twopence example tests with jenkins
Group:		QA
BuildArch:	noarch
Requires:	%{name} = %version-%release

%description
This package contains sample twopence scripts.

Authors:
--------
    Olaf Kirch

%description control
This package contains sample twopence scripts and integration to make them
run under jenkins

%prep
%setup -q -n %{name}-%{snapshot}

%build
# make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/lib/twopence
/usr/lib/twopence/example

%files control
%defattr(-,root,root)
%dir %{testsuite_dir}
%{testsuite_dir}/%{name}

%changelog
