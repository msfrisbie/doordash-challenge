from utils import *

class Driver:

  orders = []

  def __init__(self,coordinate_str):
    self.x = cd_val(coordinate_str,0)
    self.y = cd_val(coordinate_str,1)