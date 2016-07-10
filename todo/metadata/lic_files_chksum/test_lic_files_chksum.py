import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from oebase import OEBase
from unittest import skip
from parse_subject import subject

class OELicFilesChksum(OEBase):
    def test_lic_files_chksum_presence(self):
        for patch in OELicFilesChksum.patchset:
            # Get relevant patches: new .bb and .bbappend
            if patch.path.endswith('.bb') or patch.path.endswith('.bbappend'):
                # If this patch adds the .bb or .bbappend file
                if patch.is_added_file:
                    payload = str(patch)
                    # verify that patch includes license file information
                    if ((not payload.find('LIC_FILES_CHKSUM =') == -1) |
                        (not payload.find('LIC_FILES_CHKSUM ?=') == -1)):
                        # if it does, then we are ok
                        return
                    else:
                        # if it does not include it, patch does not have 
                        # required license file information
                        raise self.fail()


    def test_lic_files_chksum_modified_not_mentioned(self):
        self.sub = 'subject'
        for patch in OELicFilesChksum.patchset:
            # Get relevant patches: modified .bb and .bbappend
            if patch.path.endswith('.bb') or patch.path.endswith('.bbappend'):
                if patch.is_modified_file:
                    payload = str(patch)
                    # verify if license file information is modified
                    if ((not payload.find('-LIC_FILES_CHKSUM ') == -1) |
                        (not payload.find('+LIC_FILES_CHKSUM ') == -1)):
                        # verify that the modification is mentioned in subject
                        for message in OELicFilesChksum.mbox:
                            # Fail if subject is empty
                            try:
                                msgsubj = message[self.sub]
                            except:
                                self.fail()
                            # If subject contains the mention, we are ok
                            if (not msgsubj.find('LIC_FILES_CHKSUM') == -1):
                                return
                            # Split commit message from diff
                            fullmsg = message.get_payload(decode=True)
                            msglimit = message.get_payload().find('---')
                            commsg = fullmsg[:msglimit]

                            # If the mention is in commit message, we're ok
                            if (not commsg.find('LIC_FILES_CHKSUM') == -1):
                                return
                            else:
                                self.fail()
