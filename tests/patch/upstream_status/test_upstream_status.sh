#!/usr/bin/env bash

PTSUITE=$1
TEST=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_upstream_status_presence() {
    # test pass
    exec_patchtest $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Upstream-Status:.*/+/g' $TESTMBOX > $TMP
    exec_patchtest $TMP $FAIL
    rm $TMP
}

test_upstream_status_valid_status() {
    # test pass
    exec_patchtest $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^+Upstream-Status:.*/+Upstream-Status:invalid/g' $TESTMBOX > $TMP
    exec_patchtest $TMP $FAIL
    rm $TMP
}

# main
test_upstream_status_presence
test_upstream_status_valid_status
