import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff
from pylint import epylint as lint
from re import sub

from patchtestdata import PatchTestDataStore as d

class OEPyLint(OEDiff):

    @classmethod
    def setUpClassLocal(cls):
        cls.pythonpatches = []
        # get just those patches touching python files
        for patchset in cls.patchsets:
            for patch in patchset:
                if patch.path.endswith('.py'):
                    cls.pythonpatches.append(patch)

    def pretest_pylint(self):
        """(Python)Lint non-modified python files"""
        if not OEPyLint.pythonpatches:
            self.skipTest('No python related patches, skipping test')

        d['pylint_pretest'] = list()
        for pythonpatch in OEPyLint.pythonpatches:
            (pylint_stdout, pylint_stderr) = lint.py_run(pythonpatch.path, return_std=True)
            d['pylint_pretest'].extend(pylint_stdout.readlines())

    def test_pylint(self):
        """(Python)Lint modified python files"""
        if not OEPyLint.pythonpatches:
            self.skipTest('No python related patches, skipping test')

        d['pylint_test'] = list()
        for pythonpatch in OEPyLint.pythonpatches:
            (pylint_stdout, pylint_stderr) = lint.py_run(pythonpatch.path, return_std=True)
            d['pylint_test'].extend(pylint_stdout.readlines())

        # Removing line numbers of pylint log so system focus just on introduced issues
        pretest = [sub(':\d+:', ':', pyline) for pyline in d['pylint_pretest']]
        test = [sub(':\d+:', ':', pyline) for pyline in d['pylint_test']]

        # Remove those pylint lines already present on python file
        while pretest:
            test.remove(pretest.pop(0))

        # it test is empty, then pylint did not complain on the new python code
        self.assertFalse(test, 'pylint complains %s' % ' '.join(test))

