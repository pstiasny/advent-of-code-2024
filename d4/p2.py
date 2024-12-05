#!/usr/bin/env python

from collections import defaultdict
import fileinput


locs = defaultdict(set)


for i, l in enumerate(fileinput.input()):
    for j, c in enumerate(l):
        if c in ['M', 'A', 'S']:
            locs[c].add((i, j))


c = 0
for i, j in locs['A']:
    # M
    #  A
    #   S
    d1a = (i-1,j-1) in locs['M'] and (i+1,j+1) in locs['S']
    # S
    #  A
    #   M
    d1b = (i+1,j+1) in locs['M'] and (i-1,j-1) in locs['S']

    #   M
    #  A
    # S
    d2a = (i-1,j+1) in locs['M'] and (i+1,j-1) in locs['S']
    #   S
    #  A
    # M
    d2b = (i+1,j-1) in locs['M'] and (i-1,j+1) in locs['S']

    if (d1a or d1b) and (d2a or d2b):
        c+=1

print(c)
