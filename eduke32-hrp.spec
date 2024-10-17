Name:		eduke32-hrp
Version:	4.2.132
Release:	3
License:	Freeware
Summary:	Duke Nukem 3D High Resolution Pack
Group:		Games/Arcade
URL:		https://hrp.eduke4.net/
Source0:	http://www.duke4.org/files/nightfright/beta/polymer_hrp132.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	eduke32_engine >= 2.0.1

%description
For all Duke fans who want to play the game again 
in a modern Windows environment with 3D accelerated graphics,
the Duke3D community has created the High Resolution
Pack (HRP). Utilizing the amazing skills of various 
texturing and modelling artists, the project´s goal is to 
replace all textures and sprites with high-res versions,
optimizing it for latest OpenGL ports.


%prep
%setup -q -c %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/eduke32/autoload/
install -Dm 0644 %{SOURCE0} %{buildroot}%{_gamesdatadir}/eduke32/autoload/duke3d_hrp.zip


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_gamesdatadir}/eduke32/autoload/duke3d_hrp.zip
%doc hrp_art_license.txt hrp_readme.txt
