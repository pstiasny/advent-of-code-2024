#!/usr/bin/env python

from fileinput import input
from collections import defaultdict

locs = {}
heights = defaultdict(list)

for i, l in enumerate(input()):
    for j, c in enumerate(l.strip()):
        y = int(c)
        locs[i, j]  = y
        heights[y].append((i,j))

reaches = defaultdict(set)
for loc in heights[9]:
    reaches[loc].add(loc)

for h in range(8, -1, -1):
    for i,j in heights[h]:
        for n in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if locs.get(n) == h+1:
                reaches[i,j].update(reaches[n])

print(reaches)
print(heights[0])

s = 0

for loc in heights[0]:
    s += len(reaches[loc])

print(s)
