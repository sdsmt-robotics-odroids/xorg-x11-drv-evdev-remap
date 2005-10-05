%define tarball xf86-input-evdev
# All packages should own all dirs they lead up to, for saner
# rpm packaging, in particular if the leading dirs are not owned by
# the "filesystem" package.
%define moduledir %(pkg-config xorg-server --variable=moduledir )
# define driverdir to the appropriate type for this driver class
%define driverdir %(pkg-config xorg-server --variable=inputdir )

%define cvsdate xxxxxxx

Summary:   Xorg X11 evdev input driver
Name:      xorg-x11-drv-evdev
Version:   1.0.0
Release:   0
URL:       http://www.x.org
# FIXME: If using a CVS version, uncomment the second Source0 line and use
# it instead.
Source0:   http://xorg.freedesktop.org/X11R7.0-RC0/driver/%{tarball}-%{version}.tar.bz2
#Source0:   http://xorg.freedesktop.org/X11R7.0-RC0/driver/%{tarball}-%{version}-%{cvsdate}.tar.bz2
License:   MIT/X11
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# FIXME:  If you can see this comment, then the ExclusiveArch entry below
# is set to the spec file template default.  Please examine the monolithic
# xorg-x11 package for each architecture for this driver, to determine which
# architectures it should be built or not built on, and update the list
# below.  When doing this, take "sparc, sparc64, alpha" also into
# consideration if you know a given driver was built for those arches in
# the past.  That makes it easier for the community Alphacore/AuroraLinux
# projects to rebuild our rpm packages.  If you're not sure if a given
# driver should be on any of those arches however, just leave it out of
# the list, and the community can let us know which drivers they are
# missing.  Remove this comment once the ExclusiveArch line is updated and
# considered reliable/correct.
ExclusiveArch: %{ix86} x86_64 ia64 ppc

BuildRequires: pkgconfig
BuildRequires: xorg-x11-server-sdk

Requires:  xorg-x11-server-Xorg
%description 
X.Org X11 evdev input driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
# FIXME: This should be using makeinstall macro instead.  Please test
# makeinstall with this driver, and if it works, check it into CVS. If
# it fails, fix it in upstream sources and file a patch upstream.
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT%{moduledir} -name '*.la' | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{moduledir}
%dir %{driverdir}
# FIXME: A glob is used here in the specfile template to make it easy to
# generate spec files automatically.  When everything is in CVS, if you're
# updating the spec file, please change the glob to a list of explicit
# filenames, so that rpm tracks individual files, and we know when a new
# one gets added.  Explicitly naming files also helps avoid random
# unexpected .so files (or others) from getting included in a shipping
# product.  Ditto for the manpages.
%{driverdir}/*.so
# NOTE: Uncomment these if someone ever writes manpages for this driver
#%dir %{_mandir}
#%dir %{_mandir}/man4
#%{_mandir}/man4/*.4*

%changelog
* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for evdev input driver generated automatically
  by my xorg-driverspecgen script.
