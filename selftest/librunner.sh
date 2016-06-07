# variables
PASS='PASS'
FAIL='FAIL'

# functions

#
# Execute patchtest and compare current result with expected result.
# On error, print the test. It expects PTSUITE and TEST variables
# already defined
#
exec_patchtest() {
    MBOX=$1
    EXPECTED_RESULT=$2

    TESTRESULT=$(patchtest --test-dir $PTSUITE -m $MBOX --no-patch | \
	sed -n -e "/$TEST/p")

    if [ -z "$(echo "$TESTRESULT" | sed -n -e "/$EXPECTED_RESULT/p")" ]; then
        echo "$TESTRESULT $EXPECTED_RESULT"
    fi
}

# convert a filepath into a python unittest id
testid() {
    echo $1 | sed -e 's/\//./g' \
	          -e 's/^.*\.tests\./tests\./g' \
                  -e 's/\.sh//g'
}
