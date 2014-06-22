Summary: sme server system monitor
%define name smeserver-system_monitor
Name: %{name}
%define version 1.1
%define release 2%{?dist}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Service
Source: %{name}-%{version}.tar.gz
Packager: Michel Van hees <michel@vanhees.cc>
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: smeserver-release >= 8, sysstat >= 5, rrdtool, perl-rrdtool
AutoReqProv: no

%changelog
* Fri Mar 12 2010 Federico Simoncelli <federico@nethesis.it> - 1.1-2
- Replace sar with sadf (sme8)
 
* Sun May 11 2008 Pascal Schrrims <webmaster@schrrims.net>
- 1.1-1
- Adapt for rrdtool 1.2

* Mon Mar 31 2008 Michel Van hees <michel@vanhees.cc>
- 1.0-1
- Fork from sysmon

* Sun Feb 17 2008 Michel Van hees <michel@vanhees.cc>
- 6.0-2
- Restriction on rrdtools version

* Tue Feb 14 2008 Michel Van hees <michel@vanhees.cc>
- 6.0-1
- Add multi HD graph
- Add debug message on service to help debug

* Tue Feb 05 2008 Michel Van hees <michel@vanhees.cc>
- 5.1.3
- Fix several bug in daemon file

* Mon Feb 04 2008 Michel Van hees <michel@vanhees.cc>
- 5.1.2
- Fix bug in server-manager naviguation

* Mon Feb 04 2008 Michel Van hees <michel@vanhees.cc>
- 5.1.1
- Add number of user connected using samba

* Thu Oct 25 2007 Michel Van hees <michel@vanhees.cc>
- Fix a bug with different language

* Mon Jul 24 2006 Michel Van hees <michel@vanhees.cc>
- 5.0.3
- Multi cpu graph display

* Fri Jul 14 2006 Michel Van hees <michel@vanhees.cc>
- 5.0.2
- Disk size bug correction

* Sat Jul 08 2006 Michel Van hees <michel@vanhees.cc>
- 5.0-1
- adapt to sme server version 7

* Fri Apr 11 2003 Shad L. Lords <slords@mail.com>
- 4.1-1
- changed rrd file layout to include max/min/avg
- added support for nutups logging
- changed graphs to use all functions
- removed sysmon conversion from v2.0

* Thu Apr 10 2003 Shad L. Lords <slords@mail.com>
- 4.0-9
- fixed gateway to find default gateway only

* Wed Jan 22 2003 Shad L. Lords <slords@mail.com>
- 4.0-8
- fixed decimal point (accept . or ,)
- updated sensors to accept numbers without decimals

* Fri Jan  3 2003 Shad L. Lords <slords@mail.com>
- 4.0-7
- need of code police again (!= not same as ne).  Thanks Craig Foster.

* Fri Jan  3 2003 Shad L. Lords <slords@mail.com>
- 4.0-6
- more updates for sensors
- don't save sensors or ups if no data found
- timeout ping after (interval*count+2) (7) seconds (hang bug)

* Wed Jan  1 2003 Shad L. Lords <slords@mail.com>
- 4.0-5
- more updates for sensors

* Tue Dec 31 2002 Shad L. Lords <slords@mail.com>
- 4.0-4
- added swap to memory graph

* Tue Dec 31 2002 Shad L. Lords <slords@mail.com>
- 4.0-3
- updated sensors to pull more combinations

* Tue Dec 31  2002 Shad L. Lords <slords@mail.com>
- 4.0-2
- update ups headers to not wrap

