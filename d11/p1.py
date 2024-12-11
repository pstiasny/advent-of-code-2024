#!/usr/bin/env python

from sys import stdin


X = [int(i, 10) for i in stdin.read().strip().split(' ')]
print(X)
for i in range(25):
    Y = []
    for x in X:
        s = str(x)
        if x == 0:
            Y.append(1)
        elif len(s) & 1 == 0:
            Y.append(int(s[:len(s)//2], 10))
            Y.append(int(s[len(s)//2:], 10))
        else:
            Y.append(x*2024)

    X = Y

print(len(X))
