#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_patch_trailing_spaces() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # TODO: test fail: create a mbox with patches containing trailing spaces
}

test_patch_trailing_spaces
