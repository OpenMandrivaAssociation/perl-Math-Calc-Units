%define upstream_name    Math-Calc-Units
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Human-readable unit-aware calculator
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SF/SFINK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod
BuildArch:	noarch

%description
Human-readable unit-aware calculator.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Math/Calc/Units*
%{_bindir}/ucalc
%{_mandir}/*/*


%changelog
* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 415027
- update to 1.07

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 401635
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.06-4mdv2009.0
+ Revision: 257795
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.06-3mdv2009.0
+ Revision: 245829
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Oct 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.06-1mdv2008.1
+ Revision: 97091
- import perl-Math-Calc-Units


* Thu Oct 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.06-1mdv2008.1
- initial Mandriva package 
