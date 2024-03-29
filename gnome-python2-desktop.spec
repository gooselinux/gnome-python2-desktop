%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Last updated for version 2.28.0
# The order here corresponds to that in configure.ac,
# for easier comparison.  Please do not alphabetize.
%define pygtk_version                   2.10.3
%define glib_version                    2.6.0
%define gtk_version                     2.4.0
%define gnome_python_version            2.10.0
%define gnome_panel_version             2.13.4
# Version not necessary for libgnomeprintui
%define gtksourceview_version           1:1.8.5-2
%define libwnck_version                 2.19.3
%define libgtop_version                 2.13.0
%define brasero_version                 0.9.0
%define gnome_media_version             2.10.0
%define gconf2_version                  2.10.0
%define metacity_version                2.21.5
%define librsvg2_version                2.13.93
%define gnome_keyring_version           0.5.0
%define gnome_desktop_version           2.10.0
%define totem_version                   1.4.0
%define eds_version                     1.4.0
%define bug_buddy_version               2.16.0
%define evince_version                  2.25

### Abstract ###

Name: gnome-python2-desktop
Version: 2.28.0
Release: 4%{?dist}.goose.2
License: GPLv2+
Group: Development/Languages
Summary: The sources for additional PyGNOME Python extension modules
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/2.28/gnome-python-desktop-%{version}.tar.bz2

### Dependencies ###

Requires: gnome-python2-canvas >= %{gnome_python_version}

### Build Dependencies ###

BuildRequires: brasero-devel >= %{brasero_version}
BuildRequires: bug-buddy >= %{bug_buddy_version}
BuildRequires: evince-devel >= %{evince_version}
BuildRequires: evolution-data-server-devel >= %{eds_version}
BuildRequires: glib2-devel >= %{glib_version}
BuildRequires: GConf2-devel >= %{gconf2_version}
BuildRequires: gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires: gnome-keyring-devel >= %{gnome_keyring_version}
BuildRequires: gnome-panel-devel >= %{gnome_panel_version}
BuildRequires: gnome-python2-bonobo >= %{gnome_python_version}
BuildRequires: gnome-python2-canvas >= %{gnome_python_version}
BuildRequires: gnome-python2-devel >= %{gnome_python_version}
BuildRequires: gnome-python2-gconf >= %{gnome_python_version}
BuildRequires: gtk2-devel >= %{gtk_version}
BuildRequires: gtksourceview-devel >= %{gtksourceview_version}
BuildRequires: libgnomeui-devel
BuildRequires: libgnomeprintui22-devel
BuildRequires: libgtop2-devel >= %{libgtop_version}
BuildRequires: librsvg2-devel >= %{librsvg2_version}
BuildRequires: libwnck-devel >= %{libwnck_version}
BuildRequires: metacity-devel >= %{metacity_version}
BuildRequires: pygtk2-devel >= %{pygtk_version}
BuildRequires: python-devel
BuildRequires: totem-pl-parser-devel >= %{totem_version}
BuildRequires: autoconf, libtool
%ifnarch s390 s390x
BuildRequires: gnome-media-devel >= %{gnome_media_version}
%endif

%description
The gnome-python-desktop package contains the source packages for additional 
Python bindings for GNOME. It should be used together with gnome-python.

%package -n gnome-python2-applet
Summary: Python bindings for GNOME Panel applets.
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
# applets from GNOME 1.4 are no longer supported - we only have 1 panel
Obsoletes: pygnome-applet <= 1.4.2
Requires: gnome-python2-bonobo
Requires: gnome-python2-gnome

%description -n gnome-python2-applet
This module contains a wrapper that allows GNOME Panel applets to be
written in Python.

# The obsoletes here is questionable but apparently necessary to
# ensure gnome-python2-nautilus-cd-burner is removed on upgrades.
%package -n gnome-python2-brasero
Summary: Python bindings for interacting with brasero
License: LGPLv2
Group: Development/Languages
Obsoletes: gnome-python2-nautilus-cd-burner <= 2.26.0
Requires: %{name} = %{version}-%{release}
Requires: brasero-libs >= %{brasero_version}

%description -n gnome-python2-brasero
This module contains a wrapper that allows the use of brasero via Python.

