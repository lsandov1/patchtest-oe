#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_bugzilla_entry_format() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail: yocto word in lower case
    TMP=$(mktemp)
    sed -e 's/^\[YOCTO.*\]/\[yocto #0000\]/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP

    # TODO: test fail: missing '#'
    # TODO: test fail: bugzilla entry not a number
    # TODO: test fail: YOCTO with no surrounding square brackets
}

test_bugzilla_entry_format
