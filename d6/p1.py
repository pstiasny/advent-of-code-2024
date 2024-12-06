#!/usr/bin/env python

from collections import defaultdict
import fileinput


obs = set()


gp = None
for i, l in enumerate(fileinput.input()):
    l = l.strip()
    for j, c in enumerate(l):
        if c == '^':
            gp = (i,j)
        if c == '#':
            obs.add((i, j))
H,W=i+1,j


vis = set()
di, dj = -1, 0
i, j = gp
while 0 <= i < H and 0 <= j < W:
    vis.add((i, j))
    for _ in range(4):
        ni, nj = i + di, j + dj
        if (ni, nj) not in obs:
            break
        di, dj = dj, di*(-1)
    i, j = ni, nj


print(len(vis))
