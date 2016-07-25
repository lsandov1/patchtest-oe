import sys, os
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix

class Bugzilla(Base):
    rexp_detect     = re.compile("\[.*YOCTO.*\]", re.IGNORECASE)
    rexp_validation = re.compile("\[YOCTO #(\d+)\]$")

    @fix("""
Amend the commit message and include the bugzilla entry at the end of the commit description as

    [YOCTO #<bugzilla ID>]

where <bugzilla ID> is the bugzilla entry that this patch fixes""")
    def test_bugzilla_entry_format(self):
        for description in Bugzilla.descriptions:
            for line in description.splitlines():
                if self.rexp_detect.match(line):
                    if not self.rexp_validation.match(line):
                        self.fail([('Entry', line)])

