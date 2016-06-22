import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
import mboxmsg as msg

class OEDescription(OEBase):

    def test_description_presence(self):
        for message in OEDescription.mbox:
            payload = message.get_payload()
            raise self.fail(self.formaterror(msg.test_description_presence.reason,
                                             msg.test_description_presence.error,
                                             msg.test_description_presence.fix,
                                             status='TODO'))


