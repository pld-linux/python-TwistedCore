%define 	module	TwistedCore

Summary:	Event-driven networking framework written in Python
Summary(pl):	Narzêdzia do zdarzeniowego i rozproszonego programowania w Pythonie
Name:		python-%{module}
Version:	2.4.0
Release:	0.1
License:	LGPL
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Twisted/2.4/%{module}-%{version}.tar.bz2
# Source0-md5:	042a57f65fe919a9234047d7ce8c43f1
Patch0:		%{name}-basedir-import.patch
URL:		http://www.twistedmatrix.com/
BuildRequires:	ZopeInterface
BuildRequires:	python-devel >= 2.2
Requires:	ZopeInterface
Requires:	python-Crypto
Requires:	python-devel-tools
%pyrequires_eq	python-modules
Obsoletes:	python-Twisted-web-resource-script < 2.0.0
Conflicts:	python-Twisted
Conflicts:	python-Twisted-ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An event-driven networking framework written in Python and licensed
under the LGPL. Twisted supports TCP, UDP, SSL/TLS, multicast, Unix
sockets, a large number of protocols (including HTTP, NNTP, SSH, IRC,
FTP, and others), and much more.

%description -l pl
Narzêdzia i biblioteki do budowania rozproszonych aplikacji sieciowych
napisane w Pythonie i udostêpnione na licencji LGPL. Twisted wspiera
TCP, UDP, SSL/TLS, multicast, gniazda uniksowe, spor± ilo¶æ protoko³ów
(w tym HTTP, NNTP, SSH, IRC, FTP i wiele innych), i du¿o wiêcej.

%package examples
Summary:	Example programs for Twisted
Summary(pl):	Programy przyk³adowe do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-Twisted-examples
Obsoletes:	python-Twisted-examples-sandbox < 2.0.0

%description examples
This package contains example programs for Twisted.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla Twisted.

%package ssl
Summary:	SSL module for Twisted
Summary(pl):	Modu³ SSL dla Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyOpenSSL
Obsoletes:	python-Twisted-ssl
Conflicts:	python-Twisted

%description ssl
This package contains SSL transport module for Twisted

%description ssl -l pl
Ten pakiet zawiera modu³ SSL dla Twisted.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
for dir in *; do
	[ ! -d "$dir/doc/examples" ] && continue
	cp -ar "$dir/doc/examples/" "$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$dir"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README
%doc doc/{index.html,benchmarks,fun,howto,img,specifications,upgrades,vision}
%attr(755,root,root) %{_bindir}/manhole
%attr(755,root,root) %{_bindir}/mktap
%attr(755,root,root) %{_bindir}/tap2deb
%attr(755,root,root) %{_bindir}/tap2rpm
%attr(755,root,root) %{_bindir}/tapconvert
%attr(755,root,root) %{_bindir}/tkmktap
%attr(755,root,root) %{_bindir}/trial
%attr(755,root,root) %{_bindir}/twistd
%dir %{py_sitedir}/twisted
%{py_sitedir}/twisted/*.py[oc]
%{py_sitedir}/twisted/application
%{py_sitedir}/twisted/cred
%{py_sitedir}/twisted/enterprise
%{py_sitedir}/twisted/internet
%{py_sitedir}/twisted/manhole
%{py_sitedir}/twisted/persisted
%{py_sitedir}/twisted/protocols
%{py_sitedir}/twisted/python
%{py_sitedir}/twisted/scripts
%{py_sitedir}/twisted/spread
%{py_sitedir}/twisted/tap
%{py_sitedir}/twisted/test
%{py_sitedir}/twisted/trial
%dir %{py_sitedir}/twisted/plugins
%{py_sitedir}/twisted/plugins/__*.py[oc]
%{py_sitedir}/twisted/plugins/*plugin.py[oc]
%{py_sitedir}/twisted/plugins/twisted_ftp.py[oc]
%{py_sitedir}/twisted/plugins/twisted_inet.py[oc]
%{py_sitedir}/twisted/plugins/twisted_manhole.py[oc]
%{py_sitedir}/twisted/plugins/twisted_portforward.py[oc]
%{py_sitedir}/twisted/plugins/twisted_socks.py[oc]
%{py_sitedir}/twisted/plugins/twisted_telnet.py[oc]
%{py_sitedir}/twisted/plugins/twisted_trial.py[oc]
%exclude %{py_sitedir}/twisted/internet/ssl.py[oc]
%{_mandir}/man1/manhole.1*
%{_mandir}/man1/mktap.1*
# this script is not installed
#%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tap2deb.1*
%{_mandir}/man1/tap2rpm.1*
%{_mandir}/man1/tapconvert.1*
%{_mandir}/man1/tkmktap.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*

%files ssl
%defattr(644,root,root,755)
%{py_sitedir}/twisted/internet/ssl.py[oc]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
