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

import base
import re
import subprocess
from patchtestdata import PatchTestInput as pti

def bitbake(args):

    bitbake_cmd = 'bitbake %s' % ' '.join(args)

    # change dir, prepare system and exec bitbake
    cmd = 'cd %s;. %s/oe-init-build-env;%s' % (pti.repodir,
                                               pti.repodir,
                                               bitbake_cmd)
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)

def filter(log, regex):
    """ Filter those lines defined by the regex """
    prog = re.compile(regex)
    greplines = []
    if log:
        for line in log.splitlines():
            if prog.search(line):
                greplines.append(line)
    if not greplines:
        # something went really wrong, so provide the complete log
        base.logger.warn(log)

    return greplines

def getVar(var, target=''):
    plain = ' '.join(filter(bitbake(['-e', target]), '^%s=' % var))
    return plain.lstrip('%s=' % var).strip('"')

def formaterror(e, regex='^ERROR:'):
    lines = filter(e.output, regex)
    out = [('Output', lines[0])]
    out.extend([('', line) for line in lines[1:]])
    return out

class Bitbake(base.Base):

    # Matches PN and PV from a recipe filename
    pnpv = re.compile("(?P<pn>^\S+)_(?P<pv>\S+)\.\S+")

    @classmethod
    def setUpClassLocal(cls):
        cls.newrecipes = []
        cls.modifiedrecipes = []
        cls.recipes = []
        # get just those patches touching python files
        for patch in cls.patchset:
            if patch.path.endswith('.bb') or patch.path.endswith('.bbappend'):
                if patch.is_added_file:
                    cls.newrecipes.append(patch)
                elif patch.is_modified_file:
                    cls.modifiedrecipes.append(patch)

        cls.recipes.extend(cls.newrecipes)
        cls.recipes.extend(cls.modifiedrecipes)

    def setUp(self):
        if self.unidiff_parse_error:
            self.skip([('Python-unidiff parse error', self.unidiff_parse_error)])
