#!/usr/bin/env python

import fileinput
from collections import defaultdict
from itertools import product


d = defaultdict(set)


for i, l in enumerate(fileinput.input()):
    for j, c in enumerate(l.strip()):
        if c == '.': continue
        d[c].add((i,j))
H,W = i+1,j+1


s = set()
for c, p in d.items():
    pairs = product(p, p)
    for a, b in pairs:
        if a == b: continue
        (ai, aj) = a
        (bi, bj) = b
        di = bi-ai
        dj = bj-aj

        pi, pj = ai, aj
        while 0 <= pi < H and 0 <= pj < W:
            s.add((pi, pj))
            pi += di
            pj += dj
        pi, pj = ai, aj
        while 0 <= pi < H and 0 <= pj < W:
            s.add((pi, pj))
            pi -= di
            pj -= dj
print( len(s) )
