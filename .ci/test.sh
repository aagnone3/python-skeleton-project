#!/bin/bash
set -eoxu pipefail

TEST_DIR=${1:-/tmp/module_testing}

# ensure a clean temporary test directory
function ensure_clean_test_dir() {
    [[ -d ${TEST_DIR} ]] && rm -rf ${TEST_DIR}
    mkdir -p ${TEST_DIR}
}

function do_test() {
    cd ${TEST_DIR}
    PYTHONPATH=${PYTHONPATH:=}:${GITHUB_WORKSPACE} \
        py.test \
        --cov=${MODULE} \
        -xvs \
        --pyargs ${MODULE} \
        ${GITHUB_WORKSPACE}

    cp ${TEST_DIR}/.coverage ${GITHUB_WORKSPACE}
}

ensure_clean_test_dir
do_test
