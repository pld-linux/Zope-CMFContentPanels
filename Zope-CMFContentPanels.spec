%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFContentPanels
Summary:	A CMF/Plone portlets product
Summary(pl):	Produkt dla CMF/Plone pozwalaj±cy na manipulacje panelami portalu
Name:		Zope-%{zope_subname}
Version:	1.2.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/panjunyong/%{zope_subname}/%{zope_subname}-1_2_0/contentpanels-1_2_0.tgz
# Source0-md5:	e882c30a13af77cb3af3c328a6c83aed
URL:		http://zope.org/Members/panjunyong/CMFContentPanels/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%description
A CMF/Plone portlets product.

%description -l pl
Produkt dla CMF/Plone pozwalaj±cy na manipulacje panelami portalu.

%prep
%setup -q -n %{zope_subname}

find . -type d -name .svn | xargs rm -rf
find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,*.gif,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt INSTALL.txt
%{_datadir}/%{name}
