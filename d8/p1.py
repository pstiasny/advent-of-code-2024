#!/usr/bin/env python

import fileinput
from collections import defaultdict
from itertools import product


d = defaultdict(set)


def pp(s):
    for i in range(H):
        for j in range(W):
            if (i,j) in s: print('O', end='')
            else: print('.', end='')
        print()
    print('&&&&&')
    print()

t = 0
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
        Ai = ai -di
        Aj = aj-dj
        if 0 <= Ai < H and 0 <= Aj < W:
            s.add((Ai, Aj))
            # t+=1
        Bi = bi+di
        Bj = bj+dj
        if 0 <= Bi < H and 0 <= Bj < W:
            s.add((Bi, Bj))
            # t+=1
    # print(s)
t += len(s)



print(t)
