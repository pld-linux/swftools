Summary:	Utilities for SWF files manipulation
Summary(pl.UTF-8):	Narzędzia do manipulacji na plikach SWF
Name:		swftools
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
#Source0Download: http://www.swftools.org/download.html
Source0:	http://www.swftools.org/%{name}-%{version}.tar.gz
# Source0-md5:	1055ebbe3b4cadcc71e83775a5a0906d
Patch0:		%{name}-swfstrings-print_unknown_chars.patch
Patch1:		%{name}-missing-m4.patch
Patch2:		%{name}-giflib.patch
Patch3:		%{name}-poppler.patch
Patch4:		%{name}-poppler2.patch
Patch5:		%{name}-install.patch
URL:		http://www.swftools.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel >= 5.1
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	poppler-devel
BuildRequires:	t1lib-devel >= 5.0.1
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel
Requires:	fonts-Type1-urw
Requires:	t1lib >= 5.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for SWF files manipulation.

%description -l pl.UTF-8
Narzędzia do manipulacji na plikach SWF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	ac_cv_header_pdflib_h=no \
	AVIFILE_CONFIG=x \
	POPPLER_CFLAGS="-I/usr/include/poppler" \
	--enable-poppler

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
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
