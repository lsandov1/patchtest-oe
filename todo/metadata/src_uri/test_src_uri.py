import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
import metadatamsg as msg

class OESrcUri(OEBase):

    def test_src_uri_left_files(self):
        for patch in OESrcUri.patchset:
            payload = str(patch)
            self.fail(self.formaterror(msg.test_src_uri_left_files.reason,
                                       msg.test_src_uri_left_files.error,
                                       msg.test_src_uri_left_files.fix,
                                       status='TODO'))

    def test_src_uri_checksums_not_changed(self):
        for patch in OESrcUri.patchset:
            payload = str(patch)
            self.fail(self.formaterror(msg.test_src_uri_checksums_not_changed.reason,
                                       msg.test_src_uri_checksums_not_changed.error,
                                       msg.test_src_uri_checksums_not_changed.fix,
                                       status='TODO'))

