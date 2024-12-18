#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv
import heapq

N = int(argv[1])
argv.pop(1)

W = H = int(argv[1])
argv.pop(1)


m = set()
for k, l in enumerate(fileinput.input()):
    if k == N:
        break
    x,y = map(int, l.strip().split(','))
    m.add((x,y))

def pp():
    for j in range(H):
        for i in range(W):
            if (i,j) in m: print('#', end='')
            elif (i,j) in d: print('O', end='')
            else: print('.', end='')
        print()
    print('&&&&&')
    print()


d = {}
q = [(0, (0,0))]
vis = set()
while q:
    l, (x,y) = heapq.heappop(q)
    if (x,y) in m:
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

pp()
print(d[W-1, H-1])
