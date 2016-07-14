import sys, os
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base

class Bugzilla(Base):
    rexp_detect     = re.compile("\[.*YOCTO.*\]", re.IGNORECASE)
    rexp_validation = re.compile("\[YOCTO #(\d+)\]$")

    def test_bugzilla_entry_format(self):
        for description in Bugzilla.descriptions:
            for line in description.splitlines():
                if self.rexp_detect.match(line):
                    if not self.rexp_validation.match(line):
                        self.fail([('Entry', line)])

