from graph_tool.all import *
import numpy
import csv

N = 125906
g = Graph(directed=False)
for i in xrange(N):
    g.add_vertex()
l = numpy.zeros(N)
with open("hipo_pl_ind.csv",'r') as file:
    r = csv.reader(file, delimiter='\t')
    for line in r:
        g.add_edge(g.vertex(line[0]), g.vertex(line[1]))
        l[int(line[0])] += 1
        l[int(line[1])] += 1
        print(line[0])
# pos = arf_layout(g, max_iter=0)
#root = 1042 / 1043
j = numpy.argmax(l)
# pos = radial_tree_layout(g)
# graph_draw(g, pos=pos, output="graph_pl1.png", output_size=(6000,6000))
pos = fruchterman_reingold_layout(g, n_iter=10)
graph_draw(g, pos=pos)