#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	DBSchema
Summary:	DBIx::DBSchema - Database-independent schema objects
Summary(pl.UTF-8):	DBIx::DBSchema - obiekty schematów niezależne od bazy danych
Name:		perl-DBIx-DBSchema
Version:	0.45
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45f2d5c134fd3f74afa378c8e33bc65f
URL:		http://search.cpan.org/dist/DBIx-DBSchema/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::Oracle)'

%description
DBIx::DBSchema - Database-independent schema objects.

%description -l pl.UTF-8
DBIx::DBSchema - obiekty schematów niezależne od bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/DBIx/DBSchema.pm
%{perl_vendorlib}/DBIx/DBSchema
%{_mandir}/man3/*
