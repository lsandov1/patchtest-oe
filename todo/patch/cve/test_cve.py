import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase

class OECVE(OEBase):

    re_cve_pattern = re.compile("CVE\-\d{4}\-\d+", re.IGNORECASE)
    re_cve_word    = re.compile("\s*\+CVE\s?", re.IGNORECASE)
    re_cve_tag     = re.compile("CVE:(\s+CVE\-\d{4}\-\d+)+", re.IGNORECASE)

    def test_cve_presence_on_subject(self):
        """
        Checks if CVE-xxxx-xxxx is in subject if CVE word is in the payload.
        """
        for i in xrange(OECVE.nmessages):
            if self.re_cve_word.search(OECVE.payloads[i]):
                if not self.re_cve_pattern.search(OECVE.subjects[i]):
                    self.fail()

    def test_cve_tag_format(self):
        """
        Checks if patch contains CVE tag if "CVE-xxxx-xxxx" is in subject.
        """
        for i in xrange(OECVE.nmessages):
            if self.re_cve_pattern.search(OECVE.subjects[i]):
                if not self.re_cve_tag.search(OECVE.payloads[i]):
                    self.fail()
