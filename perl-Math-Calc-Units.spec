%define real_name Math-Calc-Units

Summary:	Human-readable unit-aware calculator
Name:		perl-%{real_name}
Version:	1.06
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SF/SFINK/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod
BuildArch:	noarch

%description
Human-readable unit-aware calculator

%prep

%setup -q -n %{real_name}-%{version} 

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

