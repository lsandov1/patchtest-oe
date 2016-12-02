#!/usr/bin/env python

# Checks related to bitbake parsing and environment
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

import bitbake
from patchtestdata import PatchTestInput as pti
import subprocess

class BitbakeEnvironment(bitbake.Bitbake):

    def test_bitbake_environment_on_target(self):
        if not pti.repo.ismerged:
            self.skipTest('Patch could not be merged, no reason to execute the test method')

        # test added or modified recipes can be bitbake parse (-e)
        for pn,_ in self.added_pnpvs + self.modified_pnpvs:
            try:
                bitbake.bitbake(['-e', pn])
            except subprocess.CalledProcessError as e:
                self.fail("Bitbake encountered problems while getting the environment for the proposed target %s" % pn,
                          "Run bitbake %s and correct the found issues before sending the patch to the mailing list" % pn,
                          data=bitbake.formaterror(e))
