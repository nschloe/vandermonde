# -*- coding: utf-8 -*-
#
import vandermonde
import numpy


def test_solve():
    n = 5
    x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)

    ref_sol = numpy.ones(n)
    V = vandermonde.matrix(x)
    b = numpy.dot(V, ref_sol)

    sol = vandermonde.solve(x, b)

    assert max(abs(sol - ref_sol)) < 1.0e-14
    return


def test_solve_transpose():
    n = 5
    x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)

    ref_sol = numpy.ones(n)
    V = vandermonde.matrix(x)
    b = numpy.dot(V.T, ref_sol)

    sol = vandermonde.solve_transpose(x, b)

    assert max(abs(sol - ref_sol)) < 1.0e-14
    return


def test_determinant():
    n = 5
    x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)
    d = numpy.linalg.det(vandermonde.matrix(x))
    assert abs(d - vandermonde.det(x)) < 1.0e-14
    return
