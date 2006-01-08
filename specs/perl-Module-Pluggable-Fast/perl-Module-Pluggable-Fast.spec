# $Id$
# Authority: dries
# Upstream: Sebastian Riedel <sri$oook,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Pluggable-Fast

Summary: Fast plugins with instantiation
Name: perl-Module-Pluggable-Fast
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Pluggable-Fast/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SRI/Module-Pluggable-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Similar to "Module::Pluggable" but instantiates plugins as soon as
they're found, useful for code generators like "Class::DBI::Loader".

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Pluggable/Fast.pm

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
