import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff
from patchtestdata import PatchTestInput as pti
from subprocess import check_output, CalledProcessError
from os.path import basename
from re import compile
from oebase import warn

def bitbake_check_output(args):
    bitbake_cmd = 'bitbake %s' % ' '.join(args)

    # change dir, prepare system and exec bitbake
    cmd = 'cd %s;source %s/oe-init-build-env;%s' % (pti.repodir,
                                                    pti.repodir,
                                                    bitbake_cmd)
    return check_output(cmd, shell=True)

class OEBitbakeParse(OEDiff):

    @classmethod
    def setUpClassLocal(cls):
        cls.newrecipes = []
        cls.modifiedrecipes = []
        # get just those patches touching python files
        for patchset in cls.patchsets:
            for patch in patchset:
                if patch.path.endswith('.bb'):
                    if patch.is_added_file:
                        cls.newrecipes.append(patch)
                    elif patch.is_modified_file:
                        cls.modifiedrecipes.append(patch)

    def pretest_bitbake_parse(self):
        """Bitbake parse on non-modified repo"""
        try:
            bitbake_check_output(['-p'])
        except CalledProcessError as e:
            self.fail('Bitbake parsing failed on non-patched repo: %s' % e.output)

    def test_bitbake_parse(self):
        """Bitbake parse on modified repo"""
        try:
            bitbake_check_output(['-p'])
        except CalledProcessError as e:
            self.fail('Bitbake parsing failed on patched repo: %s' % e.output)

    def pretest_bitbake_environment(self):
        """Show bitbake environment on non-modified repo"""
        try:
            bitbake_check_output(['-e'])
        except CalledProcessError as e:
            self.fail('Bitbake environment failed on patched repo: %s' % e.output)

    def test_bitbake_environment(self):
        """Show bitbake environment on modified repo"""
        try:
            bitbake_check_output(['-e'])
        except CalledProcessError as e:
            self.fail('Bitbake environment failed on patched repo: %s' % e.output)

    def pretest_bitbake_environment_on_target(self):
        """Show target's bitbake environment on non-modified repo"""
        # Skip this test if patch changes apply on target (recipes)
        # already present
        if not OEBitbakeParse.modifiedrecipes:
            self.skipTest('No previous bitbake targets to parse')

        prog = compile("(?P<pn>^[a-zA-Z]+)")
        pn_pv_list = [basename(recipe.path) for recipe in OEBitbakeParse.modifiedrecipes]
        pn_list = [(pn_pv, prog.match(pn_pv)) for pn_pv in pn_pv_list]

        for pn_pv, match in pn_list:
            if not match:
                warn('Target name cannot be extracted from %s' % pn_pv)
            else:
                pn = match.group('pn')
                try:
                    bitbake_check_output(['-e', pn])
                except CalledProcessError as e:
                    self.fail('Target bitbake environment failed on patched repo: %s' % e.output)

    def test_bitbake_environment_on_target(self):
        """Show target's bitbake environment on modified repo"""
        prog = compile("(?P<pn>^[a-zA-Z]+)")
        pn_pv_list = [basename(recipe.path) for recipe in OEBitbakeParse.modifiedrecipes]
        pn_list = [(pn_pv, prog.match(pn_pv)) for pn_pv in pn_pv_list]

        for pn_pv, match in pn_list:
            if not match:
                warn('Target name cannot be extracted from %s' % pn_pv)
            else:
                pn = match.group('pn')
                try:
                    bitbake_check_output(['-e', pn])
                except CalledProcessError as e:
                    self.fail('Target bitbake environment failed on patched repo: %s' % e.output)

