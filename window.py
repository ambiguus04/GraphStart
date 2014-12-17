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
txt = g.new_vertex_property("vector<string>")
# help(GraphWindow)
for v in g.vertices():
    value[v] = black # if value[v] = random.random() -> TypeError: 'float' object is not iterable ????
    txt[v] = ""
win = GraphWindow(g, pos, geometry=(800,600), vertex_text = txt, vertex_fill_color = white, vertex_halo = False, vertex_size = 20)
win.set_title("nananan")
picked = None
index = g.new_vertex_property
def change_values():
    global picked
    if win.graph.picked is not None and win.graph.picked is not False and win.graph.picked is not picked:
        if picked is not None:
            txt[picked] = ""
        txt[win.graph.picked] = str(int(win.graph.picked)) ## argh, adding commas!
        picked = win.graph.picked
    win.graph.regenerate_surface(lazy=False)
    win.graph.queue_draw()

    return True
def _motion_notify_event():
    global white
    white = [1,0,1,1]
    return True
cid = GObject.idle_add(change_values)
# win.connect("motion_notify_event", _motion_notify_event)

win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()
