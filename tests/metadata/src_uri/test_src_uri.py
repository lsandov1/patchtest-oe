import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oediff import OEDiff

class OESrcUri(OEDiff):

    def test_src_uri_left_files(self):
        """Test that files are removed if these are removed from the SRC_URI"""
        self.fail('TODO')

    def test_src_uri_checksums_not_changed(self):
        """Test that checksums changed if SRC_URI upstream changed"""
        self.fail('TODO')
