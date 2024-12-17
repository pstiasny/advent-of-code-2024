#!/usr/bin/env python

import fileinput
from math import inf
from sys import stdin
import heapq
from collections import deque
import re

r = r'''Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: ([0-9,]+)'''

m = re.match(r, stdin.read(), re.MULTILINE)
a,b,c = map(int, m.groups()[0:3])
p = [int(x) for x in m.group(4).split(',')]

class Wrong(Exception):
    pass


def run(p,a,b,c):
    ip = 0
    outl = []
    vis = set()

    # print(a,b,c,p)
    def comb(arg):
        match arg:
            case 0 | 1| 2| 3: return arg
            case 4: return a
            case 5: return b
            case 6: return c
            case 7: raise ValueError()

    op = {}
    def adv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        a = num >> den
    op[0] = adv

    def bxl(arg):
        nonlocal a,b,c
        b = b ^ arg
    op[1] = bxl

    def bst(arg):
        nonlocal b
        b = comb(arg) & 0b111
    op[2] = bst

    def jnz(arg):
        nonlocal ip
        if a != 0:
            ip = arg
    op[3] = jnz

    def bxc(arg):
        nonlocal b
        b = b ^ c
    op[4] = bxc

    def out (arg):
        outl.append(comb(arg) & 0b111)
    op[5] = out

    def bdv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        b = num >> den
    op[6] = bdv

    def cdv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        c = num >> den
    op[7] = cdv

    def eva(ins, arg):
        op[ins](arg)


    while ip < len(p)-1:
        ip += 2
        if (ip,a,b,c) in vis:
            print('loop')
            raise Wrong()
        vis.add((ip,a,b,c))
        eva(p[ip-2], p[ip-1])

    return outl


# a = 0
outl = []
outl = run(p, a, b, c)
print(outl)
# while outl != p:
#     try:
#         outl = run(p, a, b, c)
#     except Wrong:
#         pass
#     a += 1

print('a', a-1)
