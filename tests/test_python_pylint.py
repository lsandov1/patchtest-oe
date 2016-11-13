#!/usr/bin/env python

# Checks related to the python code done with pylint
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
import re
from unittest import skip
from patchtestdata import PatchTestInput as pti

from patchtestdata import PatchTestDataStore as d

@skip('Test case is not ready yet, pending openembedded recipe and module review')
class PyLint(Base):
    try:
        from pylint import epylint as lint
    except ImportError as ie:
        pass

    @classmethod
    def setUpClassLocal(cls):
        cls.pythonpatches = []
        # get just those patches touching python files
        for patch in cls.patchset:
            if patch.path.endswith('.py'):
                cls.pythonpatches.append(patch)

    def setUp(self):
        if self.unidiff_parse_error:
            self.skip([('Python-unidiff parse error', self.unidiff_parse_error)])

    def pretest_pylint(self):
        if not pti.repo.canbemerged:
            self.skipTest('Patch cannot be merged, no reason to execute the test method')
        if not PyLint.pythonpatches:
            self.skipTest('No python related patches, skipping test')

        d['pylint_pretest'] = list()
        for pythonpatch in PyLint.pythonpatches:
            # run pylint just on modified files
            if pythonpatch.is_modified_file:
                (pylint_stdout, pylint_stderr) = lint.py_run(pythonpatch.path, return_std=True)
                d['pylint_pretest'].extend(pylint_stdout.readlines())

    @fix("Check your modified python lines with pylint, specially those lines introduced by your patch")
    def test_pylint(self):
        if not pti.repo.ismerged:
            self.skipTest('Patch could not be merged, no reason to execute the test method')
        if not PyLint.pythonpatches:
            self.skipTest('No python related patches, skipping test')

        d['pylint_test'] = list()
        for pythonpatch in PyLint.pythonpatches:
            (pylint_stdout, pylint_stderr) = lint.py_run(pythonpatch.path, return_std=True)
            d['pylint_test'].extend(pylint_stdout.readlines())

        # Removing line numbers of pylint log so system focus just on introduced issues
        pretest = [re.sub(':\d+:', ':', pyline) for pyline in d['pylint_pretest']]
        test = [re.sub(':\d+:', ':', pyline) for pyline in d['pylint_test']]

        # Remove those pylint lines already present on python file
        while pretest:
            test.remove(pretest.pop(0))

        # it test is non-empty, then pylint complained on the new python code
        if test:
            #TODO: 1. Include the line number on test items
            #      2. Better test format
            self.fail([('Pylint lines', ''.join(test))])

