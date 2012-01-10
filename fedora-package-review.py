#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
# package_review - a simple function to retrieve the review request of a
# package
#
# Copyright (C) 2011 Pierre-Yves Chibon
# Author: Pierre-Yves Chibon <pingou@pingoured.fr>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
# See http://www.gnu.org/copyleft/gpl.html  for the full text of the
# license.
"""

import sys
from bugzilla.rhbugzilla import RHBugzilla3
BZCLIENT = RHBugzilla3(url='https://bugzilla.redhat.com/xmlrpc.cgi')


def get_package_review(packagename):
    """
    Return information about the review request(s) sumitted for a given
    package.

    This function queries the Fedora/RedHat's bugzilla to find the review
    or reviews submitted for a given package.
    It prints out the bug number, the assignee, the summary and the
    resolution of each bug found.

    :arg packagename the name of the package to search for
    """
    bugbz = BZCLIENT.query(
            {#'bug_status': ['CLOSED'],
             'short_desc': "Request: {0} -.*".format(packagename),
             'short_desc_type': 'regexp',
             'component': 'Package Review'})

    for bug in bugbz:
        print bug, '-', bug.resolution
        print "\t",bug.url

    return bugbz


if __name__ == '__main__':
    for package in sys.argv[1:]:
        get_package_review(package)
