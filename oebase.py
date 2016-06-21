from unittest import TestCase
from logging import getLogger
from json import dumps

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyparsing'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'msg'))

logger=getLogger('patchtest')
debug=logger.debug
info=logger.info
warn=logger.warn

class OEBase(TestCase):
    def formaterror(self, reason, error, fix, data='', status='FAIL'):
        """Encodes failure data passed to the testing framework"""
        return dumps({'status': status,
                      'reason': reason,
                      'error' : error,
                      'fix'   : fix,
                      'data'  : data})

