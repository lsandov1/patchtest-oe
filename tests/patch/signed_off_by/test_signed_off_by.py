import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff

from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import search

class OEPatchSignedOffBy(OEDiff):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patchset in cls.patchsets:
            for patch in patchset:
                if patch.path.endswith('.patch') and patch.is_added_file:
                    cls.newpatches.append(patch)

    def setUp(self):
        self.mark = str(signed_off_by_mark).strip('"')

    def test_signed_off_by_presence(self):
        """Test presence of 'Signed-off-by' on patch"""
        if not OEPatchSignedOffBy.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEPatchSignedOffBy.newpatches:
            self.assertRegexpMatches(str(newpatch), self.mark,
                                     "Patch must be signed-off, please git configure your name/email and commit your changes with git commit --signoff")

    def test_signed_off_by_format(self):
        """Test 'Signed-off-by' format on patch"""
        for newpatch in OEPatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not payload:
                self.skipTest('Empty patch payload, no reason to execute signed-off-by format tests')
            for line in payload.splitlines():
                if search(self.mark, line):
                    try:
                        signed_off_by.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail("Patch signature has wrong format, please commit your changes with git commit --signoff")

