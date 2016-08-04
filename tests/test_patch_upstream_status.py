#!/usr/bin/env python

# Checks related to the patch's upstream-status lines
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

from parse_upstream_status import upstream_status, upstream_status_valid_status
from parse_upstream_status import upstream_status_mark as mark
from pyparsing import ParseException
from re import compile, search

class PatchUpstreamStatus(Base):

    upstream_status_mark  = str(mark).strip('"')
    upstream_status_regex = compile("(?<=\+)%s" % upstream_status_mark)

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)


    @fix("""
Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines""")
    def test_upstream_status_presence(self):
        if not PatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.upstream_status_mark)

        for newpatch in PatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not self.upstream_status_regex.search(payload):
                self.fail([('Patch path', newpatch.path)])

    @fix("""
Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines""")
    def test_upstream_status_format(self):
        for newpatch in PatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not self.upstream_status_regex.search(payload):
                continue
            for line in payload.splitlines():
                if self.upstream_status_regex.search(line):
                    try:
                        upstream_status.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('Line', pe.line), ('Column', pe.col)])
