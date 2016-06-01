from unittest import TestCase
from tempfile import NamedTemporaryFile
from mailbox import mbox
from patchtestdata import PatchTestInput as pti

class OEBase(TestCase):

    @classmethod
    def setUpClass(cls):

        # dump item contents into temporary files
        cls.fns = []
        for item in pti.repo.items:
            fn = NamedTemporaryFile(delete=True)
            fn.write(item.contents.encode('utf-8'))
            cls.fns.append(fn)

        # create the mbox objects
        cls.mboxes = [mbox(fn.name) for fn in cls.fns]

    @classmethod
    def tearDownClass(cls):
        # close (and remove) temporary files
        for fn in cls.fns:
            fn.close()
            
