#!/usr/bin/env bash

TESTMBOX=$1

if [ -z "$TESTMBOX" ]; then
    echo "Please provide a filepath to a mbox file"
    exit -1
else
    TESTMBOX=$(realpath $TESTMBOX)
fi

CD=$(dirname $0)
SELFTESTDIR=$(realpath $CD)
PTSUITE=$(dirname $SELFTESTDIR)

for script in $(find $PTSUITE -name '*.sh'); do
    # run all scripts except this script
    if [ -z "$(echo "$script" | sed -n -e '/selftest\/runner.sh/p')" ]; then
	source $script
    fi
done
