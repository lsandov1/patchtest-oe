import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile, match

class OESignedOffBy(OEBase):

    @classmethod
    def setUpClassLocal(cls):
        # match self.mark with no '+' preceding it
        cls.mark = str(signed_off_by_mark).strip('"')
        cls.prog = compile("(?<!\+)%s" % cls.mark)

    def test_signed_off_by_presence(self):
        for message in OESignedOffBy.mbox:
            if not OESignedOffBy.prog.search(message.get_payload()):
                self.fail()

    def test_signed_off_by_format(self):
        for message in OESignedOffBy.mbox:
            payload = message.get_payload()
            if not payload or not OESignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % OESignedOffBy.mark)
            for line in payload.splitlines():
                if match(self.mark, line):
                    try:
                        signed_off_by.parseString(line)
                    except ParseException as pe:
                        self.fail([('Parse Exception', str(pe))])

