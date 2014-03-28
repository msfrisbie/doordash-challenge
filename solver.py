#!/usr/bin/python

from solver.utils import *

# f = open('testfile')
# print f.read()

print open('testfile').read().split('\n')

# split by intersection, so that graph directions can be mapped to cardinal directions
# will need to implement A* (incl. dijkstra)
