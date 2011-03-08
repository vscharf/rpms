# $Id$
# Authority: shuff

# ExcludeDist: el4
### EL6 ships with augeas-0.7.2-3.el6
%{?el6:# Tag: rfx}

Summary: Configuration API and editing tool
Name: augeas
Version: 0.8.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Base
URL: http://augeas.net/

Source: http://augeas.net/download/augeas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: readline-devel
Provides: augeas-libs = %{version}-%{release}

%description
Augeas is a configuration API and editing tool. It parses common configuration
files like /etc/hosts or /etc/grub.conf in their native formats and transforms
them into a tree. Configuration changes are made by manipulating this tree and
saving it back into native configuration files. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n vim-augeas
Summary: Vim syntax definitions for %{name}.
Group: Applications/Editors
Requires: vim-common >= 7.0
Provides: augeas-vim = %{version}-%{release}
Obsoletes: augeas-vim < %{version}

%description -n vim-augeas
Syntax and filetype detection files to make editing Augeas configurations in
Vim 7 easier.

%prep
%setup

%build
%configure --disable-dependency-tracking --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix location of Vim files
%{!?el6:%{__mv} %{buildroot}%{_datadir}/vim/vimfiles %{buildroot}%{_datadir}/vim/vim70}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_datadir}/augeas/
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc
%exclude %{_libdir}/libaugeas.la
%exclude %{_libdir}/libfa.la

%files -n vim-augeas
%{_datadir}/vim/vim*/*/augeas.vim

%changelog
* Tue Mar 08 2011 Steve Huff <shuff@vecna.org> - 0.8.0-1
- Update to version 0.8.0.
- Rename augeas-vim subpackage to vim-augeas, for consistency.

* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 0.7.4-1
- Update to version 0.7.4.
- RFX in el6.
- Split off Vim config files.
- Patch no longer necessary.

* Sun Jul 20 2008 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Initial package. (using DAR)
