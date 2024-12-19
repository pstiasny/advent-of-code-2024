#!/usr/bin/env python

import fileinput
from math import inf
from sys import argv, stdin
import heapq

# N = int(argv[1])
# argv.pop(1)

A, B = stdin.read().split('\n\n')
A = set(A.strip().split(', '))
B = B.strip().split('\n')
L = max(map(len, A))
print('A', A)
print('B', B)
c = 0
for q in B:
    ca = {}
    def go(t):
        if not t:
            return True

        lt = len(t)
        if lt in ca:
            return ca[lt]

        for l in range(1,L+1):
            if t[:l] in A:
                # print(t[:l])
                if go(t[l:]):
                    # print('OK')
                    ca[lt] = True
                    return True
        # print('NO')
        ca[lt] = False
        return False


    if go(q):
        c+=1

print(c)
