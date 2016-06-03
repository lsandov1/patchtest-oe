import sys
import os

basepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))
if not basepath in sys.path:
    sys.path.insert(0, basepath)

from oediff import OEDiff

class OEPatch(OEDiff):
    pass
