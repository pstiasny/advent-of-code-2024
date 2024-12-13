#!/usr/bin/env python

from sys import stdin
import sys
from fileinput import input
import re
from math import inf
sys.setrecursionlimit(10000)


s = 0
for Q in stdin.read().split('\n\n'):
    m = re.match(r'''Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)
Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)
Prize: X=(?P<px>\d+), Y=(?P<py>\d+)$''', Q, re.MULTILINE)

    print(Q)
    ax = int(m.group('ax'))
    ay = int(m.group('ay'))
    bx = int(m.group('bx'))
    by = int(m.group('by'))
    px = int(m.group('px'))
    py = int(m.group('py'))
    print(m.groups())


    vis = {}
    def search(x, y):
        if x == px and y == py:
            return 0
        if (x,y) in vis:
            return vis[x,y]
        if x > px or y > py:
            return inf

        r = min(
            search(x+ax, y+ay) + 3,
            search(x+bx, y+by) + 1,
        )
        vis[x,y] = r

        return r

    sr = search(0,0)
    if sr != inf:
        s += sr


print(s)
