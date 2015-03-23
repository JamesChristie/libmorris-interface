from arenalib import board_space

class Piece:
  def __init__(self, position):
    self.x_pos = position[0]
    self.y_pos = position[1]

  def lower_x(self, width):
    return int(self.x_position(width) - self.half_span(width) + self.x_intercept(width))

  def upper_x(self, width):
    return int(self.x_position(width) + self.half_span(width) + self.x_intercept(width))

  def lower_y(self, height):
    return int(self.y_position(height) - self.half_span(height) + self.y_intercept(height))

  def upper_y(self, height):
    return int(self.y_position(height) + self.half_span(height) + self.y_intercept(height))

  def x_position(self, width):
    return (self.horizontal_space(width) / 3) * self.x_pos - self.padded_span(width)

  def y_position(self, height):
    return (self.vertical_space(height) / 3) * self.y_pos - self.padded_span(height)

  def horizontal_space(self, width):
    return width - self.x_intercept(width) - (width * board_space.PADDING)

  def vertical_space(self, height):
    return height - self.y_intercept(height) - (height * board_space.PADDING)

  def padded_span(self, dimension):
    return self.half_span(dimension) + self.half_padding(dimension)

  def half_span(self, dimension):
    return (dimension * board_space.PIECE_SPAN) / 2

  def half_padding(self, dimension):
    return (dimension * board_space.PADDING) / 2

  def x_intercept(self, width):
    return width * board_space.LOWER_X

  def y_intercept(self, height):
    return height * board_space.LOWER_Y

  def thickness(self, width):
    return int(width * board_space.LINE_WIDTH)
