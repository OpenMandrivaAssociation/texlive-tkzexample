%global tl_name tkzexample
%global tl_revision 63908

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.45c
Release:	%{tl_revision}.1
Summary:	Package for the documentation of all tkz-* packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkzexample
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkzexample.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkzexample.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is needed to compile the documentation of all tkz-*
packages (like tkz-euclide).

