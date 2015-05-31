# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-dolphin-keyboard

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    harbour-dolphin-keyboard
Version:    1.2
Release:    0
Group:      Qt/Qt
License:    LICENSE
URL:        http://www.saberaltria.co.uk/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-dolphin-keyboard.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtdeclarative-import-folderlistmodel
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
harbour-dolphin-keyboard


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%post
systemctl-user restart lipstick.service

%files
%defattr(755,nemo,nemo,755)
%{_localstatedir}/lib/harbour-dolphin-keyboard/config/
%defattr(-,root,root,-)
%{_libdir}
%{_datadir}/maliit/plugins/com/jolla/dolphin/
%{_datadir}/maliit/plugins/com/jolla/layouts/
%{_datadir}/fonts/symbola/
%{_bindir}/harbour-dolphin-settings/
%{_datadir}/harbour-dolphin-settings/
%{_datadir}/applications/harbour-dolphin-settings.desktop
%{_datadir}/icons/hicolor/86x86/apps/harbour-dolphin-settings.png
# >> files
# << files