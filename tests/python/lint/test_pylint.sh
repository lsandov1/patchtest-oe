#!/usr/bin/env bash

PTSUITE=$1
TESTDIR=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

pretest_pylint() {
    #test pass
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $PASS
}

test_pylint() {
    # test fail
    exec_patchtest $TESTDIR $FUNCNAME $TESTMBOX $FAIL
}

pretest_pylint
test_pylint
