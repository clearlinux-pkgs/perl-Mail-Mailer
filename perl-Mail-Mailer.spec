#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mail-Mailer
Version  : 2.21
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-2.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-2.21.tar.gz
Summary  : 'Various ancient e-mail related modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Mail-Mailer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Date::Format)
BuildRequires : perl(Date::Parse)

%description
=   Generated on Tue May 21 16:26:37 2019 by OODoc 2.02
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
%setup -q -n MailTools-2.21
cd %{_builddir}/MailTools-2.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Address.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Address.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Cap.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Cap.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/AddrList.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/AddrList.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/Date.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/Date.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/Generic.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Field/Generic.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Filter.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Header.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Header.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Internet.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Internet.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/qmail.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/rfc822.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/sendmail.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/smtp.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/smtps.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Mailer/testfile.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Send.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Send.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mail/Util.pod
/usr/lib/perl5/vendor_perl/5.28.2/MailTools.pm
/usr/lib/perl5/vendor_perl/5.28.2/MailTools.pod