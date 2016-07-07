import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from unittest import skip

@skip('Not implemented yet')
class OESrcUri(OEBase):
    def test_src_uri_left_files(self):
        for patch in OESrcUri.patchset:
            payload = str(patch)

    def test_src_uri_checksums_not_changed(self):
        for patch in OESrcUri.patchset:
            payload = str(patch)
