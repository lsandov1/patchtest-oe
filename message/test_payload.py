from oemessage import OEMessage

class OEPayload(OEMessage):

    def test_payload_presence(self):
        """ Check that presence of message payload """
        for mbox in OEPayload.mboxes:
            for message in mbox:
                self.assertTrue(message.get_payload(), "Patch's payload is empty, please include your file changes into the patch")
