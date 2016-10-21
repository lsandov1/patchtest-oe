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
from re import compile, match
from unittest import skip

class SignedOffBy(Base):

    @classmethod
    def setUpClassLocal(cls):
        # match self.mark with no '+' preceding it
        cls.mark = str(signed_off_by_mark).strip('"')
        cls.prog = compile("(?<!\+)%s" % cls.mark)

    @fix("Sign off the patch")
    def test_signed_off_by_presence(self):
        for i in xrange(SignedOffBy.nmessages):
            payload = SignedOffBy.payloads[i]
            if not SignedOffBy.prog.search(payload):
                self.fail([('Commit shortlog', SignedOffBy.shortlogs[i])])
