from base import Base
from unittest import skip

# this check is being track at https://bugzilla.yoctoproject.org/show_bug.cgi?id=9876
# According to Paul/Ross, this check is too paranoid/negligible but it wont be removed
# because it may be useful for some people

# When parsing the patch data, empty lines turn into lines
# with one space. This problem is matching with the proposed
# regex so giving false positives, so for the moment this test
# will be skipped

@skip('Not accepted by community and also it could catch false positives')
class TrailingSpaces(Base):

    def test_patch_trailing_spaces(self):

        """
        Summary:  Check if patches contain trailing white spaces.
        Steps:    1. Read all the patches defined in the patcset.
                  2. Get the payload of the patch.
                  3. Check line by line to find trailing spaces.

        Expected: No trailing spaces found in patch
        Author:   Jose Perez Carranza <jose.perez.carranza@intel.com>
        """

        for patch in TrailingSpaces.patchset:
            payload = str(patch)
            for line in payload.splitlines():
                 if re.search('.\s$',line):
                    self.fail()
