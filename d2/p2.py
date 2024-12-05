#!/usr/bin/env python

import fileinput
from math import inf
from unittest.mock import ANY


pos = True
neg = False

c = 0
for l in fileinput.input():
    X = [int(x, 10) for x in l.strip().split(' ')]

    E = {}
    for i, x in enumerate(X):
        for dsign in [pos, neg]:
            E[i, dsign] = inf
            if i == 0:
                E[i, dsign] = 0
            if i == 1:
                E[i, dsign] = 1
            if i >= 1 and (X[i] - X[i-1] > 0) == dsign and 1 <= abs(X[i] - X[i-1]) <= 3:
                E[i, dsign] = min(E[i, dsign], E[i-1, dsign])
            if i >= 2 and (X[i] - X[i-2] > 0) == dsign and 1 <= abs(X[i] - X[i-2]) <= 3:
                E[i, dsign] = min(E[i, dsign], E[i-2, dsign] + 1)

    # print(X, E)
    best = min(E[len(X) - 1, pos], E[len(X) - 1, neg])
    if len(X) >= 2:
        best = min(E[len(X) - 2, pos] + 1, E[len(X) - 2, neg] + 1, best)
    if best <= 1:
        c+=1

print(c)
