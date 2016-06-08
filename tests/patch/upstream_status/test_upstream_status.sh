#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_upstream_status_presence() {
    local TMP
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Upstream-Status:.*/+/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_upstream_status_valid_status() {
    local TMP
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Upstream-Status:.*/+Upstream-Status:invalid/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_upstream_status_presence
test_upstream_status_valid_status
