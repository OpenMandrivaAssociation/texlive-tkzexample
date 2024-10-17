Name:		texlive-tkzexample
Version:	63908
Release:	2
Summary:	Package for the documentation of all tkz-* packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkzexample
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkzexample.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkzexample.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is needed to compile the documentation of all
tkz-* packages (like tkz-euclide).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tkzexample
%doc %{_texmfdistdir}/doc/latex/tkzexample

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
