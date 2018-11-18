.. -*- mode: rst -*-

|Travis|_ |PyPi|_ |TestStatus|_ |PythonVersion|_

.. |Travis| image:: https://travis-ci.org/aagnone3/python-skeleton-project-project.svg?branch=master
.. _Travis: https://travis-ci.org/aagnone3/python-skeleton-project-project

.. |PyPi| image:: https://badge.fury.io/py/python-skeleton-project-project.svg
.. _PyPi: https://badge.fury.io/py/python-skeleton-project-project

.. |TestStatus| image:: https://travis-ci.org/aagnone3/python-skeleton-project-project.svg
.. _TestStatus: https://travis-ci.org/aagnone3/python-skeleton-project-project.svg

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/python-skeleton-project-project.svg
.. _PythonVersion: https://img.shields.io/pypi/pyversions/python-skeleton-project-project.svg

python-skeleton-project-project
================

python-skeleton-project-project is a barebones repository intended as a quick-start for new python
applications which plan to utilize the following functionalities:
- Unit testing with pytest
- Continuous integration testing with Travis CI
- Packaging and publishing to PyPi
- Documentation with Sphinx and Github Pages

Documentation
-------------

Documentation can be found at the github pages here_

.. _here: https://aagnone3.github.io/python-skeleton-project-project/

Dependencies
~~~~~~~~~~~~

python-skeleton-project-project is tested to work under Python 3.x.
See the requirements via the following command:

.. code-block:: bash

  cat requirements.txt

Installation
~~~~~~~~~~~~

python-skeleton-project-project is currently available on the PyPi's repository and you can
install it via `pip`:

.. code-block:: bash

  pip install -U python-skeleton-project-project

If you prefer, you can clone it and run the setup.py file. Use the following
commands to get a copy from GitHub and install all dependencies:

.. code-block:: bash

  git clone https://github.com/aagnone3/python-skeleton-project-project.git
  cd python-skeleton-project-project
  pip install .

Or install using pip and GitHub:

.. code-block:: bash

  pip install -U git+https://github.com/aagnone3/python-skeleton-project-project.git

Testing
~~~~~~~

.. code-block:: bash

  make test
  
