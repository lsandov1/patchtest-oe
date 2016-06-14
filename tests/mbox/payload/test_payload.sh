#!/usr/bin/env bash
#
# Script to test assertions for test_payload.py
#

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_payload_presence() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e '/^$/q' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_payload_presence
