#
# TODO:
# - use more shared libraries (lame, make shared librfxswf?)
# - hack to find system Type1 fonts and afms w/o symlinks
# - separate avi2swf (requires avifile)
#
Summary:	Utilities for SWF files manipulation
Summary(pl):	Narzêdzia do manipulacji na plikach SWF
Name:		swftools
Version:	0.4.3
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.quiss.org/swftools/%{name}-%{version}.tar.gz
# Source0-md5:	ce1a8075cd35ba62f1bb67c281cc3774
URL:		http://www.quiss.org/swftools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	t1lib-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for SWF files manipulation.

%description -l pl
Narzêdzia do manipulacji na plikach SWF.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
CPPFLAGS="-I/usr/X11R6/include"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

# use system Type1 fonts, fix broken .swf symlinks
rm -rf $RPM_BUILD_ROOT%{_datadir}/swftools/{fonts,swfs/default_*}
ln -sf %{_fontsdir}/Type1 $RPM_BUILD_ROOT%{_datadir}/swftools/fonts
ln -sf tessel_loader.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_loader.swf
ln -sf simple_viewer.swf $RPM_BUILD_ROOT%{_datadir}/swftools/swfs/default_viewer.swf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
