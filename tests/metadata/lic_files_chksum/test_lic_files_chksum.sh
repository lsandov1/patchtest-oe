#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_lic_files_chksum_presence() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # TODO: test fail: new recipe, no LIC_FILES_CHKSUM
}

test_lic_files_chksum_modified_not_mentioned() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # TODO: test fail: change chksum, no comment on subject
}

test_lic_files_chksum_presence
test_lic_files_chksum_modified_not_mentioned
