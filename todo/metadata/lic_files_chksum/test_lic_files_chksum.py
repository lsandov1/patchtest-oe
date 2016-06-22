import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from oebase import OEBase
import metadatamsg as msg

class OELicFilesChksum(OEBase):

    def test_lic_files_chksum_presence(self):
        for patch in OELicFilesChksum.patchset:
            payload = str(patch)
            self.fail(self.formaterror(msg.test_lic_files_chksum_presence.reason,
                                       msg.test_lic_files_chksum_presence.error,
                                       msg.test_lic_files_chksum_presence.fix,
                                       status='TODO'))

    def test_lic_files_chksum_modified_not_mentioned(self):
        for patch in OELicFilesChksum.patchset:
            payload = str(patch)
            self.fail(self.formaterror(msg.test_lic_files_chksum_modified_not_mentioned.reason,
                                       msg.test_lic_files_chksum_modified_not_mentioned.error,
                                       msg.test_lic_files_chksum_modified_not_mentioned.fix,
                                       status='TODO'))

