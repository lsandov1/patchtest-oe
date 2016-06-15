from unittest import TestCase
from logging import getLogger

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyparsing'))

logger=getLogger('patchtest')
debug=logger.debug
info=logger.info
warn=logger.warn

class OEBase(TestCase):
    pass
