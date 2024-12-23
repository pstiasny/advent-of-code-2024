#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv, stdin
import heapq
import string
from pprint import pprint
from collections import deque

class Path:
    def __init__(self, le, m):
        self.le=le
        self.m = m

    def __add__(self, other):
        if self.le == inf or other.le == inf:
            return Path.impossible()
        return Path(self.le + other.le, self.m + other.m)

    def __lt__(self, other):
        return self.le < other.le
    def __eq__(self, other):
        return self.le == other.le

    def __rmul__(self, k):
        return Path(k*self.le, k*self.m)
    def __str__(self):
        return self.m
    def __repr__(self):
        if self.le == inf:
            return 'Path.impossible()'
        return f'Path({self.le}, {self.m!r})'
    def __len__(self):
        return self.le

    @classmethod
    def zero(cls):
        return cls(0, '')
    @classmethod
    def single(cls, s):
        assert len(s) == 1
        return cls(1, s)
    @classmethod
    def impossible(cls):
        return cls(inf, None)


LD = ''' ^A
<v>'''.splitlines()
PD = {}
for i,l in enumerate(LD):
    for j,c in enumerate(l):
        PD[c]=(i,j)

CD = {}
for a,(ai,aj) in PD.items():
    for b,(bi,bj) in PD.items():
        CD[a,b] = Path.single(b)

CD2 = {}
CD3  ={}

LN = '''789
456
123
 0A'''.splitlines()
PN = {}
for i,l in enumerate(LN):
    for j,c in enumerate(l):
        PN[c] = (i,j)

CN = {}

for CA, CB, P, A in [(CD, CD2, PD, LD), (CD2, CD3, PD, LD), (CD3, CN, PN, LN)]:
    iblank, jblank = P[' ']
    for a,(i,j) in P.items():
        if a == ' ': continue
        q = [(Path.zero(), i, j, 'A')]
        vis = set()
        CB[a, a] = CA['A', 'A']
        while q:
            d, i, j, di = heapq.heappop(q)
            if (i, j, di) in vis:
                continue
            vis.add((i,j, di))

            if di == 'A' and d != Path.zero():
                CB[a, A[i][j]] = d

            for ndi, k, l in [('v', i+1, j), ('^', i-1, j), ('<', i, j-1), ('>', i, j+1), ('A', i, j)]:
                if k < 0 or l < 0:
                    continue
                try:
                    b = A[k][l]
                except IndexError:
                    continue
                if b == ' ':
                    continue
                nd = d + CA[di, ndi]
                heapq.heappush(q, (nd, k,l, ndi))


pprint('CD')
pprint(CD)
pprint('CD2')
pprint(CD2)
pprint('CD3')
pprint(CD3)
pprint('CN')
pprint(CN)
assert CD2['A', 'v'] == Path(3, 'v<A')
assert CD2['v', '<'] == Path(2, '<A')
assert CD2['<', '<'] == Path(1, 'A')
assert CD2['<', 'A'] == Path(4, '>>^A')

assert CD3['A', '<'] == Path(10, 'v<A<AA>>^A')
assert CD3['>', 'A'] == CD2['A', '^'] + CD2['^', 'A'] #+ CD['A', 'A']

assert CN['A', '0'] == CD3['A', '<'] + CD3['<', 'A']


t = 0
for i, l in enumerate(fileinput.input()):
    code = l.strip()
    print(code)
    nc = int(''.join(c for c in code if ord('0') <= ord(c) <= ord('9') ), 10)
    c = CN['A', code[0]]
    print('A', code[0], c)
    for s1, s2 in zip(code, code[1:]):
        print( 'cn', s1, s2, CN[s1,s2] )
        c += CN[s1,s2]
    print('c', len(c), c)
    print('nc', nc)
    t += nc * len(c)

print(t)
