from unittest import TestCase
from logging import getLogger
from json import dumps
from unidiff import PatchSet
from patchtestdata import PatchTestInput as pti
from mailbox import mbox

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyparsing'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'msg'))

logger=getLogger('patchtest')
debug=logger.debug
info=logger.info
warn=logger.warn
error=logger.error

class OEBase(TestCase):
    def formaterror(self, reason, error, fix, cmd='', result='FAIL', stdout='', returncode=0, data=''):
        """Encodes failure data passed to the testing framework"""
        return dumps({'result': result,
                      'id': self.id(),
                      'cmd': cmd,
                      'stdout': stdout,
                      'return': returncode,
                      'reason': reason,
                      'error' : error,
                      'fix'   : fix,
                      'data'  : data})

    @classmethod
    def setUpClass(cls):

        cls.patchset = PatchSet.from_filename(pti.repo.patch)
        cls.mbox = mbox(pti.repo.patch)

        cls.setUpClassLocal()

    @classmethod
    def setUpClassLocal(cls):
        pass

