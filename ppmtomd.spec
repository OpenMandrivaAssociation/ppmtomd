Summary:	Driver for the Alps Micro-Dry printers and similars
Name:		ppmtomd
Version:	1.6
Release:	6
License:	GPL
Group:		System/Printing
URL:		http://www.stevens-bradfield.com/ppmtomd/
Source0:	http://www.stevens-bradfield.com/ppmtomd/%{name}-%{version}.tar.gz
Patch0:		ppmtomd-mdv_conf.diff
Patch1:		ppmtomd-1.5-LDFLAGS.diff
Patch2:		ppmtomd-1.6-mdv-fix-netpbm-includes.patch
BuildRequires:	netpbm-devel

%description
A program to convert images from PPM format into the control language for the
Alps Micro-Dry printers, at various times sold by Citizen, Alps and Okidata.

This program drives the Alps Micro-Dry series of printers, including the
Citizen Printiva series, Alps MD series, and Oki DP series (but not yet the
DP-7000).

In the current release, the program drives the standard mode fairly well; the
dye sublimation mode very well; and the VPhoto mode reasonably well.

It supports all the colours available up to the DP-5000, including the foil
colours.

%prep

%setup -q
%patch0 -p0
%patch1 -p0
%if %{mdkversion} >= 201010
%patch2 -p1
%endif

# fix attribs
chmod 644 *

%build

%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 ppmtomd %{buildroot}%{_bindir}/
install -m0644 ppmtomd.man %{buildroot}%{_mandir}/man1/ppmtomd.1

%clean

%files
%doc LICENCE README
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5-10mdv2011.0
+ Revision: 667818
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-9mdv2011.0
+ Revision: 607202
- rebuild

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 1.5-8mdv2010.1
+ Revision: 493082
- fix netpbm includes for mdkversion >= 201010

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5-7mdv2010.0
+ Revision: 426777
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-6mdv2009.1
+ Revision: 319083
- use %%ldflags (P2)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2009.0
+ Revision: 225044
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-4mdv2008.1
+ Revision: 179258
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-3mdv2008.0
+ Revision: 75357
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdv2008.0
+ Revision: 64176
- use the new System/Printing RPM GROUP

* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2008.0
+ Revision: 63033
- Import ppmtomd



* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2008.0
- initial Mandriva package

* Tue May 18 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-05-18 14:53:56 (60727)
- New upstream: 1.3  Fixes not yet supported options for Alps-MD-5000
- Minor specfile cleanup.

* Wed Jan 14 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-01-14 16:13:22 (44644)
- New upstream: 1.1
- Added missing BuildRequires

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:55:09 (9512)
- Imported package from 8.0.

