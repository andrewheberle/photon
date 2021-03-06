Name:           libmicrohttpd
Summary:        Lightweight library for embedding a webserver in applications
Version:        0.9.70
Release:        1%{?dist}
License:        LGPLv2+
URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
%define sha1    libmicrohttpd=eb40b0c5b80b7d2201cf0dc524fd543ae2f84785

BuildRequires:  autoconf, automake, libtool
BuildRequires:  gnutls-devel

Requires:       gnutls

%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.
Key features that distinguish libmicrohttpd from other projects are:

%package devel
Summary:        Development files for libmicrohttpd
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for libmicrohttpd

%prep
%autosetup -p1

%build
autoreconf --install
%configure --disable-static --with-gnutls --enable-https=yes
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_bindir}/demo

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libmicrohttpd.so.*

%files devel
%{_includedir}/microhttpd.h
%{_libdir}/libmicrohttpd.so
%{_libdir}/pkgconfig/libmicrohttpd.pc

%{_datadir}/info/libmicrohttpd-tutorial.info.gz
%{_datadir}/info/libmicrohttpd.info.gz
%{_datadir}/info/libmicrohttpd_performance_data.png.gz
%{_datadir}/man/man3/libmicrohttpd.3.gz

%changelog
* Wed Aug 12 2020 Susant Sahani <ssahani@vmware.com> 0.9.70-1
- Initial rpm release
