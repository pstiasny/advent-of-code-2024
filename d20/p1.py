#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv, stdin
import heapq

# N = int(argv[1])
# argv.pop(1)

c = 0
wall = set()
for i, l in enumerate(fileinput.input()):
    for j, c in enumerate(l.strip()):
        if c == '#':
            wall.add((i,j))
        if c == 'S':
            s = (i,j)
        if c == 'E':
            e = (i,j)
W,H = i+1, j+1


d = {}
q = [(0, e)]
vis = set()
while q:
    l, p = heapq.heappop(q)
    x, y = p
    if  p in wall:
        d[x,y]=inf
        continue

    d[x,y]=l
    if (x,y) in vis:
        continue
    vis.add((x,y))

    if x+1 < W:
        heapq.heappush(q, (l+1, (x+1, y)))
    if x-1 >= 0:
        heapq.heappush(q, (l+1, (x-1, y)))
    if y+1 < H:
        heapq.heappush(q, (l+1, (x, y+1)))
    if y-1 >= 0:
        heapq.heappush(q, (l+1, (x, y-1)))


c = 0
for (x,y) in wall:
    for a, b in [
        ( (x-1, y), (x+1, y) ),
        ( (x, y-1), (x, y+1) ),
        ( (x-1, y), (x, y-1) ),
        ( (x-1, y), (x, y+1) ),
        ( (x+1, y), (x, y-1) ),
        ( (x+1, y), (x, y+1) ),
    ]:
        da = d.get(a, inf)
        db = d.get(b, inf)
        if da == inf or db ==inf: continue
        D = abs(da-db) - 2
        # print(D)
        if D >= 100:
            c+=1
print('fastest', d[s])
print(c)
