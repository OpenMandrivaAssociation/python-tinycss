%global debug_package %{nil}
%define partnme tinycss 

Name:           python-tinycss
Summary:        CSS parser for Python
Version:        0.4
Release:        4
Group:          System/Libraries
License:        BSD
URL:            https://pythonhosted.org/tinycss/
Source0:        https://github.com/SimonSapin/tinycss/archive/%{partnme}-%{version}.tar.gz

BuildRequires:  dos2unix
BuildRequires:  python-devel 
BuildRequires:  python-setuptools 
BuildRequires:  python-cython
BuildRequires:  python2-devel 
BuildRequires:  python2-setuptools 
BuildRequires:  python2-cython

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
#%global __provides_exclude_from ^(%{python_sitearch}|%{python3_sitearch})/.*\\.so$

%description
tinycss is a complete yet simple CSS parser for Python. It supports
the full syntax and error handling for CSS 2.1 as well as some CSS 3
modules. It is designed to be easy to extend for new CSS modules and
syntax, and integrates well with cssselect for Selectors 3 support.

%package -n python2-tinycss
Summary:        CSS parser for Python
Group:          System/Libraries

%description -n python2-tinycss
tinycss is a complete yet simple CSS parser for Python. It supports
the full syntax and error handling for CSS 2.1 as well as some CSS 3
modules. It is designed to be easy to extend for new CSS modules and
syntax, and integrates well with cssselect for Selectors 3 support.

%prep
%setup -q -n tinycss-%{version}
dos2unix LICENSE

rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python2}|'

%build
%{__python} setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}
popd

%files
%doc LICENSE README.rst
%{python_sitearch}/*

%files -n python2-tinycss
%doc LICENSE README.rst
%{python2_sitearch}/*
