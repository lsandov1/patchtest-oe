import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from oebase import OEBase, warn, info
import parse_subject
from pyparsing import ParseException

class OESubject(OEBase):

    maxlength = 50

    def setUp(self):
        self.key      = 'subject'
        self.subjects = list()
        endprefix = ']'

        # go through all subjects and lstrip the first '[]' and replace newlines
        for message in OESubject.mbox:
            subject         = message[self.key]
            closebracketpos = subject.find(endprefix)
            if closebracketpos < 0:
                warn('Patch does not contain square bracket prefix')
                continue
            stripsubject = subject[closebracketpos+len(endprefix):].replace('\n','')
            self.subjects.append(stripsubject)

    def test_subject_presence(self):
        for subject in self.subjects:
            if not subject or not subject.strip():
                self.fail()

    def test_subject_format(self):
        for subject in self.subjects:
            if not subject or not subject.strip():
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    parse_subject.subject.parseString(subject)
                except ParseException as pe:
                    self.fail([('Subject', pe.line),
                               ('Pyparsing exception', pe.message)])

    def test_subject_length(self):
        for subject in self.subjects:
            l = len(subject)
            if l > OESubject.maxlength:
                self.fail([('Subject', subject), ('Length', 'Current length %s Max length %s' % (l, OESubject.maxlength))])
