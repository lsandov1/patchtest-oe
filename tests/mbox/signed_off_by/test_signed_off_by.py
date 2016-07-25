import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile, match
from unittest import skip

class SignedOffBy(Base):

    @classmethod
    def setUpClassLocal(cls):
        # match self.mark with no '+' preceding it
        cls.mark = str(signed_off_by_mark).strip('"')
        cls.prog = compile("(?<!\+)%s" % cls.mark)

    @fix("""
Amend the commit including your signature:

    $ git commit --amend -s
    $ git format-patch -1
    $ git send-email --to <target mailing list> <created patch>""")
    def test_signed_off_by_presence(self):
        for i in xrange(SignedOffBy.nmessages):
            payload = SignedOffBy.payloads[i]
            if not SignedOffBy.prog.search(payload):
                self.fail([('Subject',     SignedOffBy.subjects[i]),
                           ('Description', SignedOffBy.descriptions[i])])

    @skip('due to http://bugzilla.yoctoproject.org/show_bug.cgi?id=9959')
    @fix("""
Amend the commit including your signature:

    $ git commit --amend -s
    $ git format-patch -1
    $ git send-email --to <target mailing list> <created patch>

NOTE: Make sure you have set your name and e-mail on the git configuration""")
    def test_signed_off_by_format(self):
        for payload in SignedOffBy.payloads:
            if not payload or not SignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % SignedOffBy.mark)
            for line in payload.splitlines():
                if match(self.mark, line):
                    try:
                        signed_off_by.parseString(line)
                    except ParseException as pe:
                        self.fail([('line', pe.line), ('column', pe.col)])

