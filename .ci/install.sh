#!/bin/bash
set -eoxu pipefail

# install test dependencies
pip install --upgrade pip
pip install pytest pytest-cov codecov sphinx black flake8 pre-commit

# install the package
pip install .
