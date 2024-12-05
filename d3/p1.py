#!/usr/bin/env python

from sys import stdin
import re

MUL = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')

text = stdin.read()

t = 0
i = 0
while True:
    s = MUL.search(text, pos=i)
    if not s:
        break
    l = int(s.group(1))
    r = int(s.group(2))
    t += l*r
    i = s.end(0)
print(t)
