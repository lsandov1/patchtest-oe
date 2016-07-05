from collections import defaultdict, OrderedDict

keyid           = 'ID'
keyfix          = 'Proposed Fix'

class oedefaultdict(defaultdict):
    def __missing__(self, key):
        return list([(keyid,key)])

oemessages = oedefaultdict()

# Bitbake related messages
oemessages['OEBitbakeParse.pretest_bitbake_parse'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_parse'),
    (keyfix,"""Make sure you can (bitbake) parse manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -p
"""),
]

oemessages['OEBitbakeParse.test_bitbake_parse'] = [
    (keyid,'OEBitbakeParse.test_bitbake_parse'),
    (keyfix,"""Make sure you can (bitbake) parse manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -p
"""),
]

oemessages['OEBitbakeParse.pretest_bitbake_environment'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_environment'),
    (keyfix,"""Make sure you can get the (bitbake) environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e
"""),
]

oemessages['OEBitbakeParse.test_bitbake_environment'] = [
    (keyid,'OEBitbakeParse.test_bitbake_environment'),
    (keyfix,"""Make sure you can get the (bitbake) environment manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -e
"""),
]

oemessages['OEBitbakeParse.pretest_bitbake_environment_on_target'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_environment_on_target'),
    (keyfix,"""Make sure you can get the environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e <target>
"""),
]

oemessages['OEBitbakeParse.test_bitbake_environment_on_target'] = [
    (keyid,'OEBitbakeParse.test_bitbake_environment_on_target'),
    (keyfix,"""Make sure you can get the environment manually on a specific target
after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -e <target>
"""),
]

# MBOX related messages
oemessages['OESubject.test_subject_presence'] = [
    (keyid,'OESubject.test_subject_presence'),
    (keyfix,"""Amend the commit message and include a summary with
the following format:

<target>: <summary>

where <target> is the filename where main code changes apply."""),
]

oemessages['OESubject.test_subject_format'] = [
    (keyid,'OESubject.test_subject_format'),
    (keyfix,"""Amend the commit message and include a summary with
the following format:

<target>: <summary>

where <target> is the filename where main code changes apply."""),
]

oemessages['OESignedOffBy.test_signed_off_by_presence'] = [
    (keyid,'OESignedOffBy.test_signed_off_by_presence'),
    (keyfix,"""Amend the commit including your signature:
$ git commit --amend -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>"""),
]

oemessages['OESignedOffBy.test_signed_off_by_format'] = [
    (keyid,'OESignedOffBy.test_signed_off_by_format'),
    (keyfix,"""Amend the commit including your signature:
$ git commit --amend -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>

NOTE: Make sure you have configured git before, setting name and email
correctly.
"""),
]

# patch related messages
oemessages['OECVE.test_cve_presence_on_subject'] = [
    (keyid,'OECVE.test_cve_presence_on_subject'),
]

oemessages['OECVE.test_cve_tag_format'] = [
    (keyid,'OECVE.test_cve_tag_format'),
]

oemessages['OEPatchSignedOffBy.test_signed_off_by_presence'] = [
    (keyid,'OEPatchSignedOffBy.test_signed_off_by_presence'),
    (keyfix, """Every patch added next to a recipe must be signed off,
so amend every commit and include your signature:
$ git commit --amend -s
$ git format-patch -1
"""),
]

oemessages['OEPatchSignedOffBy.test_signed_off_by_format'] = [
    (keyid,'OEPatchSignedOffBy.test_signed_off_by_format'),
    (keyfix, """Every patch added next to a recipe must be signed off,
so amend every commit and include your signature:
$ git commit --amend -s
$ git format-patch -1

NOTE: Make sure you have configured git before, setting name and email
correctly.
""")

]

oemessages['OEPatchTrailingSpaces.test_patch_trailing_spaces'] = [
    (keyid,'OEPatchTrailingSpaces.test_patch_trailing_spaces'),
]

oemessages['OEPatchUpstreamStatus.test_upstream_status_presence'] = [
    (keyid,'OEPatchUpstreamStatus.test_upstream_status_presence'),
    (keyfix, """Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines
"""),
]

oemessages['OEPatchUpstreamStatus.test_upstream_status_valid_status'] = [
    (keyid,'OEPatchUpstreamStatus.test_upstream_status_valid_status'),
    (keyfix, """Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines
""")
]

oemessages['OEPyLint.test_pylint'] = [
    (keyid,  'OEPyLint.test_pylint'),
    (keyfix, """Check your modified python lines with pylint, specially those being
introduced by your changes"""),
]

