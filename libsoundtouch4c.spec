%define	major 0
%define libname %mklibname soundtouch4c %{major}
%define develname %mklibname -d soundtouch4c

Summary:	A wrapper for soundtouch so you can use it in C programs
Name:		libsoundtouch4c
Version:	0.4
Release:	%mkrel 1
Group:		System/Libraries
License:	GPL
URL:		http://www.lobstertech.com/code/voicechanger/
Source0:	http://www.lobstertech.com/code/libsoundtouch4c/releases/%{name}-%{version}.tar.gz
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

%setup -q -n %{name}-%{version}

# instead of a patch
perl -pi -e "s|^AM_CFLAGS.*|AM_CFLAGS=%{optflags} -fPIC -Isrc -I%{_includedir}/soundtouch|g" Makefile.am

libtoolize --force --copy; aclocal; automake --add-missing --copy --gnu; autoconf

%build

%configure2_5x \
    --enable-shared

%make

%install
rm -rf %{buildroot}

%makeinstall

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
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
