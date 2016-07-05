import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase,info
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile

class OEPatchSignedOffBy(OEBase):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)

        cls.mark = str(signed_off_by_mark).strip('"')

        # match OEPatchSignedOffBy.mark with '+' preceding it
        cls.prog = compile("(?<=\+)%s" % cls.mark)

    def test_signed_off_by_presence(self):
        if not OEPatchSignedOffBy.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % OEPatchSignedOffBy.mark)

        for newpatch in OEPatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not OEPatchSignedOffBy.prog.search(payload):
                self.fail()

    def test_signed_off_by_format(self):
        for newpatch in OEPatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not payload or not OEPatchSignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % OEPatchSignedOffBy.mark)
            for line in payload.splitlines():
                if OEPatchSignedOffBy.prog.search(line):
                    try:
                        signed_off_by.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('line', line), ('Parse Exception', str(pe))])

