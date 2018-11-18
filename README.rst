.. -*- mode: rst -*-

|Travis|_ |PyPi|_ |TestStatus|_ |PythonVersion|_

.. |Travis| image:: https://travis-ci.org/aagnone3/python-skeleton-project.svg?branch=master
.. _Travis: https://travis-ci.org/aagnone3/python-skeleton-project

.. |PyPi| image:: https://badge.fury.io/py/python-skeleton-project.svg
.. _PyPi: https://badge.fury.io/py/python-skeleton-project

.. |TestStatus| image:: https://travis-ci.org/aagnone3/python-skeleton-project.svg
.. _TestStatus: https://travis-ci.org/aagnone3/python-skeleton-project.svg

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/python-skeleton-project.svg
.. _PythonVersion: https://img.shields.io/pypi/pyversions/python-skeleton-project.svg

python-skeleton-project
================

python-skeleton-project is a barebones repository intended as a quick-start for new python
applications which plan to utilize the following functionalities:
- Unit testing with pytest
- Continuous integration testing with Travis CI
- Packaging and publishing to PyPi
- Documentation with Sphinx and Github Pages

Documentation
-------------

Documentation can be found at the github pages here_

.. _here: https://aagnone3.github.io/python-skeleton-project/

Dependencies
~~~~~~~~~~~~

python-skeleton-project is tested to work under Python 3.x.
See the requirements via the following command:

.. code-block:: bash

  cat requirements.txt

Installation
~~~~~~~~~~~~

python-skeleton-project is currently available on the PyPi's repository and you can
install it via `pip`:

.. code-block:: bash

  pip install -U python-skeleton-project

If you prefer, you can clone it and run the setup.py file. Use the following
commands to get a copy from GitHub and install all dependencies:

.. code-block:: bash

  git clone https://github.com/aagnone3/python-skeleton-project.git
  cd python-skeleton-project
  pip install .

Or install using pip and GitHub:

.. code-block:: bash

  pip install -U git+https://github.com/aagnone3/python-skeleton-project.git

Local Testing
~~~~~~~~~~~~~

.. code-block:: bash

  make test
  
Travis Testing
~~~~~~~~~~~~~~

The `Makefile`, `.travis.yml` file and `.ci` directory contain the structure necessary to have Travis_ test the repository upon all branch updates. Some additional steps, however, are needed:

* Enable the repository to be monitored by Travis via your Travis profile.
* Generate a Github app token, and assign it to the (private) environment variable ${GITHUB_TOKEN} in the Travis environment.

.. _Travis: https://travis-ci.org
