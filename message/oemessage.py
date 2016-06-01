import sys
import os

# insert relevant folders
basepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))
pyparsepath = os.path.join(basepath, 'pyparsing')

if not basepath in sys.path:
    sys.path.insert(0, basepath)

if not pyparsepath in sys.path:
    sys.path.insert(0, pyparsepath)

from oebase import OEBase

class OEMessage(OEBase):
    pass
