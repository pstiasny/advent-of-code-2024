#!/usr/bin/env python

import fileinput


obs = set()


gp = None
for i, l in enumerate(fileinput.input()):
    l = l.strip()
    for j, c in enumerate(l):
        if c == '^':
            gp = (i,j)
        if c == '#':
            obs.add((i, j))
H,W=i+1,j+1


tries = {}

def pp(o, vis):
    for i in range(H):
        for j in range(W):
            if (i,j) == gp: print('x', end='')
            elif (i,j) == o: print('O', end='')
            elif (i,j) in obs: print('#', end='')
            elif (i,j,-1,0) in vis or (i,j,1,0) in vis: print('|', end='')
            elif (i,j,0,-1) in vis or (i,j,0,1) in vis: print('-', end='')
            else: print('.', end='')
        print()
    print('&&&&&')
    print()


def walk(x, d, trying, prev_vis):
    vis = set()
    i, j = x
    di, dj = d
    while 0 <= i < H and 0 <= j < W:
        if (i, j, di, dj) in vis:
            # if trying:
            #     print('loop')
            #     pp(trying, vis | prev_vis)
            return True
        vis.add((i, j, di, dj))

        for _ in range(4):
            ni, nj = i + di, j + dj
            if (ni, nj) not in obs:
                break
            di, dj = dj, di*(-1)
        else:
            raise ValueError('blocked')

        ti,tj = ni,nj
        if (
            not trying and
            (ti,tj) not in obs and
            (ti,tj) != gp and
            not(
                (ti,tj,-1,0) in vis or (ti,tj,1,0) in vis or
                (ti,tj,0,-1) in vis or (ti,tj,0,1) in vis
            ) and
            (ti,tj,di,dj) not in tries and
            0 <= ti < H and
            0 <= tj < W
        ):
            obs.add((ti,tj))
            tres = walk((i,j), (di, dj), (ti, tj), vis)
            # if tres:
            #     pp((ti, tj), vis)
            obs.remove((ti,tj))
            tries[(ti, tj, di, dj)]  = tres

        i, j = ni, nj
    return False

walk(gp, (-1 , 0), False, set())

# print(tries)
olocs = { (oi, oj) for (oi, oj, _, _), v in tries.items() if v }

# for (oi, oj) in olocs:
#     print('---------')
print(olocs)
print(len(olocs))
