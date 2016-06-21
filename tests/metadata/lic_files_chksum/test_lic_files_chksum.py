import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from oediff import OEDiff
from oembox import OEMBox
import metadatamsg as msg

class OELicFilesChksum(OEDiff, OEMBox):
    # the reason of this double inheritance is that one test
    # check subject and patch data

    def test_lic_files_chksum_presence(self):
        self.fail(self.formaterror(msg.test_lic_files_chksum_presence.reason,
                                   msg.test_lic_files_chksum_presence.error,
                                   msg.test_lic_files_chksum_presence.fix,
                                   status='TODO'))

    def test_lic_files_chksum_modified_not_mentioned(self):
        self.fail(self.formaterror(msg.test_lic_files_chksum_modified_not_mentioned.reason,
                                   msg.test_lic_files_chksum_modified_not_mentioned.error,
                                   msg.test_lic_files_chksum_modified_not_mentioned.fix,
                                   status='TODO'))

