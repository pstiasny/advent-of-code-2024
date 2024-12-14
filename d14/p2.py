#!/usr/bin/env python

# pipe output to less/grep, search for consecutive O's

from collections import defaultdict
from fileinput import input
import re
from sys import argv, stdin
from math import inf

def pp(s):
    for i in range(H):
        for j in range(W):
            if (i,j) in s: print('O', end='')
            else: print('.', end='')
        print()
    print('&&&&&')
    print()

T = 100
W = int(argv[1])
H = int(argv[2])
s = 1
mx = W // 2
my = H // 2
quads = [0,0,0,0]
sets = {}
rs = []
for l in stdin.read().split('\n'):
    l = l.strip()
    if not l: continue
    m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', l)
    px,py,vx,vy = map(int, m.groups())

    rs.append((px,py,vx,vy))


for  i in range(10000):
    S = set()
    for px,py,vx,vy in rs:
        px = (px + i * vx) % W
        py = (py + i * vy) % H
        S.add((px, py))

    print(f'************* {i} ***********')
    pp(S)
