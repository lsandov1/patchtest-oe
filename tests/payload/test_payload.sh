#!/usr/bin/env bash
#
# Script to test assertions for test_payload.py
#

test_payload_presence() {
    MBOX=$1
    EXPECTED_RESULT=$2
    TESTRESULT=$(patchtest --test-dir $PTSUITE -m $MBOX --no-patch | \
	sed -n -e "/$TEST/p")

    if [ -z "$(echo "$TESTRESULT" | sed -n -e "/$EXPECTED_RESULT/p")" ]; then
        echo "$TESTRESULT $EXPECTED_RESULT"
    fi
}

# test pass
test_payload_presence $TESTMBOX $PASS

# test fail
NOPAYLOAD=$(mktemp)
sed -e '/^$/q' $TESTMBOX > $NOPAYLOAD
test_payload_presence $NOPAYLOAD $FAIL
rm $NOPAYLOAD

