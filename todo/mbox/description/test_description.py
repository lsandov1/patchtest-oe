import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from parse_signed_off_by import signed_off_by_mark

class OEDescription(OEBase):

    @classmethod
    def setUpClassLocal(cls):
        cls.mark = str(signed_off_by_mark).strip('"')
        cls.final_description_marks = [cls.mark, '---']

    def final_description_reached(self, line):
        for mark in OEDescription.final_description_marks:
            if line.startswith(mark):
                return True
        return False

    def test_description_presence(self):
        for message in OEDescription.mbox:
            payload = message.get_payload()

            # find the position where the description ends
            pos = min([payload.find(mark) for mark in OEDescription.final_description_marks])

            # in case there are no description at all
            if not pos:
                self.fail()

            # in case the description are just white spaces
            if not payload[0:pos].strip():
                self.fail()

