#!/bin/bash

# Change directory to tests dir.
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pushd ${SCRIPT_DIR} &> /dev/null

TESTS=("and" "and16" "dmux" "dmux4way" "dmux8way" "mux" "mux4way16" "mux8way16" "mux16" "not" "not16" "or" "or8way" "or16" "xor")

for TEST in ${TESTS[@]};
do
    # Skip if file not present
    [[ ! -s ../${TEST}.v ]] && {
        echo "${TEST}.v not found"
        continue
    }

    iverilog -o /tmp/${TEST}_test.vvp ${TEST}_test.v ../${TEST}.v
    vvp /tmp/${TEST}_test.vvp 2> /dev/null | head -n -1 1> /tmp/${TEST}.out 2> /dev/null
    diff /tmp/${TEST}.out expected-outputs/${TEST}.cmp -qsw --strip-trailing-cr &> /dev/null && echo "${TEST^^} Test Passed"
done

popd &> /dev/null
