from unittest import TestCase
from logging import getLogger
from json import dumps
from unidiff import PatchSet, UnidiffParseError
from patchtestdata import PatchTestInput as pti
from mailbox import mbox
from collections import defaultdict
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyparsing'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'doc'))

logger=getLogger('patchtest')
debug=logger.debug
info=logger.info
warn=logger.warn
error=logger.error

class OEBase(TestCase):
    keyid = 'ID'

    @classmethod
    def setUpClass(cls):

        # General objects: mbox and patchset
        cls.mbox = mbox(pti.repo.patch)
        f = open(pti.repo.patch, 'r')
        cls.patchset = PatchSet(f, encoding=u'UTF-8')

        # Derived objects: nmessages, subjects, payloads and descriptions
        cls.nmessages    = len(cls.mbox)

        fullsubjects     = [message['subject'] for message in cls.mbox]
        endprefixindexes = [fullsubject.find(']') for fullsubject in fullsubjects]
        cls.subjects     = [fullsubjects[i][endprefixindexes[i]+1:].replace('\n','') for i in range(len(fullsubjects))]

        cls.payloads     = [msg.get_payload() for msg in cls.mbox]

        enddescriptions  = [((payload.find('Signed-off-by:')>=0) or payload.find('---')) for payload in cls.payloads]
        cls.descriptions = [cls.payloads[i][:enddescriptions[i]] for i in range(cls.nmessages)]

        cls.setUpClassLocal()

    @classmethod
    def setUpClassLocal(cls):
        pass

    def fail(self, data=[]):
        """ Convert to a JSON string failure data"""
        value = list([(OEBase.keyid, self.id())])
        if data:
            value.extend(data)
        return super(OEBase, self).fail(dumps(value))
