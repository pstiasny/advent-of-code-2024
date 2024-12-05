#!/usr/bin/env python

import fileinput
import math


c = 0
for l in fileinput.input():
    ls = list(map(int, l.strip().split(' ')))
    ds = [r - l for r, l in zip(ls, ls[1:])]
    signs = [x>0 for x in ds]
    if not all(signs[0] == x for x in signs): continue
    if not all(1 <= abs(x) <= 3 for x in ds): continue
    c+=1

print(c)
