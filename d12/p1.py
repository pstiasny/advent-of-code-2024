#!/usr/bin/env python

from sys import stdin
from fileinput import input


m = {}
for i, l in enumerate(input()):
    for j, c in enumerate(l.strip()):
        m[i,j]=c

H,W = i+1, j+1

v = set()
def walk(i,j):
    if (i,j) in v:
        return 0,0
    peri = 0
    ar = 0
    q = [(i,j)]
    v.add((i,j))

    c = m[i,j]

    while q:
        i,j=q.pop()
        ar += 1
        for n in [(i+1,j), (i-1,j), (i,j-1), (i, j+1)]:
            if m.get(n) == c:
                if n not in v:
                    q.append(n)
                    v.add(n)
            else:
                peri += 1
                print(i,j, n, m.get(n))
    print(peri, ar)
    return peri, ar

s = 0
for i in range(H):
    for j in range(W):
        p, a = walk(i,j)
        s += p * a
print(s)
