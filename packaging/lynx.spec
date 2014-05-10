# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       lynx
Summary:    Text-mode WWW Browser with NLS support
Version:    2.8.8dev.9
Release:    2
Group:      Applications/Internet
License:    LGPLv2
URL:        http://lynx.isc.org/
Source0:    http://lynx.isc.org/current/%{name}%{version}.tar.bz2
Source100:  lynx.yaml
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bzip2-devel


%description
Lynx is a fully-featured World Wide Web (WWW) client for users running
cursor-addressable, character-cell display devices.
It is very fast and easy to use. It will display HTML documents
containing links to files residing on the local system,
as well as files residing on remote systems running Gopher, HTTP, FTP,
WAIS, and NNTP servers.

This package contains a development version of lynx.



%package doc
Summary:    Text-mode WWW Browser - documentation
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Lynx is a fully-featured World Wide Web (WWW) client for users running
cursor-addressable, character-cell display devices.
It is very fast and easy to use. It will display HTML documents
containing links to files residing on the local system,
as well as files residing on remote systems running Gopher, HTTP, FTP,
WAIS, and NNTP servers.

This package contains the documentation.



%prep
%setup -q -n %{name}2-8-8

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --enable-cgi-links \
    --enable-cjk \
    --enable-default-colors \
    --enable-exec-links \
    --enable-exec-scripts \
    --enable-externs \
    --enable-gzip-help \
    --enable-ipv6 \
    --enable-kbd-layout \
    --enable-japanese-utf8 \
    --enable-nested-tables \
    --enable-nls \
    --enable-nsl-fork \
    --enable-syslog \
    --with-bzlib \
    --with-screen=ncursesw \
    --with-ssl \
    --with-zlib

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post









%files
%defattr(-,root,root,-)
# >> files
# << files


%files doc
%defattr(-,root,root,-)
# >> files doc
# << files doc

