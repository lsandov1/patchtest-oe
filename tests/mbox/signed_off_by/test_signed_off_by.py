import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile, match

class SignedOffBy(Base):

    @classmethod
    def setUpClassLocal(cls):
        # match self.mark with no '+' preceding it
        cls.mark = str(signed_off_by_mark).strip('"')
        cls.prog = compile("(?<!\+)%s" % cls.mark)

    def test_signed_off_by_presence(self):
        for message in SignedOffBy.mbox:
            if not SignedOffBy.prog.search(message.get_payload()):
                self.fail()

    def test_signed_off_by_format(self):
        for message in SignedOffBy.mbox:
            payload = message.get_payload()
            if not payload or not SignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % SignedOffBy.mark)
            for line in payload.splitlines():
                if match(self.mark, line):
                    try:
                        signed_off_by.parseString(line)
                    except ParseException as pe:
                        self.fail([('line', line), ('Parse Exception', str(pe))])

