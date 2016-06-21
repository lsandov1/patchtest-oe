class bitbake:
    patch_has_no_bbfiles="Patch data does not modified any bb or bbappend file"

class pretest_bitbake_parse:
    reason="Check correct bitbake parsing on non-modified repository"
    error="Bitbake failed to parse current metadata"
    fix="""Make sure you can bitbake parse manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -p
"""

class test_bitbake_parse:
    reason="Check correct bitbake parsing on (patchtest) patched repository"
    error="Bitbake failed to parse on (patchtest) patched metadata"
    fix="""Make sure you can bitbake parse manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -p
"""

class pretest_bitbake_environment:
    reason="Check correct bitbake environment on non-modified repository"
    error="Bitbake failed to show current environment"
    fix="""Make sure you can get the environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e
"""

class test_bitbake_environment:
    reason="Check correct bitbake environment on (patchtest) patched repository"
    error="""Bitbake failed to show environment on (patchtest) patched metadata"""
    fix="""Make sure you can bitbake parse manually after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -e
"""

class pretest_bitbake_environment_on_target:
    reason="""Check correct bitbake environment on non-modified repository and a
specific target"""
    error="Bitbake failed to show current environment on a specific target"
    fix="""Make sure you can get the environment manually before using patchtest:
$ cd <your poky repo>
$ source oe-init-build-env
$ bitbake -e <target>
"""

class test_bitbake_environment_on_target:
    reason="""Check correct bitbake environment on (patchtest) patched repository
and a specific target"""
    error="""Bitbake failed to show environment on (patchtest) patched metadata and
a specific target"""
    fix="""Make sure you can get the environment manually on a specific target
after patching:
$ cd <your poky repo>
$ git am <your patch>
$ source oe-init-build-env
$ bitbake -e <target>
"""

