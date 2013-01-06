Summary:	Bootstrapping tool for creating supermin appliances
Summary(pl.UTF-8):	Narzędzie bootstrapujące do tworzenia minimalistycznych instalacji
Name:		febootstrap
Version:	3.21
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://libguestfs.org/download/febootstrap/%{name}-%{version}.tar.gz
# Source0-md5:	8938bc9af564ba389651ee24cc3d3d30
URL:		http://people.redhat.com/~rjones/febootstrap/
BuildRequires:	e2fsprogs-devel
BuildRequires:	gawk
BuildRequires:	libcom_err-devel
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-findlib
# not needed in releases (BTW: perldoc is checked, but pod2man is actually used)
#BuildRequires:	perl-perldoc
#BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
Suggests:	filelight
Suggests:	qemu
Suggests:	yum >= 3.2
Suggests:	yum-utils
Requires:	%{name}-supermin-helper = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Febootstrap is a tool for building supermin appliances. These are tiny
appliances [similar to virtual machines], usually around 100KB in
size, which get fully instantiated on-the-fly in a fraction of a
second when you need to boot one of them.

Currently only Fedora and Debian are supported.

%description -l pl.UTF-8
Febootstrap to narzędzie do tworzenia minimalistycznych instalacji
zwanych "appliance". Są to małe instalacje (podobne do maszyn
wirtualnych), zwykle mające ok. 100kB, które można zainstalować w
całości w locie w ciągu ułamku sekundy, kiedy zachodzi potrzeba
uruchomienia takowej.

Obecnie obsługiwane są tylko Fedora i Debian.

%package supermin-helper
Summary:	Runtime support for febootstrap
Summary(pl.UTF-8):	Wsparcie uruchomieniowe dla narzędzia febootstrap
Group:		Development/Tools
Requires:	util-linux
Requires:	cpio
Requires:	/sbin/mke2fs

%description supermin-helper
This package contains the runtime support for febootstrap.

%description supermin-helper -l pl.UTF-8
Ten pakiet zawiera wsparcie uruchomieniowe dla narzędzia febootstrap.

%prep
%setup -q

%build
%configure \
	APT_CACHE="apg-cache" \
	APTITUDE="aptitude" \
	DPKG="dpkg" \
	PACMAN="pacman" \
	RPM="rpm" \
	YUM="yum" \
	YUMDOWNLOADER="yumdownloader"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/febootstrap
%{_mandir}/man8/febootstrap.8*

%files supermin-helper
%defattr(644,root,root,755)
%doc helper/README
%attr(755,root,root) %{_bindir}/febootstrap-supermin-helper
%{_mandir}/man8/febootstrap-supermin-helper.8*
