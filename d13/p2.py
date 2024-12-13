#!/usr/bin/env python

from sys import stdin
import re
from z3 import Int, Optimize, IntNumRef


s = 0
for Q in stdin.read().split('\n\n'):
    m = re.match(r'''Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)
Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)
Prize: X=(?P<px>\d+), Y=(?P<py>\d+)$''', Q, re.MULTILINE)

    ax = int(m.group('ax'))
    ay = int(m.group('ay'))
    bx = int(m.group('bx'))
    by = int(m.group('by'))
    px = int(m.group('px')) + 10000000000000
    py = int(m.group('py')) + 10000000000000

    # min 3a + b
    # given
    #   a * ax + b * bx = px
    #   a * ay + b * by = py
    opt = Optimize()
    a = Int('a')
    b = Int('b')
    opt.add(
        a * ax + b * bx == px,
        a * ay + b * by == py,
    )
    h = opt.minimize(3 * a + b)
    opt.check()
    l = opt.lower(h)

    print(l, type(l))
    if isinstance(l, IntNumRef):
        s += l.as_long()


print(s)
