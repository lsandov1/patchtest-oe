import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from parse_signed_off_by import signed_off_by_mark

class OEDescription(OEBase):

    def test_description_presence(self):
        for description in OEDescription.descriptions:
            # in case there are no description at all
            if not description:
                self.fail()
            # in case the description are just white spaces
            if not description.strip():
                self.fail()

