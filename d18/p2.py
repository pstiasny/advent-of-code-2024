#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv
import heapq


W = H = int(argv[1])
argv.pop(1)


m = {}
M = {}
for k, l in enumerate(fileinput.input()):
    x,y = map(int, l.strip().split(','))
    m[x,y] =k
    M[k] = (x,y)


for K in range(k+1):
    d = {}
    q = [(0, (0,0))]
    vis = set()
    while q:
        l, (x,y) = heapq.heappop(q)
        if m.get((x,y), inf) <= K:
            d[x,y]=inf
            continue
        d[x,y]=l
        if (x,y) == (W-1, H-1):
            break
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

    if (W-1, H-1) not in d:
        print(K, M[K])
        break

