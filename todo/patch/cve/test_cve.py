import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from unittest import skip

@skip('Not implemented yet')
class OECVE(OEBase):
    def test_cve_presence_on_subject(self):
        for patch in OECVE.patchset:
            payload = str(patch)

    def test_cve_tag_format(self):
        # tip: make a pyparsing file specifying syntax and parse
        # string on the the test check mbox/subject test case
        # Request from:
        #    https://bugzilla.yoctoproject.org/show_bug.cgi?id=9249
        for patch in OECVE.patchset:
            payload = str(patch)

