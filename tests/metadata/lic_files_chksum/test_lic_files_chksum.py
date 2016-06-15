import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from oediff import OEDiff
from oembox import OEMBox

class OELicFilesChksum(OEDiff, OEMBox):
    # the reason of this double inheritance is that one test
    # check subject and patch data

    def test_lic_files_chksum_presence(self):
        """Test presence of 'LIC_FILES_CHKSUM' on new recipes"""
        self.fail('TODO')

    def test_lic_files_chksum_modified_not_mentioned(self):
        """Test change on 'LIC_FILES_CHKSUM' and not mentioned on subject"""
        self.fail('TODO')
