#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv, stdin
import heapq
import string
from pprint import pprint
from collections import deque

# N = int(argv[1])
# argv.pop(1)

LD = ''' ^A
<v>'''.splitlines()
PD = {}
for i,l in enumerate(LD):
    for j,c in enumerate(l):
        # PD[i,j]=c
        PD[c]=(i,j)

CDs = [{} for _ in range(26)]
for a,(ai,aj) in PD.items():
    for b,(bi,bj) in PD.items():
        # CD[a,b] = 2*(abs(ai-bi)+abs(aj-bj)) + 1
        # CD[a,b] = abs(ai-bi)+abs(aj-bj)+1
        CDs[0][a,b] = 1


LN = '''789
456
123
 0A'''.splitlines()
PN = {}
for i,l in enumerate(LN):
    for j,c in enumerate(l):
        # PN[i,j]=c
        PN[c] = (i,j)

CN = {}

for CA, CB, P, A in [(cd1, cd2, PD, LD) for (cd1, cd2) in zip(CDs[0:25], CDs[1:26])] +  [(CDs[25], CN, PN, LN)]:
    iblank, jblank = P[' ']
    def opt(a, i, j):
        q = [(0, i, j, 'A')]
        vis = set()
        CB[a, a] = CA['A', 'A']
        while q:
            d, i, j, di = heapq.heappop(q)
            if (i, j, di) in vis:
                continue
            vis.add((i,j, di))

            if di == 'A' and d != 0:
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

    for a,(ai,aj) in P.items():
        if a == ' ': continue
        opt(a, ai, aj)



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
    print('c', c)
    print('nc', nc)
    t += nc * c

print(t)