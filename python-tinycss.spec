Name:           python-tinycss
Summary:        CSS parser for Python
Version:        0.3
Release:        1
Group:          System/Libraries
License:        BSD
URL:            http://pythonhosted.org/tinycss/
Source0:        https://github.com/SimonSapin/tinycss/archive/v%{version}.tar.gz

BuildRequires:  dos2unix
BuildRequires:  python-devel python-setuptools python-cython
#%if 0%{?with_python3}
#BuildRequires:  python3-devel python3-setuptools python3-Cython
#%endif # if with_python3

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
#%global __provides_exclude_from ^(%{python_sitearch}|%{python3_sitearch})/.*\\.so$

%description
tinycss is a complete yet simple CSS parser for Python. It supports
the full syntax and error handling for CSS 2.1 as well as some CSS 3
modules. It is designed to be easy to extend for new CSS modules and
syntax, and integrates well with cssselect for Selectors 3 support.

#%if 0%{?with_python3}
#%package -n python3-tinycss
#Summary:        CSS parser for Python
#Group:          System Environment/Libraries
#
#%description -n python3-tinycss
#tinycss is a complete yet simple CSS parser for Python. It supports
#the full syntax and error handling for CSS 2.1 as well as some CSS 3
#modules. It is designed to be easy to extend for new CSS modules and
#syntax, and integrates well with cssselect for Selectors 3 support.
#%endif # if with_python3

%prep
%setup -q -n tinycss-%{version}
dos2unix LICENSE

#%if 0%{?with_python3}
#rm -rf %{py3dir}
#cp -a . %{py3dir}
#find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python3}|'
#%endif # with_python3

%build
%{__python} setup.py build

#%if 0%{?with_python3}
#pushd %{py3dir}
#%{__python3} setup.py build
#popd
#%endif # with_python3

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}

#%if 0%{?with_python3}
#pushd %{py3dir}
#%{__python3} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}
#popd
#%endif # with_python3

%files
%doc LICENSE README.rst
%{python_sitearch}/*

#%if 0%{?with_python3}
#%files -n python3-tinycss
#%doc LICENSE README.rst
#%{python3_sitearch}/*
#%endif # with_python3

