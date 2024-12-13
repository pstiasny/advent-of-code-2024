#!/usr/bin/env python

from sys import stdin
from fileinput import input


m = {}
for i, l in enumerate(input()):
    for j, c in enumerate(l.strip()):
        m[i,j]=c

H,W = i+1, j+1

def ne(i,j):
    return [((i+1,j),'d'), ((i-1,j), 'u'), ((i,j-1), 'l'), ((i, j+1), 'r')]


v = set()
def walk(i,j):
    if (i,j) in v:
        return 0,0
    peri = 0
    ar = 0
    q = [(i,j)]
    v.add((i,j))
    fe = set()

    c = m[i,j]
    print(c)

    while q:
        i,j=q.pop()
        ar += 1
        for n,d in ne(i,j):
            o = m.get(n)
            if o == c:
                if n not in v:
                    q.append(n)
                    v.add(n)
            else:
                fe.add((n,d))

    for n,d in fe:
        ni, nj = n
        if d in ['u', 'd'] and ((ni, nj-1), d) not in fe:
            print(ni+1, nj+1, d)
            peri += 1
        if d in ['l', 'r'] and ((ni-1, nj), d) not in fe:
            print(ni+1, nj+1, d)
            peri += 1

    print(fe)
    print(peri, ar)
    return peri, ar

s = 0
for i in range(H):
    for j in range(W):
        p, a = walk(i,j)
        s += p * a
print(s)
