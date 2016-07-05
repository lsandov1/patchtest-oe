import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from oebase import OEBase
from parse_subject import subject
from pyparsing import ParseException

class OESubject(OEBase):

    def setUp(self):
        self.sub = 'subject'

    def test_subject_presence(self):
        for message in OESubject.mbox:
            if not message[self.sub]:
                self.fail()

    def test_subject_format(self):
        for message in OESubject.mbox:
            if not message[self.sub]:
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    subj = message[self.sub].replace('\n', '')
                    subject.parseString(subj)
                except ParseException as pe:
                    self.fail([('subject', subj)])

