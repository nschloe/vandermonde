# vandermonde

[![PyPi Version](https://img.shields.io/pypi/v/vandermonde.svg?style=flat-square)](https://pypi.org/project/vandermonde)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/vandermonde.svg?style=flat-square)](https://pypi.org/pypi/vandermonde/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/vandermonde.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/vandermonde)
[![PyPi downloads](https://img.shields.io/pypi/dm/vandermonde.svg?style=flat-square)](https://pypistats.org/packages/vandermonde)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/vandermonde/ci?style=flat-square)](https://github.com/nschloe/vandermonde/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/vandermonde.svg?style=flat-square)](https://codecov.io/gh/nschloe/vandermonde)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)


vandermonde is a module with a handful of tools for working with [Vandermonde
matrices](https://en.wikipedia.org/wiki/Vandermonde_matrix).
In particular, the [Björck-Pereyra algorithm](https://doi.org/10.1090/S0025-5718-1970-0290541-1 ) 
for solving systems with the Vandermonde matrix or its transposed is
implemented.

Example:
```python
import numpy as np
import vandermonde

x = np.linspace(0.0, 1.0, 14)
b = np.random.rand(len(x))

sol = vandermonde.solve(x, b)
```

### Installation

vandermonde is [available from the Python Package
Index](https://pypi.python.org/pypi/vandermonde/), so
simply do
```
pip install -U vandermonde
```
to install/update.

### License
vandermonde is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
