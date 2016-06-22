import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
import mboxmsg as msg

class OEPayload(OEBase):

    def test_payload_presence(self):
        for message in OEPayload.mbox:
            if not message.get_payload():
                raise self.fail(self.formaterror(msg.test_payload_presence.reason,
                                                 msg.test_payload_presence.error,
                                                 msg.test_payload_presence.fix))

