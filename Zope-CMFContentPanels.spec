%define		zope_subname	CMFContentPanels
#%%define		sub_ver RC1
Summary:	A CMF/Plone portlets product
Summary(pl.UTF-8):	Produkt dla CMF/Plone pozwalający na manipulacje panelami portalu
Name:		Zope-%{zope_subname}
Version:	2.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://plone.org/products/cmfcontentpanels/releases/%{version}/contentpanels-2_0.tgz
# Source0-md5:	95e2e17255faca6f1122fc64723074b2
URL:		http://www.zopechina.com/products-en/CMFContentPanels/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
Conflicts:	CMF
Conflicts:	Plone
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A CMF/Plone portlets product.

%description -l pl.UTF-8
Produkt dla CMF/Plone pozwalający na manipulacje panelami portalu.

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
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt SUPPORT_WIKI.txt README.txt INSTALL.txt TODO.txt CREDIT.txt FAQ.txt
%{_datadir}/%{name}