* Mon Dec 30 2002 Shad L. Lords <slords@mail.com>
- 4.0-1
- updated graph formats (more condensed, no percentages)
- added new CPU graph (with support for individual CPU's)
- changed format of memory graph (more detail)
- added sensors graphs (temperature, voltage, fans)
- added apcupsd graphs (ups, ups-2)
- changed format of harddrive graph (stacked, old one still there as MEM2)

* Sun Dec 29 2002 Shad L. Lords <slords@mail.com>
- 3.5-1
- added integration with apcupsd (collection)
- added integration with lm_sensors (collection)
- added new system/user/nice CPU graph (manual)

* Fri Dec 13 2002 Shad L. Lords <slords@mail.com>
- 3.1-3
- fixed hard drive space detection for all devices
- made hard drive space more accurate

* Fri Dec 13 2002 Shad L. Lords <slords@mail.com>
- 3.1-2
- changed name to e-smith-sysmon
- fixed hard drive space detection for software raid

* Wed Aug 21 2002 Shad L. Lords <slords@mail.com>
- 3.1-1
- corrected bug to work with newer version of ping
- update routines to work better with v5.5 and v5.6alpha

* Sun Aug  4 2002 Shad L. Lords <slords@mail.com>
- 3.0-16
- Changed spec file to just require rrdtool and not a specific version
- Changed graphing code to work with newer version of rrdtool
- Added stats for each seperate CPU and hard drive (no graphs yet)

* Mon Mar 25 2002 Shad L. Lords <slords@mail.com>
- 3.0-15
- Fixed bug in daemonizing code to allow ip addresses.
- Fixed bug in service code to remove lockfile if dead.

* Tue Mar 19 2002 Shad L. Lords <slords@mail.com>
- 3.0-14
- Included labels in links for both graph pages

* Fri Mar 15 2002 Juan J. Prieto
- 3.0-13
- Minor change in spec file (Group)

* Thu Mar  7 2002 Shad L. Lords <slords@mail.com>
- 3.0-12
- Daemonized pinging routine and adjusted timing for pings.

* Sat Mar  2 2002 Shad L. Lords <slords@mail.com>
- 3.0-11
- Fixed bug in untainting code to allow '.' for hosts.

* Sat Mar  2 2002 Shad L. Lords <slords@mail.com>
- 3.0-10
- Added scaling to sysmonconv for more accurate conversion.
- Added data to DS:MAX for sysmonconv so max values show up.
- Adjusted runtime for sysmon so falls on 0 secs.
- Fixed bug with empty $badifaces in sysmon and sysmonconv.

* Fri Mar  1 2002 Shad L. Lords <slords@mail.com>
- 3.0-09
- Fixed bug in sysmonconv if no old database exists.

* Fri Mar  1 2002 Shad L. Lords <slords@mail.com>
- 3.0-08
- Fixed sysmonconv script to convert all old databases.
- Fixed sysmonconv to run faster.
- Added sysmonconv to %post script.

* Thu Feb 28 2002 Shad L. Lords <slords@mail.com>
- 3.0-07
- Added user, nice, system cpu time to database.
- Added sysmonconv script to convert eth,ppp interfaces to new format.

* Thu Feb 28 2002 Shad L. Lords <slords@mail.com>
- 3.0-06
- Fixed more problems in RPM spec file.
- Renamed sysmonitor to sysmon so as not to conflict with e-smith-monitor.

* Thu Feb 28 2002 Shad L. Lords <slords@mail.com>
- 3.0-05
- Fixed problems in RPM spec file.
- Added Obsoletes for old e-smith-monitor package

* Thu Feb 28 2002 Shad L. Lords <slords@mail.com>
- 3.0-04
- Changed webmonitor to sysmon in web/functions.
- Changed copyright footer notice to reflect Mitel's standard.
- Fixed problem with old packages not uninstalling.

* Wed Feb 27 2002 Shad L. Lords <slords@mail.com>
- 3.0-03
- Changed gather script to be daemon instead of cronjob.
- Changed gather script to use perl module instead of executable.

* Wed Feb 27 2002 Juan J. Prieto <jjptapia@eresmas.com>
- 3.0-02
- Now the web panel runs with the Taint and warnings up (-wT). Secure mode!.
- Conflicts bug fixed in the spec (e-smith-monitor only).
- The copyright is licensed under GPL.

* Mon Feb 25 2002 Shad L. Lords <slords@mail.com>
- 3.0-01
- initial release.  Completely rewriten Monitor.

%description
System monitor for SME Server version 7

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
if [ $1 -ge 2 ] ; then
    mkdir -p /var/lib/rrdsm/backup
    /bin/mv /var/lib/rrdsm/*.rrd /var/lib/rrdsm/backup/
    /bin/rm -f /var/lib/rrdsm/*.rrd
fi

%preun

%post
/sbin/e-smith/db configuration set systemmonitor service status enabled debug release
/sbin/e-smith/signal-event conf-systemmonitor
/usr/bin/killall systemmonitor > /dev/null 2>&1
/usr/sbin/systemmonitor > /dev/null 2>&1
/etc/e-smith/events/actions/navigation-conf >/dev/null 2>&1
cat << DONE

* All rrd file have been backuped in /var/lib/rrdsm/backup/
    
DONE

%postun
/etc/e-smith/events/actions/navigation-conf >/dev/null 2>&1
if ! [[ -e /usr/sbin/systemmonitor ]]; then
    /usr/bin/killall systemmonitor > /dev/null 2>&1;
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
