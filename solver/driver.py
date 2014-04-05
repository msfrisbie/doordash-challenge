from utils import *

class Driver:

  orders = {}

  def __init__(self,coordinate_str,streetmap):
    self.x = cd_val(coordinate_str,0)
    self.y = cd_val(coordinate_str,1)
    self.streetmap = streetmap

  def move(self,dx=None,dy=None,char=None,*args,**kwargs):

    if char!=None:
      if char=='N':
        if self.y>0:
          self.y -= 1
        else:
          raise Exception('Cannot move off top of map')
      elif char=='E':
        if self.x<self.streetmap.width:
          self.x += 1
        else:
          raise Exception('Cannot move off right side of map')
      elif char=='S':
        if self.y<self.streetmap.height:
          self.y += 1
        else:
          raise Exception('Cannot move off bottom of map')
      elif char=='W':
        if self.x>0:
          self.x -= 1
        else:
          raise Exception('Cannot move off left side of map')
      else:
        raise Exception('Invalid character')
    elif dx!=None and dy!=None:
      self.x += dx
      self.y += dy
    else:
      raise Exception('Invalid move command')

    tile = self.streetmap.get(self.x,self.y)

    if tile=='.':
      raise Exception('Cannot drive off road!')
    elif tile.islower():
      self.pickup(tile)
    elif tile.isupper():
      self.dropoff(tile)
    else:
      return int(tile)

    return 0

  def pickup(self,tile):
    restaurant = self.streetmap.restaurants[tile]
    if restaurant.picked_up == False:
      self.orders[tile.upper()] = True
      restaurant.picked_up = True

  def dropoff(self,tile):
    if tile in self.orders.keys():
      self.streetmap.customers[tile].delivered = True
      del self.orders[tile]

  def drive(self,path):

    score = 0

    for step in list(path):
      try:
        score += self.move(char=step)
      except Exception as e:
        print e
        # score = self.streetmap.max
        score = 999;
        break;

    return score


