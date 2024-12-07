#!/usr/bin/env python

import fileinput


s = 0
for l in fileinput.input():
    t, N = l.strip().split(':')
    t = int(t)
    N = list(map(int, N.strip().split(' ')))

    def go(N, l):
        if not N:
            return (l == t)
        else:
            return go(N[1:], l * N[0]) or go(N[1:], l + N[0])
    if go(N[1:], N[0]):
        s += t

print(s)


