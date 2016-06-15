import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff

class OETrailingSpaces(OEDiff):

    def test_patch_trailing_spaces(self):
        """Test presence of trailing spaces"""
        # tip: possible regex (no tested!!):
        #     re.compile("\S+\s+$")
        # but this does match those lines with just \s chars
        self.fail('TODO')
