from graph_tool.all import *
import csv

N = 125906
g = Graph(directed=False)
for i in xrange(N):
    g.add_vertex()
with open("hipo_pl_ind.csv",'r') as file:
    r = csv.reader(file, delimiter='\t')
    for line in r:
        g.add_edge(g.vertex(line[0]), g.vertex(line[1]))
        print(line[0])
pos = sfdp_layout(g)
graph_draw(g, pos=pos, output="graph_pl.pdf")