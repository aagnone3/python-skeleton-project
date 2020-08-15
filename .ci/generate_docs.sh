#!/bin/bash
set -eoxu pipefail

cd ${GITHUB_WORKSPACE}/docs
sphinx-apidoc \
    -d 100 \
    -f \
    -M \
    -e \
    -P \
    -o "source" \
    ${GITHUB_WORKSPACE}/${MODULE}

make html
ls -R
