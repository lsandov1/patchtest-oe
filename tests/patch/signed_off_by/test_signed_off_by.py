import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff

from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile
import patchmsg as msg

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

        # match self.mark with '+' preceding it
        self.prog = compile("(?<=\+)%s" % self.mark)

    def test_signed_off_by_presence(self):
        if not OEPatchSignedOffBy.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEPatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not self.prog.search(payload):
                self.fail(self.formaterror(msg.test_signed_off_by_presence.reason,
                                           msg.test_signed_off_by_presence.error,
                                           msg.test_signed_off_by_presence.fix))

    def test_signed_off_by_format(self):
        for newpatch in OEPatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not payload or not self.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % self.mark)
            for line in payload.splitlines():
                if self.prog.search(line):
                    try:
                        signed_off_by.parseString(line.lstrip('+'))
                    except ParseException as pe:
                            self.fail(self.formaterror(msg.test_signed_off_by_format.reason,
                                                       msg.test_signed_off_by_format.error,
                                                       msg.test_signed_off_by_format.fix))

