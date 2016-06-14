#!/usr/bin/env bash

TESTMBOX=$1
TESTCASEDIR=$2

if [ -z "$TESTMBOX" ]; then
    echo "Please provide a filepath to a mbox file"
    exit -1
else
    TESTMBOX=$(realpath $TESTMBOX)
fi

CD=$(dirname $0)
SELFTESTDIR=$(realpath $CD)
PTSUITE=$(dirname $SELFTESTDIR)
TESTSDIR="$PTSUITE/tests"

source $SELFTESTDIR/librunner.sh

if [ -z $TESTCASEDIR ]; then
    TESTCASEDIR=$TESTSDIR
fi

for TESTPATH in $(find $TESTCASEDIR -name '*.sh' | sed -e "/selftest/d"); do

    # test case directory
    TESTDIR=$(dirname $TESTPATH)

    CMD="$TESTPATH $PTSUITE $TESTDIR $TESTMBOX"
    echo "Executing $CMD"
    $CMD

done
