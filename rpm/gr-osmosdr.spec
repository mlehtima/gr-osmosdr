%{?filter_setup:
%filter_provides_in %{python3_sitearch}/osmosdr/.*\.so$
%filter_setup
}

Name:          gr-osmosdr
URL:           http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:       0.2.4
Release:       1
License:       GPLv3+
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: fftw-devel
BuildRequires: gmp-devel
BuildRequires: gnuradio-devel
BuildRequires: pybind11-devel
BuildRequires: pkgconfig(librtlsdr)
BuildRequires: pkgconfig(log4cpp)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(sndfile)
BuildRequires: python3-mako
BuildRequires: python3-numpy
BuildRequires: python3-six
#BuildRequires: libunwind-devel
#BuildRequires: uhd-devel
#BuildRequires: hackrf-devel
#BuildRequires: gr-funcube-devel
#BuildRequires: gr-iqbal-devel
#BuildRequires: airspyone_host-devel
#BuildRequires: SoapySDR-devel
#BuildRequires: spdlog-devel
#BuildRequires: libosmo-dsp-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Summary:       Common software API for various radio hardware
Source0:       https://github.com/osmocom/gr-osmosdr/archive/v%{version}/%{name}-%{version}.tar.gz
# https://osmocom.org/issues/5562
Patch0:        gr-osmosdr-0.2.4-gain-fix.patch

%description
Primarily gr-osmosdr supports the OsmoSDR hardware, but it also
offers a wrapper functionality for FunCube Dongle,  Ettus UHD
and rtl-sdr radios. By using gr-osmosdr source you can take
advantage of a common software api in your application(s)
independent of the underlying radio hardware.

%package devel
Summary:       Development files for gr-osmosdr
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-osmosdr.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

# TODO fix the lib location nicer way
#sed -i 's|/lib/|/%{_lib}/|g' CMakeLists.txt

%build
mkdir -p _build
pushd _build
%cmake -DENABLE_DOXYGEN=off ..
%make_build
popd

%install
pushd _build
%make_install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_bindir}/*
%{_libdir}/*.so.*
%{python3_sitearch}/osmosdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/osmosdr
%{_libdir}/*.so
%{_libdir}/cmake/osmosdr/*.cmake
