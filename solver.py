#!/usr/bin/python

from solver.utils import *
from solver.streetmap import *

streetmap = StreetMap(open('testfile').read())

print streetmap


# split by intersection, so that graph directions can be mapped to cardinal directions
# will need to implement A* (incl. dijkstra)
