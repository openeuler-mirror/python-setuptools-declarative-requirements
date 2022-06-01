Name:           python-setuptools-declarative-requirements
Version:        1.2.0
Release:        1
Summary:        File support for setuptools declarative setup.cfg
License:        Apache-2.0
URL:            https://github.com/s0undt3ch/setuptools-declarative-requirements
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-declarative-requirements/setuptools-declarative-requirements-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm >= 3.4
# SECTION test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-pypiserver
BuildRequires:  python3-toml
BuildRequires:  python3-virtualenv
BuildRequires:  python3-wheel
# /SECTION
BuildRequires:  fdupes
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wheel
BuildArch:      noarch
#%python_subpackages

%description
File support for setuptools declarative setup.cfg.

%package -n python3-setuptools-declarative-requirements
Summary:	This projects adds the ability for projects using setuptools declarative configuration to specify requirements using requirements files.
Provides:	python-setuptools-declarative-requirements

%description -n python3-setuptools-declarative-requirements
This projects adds the ability for projects using setuptools declarative configuration to specify requirements using requirements files.

%prep
%setup -q -n setuptools-declarative-requirements-%{version}
sed -i 's/"setuptools>=[0-9]*"/"setuptools"/g' tests/conftest.py

%build
%py3_build

%install
%py3_install
#python_expand %fdupes %{buildroot}%{$python_sitelib}


%files -n python3-setuptools-declarative-requirements
%doc CHANGELOG.md README.md
%license LICENSE
%{python3_sitelib}/*

%changelog
* Wed Jun 1 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 1.2.0-1
- Initial package