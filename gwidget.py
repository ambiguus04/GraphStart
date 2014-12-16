from graph_tool.all import *
from numpy.random import *
import cairo
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import random
g = price_network(N=100, directed=False)
pos = sfdp_layout(g)
# graph_draw(g, pos=pos)
g = GraphWidget(g, pos=pos)
# interactive_window(g)
srf =  srf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600,400)
cr = cairo.Context(srf)
da = Gtk.DrawingArea()
# help(GraphWidget.draw)
# g.regenerate_surface()
g.draw(cr,da)