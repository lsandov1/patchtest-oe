import sys
import os
from mailbox import mbox
from patchtestdata import PatchTestInput as pti

# insert root folder, so system can use base class
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
from oebase import OEBase

class OEMBox(OEBase):
    @classmethod
    def setUpClass(cls):

        # create the mbox objects
        cls.mboxes = [mbox(item.resource) for item in pti.repo.items]
