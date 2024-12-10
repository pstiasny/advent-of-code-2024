#!/usr/bin/env python

from sys import stdin


L = stdin.read().strip()

X = []
for i in range(0, len(L)//2):
    l = int(L[2*i])
    f = int(L[2*i+1])
    print(i,l,f)
    X.extend([i] * l)
    X.extend([None] * f)
l = int(L[2*(i+1)])
X.extend([i+1] * l)
print(X)

i = 0
e = len(X) - 1

while i < e:
    if X[i] == None:
        while X[e] == None and e > i:
            e -= 1
        X[i] = X[e]
        X[e] = None
        e -= 1
    i += 1

s =0
for i, k in enumerate(X):
    if k != None:
        s += i * k

print(X)
print(s)


