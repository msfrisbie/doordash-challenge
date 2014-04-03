from streetmap import *
from driver import *

def generate_solution(mapfilename):
  streetmap = StreetMap(open(mapfilename).read())

  print streetmap

  # should return output file string?


def score_solution(mapfilename,routefilename):
  routes = open(routefilename).read().split('\n')

  mapfile = open(mapfilename).read()

  streetmap = StreetMap(mapfile)

  drivers = []

  for driver_cood in mapfile.split('\n')[0].split(';'):
    drivers.append(
      Driver(driver_cood,streetmap))

  if len(routes)!=len(drivers):
    raise Exception('# of routes does not match # of drivers')

  print '<<<'
  print routes
  print '<<<'