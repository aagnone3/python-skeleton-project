.. -*- mode: rst -*-

|Travis|_ |PyPi|_ |TestStatus|_ |PythonVersion|_

.. |Travis| image:: https://travis-ci.org/aagnone3/python-skeleton.svg?branch=master
.. _Travis: https://travis-ci.org/aagnone3/python-skeleton

.. |PyPi| image:: https://badge.fury.io/py/python-skeleton.svg
.. _PyPi: https://badge.fury.io/py/python-skeleton

.. |TestStatus| image:: https://travis-ci.org/aagnone3/python-skeleton.svg
.. _TestStatus: https://travis-ci.org/aagnone3/python-skeleton.svg

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/python-skeleton.svg
.. _PythonVersion: https://img.shields.io/pypi/pyversions/python-skeleton.svg

python-skeleton
================

python-skeleton is a barebones repository intended as a quick-start for new python
applications which plan to utilize the following functionalities:
- Unit testing with pytest
- Continuous integration testing with Travis CI
- Packaging and publishing to PyPi
- Documentation with Sphinx and Github Pages

Documentation
-------------

Documentation can be found at the github pages here_

.. _here: https://aagnone3.github.io/python-skeleton/

Dependencies
~~~~~~~~~~~~

python-skeleton is tested to work under Python 3.x.
See the requirements via the following command:

.. code-block:: bash

  cat requirements.txt

Installation
~~~~~~~~~~~~

python-skeleton is currently available on the PyPi's repository and you can
install it via `pip`:

.. code-block:: bash

  pip install -U python-skeleton

If you prefer, you can clone it and run the setup.py file. Use the following
commands to get a copy from GitHub and install all dependencies:

.. code-block:: bash

  git clone https://github.com/aagnone3/python-skeleton.git
  cd python-skeleton
  pip install .

Or install using pip and GitHub:

.. code-block:: bash

  pip install -U git+https://github.com/aagnone3/python-skeleton.git

Testing
~~~~~~~

.. code-block:: bash

  make test
  
