#!/usr/bin/env python2

DESCRIPTION = """\
rpm2sysvpkg is a tool for converting RPM packages to SystemV (Sun
Solaris) packages.
"""

from distutils.core import setup

setup (name = "rpm2sysvpkg",
       version = "0.1",
       license = "GPL",
       description = "converts RPMs to Solaris packages",
       long_description = DESCRIPTION,
       author = "Peter Astrand",
       author_email = "peter@cendio.se",
       url = "http://freshmeat.net/projects/rpm2sysvpkg/",
       py_modules = [],
       data_files=[('/usr/bin', ['rpm2sysvpkg', 'pkgtrans'])]
       )
