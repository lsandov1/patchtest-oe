#!/usr/bin/env python

# Checks related to the patch's CVE lines
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

class CVE(Base):

    re_cve_pattern = re.compile("CVE\-\d{4}\-\d+", re.IGNORECASE)
    re_cve_word    = re.compile("\s*\+CVE\s?", re.IGNORECASE)
    re_cve_tag     = re.compile("CVE:(\s+CVE\-\d{4}\-\d+)+", re.IGNORECASE)

    @fix("Please include the CVE, as CVE-xxxx-xxxx, in the subject")
    def test_cve_presence_on_subject(self):
        """
        Checks if CVE-xxxx-xxxx is in subject if CVE word is in the payload.
        """
        for i in xrange(CVE.nmessages):
            if self.re_cve_word.search(CVE.payloads[i]):
                if not self.re_cve_pattern.search(CVE.subjects[i]):
                    self.fail([('Subject', CVE.subjects[i])])

    @fix("""
Please include the CVE tag on the patch added to the recipe, see:
http://openembedded.org/wiki/Commit_Patch_Message_Guidelines#CVE_Patches""")
    def test_cve_tag_format(self):
        """
        Checks if patch contains CVE tag if "CVE-xxxx-xxxx" is in subject.
        """
        for i in xrange(CVE.nmessages):
            if self.re_cve_pattern.search(CVE.subjects[i]):
                if not self.re_cve_tag.search(CVE.payloads[i]):
                    self.fail([('Subject', CVE.subjects[i])])
