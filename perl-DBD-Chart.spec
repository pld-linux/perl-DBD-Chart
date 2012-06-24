#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Chart
Summary:	DBD::Chart - DBI driver abstraction for Rendering Charts and Graphs
Summary(pl):	DBD::Chart - warstwa abstrakcji DBI do tworzenia wykres�w i graf�w
Name:		perl-DBD-Chart
Version:	0.80
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI >= 1.14
BuildRequires:	perl-GD >= 2
BuildRequires:	perl-GD-TextUtil >= 0.80
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc imgs *.html
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
