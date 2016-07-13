import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import warn, Base
from patchtestdata import PatchTestInput as pti
from subprocess import check_output, CalledProcessError, STDOUT
from os.path import basename
from re import compile

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
        return '\n'.join(greplines)

    return list([('Command', e.cmd), ('Output', grep(e.output)), ('Return Code', e.returncode)])

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

