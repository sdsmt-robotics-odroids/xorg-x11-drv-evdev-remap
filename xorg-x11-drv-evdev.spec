%define tarball xf86-input-evdev
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/input

%define gitdate 20081013

Summary:    Xorg X11 evdev input driver
Name:	    xorg-x11-drv-evdev
Version:    2.1.0
Release:    2%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
#Source0:    %{tarball}-%{gitdate}.tar.bz2
#Source1:    make-git-snapshot.sh

ExcludeArch: s390 s390x

BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6
BuildRequires: libxkbfile-devel

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6
Requires:  xkeyboard-config >= 1.4-1

%description 
X.Org X11 evdev input driver.

%prep
#%setup -q -n %{tarball}-%{gitdate}
%setup -q -n %{tarball}-%{version}

# apply patches

%build
autoreconf -v --install || exit 1
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


%package devel
Summary:    Xorg X11 evdev input driver development package.
Group:	    Development/Libraries
%description devel
X.Org X11 evdev input driver development files.

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xorg-evdev.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/evdev-properties.h


%changelog
* Mon Dec 22 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.1.0-2
- Rebuild for server 1.6.

* Wed Nov 19 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.1.0-1
- evdev 2.1.0

* Tue Nov 4 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.99.3-1
- evdev 2.0.99.3 (evdev 2.1 RC 3)

* Fri Oct 24 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.99.2-1
- evdev 2.0.99.2 (evdev 2.1 RC 2)

* Fri Oct 17 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.99.1-1
- evdev 2.0.99.1 (evdev 2.1 RC 1)
- Upstream change now requires libxkbfile-devel to build.

* Mon Oct 13 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.99-1
- Today's git snapshot.
- Require xkeyboard-config 1.4 and higher for evdev ruleset.
- Provide devel subpackage for evdev header files.

* Fri Oct 3 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.6-1
- update to 2.0.6
- remove patches merged upstream.

* Fri Sep 12 2008 Adam Jackson <ajax@redhat.com> 2.0.4-3
- evdev-2.0.4-reopen-device.patch: When arming the reopen timer, stash it in
  the driver private, and explicitly cancel it if the server decides to
  close the device for real.
- evdev-2.0.4-cache-info.patch: Rebase to account for same.

* Thu Aug 28 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.4-2
- evdev-2.0.4-reopen-device.patch: try to reopen devices if a read error
  occurs on the fd.
- evdev-2.0.4-cache-info.patch: cache device info to ensure reopened device
  isn't different to previous one.

* Mon Aug 25 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.4-1
- evdev 2.0.4

* Fri Aug 1 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.3-1
- evdev 2.0.3

* Mon Jul 21 2008 Peter Hutterer <peter.hutterer@redhat.com> 2.0.2-1
- evdev 2.0.2

* Fri Mar 14 2008 Adam Jackson <ajax@redhat.com> 1.99.1-0.5
- Today's snapshot.  Maps REL_DIAL to REL_HWHEEL.

* Wed Mar 12 2008 Adam Jackson <ajax@redhat.com> 1.99.1-0.4
- Today's snapshot.  Fixes mouse button repeat bug, and therefore Apple
  Mighty Mice are usable.  Props to jkeating for the hardware.

* Tue Mar 11 2008 Adam Jackson <ajax@redhat.com> 1.99.1-0.3
- Today's snapshot.  Fixes right/middle button swap hilarity.

* Mon Mar 10 2008 Adam Jackson <ajax@redhat.com> 1.99.1-0.2
- Updated snapshot, minor bug fixes.

* Fri Mar 07 2008 Adam Jackson <ajax@redhat.com> 1.99.1-0.1
- evdev 2.0 git snapshot

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-2
- Autorebuild for GCC 4.3

* Tue Nov 27 2007 Adam Jackson <ajax@redhat.com> 1.2.0-1
- xf86-input-evdev 1.2.0

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.2-5
- Rebuild for PPC toolchain bug

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