%package -n gnome-python2-bugbuddy
Summary: Python bindings for interacting with bug-buddy
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: bug-buddy >= %{bug_buddy_version}

%description -n gnome-python2-bugbuddy
This module contains a wrapper that allows the use of bug-buddy via
Python.

%package -n gnome-python2-evince
Summary: Python bindings for interacting with evince
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: evince-libs >= %{evince_version}

%description -n gnome-python2-evince
This module contains a wrapper that allows the use of evince via Python.

%package -n gnome-python2-evolution
Summary: Python bindings for interacting with evolution-data-server
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: evolution-data-server >= %{eds_version}
Provides: evolution-python = %{version}-%{release}
Obsoletes: evolution-python <= 0.0.4-3

%description -n gnome-python2-evolution
This module contains a wrapper that allows the use of evolution-data-server
via Python.

%package -n gnome-python2-gnomeprint
Summary: Python bindings for interacting with libgnomeprint
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: libgnomeprint22
Requires: libgnomeprintui22
Requires: gnome-python2-canvas

%description -n gnome-python2-gnomeprint
This module contains a wrapper that allows the use of libgnomeprint via
Python.

%package -n gnome-python2-gtksourceview
Summary: Python bindings for interacting with the gtksourceview library 
License: GPLv2+
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: gtksourceview >= %{gtksourceview_version}
Requires: gnome-python2-gnomeprint

%description -n gnome-python2-gtksourceview
This module contains a wrapper that allows the use of gtksourceview via
Python.

%package -n gnome-python2-libwnck
Summary: Python bindings for interacting with libwnck
License: LGPLv2
Group: Development/Languages
Requires: libwnck >= %{libwnck_version}

%description -n gnome-python2-libwnck
This module contains a wrapper that allows the use of libwnck via
Python.

%package -n gnome-python2-libgtop2
Summary: Python bindings for interacting with libgtop
License: GPLv2+
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: libgtop2 >= %{libgtop_version}

%description -n gnome-python2-libgtop2
This module contains a wrapper that allows the use of libgtop via
Python.

%package -n gnome-python2-metacity
Summary: Python bindings for interacting with metacity
License: GPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: metacity >= %{metacity_version}

%description -n gnome-python2-metacity
This module contains a wrapper that allows the use of metacity 
via Python.

%package -n gnome-python2-totem
Summary: Python bindings for interacting with totem
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: totem-pl-parser >= %{totem_version}
Requires: gnome-python2-gconf

%description -n gnome-python2-totem
This module contains a wrapper that allows the use of totem
via Python.

%package -n gnome-python2-rsvg
Summary: Python bindings for interacting with librsvg
License: LGPLv2
Group: Development/Languages
Requires: librsvg2 >= %{librsvg2_version}

%description -n gnome-python2-rsvg
This module contains a wrapper that allows the use of librsvg
via Python.

%package -n gnome-python2-gnomedesktop
Summary: Python bindings for interacting with gnome-desktop
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: gnome-desktop >= %{gnome_desktop_version}

%description -n gnome-python2-gnomedesktop
This module contains a wrapper that allows the use of gnome-desktop
via Python.

%package -n gnome-python2-gnomekeyring
Summary: Python bindings for interacting with gnome-keyring
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: gnome-keyring >= %{gnome_keyring_version}

%description -n gnome-python2-gnomekeyring
This module contains a wrapper that allows the use of gnome-keyring
via Python.

%prep
%setup -q -n gnome-python-desktop-%{version}

%build
autoreconf -f -i
%configure --enable-metacity
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

rm -rf $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/gksu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README COPYING COPYING.GPL COPYING.LGPL
%{_libdir}/pkgconfig/gnome-python-desktop-2.0.pc
%{_datadir}/pygtk

%files -n gnome-python2-applet
%defattr(-,root,root,-)
%dir %{python_sitearch}/gtk-2.0/gnome/applet.*
%{python_sitearch}/gtk-2.0/gnomeapplet.so

%files -n gnome-python2-brasero
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/braseroburn.so
%{python_sitearch}/gtk-2.0/braseromedia.so

%files -n gnome-python2-bugbuddy
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/bugbuddy.py*

