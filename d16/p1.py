#!/usr/bin/env python

import fileinput
from math import inf
from sys import stdin
import heapq
from collections import deque



c = 0
m = {}
for i, l in enumerate(fileinput.input()):
    for j, c in enumerate(l.strip()):
        match c:
            case 'S':
                s = (i,j)
            case 'E':
                e = (i,j)

            case _:
                m[i,j]=c

d = (0, 1)

vis = set()
cost =  {}
cost[s] = 0
q = [(0,s,d)]

while True:
    # print(q)
    if not q:
        raise ValueError('no result')
    c, s, d = heapq.heappop(q)
    # print(c, s, d)
    if s == e:
        break
    if (s, d) in vis:
        continue
    vis.add((s,d))

    x, y = s
    dx, dy = d
    nx, ny = x+dx, y+dy

    if m.get((nx, ny)) != '#':
        # print('can enter', nx, ny)
        cost[nx, ny] = min(cost.get((nx,ny), inf), c+1)
        heapq.heappush(q, (c+1, (nx,ny), d))
    heapq.heappush(q, (c+1000, s, (-dy, dx)))
    heapq.heappush(q, (c+1000, s, (dy, -dx)))


print(cost[e])
