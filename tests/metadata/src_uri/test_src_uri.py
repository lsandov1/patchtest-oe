import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff
import metadatamsg as msg

class OESrcUri(OEDiff):

    def test_src_uri_left_files(self):
        self.fail(self.formaterror(msg.test_src_uri_left_files.reason,
                                   msg.test_src_uri_left_files.error,
                                   msg.test_src_uri_left_files.fix,
                                   status='TODO'))


    def test_src_uri_checksums_not_changed(self):
        """Test that checksums changed if SRC_URI upstream changed"""
        self.fail(self.formaterror(msg.test_src_uri_checksums_not_changed.reason,
                                   msg.test_src_uri_checksums_not_changed.error,
                                   msg.test_src_uri_checksums_not_changed.fix,
                                   status='TODO'))

