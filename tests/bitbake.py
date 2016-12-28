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

import os
import re
import base
import subprocess
from patchtestdata import PatchTestInput as pti
import unittest

def bitbake(args):

    # Check if environment is prepared
    cmd = 'cd %s;. %s/oe-init-build-env' % (pti.repodir,
                                            pti.repodir)
    subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)

    # Run bitbake
    bitbake_cmd = 'bitbake %s' % ' '.join(args)
    cmd = 'cd %s;. %s/oe-init-build-env;%s' % (pti.repodir,
                                               pti.repodir,
                                               bitbake_cmd)
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)

def filter(log, regex):
    """ Filter those lines defined by the regex """
    greplines = []
    if log:
        prog = re.compile(regex)
        for line in log.splitlines():
            if prog.search(line):
                greplines.append(line)
    if not greplines:
        # something went really wrong, so provide the complete log
        base.logger.warn('Pattern %s not found on bitbake output' % prog.pattern)

    return greplines

def getVar(var, target=''):
    regex = '^%s=' % var
    plain = ' '.join(filter(bitbake(['-e', target]), regex))
    return plain.lstrip('%s=' % var).strip('"')

def getFlag(flag, target=''):
    regex = '#\s+\[(?P<flag>%s)\]\s+\"(?P<value>\w+)\"' % flag
    plain = ' '.join(filter(bitbake(['-e', target]), regex))
    flag = ''
    match = prog.search(plain)
    if match:
        flag = match.group('value')
    return flag

class Bitbake(base.Base):

    # Matches PN and PV from a recipe filename
    pnpv = re.compile("(?P<pn>^\S+)(_(?P<pv>\S+))?\.\S+")

    added_pnpvs    = []
    modified_pnpvs = []
    removed_pnpvs  = []

    @classmethod
    def setUpClassLocal(cls):
        added_paths    = []
        modified_paths = []
        removed_paths  = []

        for patch in cls.patchset:
            if patch.path.endswith('.bb') or patch.path.endswith('.append') or patch.path.endswith('.inc'):
                if patch.is_added_file:
                    added_paths.append(patch.path)
                elif patch.is_modified_file:
                    modified_paths.append(patch.path)
                elif patch.is_removed_file:
                    removed_paths.append(patch.path)

        added_matches    = [cls.pnpv.match(os.path.basename(path)) for path in added_paths]
        modified_matches = [cls.pnpv.match(os.path.basename(path)) for path in modified_paths]
        removed_matches  = [cls.pnpv.match(os.path.basename(path)) for path in removed_paths]

        cls.added_pnpvs    = [(match.group('pn'), match.group('pv')) for match in added_matches if match]
        cls.modified_pnpvs = [(match.group('pn'), match.group('pv')) for match in modified_matches if match]
        cls.removed_pnpvs  = [(match.group('pn'), match.group('pv')) for match in removed_matches if match]

