import math
import pyglet

from arenalib.piece import Piece

from arenalib import board_space

class O(Piece):
  def __init__(self, position):
    super(O, self).__init__(position)

  def draw(self, client_size):
    x_origin = self.x_origin(client_size[0])
    y_origin = self.y_origin(client_size[1])
    ratio_y  = float(client_size[1]) / float(client_size[0])

    initial_radius = self.half_span(client_size[0])
    iterations     = int(2 * initial_radius * math.pi)

    sin = math.sin(2 * math.pi / iterations)
    cos = math.cos(2 * math.pi / iterations)

    dx, dy = initial_radius, 0

    pyglet.gl.glColor3f(0, 0, 255)
    pyglet.gl.glLineWidth(self.thickness(client_size[0]))
    pyglet.gl.glBegin(pyglet.gl.GL_LINE_LOOP)
    for i in range(iterations + 1):
        pyglet.gl.glVertex2f(
          (x_origin + dx),
          (y_origin + (dy * ratio_y))
        )

        dx, dy = (dx * cos - dy * sin), \
                 (dy * cos + dx * sin)
    pyglet.gl.glEnd()

  def x_origin(self, width):
    return self.lower_x(width) + self.half_span(width)

  def y_origin(self, height):
    return self.lower_y(height) + self.half_span(height)
