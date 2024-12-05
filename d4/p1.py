#!/usr/bin/env python

import fileinput
import re

import numpy as np

XMAS = re.compile('XMAS')


L = [list(l.strip()) for l in fileinput.input()]
L = np.array(L)

c=0
def sr(r):
    global c
    f = XMAS.findall(''.join(r))
    c += len(f)
    f = XMAS.findall(''.join(reversed(r)))
    c += len(f)


for a in [L, L.T]:
    for r in a:
        sr(r)

w = max(L.shape)
for i in range(-w, w):
    sr(np.diagonal(L, i))
    sr(np.diagonal(L[::-1, :], i))

print(c)
