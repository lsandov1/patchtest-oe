import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oembox import OEMBox
import mboxmsg as msg

class OEBugzilla(OEMBox):
    def test_bugzilla_entry_format(self):
        raise self.fail(self.formaterror(msg.test_bugzilla_entry_format.reason,
                                         msg.test_bugzilla_entry_format.error,
                                         msg.test_bugzilla_entry_format.fix,
                                         status='TODO'))

