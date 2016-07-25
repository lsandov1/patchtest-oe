import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix

from parse_upstream_status import upstream_status, upstream_status_mark, upstream_status_valid_status
from pyparsing import ParseException
from re import compile, search

class PatchUpstreamStatus(Base):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)

        cls.mark = str(upstream_status_mark).strip('"')

        # match PatchUpstreamStatus.mark with '+' preceding it
        cls.prog = compile("(?<=\+)%s" % cls.mark)

    @fix("""
Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines""")
    def test_upstream_status_presence(self):
        if not PatchUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % PatchUpstreamStatus.mark)

        for newpatch in PatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not PatchUpstreamStatus.prog.search(payload):
                self.fail()

    @fix("""
Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines""")
    def test_upstream_status_format(self):
        for newpatch in PatchUpstreamStatus.newpatches:
            payload = str(newpatch)
            if not PatchUpstreamStatus.prog.search(payload):
                continue
            for line in payload.splitlines():
                if PatchUpstreamStatus.prog.search(payload):
                    try:
                        upstream_status.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('Line', pe.line), ('Column', pe.col)])
