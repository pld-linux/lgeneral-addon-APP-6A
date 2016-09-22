# TODO:
# It overrides all pg files in gfx/terrain/pg,sounds/pg dirs and units/pg.udb file;
# either split lgeneral-data-pg to allow overriding by Obsoletes, or use new data name
# (e.g. pg-APP-6A) and symlink original pg data where not overridden; note: probably
# requires to edit some paths in .udb file (and maybe other?)
Summary:	LGeneral game - APP-6A mod for Panzer General data
Summary(pl.UTF-8):	Gra Linux General - modyfikacja APP-6A dla danych Panzer General
Name:		lgeneral-addon-APP-6A
Version:	1.2
Release:	0.1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/APP-6A.zip
# Source0-md5:	8ea6f92c64374b38b4f5cfa649cd48bd
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
Requires:	lgeneral-data-pg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains APP-6A mod for Panzer General data. It
tries to use the exact NATO (APP-6A) symbols and map style (replaces
original graphics).

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera modyfikacje APP-6A dla danych gry Panzer General.
Próbuje wykorzystywać dokładne symbole oraz styl map NATO (APP-6A),
zastępując oryginalną grafikę.

%prep
%setup -q -n APP-6A

# junk
%{__rm} gfx/terrain/pg/Thumbs.db
%{__rm} gfx/units/Thumbs.db

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a gfx sounds units $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
# overrides all pg files
%{_datadir}/lgeneral/gfx/terrain/pg/*.bmp
%{_datadir}/lgeneral/gfx/units/military.bmp
# overrides all pg files
%{_datadir}/lgeneral/sounds/pg/*.wav
# overrides pg file
%{_datadir}/lgeneral/units/pg.udb
