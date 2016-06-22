import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile, match
import mboxmsg as msg

class OESignedOffBy(OEBase):

    def setUp(self):
        self.mark = str(signed_off_by_mark).strip('"')

        # match self.mark with no '+' preceding it
        self.prog = compile("(?<!\+)%s" % self.mark)

    def test_signed_off_by_presence(self):
        for message in OESignedOffBy.mbox:
            if not self.prog.search(message.get_payload()):
                self.fail(self.formaterror(msg.test_signed_off_by_presence.reason,
                                           msg.test_signed_off_by_presence.error,
                                           msg.test_signed_off_by_presence.fix))

    def test_signed_off_by_format(self):
        for message in OESignedOffBy.mbox:
            payload = message.get_payload()
            if not payload or not self.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % self.mark)
            for line in payload.splitlines():
                if match(self.mark, line):
                    try:
                        signed_off_by.parseString(line)
                    except ParseException as pe:
                        self.fail(self.formaterror(msg.test_signed_off_by_format.reason,
                                                   msg.test_signed_off_by_format.error,
                                                   msg.test_signed_off_by_format.fix))

