import pyglet

from arenalib.entity import Entity

from arenalib import board_space

class HorizontalLine(Entity):
  def __init__(self, ratio_y):
    super(HorizontalLine, self).__init__(None, ratio_y)

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
    return int(width * board_space.LOWER_X)

  def upper_x(self, width):
    return int(width * board_space.UPPER_X)

  def lower_y(self, height):
    return int(self.position(height) - self.half_thickness(height) + self.intercept(height))

  def upper_y(self, height):
    return int(self.position(height) + self.half_thickness(height) + self.intercept(height))

  def position(self, height):
    return self.vertical_space(height) * self.ratio_y

  def vertical_space(self, height):
    return height - (height * board_space.LOWER_Y) - (height * board_space.PADDING)

  def half_thickness(self, height):
    return height * board_space.LINE_WIDTH

  def intercept(self, height):
    return height * board_space.LOWER_Y
