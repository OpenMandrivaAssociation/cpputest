
%define _disable_ld_no_undefined 1

Name:           cpputest
Version:        4.0
Release:        1
Summary:        Unit testing and mocking framework for C/C++
 
License:        BSD
URL:            https://cpputest.github.io/
Source0:        https://github.com/cpputest/cpputest/releases/download/v%{version}/%{name}-%{version}.tar.gz
# compile the extension library as a shared library
Patch0:         %%{name}-no-static-ext.patch
# fix installation location of cmake files
Patch1:         %{name}-fix-cmake-dest.patch
 
BuildRequires:  cmake
 
%global _description %{expand:
CppUTest is a C/C++ based unit xUnit test framework for unit testing and for
test-driving your code. It is written in C++ but is used in C and C++ projects
and frequently used in embedded systems but it works for any C/C++ project.
 
CppUTestâ€™s core design principles are:
- Simple in design and simple in use.
- Portable to old and new platforms.
- Build with Test-driven Development for Test-driven Developers.}
 
%description    %{_description}
 
 
%package        devel
Summary:        Development files for %{name}
 
%description    devel %{_description}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
 
%prep
%autosetup -p1
 
 
%build
%cmake   \
         -DCPPUTEST_TEST_DISCOVERY=OFF
%make_build
 
%install
%make_install -C build

%files devel
%license COPYING
%doc README.md README_CppUTest_for_C.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/CppUTest
%{_libdir}/pkgconfig/cpputest.pc
