from utils import *
from driver import *
from restaurant import *
from customer import *
from itertools import chain

class StreetMap:

  # drivers should all reference the same streetmap
  # they will perform methods on it
  # drivers are the actors, the streetmap is static

  # there will have to be a special code to represent
  # pickup of an order. or perhaps just visit the tile?

  tiles = []
  restaurants = {}
  customers = {}

  def __init__(self, mapdata):

    self.width = cd_val(mapdata[1],0)
    self.height = cd_val(mapdata[1],1)

    self.tiles = list(chain(*map(lambda x: list(x),mapdata[2:])))

    for index,tile in enumerate(self.tiles):
      if tile.islower():
        self.restaurants[tile] = Restaurant(self.i2c(index))
      elif tile.isupper():
        self.customers[tile] = Customer(self.i2c(index))


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

  # index to x,y coordinate
  def i2c(self,index):
    if index<0 or index>=self.width*self.height:
      raise Exception("Tile index out of bounds")
    return [index%self.width,index/self.width]

  def completed(self):
    for index,key in enumerate(self.restaurants):
      if self.restaurants[key].picked_up == False:
        return False
    for index,key in enumerate(self.customers):
      if self.customers[key].delivered == False:
        return False
    return True
