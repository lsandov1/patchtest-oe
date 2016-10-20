#!/usr/bin/env python

# Check if mbox was merged by patchtest
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

import re
from base import Base, fix
from patchtestdata import PatchTestInput as pti
from subprocess import check_output

class Merge(Base):

    @fix("Rebase your series on top of master's HEAD")
    def test_merge(self):
        def headlog():
            return check_output("cd %s; git log --pretty='%%h: %%aN: %%cd: %%s' -1" % pti.repodir, shell=True)

        if not pti.repo.ismerged:
            self.fail([('HEAD shortlog', headlog())])
