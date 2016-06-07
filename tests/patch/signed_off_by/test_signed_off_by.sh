#!/usr/bin/env bash

PTSUITE=$1
TEST=$2
TESTMBOX=$3

# source the runner's lib, containing function definitions
source $PTSUITE/selftest/librunner.sh

# test pass
exec_patchtest $TESTMBOX $PASS

# test fail
TMP=$(mktemp)
sed -e 's/^+Signed-off-by:.*/+/g' $TESTMBOX > $TMP
exec_patchtest $TMP $FAIL
rm $TMP
