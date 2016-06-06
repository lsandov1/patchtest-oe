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
export PTSUITE=$(dirname $SELFTESTDIR)
export TESTMBOX
export PASS='PASS'
export FAIL='FAIL'

for script in $(find $PTSUITE -name '*.sh'); do
    # run all scripts except this script
    if [ -z "$(echo "$script" | sed -n -e '/selftest\/runner.sh/p')" ]; then
	export TEST=$(echo $script | sed -e 's/\//./g' -e 's/^.*\.tests\./tests\./g' -e 's/\.sh//g')
	$script
    fi
done
