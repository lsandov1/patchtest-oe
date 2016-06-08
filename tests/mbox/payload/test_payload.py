import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from oembox import OEMBox

class OEPayload(OEMBox):

    def test_payload_presence(self):
        """ Check that presence of message payload """
        for mbox in OEPayload.mboxes:
            for message in mbox:
                self.assertTrue(message.get_payload(), "Patch's payload is empty, please include your file changes into the patch")
