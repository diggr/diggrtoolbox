============
Installation
============

It is recommended to use *diggrtoolbox* in a virtualenvironment such as `virtualenv <https://virtualenv.pypa.io/en/stable/>`_. Please refer to the documentation of virtualenv and/or `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_ or `pipenv <https://docs.pipenv.org/>`_ to see how to set it up.

*diggrtoolbox* is provided in two versions. The stable version is recommended for all users who are interested in using the software for their research project. The unstable version is for users who want to use the software, but require the latest features and bugfixes who were not yet merged into the stable version. Th

Stable via the Python Package Index (PyPI)
------------------------------------------

Currently, the project is not yet published to the Python Package Index, but in the future you will be able to install the project with pip::

    pip install diggrtoolbox

Unstable via github
-------------------

Clone the github repository and install with pip::

    git clone git@github.com/digr/diggrtoolbox
    pip install ./diggrtoolbox

Development
-----------

If you plan to develop *diggrtoolbox* it is recommended to clone the github repository::

    git clone git@github.com/diggr/diggrtoolbox

Installation is performed using pip, but in editable mode, i.e. such that changes in the source take effect immediately::

    pip install -e ./diggrtoolbox
