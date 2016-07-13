import sys, os
from re import compile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, info

class Bugzilla(Base):
    base_url = "https://bugzilla.yoctoproject.org/show_bug.cgi?id=%s"

    def test_bugzilla_entry_format(self):
        rexp_detect = compile("\[.*[Y|y][O|o][C|c][T|t][O|o].*\]")
        rexp_validation = compile("^\[YOCTO #(\d+)\]$")
        for message in Bugzilla.mbox:
            payload = message.get_payload()
            for line in payload.splitlines():
                if rexp_detect.match(line):
                    if not rexp_validation.match(line):
                        self.fail([('Entry', line)])

