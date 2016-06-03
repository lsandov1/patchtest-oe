from oemessage import OEMessage
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import match
from oebase import info

class OESignedOffBy(OEMessage):

    def setUp(self):
        self.mark = str(signed_off_by_mark).strip('"')

    def test_signed_off_by_presence(self):
        """Test presence of 'Signed-off-by' string"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                self.assertRegexpMatches(message.get_payload(), self.mark,
                                         "Patch must be signed-off, please git configure your name/email and commit your changes with git commit --signoff")

    def test_signed_off_by_format(self):
        """Test 'Signed-off-by' format"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                payload = message.get_payload()
                if not payload:
                    self.skipTest('Empty payload, no reason to execute signed-off-by format tests')
                for line in payload.splitlines():
                    if match(self.mark, line):
                        try:
                            signed_off_by.parseString(line)
                        except ParseException as pe:
                            self.fail("Patch signature has wrong format, please commit your changes with git commit --signoff")

