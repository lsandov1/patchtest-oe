import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from base import Base, fix
from parse_signed_off_by import signed_off_by, signed_off_by_mark
from pyparsing import ParseException
from re import compile
from unittest import skip

class PatchSignedOffBy(Base):

    @classmethod
    def setUpClassLocal(cls):
        cls.newpatches = []
        # get just those relevant patches: new software patches
        for patch in cls.patchset:
            if patch.path.endswith('.patch') and patch.is_added_file:
                cls.newpatches.append(patch)

        cls.mark = str(signed_off_by_mark).strip('"')

        # match PatchSignedOffBy.mark with '+' preceding it
        cls.prog = compile("(?<=\+)%s" % cls.mark)

    @fix("""
Every patch added next to a recipe must be signed off, so amend every commit
and include your signature:

    $ git commit --amend -s
    $ git format-patch -1""")
    def test_signed_off_by_presence(self):
        if not PatchSignedOffBy.newpatches:
            self.skipTest("There are no new software patches, no reason to test %s presence" % PatchSignedOffBy.mark)

        for newpatch in PatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not PatchSignedOffBy.prog.search(payload):
                self.fail()

    @skip('due to http://bugzilla.yoctoproject.org/show_bug.cgi?id=9959')
    @fix("""
Every patch added next to a recipe must be signed off, so amend every commit
and include your signature:

    $ git commit --amend -s
    $ git format-patch -1

NOTE: Make sure you have configured git before, setting name and email
correctly"""
    def test_signed_off_by_format(self):
        for newpatch in PatchSignedOffBy.newpatches:
            payload = str(newpatch)
            if not payload or not PatchSignedOffBy.prog.search(payload):
                self.skipTest("%s not present, skipping format test" % PatchSignedOffBy.mark)
            for line in payload.splitlines():
                if PatchSignedOffBy.prog.search(line):
                    try:
                        signed_off_by.parseString(line.lstrip('+'))
                    except ParseException as pe:
                        self.fail([('line', pe.line), ('column', pe.col)])

