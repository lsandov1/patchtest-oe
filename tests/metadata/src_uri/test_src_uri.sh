#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_src_uri_left_files() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # TODO: test fail: remove file items on SRC_URI but no patches removing these
}

test_src_uri_checksums_not_changed() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # TODO: test fail: change SRC_URI upstream but no checksums
}

test_src_uri_left_files
test_src_uri_checksums_not_changed