%files -n gnome-python2-evince
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/evince.so

%files -n gnome-python2-evolution
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/evolution/

%files -n gnome-python2-gnomeprint
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gnomeprint/
%{_datadir}/gtk-doc/html/pygnomeprint
%{_datadir}/gtk-doc/html/pygnomeprintui
%defattr(644,root,root,755)
%doc ../gnome-python-desktop-%{version}/examples/gnomeprint/*

%files -n gnome-python2-gtksourceview
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gtksourceview.so
%{_datadir}/gtk-doc/html/pygtksourceview
%defattr(644,root,root,755)
%doc ../gnome-python-desktop-%{version}/examples/gtksourceview/*

%files -n gnome-python2-libwnck
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/wnck.so

%files -n gnome-python2-libgtop2
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gtop.so

%files -n gnome-python2-metacity
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/metacity.so

%files -n gnome-python2-totem
%defattr(-,root,root,-)
%ifnarch s390 s390x
%{python_sitearch}/gtk-2.0/mediaprofiles.so
%endif
%{python_sitearch}/gtk-2.0/totem

%files -n gnome-python2-rsvg
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/rsvg.so

%files -n gnome-python2-gnomedesktop
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gnomedesktop

%files -n gnome-python2-gnomekeyring
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/gnomekeyring.so

%changelog
* Fri Dec 30 2011 Clint Savage <herlo@gooseproject.org> - 2.28.0-4.goose.2
- GoOSe Koji rebuild

* Fri Dec 30 2011 Clint Savage <herlo@gooseproject.org> - 2.28.0-4.goose.1
- Rebuilding in mock to bootstrap for recursive deps

* Thu Jan 14 2010 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-4.el6
- Fix rpmlint warnings.

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-3.fc12
- Provide a complete URI for the Source field.

* Fri Nov 13 2009 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-2.fc12
- gnome-python2-nautilus-cd-burner obsoleted by gnome-python2-brasero,
  sort of (RH bug #536757).

* Mon Sep 21 2009 Matthew Barnes <mbarnes@redhat.com> - 2.28.0-1.fc12
- Update to 2.28.0

* Wed Sep 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.3-1.fc12
- Update to 2.27.3

* Sun Aug 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.2-3.fc12
- Disable nautilus-cd-burner bindings.  Package is dead.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.2-1.fc12
- Update to 2.27.2

* Tue Jun 02 2009 Peter Robinson <pbrobinson@gmail.com> - 2.27.1-2.fc12
- Change gnome-python2-evince to depend on evince-libs

* Sun May 03 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.1-1.fc12
- Update to 2.27.1
- New subpackage: gnome-python2-brasero

* Fri Apr 24 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-3
- Removed cd-burner subpackage Require on nautilus-cd-burn

* Wed Apr 22 2009 Matthew Barnes <mbarnes@redhat.com> - 2.26.0-2.fc11
- Rebuild against newer libnautilus-burn.

* Sat Mar 14 2009 Matthew Barnes <mbarnes@redhat.com> - 2.26.0-1.fc11
- Update to 2.26.0

* Fri Mar 13 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.91-3.fc11
- Evince subpackage should depend on evince, not evince-devel (RH bug #490112).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.91-1.fc11
- Update to 2.25.91

* Wed Feb 04 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.90-2.fc11
- New subpackage: gnome-python2-evince

* Sun Feb 01 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.90-1.fc11
- Update to 2.25.90

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.1-1.fc11
- Update to 2.25.1
- Remove patch for GNOME bug #564525 (fixed upstream).

* Tue Dec 23 2008 Caolán McNamara <caolanm@redhat.com> - 2.24.1-2.fc11
- make build

* Fri Dec 19 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.1-1.fc11
- Update to 2.24.1
- Add patch for GNOME bug #564525 (build failure).

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0-6
- Rebuild for new libgnome-desktop

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.24.0-5
- Rebuild for Python 2.6

* Fri Nov 14 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-4.fc11
- Update subpackage requirements, since gnome-python2 no longer drags in
  the world.

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-3
- Rebuild

* Sun Sep 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-2.fc10
- Change gnome-python2 requirement to gnome-python2-canvas.

* Sun Sep 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-1.fc10
- Update to 2.24.0

* Sun Aug 31 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-1.fc10
- Update to 2.23.1
- Update version requirements.

* Mon Jun 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.0-1.fc10
- Update to 2.23.0

* Wed Jun 11 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-6.fc10
- Don't drag in devel packages when installing gnome-python2-evolution
  (RH bug #450932).

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-5
- Rebuild

* Tue May 13 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-4.fc10
- Rebuild against newer libedataserver and libtotem-plparser.

* Tue Apr 29 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-3.fc10
- gnome-python2-evolution obsoletes evolution-python (RH bug #444263).

* Sat Mar 15 2008 Christopher Aillon <caillon@redhat.com> - 2.22.0-2
- Bring gnome-python2-nautilus-cd-burner back to ppc and ppc64

* Sun Mar 09 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-1.fc9
- Update to 2.22.0
- Exclude gnome-python2-nautilus-cd-burner from ppc and ppc64.

* Sat Feb 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.3-1.fc9
- Update to 2.21.3

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.2-2.fc9
- Rebuild with GCC 4.3

* Mon Jan 14 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.2-1.fc9
- Update to 2.21.2

* Sun Dec 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.21.1-1.fc9
- Update to 2.21.1
- New subpackage: gnome-python2-evolution
- Change totem-devel BR to totem-pl-parser-devel.

* Mon Nov 12 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-2.fc9
- Rebuild against newer libtotem-plparser.so.

* Sun Sep 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-1.fc8
- Update to 2.20.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.19.2-4
- Rebuild for selinux ppc32 issue.

* Thu Aug 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.2-3.fc8
- Rebuild

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-2
- Update license fields

* Mon Jul 30 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.2-1.fc8
- Update to 2.19.2

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-2
- Rebuild against gtksourceview 

* Sat Jul 07 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.1-1
- Update to 2.19.1
- Update versions of required packages.
- Remove patch for GNOME bug #428697 (fixed upstream).

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-4
- Rebuild again

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-3
- Rebuild against new libwnck

* Sun Jun 03 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.0-2.fc8
- Require metacity-devel, not metacity, for building.
- Add patch for GNOME bug #428697 (adapt to API change).

* Mon Mar 12 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.0-1.fc7
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.93-1
- Update to 2.17.93

* Sun Feb 25 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.92-1.fc7
- Update to 2.17.92
- Remove patch for GNOME bug #401760 (fixed upstream).

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.3-3.fc7
- Add patch for GNOME bug #401760 (plparser fails to build).

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.3-2.fc7
- Rename spec file to gnome-python2-desktop.spec (RH bug #225832).

* Mon Jan 08 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.3-1
- Update to 2.17.3

* Sun Jan 07 2007 Matthew Barnes <mbarnes@redhat.com> - 2.17.2-1
- Update to 2.17.2
- New gnome-python2-bugbuddy subpackage.
- Update version requirements to match configure.ac.
- Use python_sitearch macro for installing libraries.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.17.1-2
- rebuild for python 2.5
- BR gnome-python2-devel

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Tue Aug 22 2006 Dan Williams <dcbw@redhat.com> - 2.15.90-2.fc6
- Remove unecessary dependencies on gnome-python2-desktop from
    -libwnck and -rsvg subpackages (OLPC)

* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.90-1.fc6
- Update to 2.15.90

* Thu Jul 20 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-2
- Rebuild against dbus

* Thu Jul 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-1
- Update to 2.15.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-4.1
- rebuild

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-4
- Create gnomekeyring subpackage
- block out the nautilus-cd stuff

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-2
- Bump for new nautilus-cd-burner

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Tue May 30 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1
- Update to 2.15.2
- Add subpackages gnome-python2-rsvg and gnome-python2-gnomedesktop

* Wed May 24 2006 John (J5) Palmieri <johnp@redhat.com> - 2.14.0-2
- Add pygtk2 BR

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.de> 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.13.3-2
- Buildrequires: python-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.3-1.1
- bump again for double-long bug on ppc(64)

* Mon Feb  6 2006 John (J5) Palmieri <johnp@redhat.com> - 2.13.3-1
- Initial build.

