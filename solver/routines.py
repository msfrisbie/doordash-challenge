from streetmap import *
from driver import *

def generate_solution(mapfilename):
  streetmap = StreetMap(open(mapfilename).read())

  print streetmap

  # should return output file string?

def score_solution(mapfilename,routefilename):
  routes = open(routefilename).read().split('\n')

  mapfile = open(mapfilename).read().split('\n')

  streetmap = StreetMap(mapfile)

  drivers = []

  for driver_cood in mapfile[0].split(';'):
    drivers.append(
      Driver(driver_cood,streetmap)
    )

  if len(routes)!=len(drivers):
    raise Exception('# of routes does not match # of drivers')

  print streetmap,'\n'

  total_score = 0

  for index,val in enumerate(drivers):
    driver_score = drivers[index].drive(routes[index])
    print "Driver "+str(index+1)+": "+str(driver_score)
    total_score += driver_score

  print "Map completed? "+str(streetmap.completed())
  print "Map score: "+str(total_score)

