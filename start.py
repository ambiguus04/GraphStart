from graph_tool.all import *
import random
g = Graph(directed=False)
p = 0.05
for x in xrange(100):
    v = g.add_vertex()
for x in xrange(100):
    for y in xrange(x):
        if (random.random() < p and x is not y):
            g.add_edge(g.vertex(x), g.vertex(y))

graph_draw(g)