Summary:	Bootstrapping tool for creating supermin appliances
Name:		febootstrap
Version:	3.12
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://people.redhat.com/~rjones/febootstrap/files/%{name}-%{version}.tar.gz
# Source0-md5:	8d0143c96c538909bf0bbc13d09604c4
Patch0:		0001-Fix-Python-code-when-_bestPackageFromList-returns-No.patch
URL:		http://people.redhat.com/~rjones/febootstrap/
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-findlib
BuildRequires:	e2fsprogs-devel
BuildRequires:	libcom_err-devel
BuildRequires:	zlib-devel
BuildRequires:	perl-perldoc
BuildRequires:	gawk
Suggests:	yum >= 3.2
Suggests:	yum-utils
Suggests:	qemu
Suggests:	filelight
Requires:	%{name}-supermin-helper = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Febootstrap is a tool for building supermin appliances.
These are tiny appliances [similar to virtual machines], usually
around 100KB in size, which get fully instantiated on-the-fly
in a fraction of a second when you need to boot one of them.

Currently we support Fedora and Debian.
We hope to support many other distros in future. 

%package supermin-helper
Summary:	Runtime support for febootstrap
Group:		Development/Tools
Requires:	util-linux
Requires:	cpio
Requires:	/sbin/mke2fs

%description supermin-helper
This package contains the runtime support for febootstrap.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	YUM="yum" \
	RPM="rpm" \
	YUMDOWNLOADER="yumdownloader" \
	APTITUDE="aptitude" \
	APT_CACHE="apg-cache" \
	DPKG="dpkg" \
	PACMAN="pacman"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/febootstrap
%{_mandir}/man8/febootstrap.8*

%files supermin-helper
%defattr(644,root,root,755)
%doc helper/README
%attr(755,root,root) %{_bindir}/febootstrap-supermin-helper
%{_mandir}/man8/febootstrap-supermin-helper.8*
