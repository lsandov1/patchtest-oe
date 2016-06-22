import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from oebase import OEBase
from parse_subject import subject
from pyparsing import ParseException
import mboxmsg as msg

class OESubject(OEBase):

    def setUp(self):
        self.sub = 'subject'

    def test_subject_presence(self):
        for message in OESubject.mbox:
            if not message[self.sub]:
                self.fail(self.formaterror(msg.test_subject_presence.reason,
                                           msg.test_subject_presence.error,
                                           msg.test_subject_presence.fix))

    def test_subject_format(self):
        for message in OESubject.mbox:
            if not message[self.sub]:
                self.skipTest('Empty subject, no reason to execute subject format test')
            else:
                try:
                    subject.parseString(message[self.sub])
                except ParseException as pe:
                    self.fail(self.formaterror(msg.test_subject_format.reason,
                                               msg.test_subject_format.error,
                                               msg.test_subject_format.fix,
                                               data=str(pe)))

