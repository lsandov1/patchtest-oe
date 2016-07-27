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
import parse_subject
from pyparsing import ParseException

class Subject(Base):

    maxlength = 80

    @fix("""
Amend the commit message and include a summary with the following format:

    <target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_subject_presence(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.fail()

    @fix("""
Amend the commit message and include a summary with the following format:

<target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_subject_format(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    parse_subject.subject.parseString(subject)
                except ParseException as pe:
                    self.fail([('Subject', pe.line),
                               ('Column',  pe.col)])

    @fix("Commit summary must not exceed 80 characters")
    def test_subject_length(self):
        for subject in Subject.subjects:
            l = len(subject)
            if l > Subject.maxlength:
                self.fail([('Subject', subject), ('Length', 'Current length %s Max length %s' % (l, Subject.maxlength))])
