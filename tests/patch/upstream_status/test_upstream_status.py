import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff

from parse_upstream_status import upstream_status, upstream_status_mark, upstream_status_valid_status
from pyparsing import ParseException
from re import compile, search
import patchmsg as msg

class OEPatchUpstreamStatus(OEDiff):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patchset in cls.patchsets:
            for patch in patchset:
                if patch.path.endswith('.patch') and patch.is_added_file:
                    cls.newpatches.append(patch)

    def setUp(self):
        self.mark = str(upstream_status_mark).strip('"')

        # match self.mark with '+' preceding it
        self.prog = compile("(?<=\+)%s" % self.mark)

    def test_upstream_status_presence(self):
        if not OEPatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEPatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not self.prog.search(payload):
                self.fail(self.formaterror(msg.test_upstream_status_presence.reason,
                                           msg.test_upstream_status_presence.error,
                                           msg.test_upstream_status_presence.fix))

    def test_upstream_status_valid_status(self):
        if not OEPatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEPatchUpstreamStatus.newpatches:
            for line in str(newpatch).splitlines():
                if self.prog.search(line):
                    try:
                        upstream_status.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail(self.formaterror(msg.test_upstream_status_valid_status.reason,
                                                   msg.test_upstream_status_valid_status.error,
                                                   msg.test_upstream_status_valid_status.fix))

