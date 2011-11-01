Name:		texlive-crosswrd
Version:	3.0
Release:	1
Summary:	Macros for typesetting crossword puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crosswrd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crosswrd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a LaTeX method of typesetting crosswords,
and assists the composer ensure that the grid all goes together
properly. Brian Hamilton Kelly's original was written for LaTeX
2.09, and needed to be updated to run with current LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crosswrd/crosswrd.sty
%doc %{_texmfdistdir}/doc/latex/crosswrd/README
%doc %{_texmfdistdir}/doc/latex/crosswrd/crosswrd.pdf
%doc %{_texmfdistdir}/doc/latex/crosswrd/grid0.tex
%doc %{_texmfdistdir}/doc/latex/crosswrd/grid1.tex
%doc %{_texmfdistdir}/doc/latex/crosswrd/grid2.tex
%doc %{_texmfdistdir}/doc/latex/crosswrd/test0.tex
%doc %{_texmfdistdir}/doc/latex/crosswrd/test1.tex
%doc %{_texmfdistdir}/doc/latex/crosswrd/test2.tex
#- source
%doc %{_texmfdistdir}/source/latex/crosswrd/crosswrd.dtx
%doc %{_texmfdistdir}/source/latex/crosswrd/crosswrd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
