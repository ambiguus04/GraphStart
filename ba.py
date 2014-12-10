from graph_tool.all import *
import random
g = price_network(N=2000, directed=False)
pos = sfdp_layout(g)
graph_draw(g, pos=pos)