import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase

from parse_upstream_status import upstream_status, upstream_status_mark, upstream_status_valid_status
from pyparsing import ParseException
from re import compile, search

class OEPatchUpstreamStatus(OEBase):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)

        cls.mark = str(upstream_status_mark).strip('"')

        # match OEPatchUpstreamStatus.mark with '+' preceding it
        cls.prog = compile("(?<=\+)%s" % cls.mark)

    def test_upstream_status_presence(self):
        if not OEPatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % OEPatchUpstreamStatus.mark)

        for newpatch in OEPatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not OEPatchUpstreamStatus.prog.search(payload):
                self.fail()

    def test_upstream_status_valid_status(self):
        if not OEPatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % OEPatchUpstreamStatus.mark)

        for newpatch in OEPatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not OEPatchUpstreamStatus.prog.search(payload):
                self.skipTest("There is no string to check")
            for line in payload.splitlines():
                if OEPatchUpstreamStatus.prog.search(payload):
                    try:
                        upstream_status.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('Possible values', ', '.join([str(status).strip('"') for status in upstream_status_valid_status])),
                                   ('Parse Exception', str(pe))])
                                   

