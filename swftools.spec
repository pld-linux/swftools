Summary:	Utilities for SWF files manipulation
Summary(pl):	Narzêdzia do manipulacji na plikach SWF
Name:		swftools
Version:	0.4.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.quiss.org/swftools/%{name}-%{version}.tar.gz
# Source0-md5:	ce1a8075cd35ba62f1bb67c281cc3774
Patch0:		%{name}-shared.patch
Patch1:		%{name}-t1lib.patch
URL:		http://www.quiss.org/swftools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	t1lib-devel >= 5.0.1
BuildRequires:	zlib-devel
Requires:	ghostscript-fonts-std
Requires:	t1lib >= 5.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for SWF files manipulation.

%description -l pl
Narzêdzia do manipulacji na plikach SWF.

%package avi
Summary:	avi2swf - convert AVI files into SWF
Summary(pl):	avi2swf - narzêdzie do konwersji plików AVI do SWF
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description avi
This package contains avi2swf tool which converts AVI Video files into
Flash SWF Animation files.

%description avi -l pl
Ten pakiet zawiera narzêdzie avi2swf konwertuj±ce pliki obrazu AVI na
pliki animacji Flash SWF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
CPPFLAGS="-I/usr/X11R6/include"
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

# fix broken .swf symlinks
rm -rf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_*
ln -sf tessel_loader.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_loader.swf
ln -sf simple_viewer.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_viewer.swf

# no -devel package, shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ TODO
%attr(755,root,root) %{_bindir}/jpeg2swf
%attr(755,root,root) %{_bindir}/pdf2swf
%attr(755,root,root) %{_bindir}/png2swf
%attr(755,root,root) %{_bindir}/wav2swf
%attr(755,root,root) %{_bindir}/swf*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man1/jpeg2swf.1*
%{_mandir}/man1/pdf2swf.1*
%{_mandir}/man1/png2swf.1*
%{_mandir}/man1/wav2swf.1*
%{_mandir}/man1/swf*.1*

%files avi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avi2swf
%{_mandir}/man1/avi2swf.1*
