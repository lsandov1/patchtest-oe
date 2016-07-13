import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base
from unittest import skip

@skip('Not implemented yet')
class SrcUri(Base):
    def test_src_uri_left_files(self):
        for patch in SrcUri.patchset:
            payload = str(patch)

    def test_src_uri_checksums_not_changed(self):
        for patch in SrcUri.patchset:
            payload = str(patch)
