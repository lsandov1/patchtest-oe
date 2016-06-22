import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff
import patchmsg as msg

class OETrailingSpaces(OEDiff):

    def test_patch_trailing_spaces(self):
        # tip: possible regex (no tested!!):
        #     re.compile("\S+\s+$")
        # but this does match those lines with just \s chars
        self.fail(self.formaterror(msg.test_patch_trailing_spaces.reason,
                                   msg.test_patch_trailing_spaces.error,
                                   msg.test_patch_trailing_spaces.fix,
                                   status='TODO'))
