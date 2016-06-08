import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from oembox import OEMBox
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import match, search

class OESignedOffBy(OEMBox):

    def setUp(self):
        self.mark = str(signed_off_by_mark).strip('"')

    def test_signed_off_by_presence(self):
        """Test presence of 'Signed-off-by'"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                # match self.mark with no '+' preceding it
                self.assertRegexpMatches(message.get_payload(), "(?<!\+)%s" % self.mark,
                                         "Patch must be signed-off, please git configure your name/email and commit your changes with git commit --signoff")

    def test_signed_off_by_format(self):
        """Test 'Signed-off-by' format"""
        for mbox in OESignedOffBy.mboxes:
            for message in mbox:
                payload = message.get_payload()
                if not payload or not search("(?<!\+)%s" % self.mark, payload):
                    self.skipTest("%s not present, skipping format test" % self.mark)
                for line in payload.splitlines():
                    if match(self.mark, line):
                        try:
                            signed_off_by.parseString(line)
                        except ParseException as pe:
                            self.fail("Patch signature has wrong format, please commit your changes with git commit --signoff")

