#!/usr/bin/env python

import fileinput
from math import inf
from sys import stdin
import heapq
from collections import deque, defaultdict


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
cost[s,d] = 0
q = [(0,s,d)]
pre = {}
pre[s,d] = set()

seats = set()

while q:
    # print(q)
    c, s, d = heapq.heappop(q)
    # print(c, s, d)
    # if s == e :
    #     seats.update(P)
    if (s, d) in vis:
        continue
    vis.add((s,d))

    x, y = s
    dx, dy = d
    n = nx, ny = x+dx, y+dy

    if m.get((nx, ny)) != '#':
        lv = cost.get((n, d), inf)
        if c+1 < lv:
            pre[n, d] = set()
            cost[n, d] = c+1
        if c+1 <= lv:
            pre[n, d].add((s, d))
        heapq.heappush(q, (c+1, n, d))

    for dr in [(-dy, dx), (dy, -dx)]:
        lv = cost.get((s, dr), inf)
        if c+ 1000 < lv:
            pre[s, dr] = set()
            cost[s, dr] = c+1000
        if c+ 1000 <= lv:
            pre[s, dr].add((s,d))
        heapq.heappush(q, (c+1000, s, dr))


def back(p, d):
    seats.add(p)
    for n,d in pre.get((p,d), []):
        back(n, d)
best =min(
    cost[e, (0, 1)],
    cost[e, (1, 0)],
    cost[e, (0, -1)],
    cost[e, (-1, 0)],
)

for d in [ (0, 1), (1, 0), (0, -1), (-1, 0), ]:
    if cost[e, d] == best:
        back(e, d)

print(len(seats))
