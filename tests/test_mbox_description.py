#!/usr/bin/env python

# Checks related to the patch's description
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

class Description(Base):

    @fix("Please include a brief description for your patch")
    def test_description_presence(self):
        for i in xrange(Description.nmessages):
            description = Description.descriptions[i]
            if not description.strip():
                subject = Description.subjects[i]
                self.fail([('Message Subject', subject)])

