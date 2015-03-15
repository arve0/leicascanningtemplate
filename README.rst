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

    # x stage position of field
    print(tmpl.field(well_x=1, well_y=1, field_x=1, field_y=1).FieldXCoordinate)

Read more on available elements and attributes in
`SCANNINGTEMPLATE.md <SCANNINGTEMPLATE.md>`__.

Documentation
-------------

Read about available commands in the API reference:
http://leicascanningtemplate.rtfd.org/

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

    pip install tox
    tox

Build documentation locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation:

.. code:: bash

    make docs

.. |build-status-image| image:: https://secure.travis-ci.org/arve0/leicascanningtemplate.png?branch=master
   :target: http://travis-ci.org/arve0/leicascanningtemplate?branch=master
.. |pypi-version| image:: https://pypip.in/version/leicascanningtemplate/badge.svg
   :target: https://pypi.python.org/pypi/leicascanningtemplate
