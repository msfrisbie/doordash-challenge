from utils import *

class Driver:

  orders = []

  def __init__(self,coordinate_str):
    self.x = cd_val(coordinate_str,0)
    self.y = cd_val(coordinate_str,1)

  def move(self,dx=None,dy=None,char=None,*args,**kwargs):
    if char!=None:
      if char=='N':
        if y>0:
          y -= 1
        else:
          raise Exception('Cannot move off top of map')
      elif char=='E':
        if x<width:
          x += 1
        else:
          raise Exception('Cannot move off right side of map')
      elif char=='S':
        if y<height:
          y += 1
        else:
          raise Exception('Cannot move off bottom of map')
      elif char=='W':
        if x>0:
          x -= 1
        else:
          raise Exception('Cannot move off left side of map')
      else:
        raise Exception('Invalid character')
    elif dx!=None and dy!=None:
      self.x += dx
      self.y += dy
    else:
      raise Exception('Invalid move command')
