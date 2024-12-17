#!/usr/bin/env python

from sys import setrecursionlimit, argv
import re
import z3

setrecursionlimit(100000)

r = r'''Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: ([0-9,]+)'''

with open(argv[1]) as f:
    P = f.read()
m = re.match(r, P, re.MULTILINE)
a,b,c = map(int, m.groups()[0:3])
p = [int(x) for x in m.group(4).split(',')]


def run(ip,a,b,c,outl):
    def comb(arg):
        match arg:
            case 0 | 1 | 2 | 3: return arg
            case 4: return a
            case 5: return b
            case 6: return c
            case 7: raise ValueError()

    op = {}
    def adv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        a = num >> den
    op[0] = adv

    def bxl(arg):
        nonlocal a,b,c
        b = b ^ arg
    op[1] = bxl

    def bst(arg):
        nonlocal b
        b = comb(arg) & 0b111
    op[2] = bst

    def jnz(arg):
        return z3.If(
            (a==0),
            run(ip, 0,b,c,outl),
            run(arg,a,b,c,outl)
        )
    op[3] = jnz

    def bxc(arg):
        nonlocal b
        b = b ^ c
    op[4] = bxc

    def out (arg):
        t = comb(arg) & 0b111

        if outl == len(p)-1 or isinstance(t, int):
            return (t == p[outl])
        rr = run(ip,a,b,c,outl+1)
        return z3.And(
            (t == p[outl]),
            rr,
        )
    op[5] = out

    def bdv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        b = num >> den
    op[6] = bdv

    def cdv(arg):
        nonlocal a,b,c
        num = a
        den = comb(arg)
        c = num >> den
    op[7] = cdv

    def eva(ins, arg):
        return op[ins](arg)


    while ip < len(p)-1:
        ip += 2

        r = eva(p[ip-2], p[ip-1])
        if r is not None:
            return r

    return False


s = z3.Solver()

bvl = 1
while True:
    A = z3.BitVec('a', bvl)
    q = run(0, A, b, c, 0)

    o = z3.Optimize()
    o.add(q)
    o.minimize(A)
    res =o.check()
    if res == z3.sat:
        print(q)
        print(res)
        print(o.model())
        break
    bvl += 1
