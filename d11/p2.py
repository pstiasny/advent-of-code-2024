#!/usr/bin/env python

from sys import stdin


X = [int(i, 10) for i in stdin.read().strip().split(' ')]
print(X)

mem = {}
N = 75
def go(x, i):
    if i == N: return 1
    if (x,i) in mem: return mem[x,i]
    s = str(x)
    if x == 0:
        r = go(1, i + 1)
    elif len(s) & 1 == 0:
        r = go(int(s[:len(s)//2], 10), i +  1) + go(int(s[len(s)//2:], 10), i + 1)
    else:
        r = go(x*2024, i + 1)

    mem[x,i] = r
    return r


s = 0
for x in X:
    s += go(x, 0)
print(s)
