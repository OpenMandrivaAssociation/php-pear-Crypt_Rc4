%define		_class		Crypt
%define		_subclass	Rc4
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Encryption class for RC4 encryption
Name:		php-pear-%{upstream_name}
Version:	1.0.3
Release:	12
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Crypt_Rc4/
Source0:	http://download.pear.php.net/package/Crypt_RC4-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
RC4 encryption class.

%prep
%setup -q -c
mv package.xml Crypt_RC4-%{version}/%{upstream_name}.xml

%install
cd Crypt_RC4-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

