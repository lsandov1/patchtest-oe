from collections import defaultdict, OrderedDict

passstatus = 'PASS'
failstatus = 'FAIL'
skipstatus = 'SKIP'

todo = 'TODO'

keyid           = 'ID'
keystatus       = 'Status'
keydescription  = 'Description'
keyfix          = 'Proposed Fix'

class oedefaultdict(defaultdict):
    def __missing__(self, key):
        return list([(keyid,key), (keystatus,passstatus), (keydescription,key), (keyfix, todo)])

oemessages = oedefaultdict()

# Bitbake related messages
oemessages['OEBitbakeParse.pretest_bitbake_parse'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_parse'),
    (keystatus, failstatus),
    (keydescription,"Check correct bitbake parsing on non-modified repository"),
    (keyfix,"""Make sure you can bitbake parse manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -p
"""),
]

oemessages['OEBitbakeParse.test_bitbake_parse'] = [
    (keyid,'OEBitbakeParse.test_bitbake_parse'),
    (keystatus, failstatus),
    (keydescription,"Check correct bitbake parsing on (patchtest) patched repository"),
    (keyfix,"""Make sure you can bitbake parse manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -p
"""),
]

oemessages['OEBitbakeParse.pretest_bitbake_environment'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_environment'),
    (keystatus, failstatus),
    (keydescription,"Check correct bitbake environment on non-modified repository"),
    (keyfix,"""Make sure you can get the environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e
"""),
]

oemessages['OEBitbakeParse.test_bitbake_environment'] = [
    (keyid,'OEBitbakeParse.test_bitbake_environment'),
    (keystatus, failstatus),
    (keydescription,"Check correct bitbake environment on (patchtest) patched repository"),
    (keyfix,"""Make sure you can bitbake parse manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -e
"""),
]

oemessages['OEBitbakeParse.pretest_bitbake_environment_on_target'] = [
    (keyid,'OEBitbakeParse.pretest_bitbake_environment_on_target'),
    (keystatus, failstatus),
    (keydescription,"""Check correct bitbake environment on non-modified repository and a
specific target"""),
    (keyfix,"""Make sure you can get the environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e <target>
"""),
]

oemessages['OEBitbakeParse.test_bitbake_environment_on_target'] = [
    (keyid,'OEBitbakeParse.test_bitbake_environment_on_target'),
    (keystatus, failstatus),
    (keydescription,"""Check correct bitbake environment on (patchtest) patched repository
and a specific target"""),
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
    (keystatus, failstatus),
    (keydescription,"Check presence of patch subject"),
    (keyfix,"Commit your changes again and include a summary"),
]
oemessages['OESubject.test_subject_format'] = [
    (keyid,'OESubject.test_subject_format'),
    (keystatus, failstatus),
    (keydescription,"Check format of patch subject"),
    (keyfix,"""Commit your changes again and include a summary with 
the following format:
        
<target>: <summary>

where <target> is the filename where main code changes apply. The filename
should contain extension (py, sh or metadata extension) and if necessary
its base folder."""),
]

oemessages['OESignedOffBy.test_signed_off_by_presence'] = [
    (keyid,'OESignedOffBy.test_signed_off_by_presence'),
    (keystatus, failstatus),
    (keydescription,"Check presence of 'Signed-off-by' line"),
    (keyfix,"""Commit your changes with your signature:
$ git commit --amend -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>"""),
]

oemessages['OESignedOffBy.test_signed_off_by_format'] = [
    (keyid,'OESignedOffBy.test_signed_off_by_format'),
    (keystatus, failstatus),
    (keydescription,"Check format of 'Signed-off-by' line"),
    (keyfix,"""Commit your changes with your signature using git
$ git add file1 file2 ...
$ git commit -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>
"""),
]

# patch related messages
oemessages['OECVE.test_cve_presence_on_subject'] = [
    (keyid,'OECVE.test_cve_presence_on_subject'),
    (keystatus, failstatus),
    (keydescription, "Check presence of CVE number on patch subject"),
]

oemessages['OECVE.test_cve_tag_format'] = [
    (keyid,'OECVE.test_cve_tag_format'),
    (keystatus, failstatus),
    (keydescription, "Check format of 'CVE: CVE-XXXX-YYYY' on patch"),
]

oemessages['OEPatchSignedOffBy.test_signed_off_by_presence'] = [
    (keyid,'OEPatchSignedOffBy.test_signed_off_by_presence'),
    (keystatus, failstatus),
    (keydescription, "Check presence of 'Signed-off-by' line on included patch"),
]

oemessages['OEPatchSignedOffBy.test_signed_off_by_format'] = [
    (keyid,'OEPatchSignedOffBy.test_signed_off_by_format'),
    (keystatus, failstatus),
    (keydescription, "Check format of 'Signed-off-by' line on included patch"),
]

oemessages['OEPatchTrailingSpaces.test_patch_trailing_spaces'] = [
    (keyid,'OEPatchTrailingSpaces.test_patch_trailing_spaces'),
    (keystatus, failstatus),
    (keydescription, "Check presence of trailing spaces on patch"),
]

oemessages['OEPatchUpstreamStatus.test_upstream_status_presence'] = [
    (keyid,'OEPatchUpstreamStatus.test_upstream_status_presence'),
    (keystatus, failstatus),
    (keydescription, "Test presence of 'Upstream-Status'"),
]

oemessages['OEPatchUpstreamStatus.test_upstream_status_valid_status'] = [
    (keyid,'OEPatchUpstreamStatus.test_upstream_status_valid_status'),
    (keystatus, failstatus),
    (keydescription, "Test format of 'Upstream-Status'"),
]

oemessages['OEPyLint.test_pylint'] = [
    (keyid,'OEPyLint.test_pylint'),
    (keystatus, failstatus),
    (keydescription,"(Python)Lint modified python files"),
]

