import sys
import os
from unidiff import PatchSet
from patchtestdata import PatchTestInput as pti

basepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))
pyparsepath = os.path.join(basepath, 'pyparsing')
if not basepath in sys.path:
    sys.path.insert(0, basepath)
if not pyparsepath in sys.path:
    sys.path.insert(0, pyparsepath)

from oebase import OEBase

class OEDiff(OEBase):

    @classmethod
    def setUpClass(cls):
        # create patchset objects
        cls.patchsets = [PatchSet.from_filename(item.resource) for item in pti.repo.items]

        # call possible classmethod implemented in an OEDiff inherited class
        cls.setUpClassLocal()

    @classmethod
    def setUpClassLocal(cls):
        pass

