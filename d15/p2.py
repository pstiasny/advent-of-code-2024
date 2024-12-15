#!/usr/bin/env python

from fileinput import input
import re
from sys import argv, stdin, setrecursionlimit
from math import inf
from itertools import chain
from dataclasses import dataclass

setrecursionlimit(10000)

@dataclass
class Proxy:
    x: tuple[int, int]
    t: str


s = 0
X = {}
world, moves = stdin.read().split('\n\n')
for i, l in enumerate(world.splitlines()):
    for j, c in enumerate(l):
        if c == '.': continue
        if c == '@':
            p = (i, 2*j)
            continue
        X[i,2*j] = c
        X[i,2*j+1] = Proxy((i,2*j), c)

W,H=2*j+1,i+1

def pp(s):
    for i in range(H):
        # for j in range(W):
        j= 0
        while j < W:
            if (i,j) == p: print('@', end='')
            elif (i,j) in s:
                v = s[i,j]
                if isinstance(v, Proxy):
                    print(']', end='')
                else:
                    print(s[i,j], end='')
            else: print('.', end='')
            j += 1
        print()
    print('&&&&&')
    print()

def can_push(l, d):
    x, y = l
    if l not in X:
        return True
    if isinstance(X[l], Proxy):
        y -= 1
    if X[x,y] == '#':
        return False

    ok = True
    match d:
        case '^':
            ok = ok and can_push((x-1, y), d) and can_push((x-1, y+1), d)
        case 'v':
            ok = ok and can_push((x+1, y), d) and can_push((x+1, y+1), d)
        case '<':
            ok = ok and can_push((x, y-1), d)
        case '>':
            ok = ok and can_push((x, y+2), d)

    return ok


def push(l, d):
    x, y = l
    if l not in X:
        return
    if isinstance(X[l], Proxy):
        y -= 1

    match d:
        case '^':
            push((x-1, y), d)
            push((x-1, y+1), d)
            X[x-1, y] = X[x,y]
            X[x-1, y+1] = Proxy((x-1, y), X[x,y])
            del X[x, y]
            del X[x, y+1]

        case 'v':
            push((x+1, y), d)
            push((x+1, y+1), d)
            X[x+1, y] = X[x,y]
            X[x+1, y+1] = Proxy((x+1, y), X[x,y])
            del X[x, y]
            del X[x, y+1]

        case '<':
            push((x, y-1), d)
            X[x, y-1] = X[x, y]
            X[x, y] = Proxy((x, y-1), X[x, y])
            del X[x, y+1]

        case '>':
            push((x, y+2), d)
            X[x, y+2] = Proxy((x, y+1), X[x, y])
            X[x, y+1] = X[x, y]
            del X[x, y]


def move(X, m, d):
    global p

    dx, dy = d
    x, y = p
    nx = x +dx
    ny = y + dy

    if can_push((nx, ny), m):
        push((nx, ny), m)
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
    print('move', m, d)
    move(X, m, d)
    # pp(X)

s = 0
for (i, j), v in X.items():
    if v == 'O':
        print(i,j)
        s  += i * 100 + j


print(s)
