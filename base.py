from unittest import TestCase
from logging import getLogger
from json import dumps
from unidiff import PatchSet, UnidiffParseError
from patchtestdata import PatchTestInput as pti
from mailbox import mbox
from collections import defaultdict
import sys, os
import re
from functools import wraps

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyparsing'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'doc'))

logger=getLogger('patchtest')
debug=logger.debug
info=logger.info
warn=logger.warn
error=logger.error

def fix(msg):
    def dec(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            return f(*args, **kwds)
        wrapper.__name__ = f.__name__
        wrapper.fix = msg
        return wrapper
    return dec

class Base(TestCase):
    # if unit test fails, fail message will throw at least the following JSON: [('ID', testid)]
    testid = 'testid'
    fix    = 'fix'

    regex_enddescriptions = re.compile('\(From \w+-\w+ rev:|(?<!\S)Signed-off-by|(?<!\S)---\n')

    @classmethod
    def setUpClass(cls):

        def description(payload):
            description = str()
            match = cls.regex_enddescriptions.search(payload)
            if match:
                description = payload[:match.start()]
            return description

        def subject(sub):
            i = sub.find(']')
            return sub[i+1:].replace('\n','').strip()

        # General objects: mbox and patchset
        cls.mbox = mbox(pti.repo.patch)
        f = open(pti.repo.patch, 'r')
        cls.patchset = PatchSet(f, encoding=u'UTF-8')

        # Derived objects: nmessages, subjects, payloads and descriptions
        cls.nmessages    = len(cls.mbox)
        cls.subjects     = [subject(msg['subject']) for msg in cls.mbox]
        cls.payloads     = [msg.get_payload()       for msg in cls.mbox]
        cls.descriptions = [description(pay)        for pay in cls.payloads]

        cls.setUpClassLocal()

    @classmethod
    def setUpClassLocal(cls):
        pass

    def fail(self, data=[]):
        """ Convert to a JSON string failure data"""
        value = list([(Base.testid, self.id())])

        # extend return value with possible fix info
        test = getattr(self, self._testMethodName)
        if hasattr(test, 'fix'):
            value.extend([(Base.fix, test.fix)])

        # extend return value with other useful info
        if data:
            value.extend(data)

        return super(Base, self).fail(dumps(value))

    def __str__(self):
        return dumps(list([(Base.testid, self.id())]))
