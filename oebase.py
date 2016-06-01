from unittest import TestCase
from tempfile import NamedTemporaryFile
from mailbox import mbox
from patchtestdata import PatchTestInput as pti
from logging import getLogger

debug=getLogger('patchtest').debug
info=getLogger('patchtest').info

class OEBase(TestCase):

    @classmethod
    def setUpClass(cls):

        # create the mbox objects
        cls.mboxes = [mbox(item.resource) for item in pti.repo.items]
            
