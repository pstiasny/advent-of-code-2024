#!/usr/bin/env python

import fileinput
import networkx as nx

g = nx.Graph()
for i, l in enumerate(fileinput.input()):
    a, b = l.strip().split('-')
    g.add_edge(a,b)


m = max(nx.find_cliques(g), key=len)
print(','.join(sorted(m)))
