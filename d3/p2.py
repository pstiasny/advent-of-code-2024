#!/usr/bin/env python

from sys import stdin
import re

STMT = re.compile(r"(?P<MUL>mul\((?P<L>[0-9]{1,3}),(?P<R>[0-9]{1,3})\))|(?P<DO>do\(\))|(?P<DONT>don\'t\(\))")

text = stdin.read()

t = 0
i = 0
active = True
while True:
    s = STMT.search(text, pos=i)
    if not s:
        break

    print(s.lastgroup, s.group(0))
    match s.lastgroup:
        case 'MUL':
            if active:
                l = int(s.group('L'))
                r = int(s.group('R'))
                t += l*r
        case 'DO':
            active = True
        case 'DONT':
            active = False
    i = s.end(0)
print(t)
