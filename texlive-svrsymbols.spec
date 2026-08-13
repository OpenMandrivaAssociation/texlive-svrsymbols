%global tl_name svrsymbols
%global tl_revision 50019
%global tl_version 2.0b

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The svrsymbols package is a LaTeX interface to the SVRsymbols font. The
glyphs of this font are ideograms that have been designed for use in
physics texts. Some symbols are standard and some are entirely new.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from svrsymbols:
Map svrsymbols.map
TL_DROPIN_EOF
