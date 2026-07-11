%global tl_name svrsymbols
%global tl_revision 50019

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0b
Release:	%{tl_revision}.1
Summary:	A font with symbols for use in physics texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/svrsymbols
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svrsymbols.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The svrsymbols package is a LaTeX interface to the SVRsymbols font. The
glyphs of this font are ideograms that have been designed for use in
physics texts. Some symbols are standard and some are entirely new.

