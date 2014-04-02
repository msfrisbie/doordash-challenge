from utils import *
from driver import *
from itertools import chain

class StreetMap:

  tiles = []
  restaurants = []
  customers = []

  def __init__(self, mapdata):
    data_arr = mapdata.split('\n')

    self.width = cd_val(data_arr[1],0)
    self.height = cd_val(data_arr[1],1)

    self.drivers = []

    for driver_cood in data_arr[0].split(';'):
      self.drivers.append(Driver(driver_cood))

    self.tiles = list(chain(*map(lambda x: list(x),data_arr[3:])))

  def __str__(self):
    return unicode(self)

  def __unicode__(self):
    arr = []
    for val in range(0,self.height):
      arr.append(''.join(self.tiles[val*self.width:(val+1)*self.width]))
    return '\n'.join(arr)

  def get(self,x,y):
    if x is None or y is None or \
    x<0 or y<0 or \
    x>=self.width or y>=self.height:
      raise Exception('invalid coordinates: '+unicode(x)+','+unicode(y))
    return self.tiles[y*self.width+x]