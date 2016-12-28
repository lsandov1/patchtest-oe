#!/usr/bin/env python

# Checks related to oe-selftest
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

import base
import subprocess
from patchtestdata import PatchTestInput as pti
import bitbake

def _run(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)

def run(oe_init_build_env_cmd, args=[]):
    # Run oe-selftest
    oe_selftest_cmd = 'oe-selftest %s' % ' '.join(args)
    return _run(oe_init_build_env_cmd + oe_selftest_cmd)

def setup(oe_init_build_env_cmd):

    # Check if environment is prepared
    _run(oe_init_build_env_cmd)

    # Include meta-selftest layer
    bb_layers_cmd = 'bitbake-layers add-layer %s/meta-selftest' % pti.repodir
    _run(oe_init_build_env_cmd + bb_layers_cmd)

class OESelfTest(base.Base):

    def setUp(self):
        self.oe_init_build_env_cmd = 'cd %s; . %s/oe-init-build-env;' % (pti.repodir, pti.repodir)
        try:
            setup(self.oe_init_build_env_cmd)
        except subprocess.CalledProcessError as cpe:
            base.logger.warn('oe-selftest (%s) cannot be executed' % cpe.cmd)
            self.skipTest('oe-selftest (%s) cannot be executed' % cpe.cmd)

    def test_wic(self):
        try:
            run(self.oe_init_build_env_cmd, ['-r', 'wic'])
        except subprocess.CalledProcessError as cpe:
            wic_fails = [('Wic Failures', '')]
            wic_fails.extend([('', fail.lstrip('FAIL:').strip()) for fail in bitbake.filter(cpe.output, '^FAIL:')])
            self.fail('The script oe-selftest fail running wic',
                      'Make sure you run %s on top of your series' % cpe.cmd,
                      data=wic_fails)

