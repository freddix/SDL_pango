Summary:	Pango bindings for SDL
Name:		SDL_pango
Version:	0.1.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sourceforge/sdlpango/SDL_Pango-%{version}.tar.gz
# Source0-md5:	85bbf9bb7b1cee0538154dadd045418c
Patch0:		SDL_Pango-0.1.2-API-adds.patch
Patch1:		matrix_declarations.patch
URL:		http://sdlpango.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pango bindings for SDL.

%package devel
Summary:	Header and development files for SDL_pango
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header and development files for SDL_pango.

%prep
%setup -qn SDL_Pango-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libSDL_Pango.so.1
%attr(755,root,root) %{_libdir}/libSDL_Pango.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_Pango.so
%{_includedir}/SDL_Pango.h
%{_pkgconfigdir}/SDL_Pango.pc

