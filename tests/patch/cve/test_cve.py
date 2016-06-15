import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff
from oembox import OEMBox

class OECVE(OEDiff, OEMBox):
    # this class inherits from both base classes because
    # it check mbox's subject and patch code. In theory, the
    # patch check should  be done under the tests/patch but
    # for the moment let's place both in this test case

    def test_cve_presence_on_subject(self):
        """Test presence of the CVE number on patch subject"""
        self.fail('TODO')

    def test_cve_tag_format(self):
        """Test 'CVE: CVE-XXXX-YYYY' format on patch"""
        # tip: make a pyparsing file specifying syntax and parse
        # string on the the test check mbox/subject test case
        # Request from:
        #    https://bugzilla.yoctoproject.org/show_bug.cgi?id=9249
        self.fail('TODO')

