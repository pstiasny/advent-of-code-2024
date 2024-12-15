#!/usr/bin/env python

from fileinput import input
import re
from sys import argv, stdin
from math import inf
from itertools import chain

s = 0
X = {}
world, moves = stdin.read().split('\n\n')
for i, l in enumerate(world.splitlines()):
    for j, c in enumerate(l):
        if c == '.': continue
        if c == '@':
            p = (i, j)
            continue
        X[i,j] = c

W,H=j+1,i+1

def pp(s):
    for i in range(H):
        for j in range(W):
            if (i,j) == p: print('@', end='')
            elif (i,j) in s: print(s[i,j], end='')
            else: print('.', end='')
        print()
    print('&&&&&')
    print()

def move(X, d):
    global p

    dx, dy = d
    x, y = p
    nx = x +dx
    ny = y + dy

    if (nx, ny) in X:
        s = []
        while (nx, ny) in X:
            if X[nx, ny] == '#':
                return
            if X[nx, ny] == 'O':
                s.append((nx, ny))
                nx, ny = nx+dx, ny+dy

        print(s)
        while s:
            lx, ly = s.pop()
            print(nx, ny, '<-', lx, ly, X[lx, ly])
            X[nx, ny] = X[lx, ly]
            nx, ny = lx, ly
        del X[nx, ny]

    p = x + dx, y + dy



for m in chain(*moves.splitlines()):
    match m:
        case '<':
            d = (0, -1)
        case '^':
            d = (-1, 0)
        case '>':
            d = (0, 1)
        case 'v':
            d = (1, 0)
    # print('move', m, d)
    move(X, d)
    # pp(X)

s = 0
for (i, j), v in X.items():
    if v == 'O':
        print(i,j)
        s  += i * 100 + j


print(s)
