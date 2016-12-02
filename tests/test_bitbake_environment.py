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
import base
from patchtestdata import PatchTestInput as pti
import subprocess
import os

class BitbakeEnvironment(bitbake.Bitbake):

    def test_bitbake_environment_on_target(self):
        if not pti.repo.ismerged:
            self.skipTest('Patch could not be merged, no reason to execute the test method')

        pn_pv_list = [os.path.basename(recipe.path) for recipe in BitbakeEnvironment.recipes]
        pn_list = [(pn_pv, BitbakeEnvironment.pnpv.match(pn_pv)) for pn_pv in pn_pv_list]

        for pn_pv, match in pn_list:
            if not match:
                base.warn('Target name cannot be extracted from %s' % pn_pv)
            else:
                pn = match.group('pn')
                try:
                    bitbake.bitbake(['-e', pn])
                except subprocess.CalledProcessError as e:
                    self.fail("Bitbake encountered problems while getting the environment for the proposed target '%s'" % pn,
                              "Run 'bitbake %s' and correct the found issues before sending the patch to the mailing list" % pn,
                              data=bitbake.formaterror(e))

