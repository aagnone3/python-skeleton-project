[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Faagnone3%2Fpython-skeleton-project%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/aagnone3/python-skeleton-project/goto?ref=master)

[![PyPi](https://badge.fury.io/py/python-skeleton-project.svg)](https://badge.fury.io/py/python-skeleton-project)

[![TestStatus](https://travis-ci.org/aagnone3/python-skeleton-project.svg)](https://travis-ci.org/aagnone3/python-skeleton-project.svg)

[![PythonVersion](https://img.shields.io/pypi/pyversions/python-skeleton-project.svg)](https://img.shields.io/pypi/pyversions/python-skeleton-project.svg)

# python-skeleton-project

python-skeleton-project is a barebones repository intended as a quick-start for new python
applications which plan to utilize the following functionalities:

- Unit testing with pytest
- Continuous integration testing with Github Actions
- Containerization via Docker
- Packaging and publishing to PyPi
- Documentation with Sphinx and Github Pages

# Documentation

Documentation can be found [here](https://aagnone3.github.io/python-skeleton-project/) via Github Pages.

# Dependencies

python-skeleton-project is tested to work under Python 3.x.
See the requirements via the following command:

```bash
cat requirements.txt
```

# Installation

Simply use `pip`:
```bash
pip install -U python-skeleton-project
# or
pip install .
```

# Testing

## Docker
```bash
make test
```
  