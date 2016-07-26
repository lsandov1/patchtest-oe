import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix
from re import compile
from subprocess import check_output
from unittest import skip

class SrcUri(Base):

    removepatch_regex = compile('-\s*file://(\S+\.patch)')
    addpatch_regex    = compile('\+\s*file://(\S+\.patch)')
    patch_regex       = compile('\.patch$')

    @fix("Amend the patch containing the software patch file removal")
    def test_src_uri_left_files(self):
        # get the removed patches indicated on diff data
        removed_diff_patches = set()
        for remove_file in SrcUri.patchset.removed_files:
            path = remove_file.path
            if self.patch_regex.search(path):
                removed_diff_patches.add(os.path.basename(path))

        # get the removed patches indicated on the bitbake metadata
        removed_metadata_patches = set()
        for payload in SrcUri.payloads:
            for line in payload.splitlines():
                removematch = self.removepatch_regex.search(line)
                addmatch    = self.addpatch_regex.search(line)
                if removematch:
                    removed_metadata_patches.add(removematch.group(1))
                if addmatch:
                    removed_metadata_patches.remove(addmatch.group(1))

        # sets removed_diff_patches and removed_metadata_patches should be the same
        # if not, lets check if other recipes need the patch file
        if removed_metadata_patches.difference(removed_diff_patches):
            self.fail()

    @skip('pending')
    def test_src_uri_checksums_not_changed(self):
        for patch in SrcUri.patchset:
            payload = str(patch)
