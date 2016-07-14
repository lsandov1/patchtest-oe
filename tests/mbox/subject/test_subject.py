import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from base import Base
import parse_subject
from pyparsing import ParseException

class Subject(Base):

    maxlength = 80

    def test_subject_presence(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.fail()

    def test_subject_format(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    parse_subject.subject.parseString(subject)
                except ParseException as pe:
                    self.fail([('Subject', pe.line),
                               ('Pyparsing exception', pe.message)])

    def test_subject_length(self):
        for subject in Subject.subjects:
            l = len(subject)
            if l > Subject.maxlength:
                self.fail([('Subject', subject), ('Length', 'Current length %s Max length %s' % (l, Subject.maxlength))])
