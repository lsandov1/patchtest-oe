import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
import mboxmsg as msg

class OEBugzilla(OEBase):
    def test_bugzilla_entry_format(self):
        for message in OEBugzilla.mbox:
            payload = message.get_payload()
            raise self.fail(self.formaterror(msg.test_bugzilla_entry_format.reason,
                                             msg.test_bugzilla_entry_format.error,
                                             msg.test_bugzilla_entry_format.fix,
                                             status='TODO'))

