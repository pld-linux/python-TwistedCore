%define 	module	TwistedCore

Summary:	Event-driven networking framework written in Python
Summary(pl.UTF-8):	Narzędzia do zdarzeniowego i rozproszonego programowania w Pythonie
Name:		python-%{module}
Version:	13.0.0
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://twistedmatrix.com/Releases/Core/13.0/%{module}-%{version}.tar.bz2
# Source0-md5:	83c2ebed9577a68138eb32b4fdfc65a0
URL:		http://www.twistedmatrix.com/
BuildRequires:	Zope-Interface
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	Zope-Interface
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

%description -l pl.UTF-8
Narzędzia i biblioteki do budowania rozproszonych aplikacji sieciowych
napisane w Pythonie i udostępnione na licencji LGPL. Twisted wspiera
TCP, UDP, SSL/TLS, multicast, gniazda uniksowe, sporą ilość protokołów
(w tym HTTP, NNTP, SSH, IRC, FTP i wiele innych), i dużo więcej.

%package examples
Summary:	Example programs for Twisted
Summary(pl.UTF-8):	Programy przykładowe do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-Twisted-examples
Obsoletes:	python-Twisted-examples-sandbox < 2.0.0

%description examples
This package contains example programs for Twisted.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla Twisted.

%package ssl
Summary:	SSL module for Twisted
Summary(pl.UTF-8):	Moduł SSL dla Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyOpenSSL
Obsoletes:	python-Twisted-ssl
Conflicts:	python-Twisted

%description ssl
This package contains SSL transport module for Twisted

%description ssl -l pl.UTF-8
Ten pakiet zawiera moduł SSL dla Twisted.

%prep
%setup -q -n %{module}-%{version}

# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}
%py_install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
for dir in *; do
	[ ! -d "$dir/doc/examples" ] && continue
	cp -a "$dir/doc/examples/" "$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$dir"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README
%doc doc/{index.html,benchmarks,howto,img,specifications}
%attr(755,root,root) %{_bindir}/manhole
%attr(755,root,root) %{_bindir}/pyhtmlizer
# %attr(755,root,root) %{_bindir}/t-im
%attr(755,root,root) %{_bindir}/tap2deb
%attr(755,root,root) %{_bindir}/tap2rpm
%attr(755,root,root) %{_bindir}/tapconvert
%attr(755,root,root) %{_bindir}/trial
%attr(755,root,root) %{_bindir}/twistd
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
%dir %{py_sitedir}/twisted
%{py_sitedir}/twisted/*.py[co]
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
%{py_sitedir}/twisted/plugins/__*.py[co]
%{py_sitedir}/twisted/plugins/twisted_core.py[co]
%{py_sitedir}/twisted/plugins/twisted_ftp.py[co]
%{py_sitedir}/twisted/plugins/twisted_inet.py[co]
%{py_sitedir}/twisted/plugins/twisted_manhole.py[co]
%{py_sitedir}/twisted/plugins/twisted_portforward.py[co]
%{py_sitedir}/twisted/plugins/twisted_reactors.py[co]
%{py_sitedir}/twisted/plugins/twisted_socks.py[co]
%{py_sitedir}/twisted/plugins/twisted_telnet.py[co]
%{py_sitedir}/twisted/plugins/twisted_trial.py[co]
%{py_sitedir}/twisted/plugins/twisted_qtstub.py[co]
%{py_sitedir}/twisted/plugins/cred_*.py[co]
%exclude %{py_sitedir}/twisted/internet/ssl.py[co]
%{_mandir}/man1/manhole.1*
%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tap2deb.1*
%{_mandir}/man1/tap2rpm.1*
%{_mandir}/man1/tapconvert.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*

%files ssl
%defattr(644,root,root,755)
%{py_sitedir}/twisted/internet/ssl.py[co]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
