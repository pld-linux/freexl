#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Simple library for extracting the contents of Microsoft Excel files
Summary(pl.UTF-8):	Prosta biblioteka do wyciągania danych z plików Microsoft Excela
Name:		freexl
Version:	1.0.2
Release:	2
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/freexl-sources/%{name}-%{version}.tar.gz
# Source0-md5:	9954640e5fed76a5d9deb9b02b0169a0
URL:		https://www.gaia-gis.it/fossil/freexl
%{?with_apidocs:BuildRequires:	doxygen >= 1.7.3}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeXL is a simple library intended for extracting the contents and
some metadata from Microsoft Excel (.xls) format files.

It makes no attempt to extract GUI-related formatting or
formulas/charts/etc.

%description -l pl.UTF-8
FreeXL to prosta biblioteka do wydobywania zawartości oraz niektórych
metadanych z plików Microsoft Excela (.xls).

Nie próbuje wydobywać formatowania graficznego ani
wzorów/wykresów/itp.

%package devel
Summary:	Header files for FreeXL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FreeXL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FreeXL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FreeXL.

%package static
Summary:	Static FreeXL library
Summary(pl.UTF-8):	Statyczna biblioteka FreeXL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FreeXL library.

%description static -l pl.UTF-8
Statyczna biblioteka FreeXL.

%package apidocs
Summary:	FreeXL API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki FreeXL
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for FreeXL library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki FreeXL.

%prep
%setup -q

%build
%configure

%{__make}

%{?with_apidocs:doxygen}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfreexl.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libfreexl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfreexl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreexl.so
%{_includedir}/freexl.h
%{_pkgconfigdir}/freexl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfreexl.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc html/*
%endif
