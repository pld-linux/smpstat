Summary:	Utility for monitoring CPU status on MultiProcessor systems
Summary(pl):	Narzêdzie do monitorowania pracy CPU na maszynach wieloprocesorowych
Name:		smpstat
Version:	0.1.1
Release:	2
URL:		http://www.mindspring.com/~joeja/programs.html
License:	GPL
Group:		Applications/System
Source0:	http://www.mindspring.com/~joeja/ftp/mpstat-%{version}.tar.bz2
# Source0-md5:	6a0eeb160c2f84e92654b2ddb205ce90
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smpstat is a utitlity for Linux to help in the monitoring of SMP
machines. Currently it displays percent usr/sys CPU, percent idle, and
interupts split between CPU's and major and minor faults.

%description -l pl
smpstat jest narzêdziem dla linuksa pomagaj±cym w monitorowaniu maszyn
SMP. Aktualnie wy¶wietla procentowe u¿ycie usr/sys CPU, czas idle i
liczbê przerwañ dzielonych miêdzy CPU a tak¿e mniejsze i wiêksze
b³êdy.

%prep
%setup -q -n mpstat-%{version}

%build
%{__cc} %{rpmcflags} -D__SMP__ mpstat.c functions.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README FAQ.txt
