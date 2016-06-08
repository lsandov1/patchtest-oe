#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_signed_off_presence() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Signed-off-by:.*/+/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_signed_off_by_format() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Signed-off-by:.*/+Signed-off-by:just name/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Signed-off-by:.*/+Signed-off-by:<just@email.com>/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_signed_off_presence
test_signed_off_by_format
