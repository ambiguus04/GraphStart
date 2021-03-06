from graph_tool.all import *
from numpy.random import *
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import random
g = price_network(N=100, directed=False)
pos = sfdp_layout(g)
# graph_draw(g, pos=pos)
white = [1,1,1,1]
black = [0,0,0,1]
value = g.new_vertex_property("vector<double>")
for v in g.vertices():
    value[v] = black # if value[v] = random.random() -> TypeError: 'float' object is not iterable ????
win = GraphWindow(g, pos, geometry=(800,600), vertex_fill_color = value)
win.set_title("nananan")
def change_values():
    p=0.2
    vs = list(g.vertices())
    shuffle(vs)
    for v in vs:
        if random.random() < p:
            if value[v] == white:
                value[v] = black
            else:
                value[v] = white
    win.graph.regenerate_surface(lazy=False)
    win.graph.queue_draw()
    return True
cid = GObject.idle_add(change_values)
win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()
