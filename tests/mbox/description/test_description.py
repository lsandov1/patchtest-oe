import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oembox import OEMBox

class OEDescription(OEMBox):

    def test_description_presence(self):
        """Test presence of mbox's description"""
        # In terms of text delimiters, the description are those lines
        # between  Subject and either [YOCTO #XXXX] or (From OE-Core rev:...).
        # Check mbox/payload to see how to extract they payload
        self.fail('TODO')

