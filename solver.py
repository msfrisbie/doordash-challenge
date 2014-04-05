#!/usr/bin/python

from solver.routines import *
import sys

try:
  datafilename = sys.argv[1]
  solutionfilename = sys.argv[2]
except:
  datafilename = 'testfile'
  solutionfilename = 'testsolution'

score_solution(datafilename,solutionfilename)

# split by intersection, so that graph directions can be mapped to cardinal directions
# will need to implement A* (incl. dijkstra)
