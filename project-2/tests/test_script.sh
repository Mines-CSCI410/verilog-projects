#!/bin/bash

# Change directory to tests dir.
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pushd ${SCRIPT_DIR} &> /dev/null

TESTS=("half_adder" "full_adder" "inc16" "add16" "alu")

for TEST in ${TESTS[@]};
do
    # Skip if file not present
    [[ ! -s ../${TEST}.v ]] && {
        echo "${TEST}.v not found"
        continue
    }

    iverilog -o /tmp/${TEST}_test.vvp ${TEST}_test.v ../*.v
    vvp /tmp/${TEST}_test.vvp 2> /dev/null 1> /tmp/${TEST}.out 2> /dev/null
    diff /tmp/${TEST}.out expected-outputs/${TEST}.cmp -qsw --strip-trailing-cr &> /dev/null && echo "${TEST^^} Test Passed" || echo "${TEST^^} Test Failed"
done

popd &> /dev/null
