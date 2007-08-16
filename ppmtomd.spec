Summary:	Driver for the Alps Micro-Dry printers and similars
Name:		ppmtomd
Version:	1.5
Release:	%mkrel 2
License:	GPL
Group:		System/Printing
URL:		http://www.stevens-bradfield.com/ppmtomd/
Source0:	http://www.stevens-bradfield.com/ppmtomd/ppmtomd-%{version}.tar.gz
Patch0:		ppmtomd-mdv_conf.diff
BuildRequires:	netpbm-devel
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

# fix attribs
chmod 644 *

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 ppmtomd %{buildroot}%{_bindir}/
install -m0644 ppmtomd.man %{buildroot}%{_mandir}/man1/ppmtomd.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE README
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
