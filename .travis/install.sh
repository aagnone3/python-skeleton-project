#!/bin/bash
set -e

# install test dependencies
pip install --upgrade pip
pip install pytest pytest-cov codecov sphinx

# install the package
pip install .
