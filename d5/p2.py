#!/usr/bin/env python


from collections import defaultdict
import fileinput
import networkx as nx


inp = fileinput.input(encoding='utf-8')
before = defaultdict(list)

# g = nx.DiGraph()

for l in inp:
    l = l.strip()
    if l == '':
        break
    left, right = l.split('|')
    before[int(right)].append(int(left))
    # g.add_edge(left, right)


mids = []
for l in inp:
    q = [int(j) for j in l.strip().split(',')]
    al = set(q)
    got = set()
    good = True
    for i in q:
        for j in before[i]:
            if j in al and not j in got:
                good = False

        got.add(i)

    if good:
        continue

    got = set()
    o = []

    def go(i):
        if i in got or i not in al:
            return

        for j in before[i]:
            go(j)

        o.append(i)
        got.add(i)


    for i in reversed(q):
        go(i)
    print(o)
    mids.append(o[len(q)//2])

print(sum(mids))
