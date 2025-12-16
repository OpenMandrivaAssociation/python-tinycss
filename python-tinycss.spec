%global debug_package %{nil}
%define module tinycss

Name:           python-tinycss
Summary:        CSS parser for Python
Version:        0.4
Release:        5
Group:          System/Libraries
License:        BSD
URL:            https://pythonhosted.org/tinycss/
Source0:        https://github.com/SimonSapin/tinycss/archive/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:  dos2unix
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
#%%global __provides_exclude_from ^(%%{python_sitearch}|%%{python3_sitearch})/.*\\.so$

%description
tinycss is a complete yet simple CSS parser for Python. It supports
the full syntax and error handling for CSS 2.1 as well as some CSS 3
modules. It is designed to be easy to extend for new CSS modules and
syntax, and integrates well with cssselect for Selectors 3 support.

%prep
%autosetup -n %{module}-%{version} -p1
dos2unix LICENSE
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}*.*-info
