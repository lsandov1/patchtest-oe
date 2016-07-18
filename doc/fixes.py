from collections import defaultdict, OrderedDict

class oedefaultdict(defaultdict):
    def __missing__(self, key):
        return str('No proposed fix yet')

fixes = oedefaultdict()

# Bitbake
fixes['bitbake.parse.test_parse.BitbakeParse.test_bitbake_parse'] = """
Make sure you can (bitbake) parse manually after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -p

"""

fixes['bitbake.parse.test_parse.BitbakeParse.test_bitbake_environment'] = """
Make sure you can get the (bitbake) environment manually after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -e

"""

fixes['bitbake.parse.test_parse.BitbakeParse.test_bitbake_environment_on_target'] = """
Make sure you can get the environment manually on a specific target
after patching:

    $ cd <your poky repo>
    $ git am <your patch>
    $ source oe-init-build-env
    $ bitbake -e <target>

"""

# MBOX
fixes['test_description.Description.test_description_presence'] = """
Please include a brief description for your patch.
"""

fixes['mbox.bugzilla.test_bugzilla.Bugzilla.test_bugzilla_entry_format'] = """
Amend the commit message and include the bugzilla entry at the end of the
commit description as

    [YOCTO #<bugzilla ID>]

where <bugzilla ID> is the bugzilla entry that this patch fixes.
"""


fixes['Subject.test_subject_presence'] = """
Amend the commit message and include a summary with the following format:

    <target>: <summary>

where <target> is the filename where main code changes apply.
"""

fixes['Subject.test_subject_format'] = """
Amend the commit message and include a summary with the following format:

<target>: <summary>

where <target> is the filename where main code changes apply.
"""

fixes['SignedOffBy.test_signed_off_by_presence'] = """
Amend the commit including your signature:

    $ git commit --amend -s
    $ git format-patch -1
    $ git send-email --to <target mailing list> <created patch>

"""

fixes['SignedOffBy.test_signed_off_by_format'] = """
Amend the commit including your signature:

    $ git commit --amend -s
    $ git format-patch -1
    $ git send-email --to <target mailing list> <created patch>

NOTE: Make sure you have set your name and e-mail on the git configuration.
"""

# Patch
fixes['test_lic_files_chksum.LicFilesChkSum.test_lic_files_chksum_modified_not_mentioned'] = """
Provide a reason for the checksum change on the commit's summary
"""
fixes['test_lic_files_chksum.LicFilesChkSum.test_lic_files_chksum_presence'] = """
Specify the variable LIC_FILES_CHKSUM on your new recipe.
"""

fixes['test_cve.CVE.test_cve_presence_on_subject'] = """
Please include the CVE, as CVE-xxxx-xxxx, in the subject
"""

fixes['test_cve.CVE.test_cve_tag_format'] = """
Please include the CVE tag on the patch added to the recipe, see:
http://openembedded.org/wiki/Commit_Patch_Message_Guidelines#CVE_Patches
"""

fixes['PatchSignedOffBy.test_signed_off_by_presence'] = """
Every patch added next to a recipe must be signed off, so amend every commit
and include your signature:

    $ git commit --amend -s
    $ git format-patch -1

"""

fixes['PatchSignedOffBy.test_signed_off_by_format'] = """
Every patch added next to a recipe must be signed off, so amend every commit
and include your signature:

    $ git commit --amend -s
    $ git format-patch -1

NOTE: Make sure you have configured git before, setting name and email
correctly.
"""

fixes['PatchUpstreamStatus.test_upstream'] = """
Every patch added next to a recipe must have an Upstream-Status
specified in the patch header having the value of Pending, Submitted, Accepted, Backport,
Denied, or Inappropriate. Make sure your are following this format

    Upstream-Status: <status>

NOTE: For more information on the meaning of each status, check
http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines
"""

fixes['PyLint.test_pylint'] = """
Check your modified python lines with pylint, specially those being introduced by your
changes.
"""

