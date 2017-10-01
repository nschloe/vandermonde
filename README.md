# vandermonde

[![Build Status](https://travis-ci.org/nschloe/vandermonde.svg?branch=master)](https://travis-ci.org/nschloe/vandermonde)
[![codecov](https://codecov.io/gh/nschloe/vandermonde/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/vandermonde)
[![PyPi Version](https://img.shields.io/pypi/v/vandermonde.svg)](https://pypi.python.org/pypi/vandermonde)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/vandermonde.svg?style=social&label=Star&maxAge=2592000)](https://github.com/nschloe/vandermonde)

vandermonde is a module with a handful of tools for working with [Vandermonde
matrices](https://en.wikipedia.org/wiki/Vandermonde_matrix).
In particular, the [Björck-Pereyra algorithm](https://doi.org/10.1090/S0025-5718-1970-0290541-1 ) 
for solving systems with the Vandermonde matrix or its transposed is
implemented.

Example:
```python
import vandermonde

x = numpy.linspace(0.0, 1.0, 14)
b = numpy.random.rand(len(x))

sol = vandermonde.solve(x, b)
```

### Installation

vandermonde is [available from the Python Package
Index](https://pypi.python.org/pypi/vandermonde/), so
simply type
```
pip install -U vandermonde
```
to install/update.

### Testing

To run the tests, check out the repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    make publish
    ```

### License

vandermonde is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
