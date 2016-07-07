import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from unittest import skip

@skip('Not implemented yet')
class OELicFilesChksum(OEBase):
    def test_lic_files_chksum_presence(self):
        for patch in OELicFilesChksum.patchset:
            payload = str(patch)

    def test_lic_files_chksum_modified_not_mentioned(self):
        for patch in OELicFilesChksum.patchset:
            payload = str(patch)
