#!/usr/bin/env python

from fileinput import input
import re
from sys import argv, stdin
from math import inf

T = 100
W = int(argv[1])
H = int(argv[2])
s = 1
mx = W // 2
my = H // 2
quads = [0,0,0,0]
for l in stdin.read().split('\n'):
    l = l.strip()
    if not l: continue
    m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', l)
    px,py,vx,vy = map(int, m.groups())
    px = (px + T * vx) % W
    py = (py + T * vy) % H

    print(px,py,vx,vy)
    if px< mx and py < my:
        quads[0] += 1
    elif px> mx and py < my:
        quads[1] += 1
    elif px> mx and py > my:
        quads[2] += 1
    elif px< mx and py > my:
        quads[3] += 1

print(mx,my)
print(quads)
for q in quads:
    s *= q


print(s)
