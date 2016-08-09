#!/usr/bin/python

# Base class to be used by all test cases defined in the suite
#
# Copyright (C) 2016 Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from unittest import TestCase, SkipTest
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
    testid = 'Test ID'
    fix    = 'Proposed Fix'

    enddescriptions_regex = re.compile('\(From \w+-\w+ rev:|(?<!\S)Signed-off-by|(?<!\S)---\n')

    @classmethod
    def setUpClass(cls):

        def description(payload):
            description = str()
            match = cls.enddescriptions_regex.search(payload)
            if match:
                description = payload[:match.start()]
            return description

        def subject(sub):
            # remove possible prefix (between brackets) before colon
            start = sub.find(']', 0, sub.find(':'))

            # remove also newlines and spaces at both sides
            return sub[start + 1:].replace('\n', '').strip()

        # Check if patch exists and not empty
        if not os.path.exists(pti.repo.patch):
            raise SkipTest('Patch not found')
        if os.path.getsize(pti.repo.patch) == 0:
            raise SkipTest('Empty patch')

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
