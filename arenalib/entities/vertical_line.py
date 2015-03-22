import pyglet

from arenalib.entity import Entity

from arenalib import board_space

class VerticalLine(Entity):
  def __init__(self, ratio_x):
    super(VerticalLine, self).__init__(ratio_x, None)

  def draw(self, client_size):
    pyglet.graphics.draw_indexed(
      4, pyglet.gl.GL_TRIANGLES,
      [0, 1, 2, 0, 2, 3],
      ('v2i', (self.lower_x(client_size[0]), self.lower_y(client_size[1]),
               self.upper_x(client_size[0]), self.lower_y(client_size[1]),
               self.upper_x(client_size[0]), self.upper_y(client_size[1]),
               self.lower_x(client_size[0]), self.upper_y(client_size[1]))),
      ('c4b', [0, 0, 0, 255] * 4)
    )

  def lower_x(self, width):
    return int(self.position(width) - self.half_thickness(width) + self.intercept(width))

  def upper_x(self, width):
    return int(self.position(width) + self.half_thickness(width) + self.intercept(width))

  def lower_y(self, height):
    return int(height * board_space.LOWER_Y)

  def upper_y(self, height):
    return int(height * board_space.UPPER_Y)

  def position(self, width):
    return self.horizontal_space(width) * self.ratio_x

  def horizontal_space(self, width):
    return width - (width * board_space.LOWER_X) - (width * board_space.PADDING)

  def half_thickness(self, width):
    return width * board_space.LINE_WIDTH

  def intercept(self, width):
    return width * board_space.LOWER_X
