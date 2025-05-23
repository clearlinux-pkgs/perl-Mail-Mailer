#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Mail-Mailer
Version  : 2.22
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-2.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-2.22.tar.gz
Summary  : 'Various ancient e-mail related modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Mail-Mailer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Date::Format)
BuildRequires : perl(Date::Parse)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=   Generated on Mon Nov 18 11:08:31 2024 by OODoc 2.03
There are various ways to install this module:

%package dev
Summary: dev components for the perl-Mail-Mailer package.
Group: Development
Provides: perl-Mail-Mailer-devel = %{version}-%{release}
Requires: perl-Mail-Mailer = %{version}-%{release}

%description dev
dev components for the perl-Mail-Mailer package.


%package perl
Summary: perl components for the perl-Mail-Mailer package.
Group: Default
Requires: perl-Mail-Mailer = %{version}-%{release}

%description perl
perl components for the perl-Mail-Mailer package.


%prep
%setup -q -n MailTools-2.22
cd %{_builddir}/MailTools-2.22
pushd ..
cp -a MailTools-2.22 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mail::Address.3
/usr/share/man/man3/Mail::Cap.3
/usr/share/man/man3/Mail::Field.3
/usr/share/man/man3/Mail::Field::AddrList.3
/usr/share/man/man3/Mail::Field::Date.3
/usr/share/man/man3/Mail::Field::Generic.3
/usr/share/man/man3/Mail::Filter.3
/usr/share/man/man3/Mail::Header.3
/usr/share/man/man3/Mail::Internet.3
/usr/share/man/man3/Mail::Mailer.3
/usr/share/man/man3/Mail::Send.3
/usr/share/man/man3/Mail::Util.3
/usr/share/man/man3/MailTools.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
