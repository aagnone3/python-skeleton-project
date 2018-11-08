#!/bin/bash
set -e

MODULE_DIR=${TRAVIS_BUILD_DIR}/${MODULE}
DOCS_BASE_DIR=${TRAVIS_BUILD_DIR}/docs

function error_out() {
    echo ${1}
    exit 1
}

# re-generate docs from docstrings
cd ${DOCS_BASE_DIR}
sphinx-apidoc -d 100 -f -M -e -P -o source ${MODULE_DIR}
[[ $? -eq 0 ]] || error_out "Failed to re-generate rst files with 'sphinx-apidoc'."

make html
[[ $? -eq 0 ]] || error_out "Failed to re-generate html files from the rst files."
