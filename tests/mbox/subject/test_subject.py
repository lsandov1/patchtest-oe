import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from base import Base, fix
import parse_subject
from pyparsing import ParseException

class Subject(Base):

    maxlength = 80

    @fix("""
Amend the commit message and include a summary with the following format:

    <target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_subject_presence(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.fail()

    @fix("""
Amend the commit message and include a summary with the following format:

<target>: <summary>

where <target> is the filename where main code changes apply""")
    def test_subject_format(self):
        for subject in Subject.subjects:
            if not subject.strip():
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    parse_subject.subject.parseString(subject)
                except ParseException as pe:
                    self.fail([('Subject', pe.line),
                               ('Column',  pe.col)])

    @fix("Commit summary must not exceed 80 characters")
    def test_subject_length(self):
        for subject in Subject.subjects:
            l = len(subject)
            if l > Subject.maxlength:
                self.fail([('Subject', subject), ('Length', 'Current length %s Max length %s' % (l, Subject.maxlength))])
