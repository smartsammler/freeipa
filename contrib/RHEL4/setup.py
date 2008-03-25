#!/usr/bin/env python
# Copyright (C) 2007  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 2 only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

"""FreeIPA python support library

FreeIPA is a server for identity, policy, and audit.
"""

DOCLINES = __doc__.split("\n")

import os
import sys
import distutils.sysconfig

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: System Environment/Base
License :: GPL
Programming Language :: Python
Operating System :: POSIX
Operating System :: Unix
"""

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

def setup_package():

    from distutils.core import setup

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(local_path)
    sys.path.insert(0,local_path)

    try:
        setup(
            name = "ipa-client",
            version = "0.99.0",
            license = "GPL",
            author = "Simo Sorce",
            author_email = "ssorce@redhat.com",
            maintainer = "freeIPA Developers",
            maintainer_email = "freeipa-devel@redhat.com",
            url = "http://www.freeipa.org/",
            description = DOCLINES[0],
            long_description = "\n".join(DOCLINES[2:]),
            download_url = "http://www.freeipa.org/page/Downloads",
            classifiers=filter(None, CLASSIFIERS.split('\n')),
            platforms = ["Linux"],
            py_modules=['ipachangeconf']
        )
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return

if __name__ == '__main__':
    setup_package()
