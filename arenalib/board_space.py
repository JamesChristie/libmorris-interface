# Constant Ratios
LOWER_Y = 0.2
UPPER_Y = 0.95
LOWER_X = 0.2
UPPER_X = 0.95

PADDING = 0.05

LINE_WIDTH = 0.01

INTERVAL = 3

class BoardSpace:
  def __init__(self, x, y, client_size):
    self.x      = x
    self.y      = y
    self.width  = client_size[0]
    self.height = client_size[1]

  def get_position(self):
    if self.within_bounds():
      return (self.x_position(), self.y_position())
    else:
      return None

  def x_position(self):
    return int((self.x - self.x_intercept()) / (self.padded_width() - self.x_intercept()) * 3) + 1

  def y_position(self):
    return int((self.y - self.y_intercept()) / (self.padded_height() - self.y_intercept()) * 3) + 1

  def within_bounds(self):
    if self.within_x() and self.within_y():
      return True
    else:
      return False

  def within_x(self):
    return (self.width * LOWER_X) < self.x < (self.width * UPPER_X)

  def within_y(self):
    return (self.height * LOWER_Y) < self.y < (self.height * UPPER_Y)

  def padded_width(self):
    return self.width - (self.width * PADDING)

  def padded_height(self):
    return self.height - (self.height * PADDING)

  def x_intercept(self):
    return self.width * LOWER_X

  def y_intercept(self):
    return self.height * LOWER_Y
