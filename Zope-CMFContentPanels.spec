%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFContentPanels
#%%define		sub_ver RC1
Summary:	A CMF/Plone portlets product
Summary(pl):	Produkt dla CMF/Plone pozwalaj±cy na manipulacje panelami portalu
Name:		Zope-%{zope_subname}
Version:	1.7
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/panjunyong/%{zope_subname}/contentpanels-1_7/contentpanels-1_7.tgz
# Source0-md5:	1d31b187685d43461bd77152fc3d2383
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
%doc HISTORY.txt README.txt INSTALL.txt TODO.txt CREDIT.txt FAQ.txt
%{_datadir}/%{name}
