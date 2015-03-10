# leicascanningtemplate

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview
Convenience library for talking with Leica matrix screener scanning template XMLs.

## Installation
Install using `pip`...

```bash
pip install leicascanningtemplate
```

## Example
```python
from leicaleicascanningtemplate import ScanningTemplate

tmpl = ScanningTemplate('path/to/scantempl.xml')
tmpl.add_well(well_x=2, well_y=3, start_x=30e-3, start_y=44e-3)
tmpl.write()
```

## API reference
http://leicascanningtemplate.readthedocs.org/


## Development
Install dependencies and link working version of leicascanningtemplate to pip:
```bash
pip install -r dev-requirements.txt
./setup.py develop
```

### Testing
```bash
tox
```

### Build documentation locally
To build the documentation, you'll need sphinx:
```bash
pip install -r docs/requirements.txt
```

To build the documentation:
```bash
make docs
```


[build-status-image]: https://secure.travis-ci.org/arve0/leicascanningtemplate.png?branch=master
[travis]: http://travis-ci.org/arve0/leicascanningtemplate?branch=master
[pypi-version]: https://pypip.in/version/leicascanningtemplate/badge.svg
[pypi]: https://pypi.python.org/pypi/leicascanningtemplate
