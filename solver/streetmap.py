from utils import *
from driver import *
from itertools import chain

class StreetMap:

  # drivers should all reference the same streetmap
  # they will perform methods on it
  # drivers are the actors, the streetmap is static

  # there will have to be a special code to represent
  # pickup of an order. or perhaps just visit the tile?

  tiles = []
  restaurants = []
  customers = []

  def __init__(self, mapdata):
    data_arr = mapdata.split('\n')

    self.width = cd_val(data_arr[1],0)
    self.height = cd_val(data_arr[1],1)

    # self.drivers = []

    # for driver_cood in data_arr[0].split(';'):
    #   self.drivers.append(Driver(driver_cood))

    self.tiles = list(chain(*map(lambda x: list(x),data_arr[3:])))

  def __str__(self):
    return unicode(self)

  def __unicode__(self):
    """
    prints the map to the terminal
    """
    arr = []
    for val in range(0,self.height):
      arr.append(''.join(self.tiles[val*self.width:(val+1)*self.width]))
    return '\n'.join(arr)

  def get(self,x,y):
    """
    get the tile value at the (x,y) coordinate
    """
    if x is None or y is None or \
    x<0 or y<0 or \
    x>=self.width or y>=self.height:
      raise Exception('invalid coordinates: '+unicode(x)+','+unicode(y))
    return self.tiles[y*self.width+x]

  # def drive_path(driver_index,path_str):
  #   driver_score = 0
  #   driver = self.drivers[driver_index]
  #   for dir in list(path_str):

  #     driver.move(dir)

  # def tangent_restaurants