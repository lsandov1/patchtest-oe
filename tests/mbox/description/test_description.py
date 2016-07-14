import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base

class Description(Base):

    def test_description_presence(self):
        for description in Description.descriptions:
            if not description.strip():
                self.fail()

