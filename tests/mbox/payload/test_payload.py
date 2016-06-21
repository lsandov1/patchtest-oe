import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oembox import OEMBox
import mboxmsg as msg

class OEPayload(OEMBox):

    def test_payload_presence(self):
        for mbox in OEPayload.mboxes:
            for message in mbox:
                if not message.get_payload():
                    raise self.fail(self.formaterror(msg.test_payload_presence.reason,
                                                     msg.test_payload_presence.error,
                                                     msg.test_payload_presence.fix))

