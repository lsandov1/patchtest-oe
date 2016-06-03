from oepatch import OEPatch
from parse_upstream_status import upstream_status, upstream_status_mark, upstream_status_valid_status
from pyparsing import ParseException
from re import search

class OEUpstreamStatus(OEPatch):

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

    def test_upstream_status_presence(self):
        """Test presence of 'Upstream-Status' string"""
        if not OEUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEUpstreamStatus.newpatches:
            self.assertRegexpMatches(str(newpatch),
                                     self.mark,
                                     "Patch (%s) must have a '%s', please include and send the series again" % (newpatch.path, self.mark))

    def test_upstream_status_valid_status(self):
        """Test format and status of 'Upstream-Status'"""
        if not OEUpstreamStatus.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % self.mark)

        for newpatch in OEUpstreamStatus.newpatches:
            for line in str(newpatch).splitlines():
                if search(self.mark, line):
                    try:
                        upstream_status.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        valid_status = '|'.join([str(s).strip('"') for s in upstream_status_valid_status])
                        self.fail("Upstream-Status has wrong format or status value, please correct it and send the series again. 'Upstream-Status: [%s]'" %
                                  valid_status)

