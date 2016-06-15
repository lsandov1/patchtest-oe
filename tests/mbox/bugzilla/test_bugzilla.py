import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oembox import OEMBox

class OEBugzilla(OEMBox):

    def test_bugzilla_entry_format(self):
        """Test '[YOCTO #XXXX]' format on description"""
        # tip: make a pyparsing file specifying syntax and parse
        # string on the the test check mbox/subject test case
        self.fail('TODO')
