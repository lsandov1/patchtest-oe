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

from base import warn, Base, fix
from patchtestdata import PatchTestInput as pti
from subprocess import check_output, CalledProcessError, STDOUT
from os.path import basename
from re import compile
from unittest import skipUnless
from patchtestdata import PatchTestInput as pti

def bitbake_check_output(args):
    bitbake_cmd = 'bitbake %s' % ' '.join(args)

    # change dir, prepare system and exec bitbake
    cmd = 'cd %s;source %s/oe-init-build-env;%s' % (pti.repodir,
                                                    pti.repodir,
                                                    bitbake_cmd)
    return check_output(cmd, stderr=STDOUT, shell=True)

def formatdata(e):
    def grep(log, regex='ERROR:'):
        prog = compile(regex)
        greplines = []
        if log:
            for line in log.splitlines():
                if prog.search(line):
                    greplines.append(line)
        # something went really wrong, so provide the complete log
        if not greplines:
            return log
        else:
            return '\n'.join(greplines)

    return list([('Command', e.cmd), ('Output', grep(e.output)), ('Return Code', e.returncode)])

@skipUnless(pti.merge, 'Test suite only makes sense when patch is merged into the repository')
class BitbakeParse(Base):

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

        # regex to extract the recipe name on a recipe filename
        cls.reciperegex = compile("(?P<pn>^\S+)(_\S+)")

    def pretest_bitbake_parse(self):
        try:
            bitbake_check_output(['-p'])
        except CalledProcessError as e:
            raise self.fail(formatdata(e))

    @fix("""Make sure you can (bitbake) parse manually after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -p
    """)
    def test_bitbake_parse(self):
        try:
            bitbake_check_output(['-p'])
        except CalledProcessError as e:
            raise self.fail(formatdata(e))

    def pretest_bitbake_environment(self):
        try:
            bitbake_check_output(['-e'])
        except CalledProcessError as e:
            raise self.fail(formatdata(e))

    @fix("""Make sure you can get the (bitbake) environment manually after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -e""")
    def test_bitbake_environment(self):
        try:
            bitbake_check_output(['-e'])
        except CalledProcessError as e:
            raise self.fail(formatdata(e))

    def pretest_bitbake_environment_on_target(self):
        if not BitbakeParse.modifiedrecipes:
            self.skipTest("Patch data does not modified any bb or bbappend file")

        pn_pv_list = [basename(recipe.path) for recipe in BitbakeParse.recipes]
        pn_list = [(pn_pv, BitbakeParse.reciperegex.match(pn_pv)) for pn_pv in pn_pv_list]

        for pn_pv, match in pn_list:
            if not match:
                warn('Target name cannot be extracted from %s' % pn_pv)
            else:
                pn = match.group('pn')
                try:
                    bitbake_check_output(['-e', pn])
                except CalledProcessError as e:
                    raise self.fail(formatdata(e))

    @fix("""Make sure you can get the environment manually on a specific target after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -e <target>
    """)
    def test_bitbake_environment_on_target(self):
        pn_pv_list = [basename(recipe.path) for recipe in BitbakeParse.recipes]
        pn_list = [(pn_pv, BitbakeParse.reciperegex.match(pn_pv)) for pn_pv in pn_pv_list]

        for pn_pv, match in pn_list:
            if not match:
                warn('Target name cannot be extracted from %s' % pn_pv)
            else:
                pn = match.group('pn')
                try:
                    bitbake_check_output(['-e', pn])
                except CalledProcessError as e:
                    raise self.fail(formatdata(e))

