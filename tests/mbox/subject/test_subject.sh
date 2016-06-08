#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

test_subject_presence() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail
    TMP=$(mktemp)
    sed -e 's/^Subject:.*//g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_subject_format() {
    # test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS

    # test fail: empty prefix
    TMP=$(mktemp)
    sed -e 's/^Subject:.*/Subject:[] a:b/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP

    # test fail: no target
    TMP=$(mktemp)
    sed -e 's/^Subject:.*/Subject:[a] b/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP

    # test fail: no summary
    TMP=$(mktemp)
    sed -e 's/^Subject:.*/Subject:[a] b:/g' $TESTMBOX > $TMP
    exec_patchtest $TESTDIR $FUNCNAME $TMP $FAIL
    rm $TMP
}

test_subject_presence
test_subject_format
