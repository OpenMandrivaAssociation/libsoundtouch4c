%define beta b1
%define	major 0
%define libname %mklibname soundtouch4c %{major}
%define develname %mklibname -d soundtouch4c

Summary:	A wrapper for soundtouch so you can use it in C programs
Name:		libsoundtouch4c
Version:	0.5
Release:	%mkrel -c %beta 2
Group:		System/Libraries
License:	GPL
URL:		http://lobstertech.com/2006/aug/23/soundtouch4c/
Source0:	http://lobstertech.com/media/file/libsoundtouch4c/soundtouch4c-%{version}b.tar.gz
BuildRequires:	soundtouch-devel >= 1.3.1
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A wrapper for soundtouch so you can use it in C programs

%package -n	%{libname}
Summary:	A wrapper for soundtouch so you can use it in C programs
Group:          System/Libraries

%description -n	%{libname}
A wrapper for soundtouch so you can use it in C programs

This package contains the shared libraries for libsoundtouch4c.

%package -n	%{develname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	soundtouch4c-devel = %{version}-%{release}

%description -n	%{develname}
Static libraries and header files for libsoundtouch4c.

%prep
%setup -q -n soundtouch4c-%{version}b

# instead of a patch
#perl -pi -e "s|^AM_CFLAGS.*|AM_CFLAGS=%{optflags} -fPIC -Isrc -I%{_includedir}/soundtouch|g" Makefile.am

%build
#autoreconf -fi
%configure2_5x \
    --enable-shared
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/soundtouch4c-demo
%{_datadir}/aclocal/*.m4
%{_mandir}/man7/*.7.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
