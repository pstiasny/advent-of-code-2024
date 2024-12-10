#!/usr/bin/env python

from sys import stdin


L = stdin.read().strip()
space = []
files = []

X = []
for i in range(0, len(L)//2):
    l = int(L[2*i])
    f = int(L[2*i+1])
    files.append((len(X), l, i))
    X.extend([i] * l)
    if f > 0:
        space.append((len(X), f))
    X.extend([None] * f)
l = int(L[2*(i+1)])
files.append((len(X), l, i+1))
X.extend([i+1] * l)

print('X', X, len(X))
print('files', files)
print('space', space)

files.reverse()
ordered = []
for i, l, k in files:
    for j, s in space:
        if j < i and s >= l:
            break
    else:
        ordered.append((i, l, k))
        continue

    space.remove((j, s))
    ordered.append((j, l, k))

    s -= l
    if s:
        space.append((j+l, s))
        space.sort() # lol

ordered.sort()

r =0
for i, l, k in ordered:
    for j in range(i, i+l):
        r +=  j * k

print('ordered', ordered)
print(r)


