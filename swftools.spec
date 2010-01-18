Summary:	Utilities for SWF files manipulation
Summary(pl.UTF-8):	Narzędzia do manipulacji na plikach SWF
Name:		swftools
Version:	0.9.0
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.swftools.org/%{name}-%{version}.tar.gz
# Source0-md5:	946e7c692301a332745d29140bc74e55
Patch0:		%{name}-gcc44.patch
Patch1:		%{name}-swfstrings-print_unknown_chars.patch
URL:		http://www.swftools.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	fonts-Type1-urw
Requires:	t1lib >= 5.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for SWF files manipulation.

%description -l pl.UTF-8
Narzędzia do manipulacji na plikach SWF.

%package avi
Summary:	avi2swf - convert AVI files into SWF
Summary(pl.UTF-8):	avi2swf - narzędzie do konwersji plików AVI do SWF
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description avi
This package contains avi2swf tool which converts AVI Video files into
Flash SWF Animation files.

%description avi -l pl.UTF-8
Ten pakiet zawiera narzędzie avi2swf konwertujące pliki obrazu AVI na
pliki animacji Flash SWF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
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
rm -f $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_*
ln -sf tessel_loader.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_loader.swf
ln -sf simple_viewer.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_viewer.swf

# no -devel package, shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ
%attr(755,root,root) %{_bindir}/as3compile
%attr(755,root,root) %{_bindir}/font2swf
%attr(755,root,root) %{_bindir}/gif2swf
%attr(755,root,root) %{_bindir}/jpeg2swf
%attr(755,root,root) %{_bindir}/pdf2swf
%attr(755,root,root) %{_bindir}/png2swf
%attr(755,root,root) %{_bindir}/swfbbox
%attr(755,root,root) %{_bindir}/swfc
%attr(755,root,root) %{_bindir}/swfcombine
%attr(755,root,root) %{_bindir}/swfdump
%attr(755,root,root) %{_bindir}/swfextract
%attr(755,root,root) %{_bindir}/swfrender
%attr(755,root,root) %{_bindir}/swfstrings
%attr(755,root,root) %{_bindir}/wav2swf
%{_mandir}/man1/as3compile.1*
%{_mandir}/man1/font2swf.1*
%{_mandir}/man1/gif2swf.1*
%{_mandir}/man1/jpeg2swf.1*
%{_mandir}/man1/pdf2swf.1*
%{_mandir}/man1/png2swf.1*
%{_mandir}/man1/swfbbox.1*
%{_mandir}/man1/swfc.1*
%{_mandir}/man1/swfcombine.1*
%{_mandir}/man1/swfdump.1*
%{_mandir}/man1/swfextract.1*
%{_mandir}/man1/swfrender.1*
%{_mandir}/man1/swfstrings.1*
%{_mandir}/man1/wav2swf.1*
%{_datadir}/%{name}

%files avi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avi2swf
%{_mandir}/man1/avi2swf.1*
