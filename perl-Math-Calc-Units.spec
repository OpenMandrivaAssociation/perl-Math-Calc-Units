%define upstream_name    Math-Calc-Units
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Human-readable unit-aware calculator
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SF/SFINK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Test-Pod
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Human-readable unit-aware calculator

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/Math/Calc/Units*
%{_bindir}/ucalc
%{_mandir}/*/*

