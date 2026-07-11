%global tl_name crosswrd
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Macros for typesetting crossword puzzles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/crosswrd
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a LaTeX method of typesetting crosswords, and
assists the composer ensure that the grid all goes together properly.
Brian Hamilton Kelly's original was written for LaTeX 2.09, and needed
to be updated to run with current LaTeX.

