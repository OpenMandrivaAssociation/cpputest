%global debug_package %{nil}

Name:           cpputest
Version:        4.0
Release:        1
Summary:        Unit testing and mocking framework for C/C++

License:        BSD-3-Clause
Group:          Development/Tools
URL:            https://cpputest.github.io/
Source0:        https://github.com/cpputest/cpputest/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Ensure that libCppUTest is built as static
Patch0:         %{name}-static.patch
# fix installation location of cmake files
Patch1:         %{name}-fix-cmake-dest.patch

BuildSystem:    cmake

%description
CppUTest is a C/C++ based unit xUnit test framework for unit testing and for
test-driving your code. It is written in C++ but is used in C and C++ projects
and frequently used in embedded systems but it works for any C/C++ project.

CppUTest's core design principles are:
- Simple in design and simple in use.
- Portable to old and new platforms.
- Build with Test-driven Development for Test-driven Developers.




%package        devel
Summary:        Development files for %{name}
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%files devel
%license COPYING
%doc README.md README_CppUTest_for_C.txt
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/cmake/CppUTest
%{_libdir}/pkgconfig/cpputest.pc

