import sys
import os
from mailbox import mbox
from patchtestdata import PatchTestInput as pti

basepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))
pyparsepath = os.path.join(basepath, 'pyparsing')
if not basepath in sys.path:
    sys.path.insert(0, basepath)
if not pyparsepath in sys.path:
    sys.path.insert(0, pyparsepath)

from oebase import OEBase

class OEMessage(OEBase):
    @classmethod
    def setUpClass(cls):

        # create the mbox objects
        cls.mboxes = [mbox(item.resource) for item in pti.repo.items]
