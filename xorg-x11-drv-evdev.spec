# Note to self: don't update to 1.1.5 until we have an input-hotplug server.

%define tarball xf86-input-evdev
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/input

Summary:   Xorg X11 evdev input driver
Name:      xorg-x11-drv-evdev
Version: 1.1.2
Release: 4%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

Patch0: evdev-1.1.2-cvs-20060605.patch

%description 
X.Org X11 evdev input driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p0 -b .cvs-20060605

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/evdev_drv.so
%{_mandir}/man4/evdev.4*

%changelog
* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.2-4
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.1.2-3
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue Jun 13 2006 Adam Jackson <ajackson@redhat.com> 1.1.2-2
- Build on ppc64

* Mon Jun 05 2006 Adam Jackson <ajackson@redhat.com> 1.1.2-1
- Update to 1.1.2 + CVS fixes.

* Mon Apr 10 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-3
- Work around header pollution on ia64, re-add to arch list.

* Mon Apr 10 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-2
- Disable on ia64 until build issues are sorted.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-evdev to version 1.0.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-evdev to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-evdev to version 1.0.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-evdev to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for evdev input driver generated automatically
  by my xorg-driverspecgen script.
