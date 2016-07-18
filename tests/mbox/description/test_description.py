import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base

class Description(Base):

    def test_description_presence(self):
        for i in xrange(Description.nmessages):
            description = Description.descriptions[i]
            if not description.strip():
                subject = Description.subjects[i]
                self.fail([('Message Subject', subject)])

