# -*- coding: utf-8 -*-
#


def solve(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(n):
        for j in range(n-1, k, -1):
            x[j] -= alpha[k] * x[j-1]

    for k in range(n - 1, 0, -1):
        for j in range(k, n):
            x[j] /= alpha[j] - alpha[j-k]
        for j in range(k, n):
            x[j-1] -= x[j]

    return x


def solveT(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(1, n):
        for j in range(n, k, -1):
            x[j-1] = (x[j-1] - x[j-2]) / (alpha[j-1] - alpha[j-k-1])

    for k in range(n-1, 0, -1):
        for j in range(k, n):
            x[j-1] -= alpha[k-1] * x[j]

    return x
