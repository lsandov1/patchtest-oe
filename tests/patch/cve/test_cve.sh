#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_cve_tag_format() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail: cve tag in lower case
    TMP=$(mktemp)
    sed -e 's/^+CVE.*/cve: CVE-XXXX-YYYY/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP

    # TODO: test fail: cve value in lower case
    # TODO: test fail: no ':' separator
    # TODO: test fail: no XXXX-YYYY
}

test_cve_presence_on_subject() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS
}
test_cve_tag_format
