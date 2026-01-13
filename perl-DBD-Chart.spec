#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	DBD
%define		pnam	Chart
Summary:	DBD::Chart - DBI driver abstraction for rendering charts and graphs
Summary(pl.UTF-8):	DBD::Chart - warstwa abstrakcji DBI do tworzenia wykresów i grafów
Name:		perl-DBD-Chart
Version:	0.82
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82490f3598c9381030f3e27816dd6f4e
URL:		http://search.cpan.org/dist/DBD-Chart/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-DBI >= 1.14
BuildRequires:	perl-GD >= 2
BuildRequires:	perl-GD-TextUtil >= 0.80
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBD::Chart provides a DBI abstraction for rendering pie charts,
bar charts, box&whisker charts (aka boxcharts), histograms, Gantt
charts, and line, point, and area graphs.

%description -l pl.UTF-8
Moduł DBD::Chart udostępnia warstwę abstrakcji DBI do rysowania
wykresów kołowych, słupkowych i pudełkowych, histogramów, wykresów
Gantta oraz grafów złożonych z linii, punktów i obszarów.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc imgs *.html
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
