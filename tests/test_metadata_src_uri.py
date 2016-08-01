import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix
from re import compile
from subprocess import check_output
from unittest import skip

class SrcUri(Base):

    metadata_regex = compile('[\+|-]\s*\S*file://(\S+\.\w*)')

    @fix("Amend the patch containing the software patch file removal")
    def test_src_uri_left_files(self):
        # get the removed files indicated on diff data
        removed_diff_files = set()
        for removed_file in SrcUri.patchset.removed_files:
            removed_diff_files.add(os.path.basename(removed_file.path))

        # get the removed files indicated on the bitbake metadata
        removed_metadata_files = set()
        for payload in SrcUri.payloads:
            for line in payload.splitlines():
                match = self.metadata_regex.search(line)
                if match:
                    patch = match.group(1)
                    if line.startswith('-'):
                        removed_metadata_files.add(patch)
                    if line.startswith('+'):
                        if match in removed_metadata_files:
                            removed_metadata_files.remove(patch)

        if removed_metadata_files.difference(removed_diff_files):
            self.fail()

    @skip('pending')
    def test_src_uri_checksums_not_changed(self):
        for patch in SrcUri.patchset:
            payload = str(patch)