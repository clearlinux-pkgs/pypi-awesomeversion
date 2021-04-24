#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awesomeversion
Version  : 21.2.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/a4/dc/a9f8224b7b02f3076e5a76b0b920a2ec567abb479c6a5b50f2721cf9b8ae/awesomeversion-21.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a4/dc/a9f8224b7b02f3076e5a76b0b920a2ec567abb479c6a5b50f2721cf9b8ae/awesomeversion-21.2.3.tar.gz
Summary  : One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them.
Group    : Development/Tools
License  : MIT
Requires: awesomeversion-license = %{version}-%{release}
Requires: awesomeversion-python = %{version}-%{release}
Requires: awesomeversion-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# AwesomeVersion
[![codecov](https://codecov.io/gh/ludeeus/awesomeversion/branch/main/graph/badge.svg)](https://codecov.io/gh/ludeeus/awesomeversion)
![python version](https://img.shields.io/badge/Python-3.6=><=3.10-blue.svg)
![dependencies](https://img.shields.io/badge/Dependencies-0-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/awesomeversion)](https://pypi.org/project/awesomeversion)
![Actions](https://github.com/ludeeus/awesomeversion/workflows/Actions/badge.svg?branch=main)

%package license
Summary: license components for the awesomeversion package.
Group: Default

%description license
license components for the awesomeversion package.


%package python
Summary: python components for the awesomeversion package.
Group: Default
Requires: awesomeversion-python3 = %{version}-%{release}

%description python
python components for the awesomeversion package.


%package python3
Summary: python3 components for the awesomeversion package.
Group: Default
Requires: python3-core
Provides: pypi(awesomeversion)

%description python3
python3 components for the awesomeversion package.


%prep
%setup -q -n awesomeversion-21.2.3
cd %{_builddir}/awesomeversion-21.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614186712
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/awesomeversion
cp %{_builddir}/awesomeversion-21.2.3/LICENCE.md %{buildroot}/usr/share/package-licenses/awesomeversion/cac557ec31c1200997ba103929b2ba901c9a3ed3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/awesomeversion/cac557ec31c1200997ba103929b2ba901c9a3ed3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
