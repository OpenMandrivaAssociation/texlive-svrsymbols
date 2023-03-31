Name:		texlive-svrsymbols
Version:	50019
Release:	2
Summary:	A font with symbols for use in physics texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svrsymbols
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The svrsymbols package is a LaTeX interface to the SVRsymbols
font. The glyphs of this font are ideograms that have been
designed for use in physics texts. Some symbols are standard
and some are entirely new.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/svrsymbols
%{_texmfdistdir}/tex/latex/svrsymbols
%{_texmfdistdir}/fonts/type1/public/svrsymbols
%{_texmfdistdir}/fonts/tfm/public/svrsymbols
%{_texmfdistdir}/fonts/opentype/public/svrsymbols
%{_texmfdistdir}/fonts/map/dvips/svrsymbols
%{_texmfdistdir}/fonts/afm/public/svrsymbols
%doc %{_texmfdistdir}/doc/fonts/svrsymbols

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
