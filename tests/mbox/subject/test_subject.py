import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from oembox import OEMBox
from parse_subject import subject
from pyparsing import ParseException

class OESubject(OEMBox):

    def test_subject_presence(self):
        """Test presence of 'Subject' field"""
        for mbox in OESubject.mboxes:
            for message in mbox:
                self.assertIsNotNone(message['subject'], "Patch's subject is empty, please redo the patch and include a subject line")

    def test_subject_format(self):
        """Test 'Subject' format"""
        for mbox in OESubject.mboxes:
            for message in mbox:
                if not message['subject']:
                    self.skipTest('Empty subject, no reason to execute subject format test')
                else:
                    try:
                        subject.parseString(message['subject'])
                    except ParseException:
                        self.fail("Patch's subject has wrong format, please redo the patch and fill the subject line with the following format: \"<target>\": <brief description>")
