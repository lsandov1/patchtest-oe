import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, info
from unittest import skip
from parse_subject import subject

class LicFilesChkSum(Base):

    licensemarks = re.compile('LIC_FILES_CHKSUM|LICENSE|CHECKSUM|CHKSUM', re.IGNORECASE)
    addmark      = re.compile('\s*\+LIC_FILES_CHKSUM\s*\??=')
    removemark   = re.compile('\s*-LIC_FILES_CHKSUM\s*\??=')
    newpatchrecipes = []

    @classmethod
    def setUpClassLocal(cls):
        """Gets those patches than introduced new recipe metadata"""
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.bb') or patch.path.endswith('.bbappend'):
                if patch.is_added_file:
                    cls.newpatchrecipes.append(patch)

    def test_lic_files_chksum_presence(self):
        for patch in self.newpatchrecipes:
            payload = str(patch)
            # verify that patch includes license file information
            if not self.addmark.search(payload):
                raise self.fail()

    def test_lic_files_chksum_modified_not_mentioned(self):
        for i in range(LicFilesChkSum.nmessages):
            payload = LicFilesChkSum.payloads[i]
            if self.addmark.search(payload) and self.removemark.search(payload):
                subject     = LicFilesChkSum.subjects[i]
                description = LicFilesChkSum.descriptions[i]
                # now lets search in the commit message (summary and description)
                if (not self.licensemarks.search(subject)) and \
                   (not self.licensemarks.search(description)):
                    raise self.fail()
