#!/usr/bin/env python

# Checks related to the patch's signed-off-by lines
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
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile
from unittest import skip

class PatchSignedOffBy(Base):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)

        cls.mark = str(signed_off_by_mark).strip('"')

        # match PatchSignedOffBy.mark with '+' preceding it
        cls.prog = compile("(?<=\+)%s" % cls.mark)

    @fix("Sign off the added patch")
    def test_signed_off_by_presence(self):
        if not PatchSignedOffBy.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % PatchSignedOffBy.mark)

        for newpatch in PatchSignedOffBy.newpatches:
            payload = str(newpatch)
            for line in payload.splitlines():
                if self.patchmetadata_regex.match(line):
                    continue
                if PatchSignedOffBy.prog.search(payload):
                    break
            else:
                self.fail([('Patch', newpatch.path)])

    @skip('due to http://bugzilla.yoctoproject.org/show_bug.cgi?id=9959')
    @fix("""
Sign off the added patch with the right format. More info on
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines
""")
    def test_signed_off_by_format(self):
        for newpatch in PatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not payload or not PatchSignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % PatchSignedOffBy.mark)
            for line in payload.splitlines():
                if self.patchmetadata_regex.match(line):
                    continue
                if PatchSignedOffBy.prog.search(line):
                    try:
                        signed_off_by.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('line', pe.line), ('column', pe.col)])

