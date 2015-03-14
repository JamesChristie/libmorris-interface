class Entity:
  def __init__(self, ratio_x, ratio_y):
    self.ratio_x   = ratio_x
    self.ratio_y   = ratio_y

  def draw(self):
    raise NotImplementedError
