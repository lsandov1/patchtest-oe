from oemessage import OEMessage
from parse_signed_off_by import signed_off_by
from pyparsing import ParseException

class OESignedOffBy(OEMessage):

    sobstr = "Signed-off-by"

    def test_signed_off_presence(self):
        """Test presence of 'Signed-off-by' string"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                self.assertRegexpMatches(OESignedOffBy.sobstr, message.get_payload(),
                                         "Patch must be signed-off, please git configure your name/email and commit your changes with git commit --signoff")

    def test_signed_off_by_format(self):
        """Test 'Subject' format"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                payload = message.get_payload()
                for line in payload.splitlines():
                    if re.match(OeSignedOffBy.sobstr, line):
                        try:
                            signed_off_by.parseString(line)
                        except ParseException as pe:
                            self.fail("Patch signature has wrong format, please commit your changes with git commit --signoff")

