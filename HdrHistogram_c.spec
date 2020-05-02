#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	C port of High Dynamic Range (HDR) histogram
Summary(pl.UTF-8):	Port C biblioteki histogramów HDR (High Dynamic Range)
Name:		HdrHistogram_c
Version:	0.9.13
Release:	1
License:	Public Domain/CC0 v1.0 or BSD
Group:		Libraries
#Source0Download: https://github.com/HdrHistogram/HdrHistogram_c/releases
Source0:	https://github.com/HdrHistogram/HdrHistogram_c/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2233212a5c0b9f39445d8498eb8b8f7e
URL:		https://github.com/HdrHistogram/HdrHistogram_c
BuildRequires:	cmake >= 2.8
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C port of High Dynamic Range (HDR) histogram.

%description -l pl.UTF-8
Port C biblioteki histogramów HDR (High Dynamic Range).

%package devel
Summary:	Header files for HdrHistogram library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki HdrHistogram
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for HdrHistogram library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HdrHistogram.

%package static
Summary:	Static HdrHistogram library
Summary(pl.UTF-8):	Statyczna biblioteka HdrHistogram
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static HdrHistogram library.

%description static -l pl.UTF-8
Statyczna biblioteka HdrHistogram.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/hdr_histogram*_test
%{__rm} $RPM_BUILD_ROOT%{_bindir}/perftest

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/hdr_decoder
%attr(755,root,root) %{_bindir}/hiccup
%attr(755,root,root) %{_libdir}/libhdr_histogram.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdr_histogram.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdr_histogram.so
%dir %{_includedir}/hdr
%{_includedir}/hdr/hdr_*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhdr_histogram_static.a
%endif
