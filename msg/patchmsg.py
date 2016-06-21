class test_cve_presence_on_subject:
    reason="Check presence of CVE number on patch subject"
    error="TODO"
    fix="TODO"

class test_cve_tag_format:
    reason="Check format of 'CVE: CVE-XXXX-YYYY' on patch"
    error="TODO"
    fix="TODO"


class test_signed_off_by_presence:
    reason="Check presence of 'Signed-off-by' line on included patch"
    error="The included patch has not been signed off"
    fix="TODO: explain instructions using devtool"


class test_signed_off_by_format:
    reason="Check format of 'Signed-off-by' line on included patch"
    error="The included patch has been signed off but it has wrong format"
    fix="TODO: provide instructions using devtool"

class test_patch_trailing_spaces:
    reason="Check presence of trailing spaces on patch"
    error="TODO"
    fix="TODO"

class test_upstream_status_presence:
    reason="Test presence of 'Upstream-Status'"
    error="TODO"
    fix="TODO"

class test_upstream_status_valid_status:
    reason="Test format of 'Upstream-Status'"
    error="TODO"
    fix="TODO"

