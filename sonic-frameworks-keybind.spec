%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksKeybind
%define devname %mklibname SonicFrameworksKeybind -d
#define git 20240217

Name: sonic-frameworks-keybind
Version: 6.28.0
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-frameworks-keybind
# %if 0%{?git:1}
# Source0: https://invent.kde.org/frameworks/kglobalaccel/-/archive/master/kglobalaccel-master.tar.bz2#/kglobalaccel-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: Global desktop keyboard shortcuts

License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries

BuildSystem:   cmake
BuildOption:   -DBUILD_QCH:BOOL=ON
BuildOption: 	-DBUILD_WITH_QT6:BOOL=ON
BuildOption: 	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
# Don't pull in plasma5
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

Conflicts:     kf6-kglobalaccel

%description
%summary

%package -n %{libname}
Summary: Global desktop keyboard shortcuts
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KF6GlobalAccel

%description -n %{libname}
%summary

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KF6GlobalAccel-devel

%description -n %{devname}
%summary

%install -a
%find_lang %{name} --all-name --with-qt --with-html
rm -rf %{buildroot}/%{_libdir}/cmake

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kglobalaccel.*
%{_datadir}/dbus-1/interfaces/kf6_*

%files -n %{devname}
%{_includedir}/KF6/KGlobalAccel

# pending rename
# %{_libdir}/cmake/KF6GlobalAccel

%files -n %{libname}
%{_libdir}/libKF6GlobalAccel.so*
