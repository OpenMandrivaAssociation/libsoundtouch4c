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
URL:		https://lobstertech.com/2006/aug/23/soundtouch4c/
Source0:	http://lobstertech.com/media/file/libsoundtouch4c/soundtouch4c-%{version}b.tar.gz
BuildRequires:	pkgconfig(soundtouch) >= 1.3.1
BuildRequires:	libtool

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

%build
%configure2_5x \
    --enable-shared
%make

%install
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-0.b1.2mdv2011.0
+ Revision: 609779
- rebuild

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 0.5-0.b1.1mdv2010.1
+ Revision: 508661
- 0.5b

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2008.0
+ Revision: 58525
- Import libsoundtouch4c



* Fri Aug 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2008.0
- initial Mandriva package
