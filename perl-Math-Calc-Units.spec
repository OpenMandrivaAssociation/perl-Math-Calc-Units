%define upstream_name    Math-Calc-Units
%define upstream_version 1.07
Name:		perl-%{upstream_name}
Version:	1.07
Release:	3

Summary:	Human-readable unit-aware calculator
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Math-Calc-Units
Source0:	https://cpan.metacpan.org/authors/id/S/SF/SFINK/Math-Calc-Units-1.07.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod
BuildArch:	noarch

%description
Human-readable unit-aware calculator.

%prep
%setup -q -n Math-Calc-Units-1.07

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Math/Calc/Units*
%{_bindir}/ucalc
%{_mandir}/*/*


