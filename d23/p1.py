#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv, stdin
import heapq
import string
from pprint import pprint
from collections import deque, defaultdict
from itertools import combinations

t = 0
con = defaultdict(set)
for i, l in enumerate(fileinput.input()):
    a, b = l.strip().split('-')
    con[a].add(b)
    con[b].add(a)



combs = set()
for k in list(con.keys()):
    if k not in con:
        continue

    for b,c in combinations(con[k], 2):
        if c not in con[b]:
            continue
        if k.startswith('t') or b.startswith('t') or c.startswith('t'):
            combs.add(tuple(sorted((k,b,c))))

pprint(combs)
print(len(combs))
