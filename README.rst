leicascanningtemplate
=====================

|build-status-image| |pypi-version|

Overview
--------

Convenience library for talking with Leica matrix screener scanning
template XMLs.

Installation
------------

Install using ``pip``...

.. code:: bash

    pip install leicascanningtemplate

Example
-------

.. code:: python

    from leicaleicascanningtemplate import ScanningTemplate

    tmpl = ScanningTemplate('path/to/scantempl.xml')
    tmpl.add_well(well_x=2, well_y=3, start_x=30e-3, start_y=44e-3)
    tmpl.write()

API reference
-------------

http://leicascanningtemplate.readthedocs.org/

Development
-----------

Install dependencies and link development version of
leicascanningtemplate to pip:

.. code:: bash

    pip install -r dev-requirements.txt
    ./setup.py develop

Testing
~~~~~~~

.. code:: bash

    tox

Build documentation locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation, you'll need sphinx:

.. code:: bash

    pip install -r docs/requirements.txt

To build the documentation:

.. code:: bash

    make docs

.. |build-status-image| image:: https://secure.travis-ci.org/arve0/leicascanningtemplate.png?branch=master
   :target: http://travis-ci.org/arve0/leicascanningtemplate?branch=master
.. |pypi-version| image:: https://pypip.in/version/leicascanningtemplate/badge.svg
   :target: https://pypi.python.org/pypi/leicascanningtemplate
