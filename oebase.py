from unittest import TestCase
from logging import getLogger

debug=getLogger('patchtest').debug
info=getLogger('patchtest').info

class OEBase(TestCase):
    pass
