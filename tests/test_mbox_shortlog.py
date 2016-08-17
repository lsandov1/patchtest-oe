#!/usr/bin/env python

# Checks related to the patch's  summary
#
# Copyright (C) 2016 Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from base import Base, fix
import parse_shortlog
from pyparsing import ParseException

class Shortlog(Base):

    maxlength = 80

    @fix("""
Amend the commit message and include a summary with the following format:

    <target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_shortlog_presence(self):
        for shortlog in Shortlog.shortlogs:
            if not shortlog.strip():
                self.fail()

    @fix("""
Amend the commit message and include a summary with the following format:

<target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_shortlog_format(self):
        for shortlog in Shortlog.shortlogs:
            if not shortlog.strip():
                self.skipTest('Empty shortlog, no reason to execute shortlog format test')
            else:
                # no reason to re-check on revert shortlogs
                if shortlog.startswith('Revert "'):
                    continue
                try:
                    parse_shortlog.shortlog.parseString(shortlog)
                except ParseException as pe:
                    self.fail([('Shortlog', pe.line),
                               ('Column',  pe.col)])

    @fix("Commit summary must not exceed 80 characters")
    def test_shortlog_length(self):
        for shortlog in Shortlog.shortlogs:
            # no reason to re-check on revert shortlogs
            if shortlog.startswith('Revert "'):
                continue
            l = len(shortlog)
            if l > Shortlog.maxlength:
                self.fail([('Shortlog', shortlog), ('Length', 'Current length %s Max length %s' % (l, Shortlog.maxlength))])
