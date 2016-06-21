class test_payload_presence:
    reason="Check presence of patch payload"
    error="Patch does not contain any code change"
    fix="""Include your code changes in your patch using
$ git add file1 file2 ...
$ git commit -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>
"""

class test_bugzilla_entry_format:
    reason="""Check '[YOCTO #XXXX]' format on description"""
    error="TODO"
    fix="TODO"

class test_description_presence:
    reason="""Check presence of patch description"""
    error="TODO"
    fix="TODO"

class test_signed_off_by_presence:
    reason="Check presence of 'Signed-off-by' line"
    error="The patch has not been signed off"
    fix="""Commit your changes with your signature:
$ git commit --amend -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>
"""
class test_signed_off_by_format:
    reason="Check format of 'Signed-off-by' line"
    error="The patch has been signed off but it has wrong format"
    fix="""Commit your changes with your signature using git
$ git add file1 file2 ...
$ git commit -s
$ git format-patch -1
$ git send-email --to <target mailing list> <created patch>
"""

class test_subject_presence:
    reason="Check presence of patch subject"
    error="The patch does not contain a subject"
    fix="Commit your changes again and include a summary"

class test_subject_format:
    reason="Check format of patch subject"
    error="The subject has a wrong format"
    fix="""Commit your changes again and include a summary with the
following format:

<target>: <summary>

where <target> is the filename where main code changes apply. The filename
should contain extension (py, sh or metadata extension) and if necessary
its base folder.
"""


