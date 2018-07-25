DIGGR toolbox
=============

This collection of tools was developed in the Databased infrastructure for global game culture reasearch (diggr) group at the University Library in Leipzig. Being a collection means, that these helpers are organised into individual packages. Each package is built for one purpose, but the functionality and purpose across functionality may be differ.

Requirements
------------

This Software was tested with Python 3.5 and 3.6. There are no further requirements. *diggrtoolboxes* uses only packages and modules which are shipped with Python. Only exception: If you plan development on *diggrtoolbox* you need to have *pytest* to run the tests.

Components
----------

* *deepget*: A small helper easing access to data in deeply nested dicts/list, by separating the definition of the route and actual call.
* *ZipSingleAccess*: Allows access to a JSON document in a ZIP-File.
* *ZipMultiAccess*: Allows access to a JSON document in a ZIP-File, where some parts of the original JSON document are separated into separate json documents. This eases the handling of large files, which otherwise would clog the RAM.
* *TreeExplore*: Class to help exploring deeply nested dicts/lists/both. It provides various helpful display and search functions. It can help exploring raw dumps aquired from APIs on the internet. The search function returns a route-object which can be fed to deepget, in order to retrieve specific datasets.
* *treehash*: Allows comparison of complex data structures by hashing it. It allows to compare deeply nested dicts/lists/both without having to compare its individual components.

Authors
-------

* F. Rämisch <raemisch@ub.uni-leipzig.de>
* P. Mühleder <muehleder@ub.uni-leipzig.de>

License
-------

* `GNU General Public License <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.

Copyright
---------

* `Universitätsbibliothek Leipzig <https://ub.uni-leipzig.de>`_, 2018.
