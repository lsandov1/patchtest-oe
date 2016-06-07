#!/usr/bin/env bash

TESTMBOX=$1

if [ -z "$TESTMBOX" ]; then
    echo "Please provide a filepath to a mbox file"
    exit -1
else
    TESTMBOX=$(realpath $TESTMBOX)
fi

# local variables
CD=$(dirname $0)
SELFTESTDIR=$(realpath $CD)

# variables exported to test scripts + TEST
PTSUITE=$(dirname $SELFTESTDIR)

source $SELFTESTDIR/librunner.sh

for TESTPATH in $(find $PTSUITE -name '*.sh' | \
                sed -n -e "/selftest/!p"); do

    # convert a filepath into a test id
    TESTID=$(testid $TESTPATH)

    # execute the script
    $TESTPATH $PTSUITE $TESTID $TESTMBOX

done
