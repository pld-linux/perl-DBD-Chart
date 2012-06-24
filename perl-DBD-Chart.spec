#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Chart
Summary:	DBD::Chart - DBI driver abstraction for rendering charts and graphs
Summary(pl):	DBD::Chart - warstwa abstrakcji DBI do tworzenia wykres�w i graf�w
Name:		perl-DBD-Chart
Version:	0.80
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	671268b54fdd46d82bfa7b9354d737aa
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu� DBD::Chart udost�pnia warstw� abstrakcji DBI do rysowania
wykres�w ko�owych, s�upkowych i pude�kowych, histogram�w, wykres�w
Gantta oraz graf�w z�o�onych z linii, punkt�w i obszar�w.

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
