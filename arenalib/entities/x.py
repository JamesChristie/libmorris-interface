import pyglet

from arenalib.piece import Piece

from arenalib import board_space

class X(Piece):
  def __init__(self, position):
    super(X, self).__init__(position)

  def draw(self, client_size):
    pyglet.gl.glColor3f(255, 0, 0)

    # Backward Arm
    pyglet.graphics.draw_indexed(
      4, pyglet.gl.GL_TRIANGLES,
      [0, 1, 2, 0, 2, 3],
      ('v2i',
        (
          self.upper_x(client_size[0]) - self.thickness(client_size[0]), # Lower-left X
          self.lower_y(client_size[1]),                                  # Lower-left Y
          self.upper_x(client_size[0]),                                  # Lower-right X
          self.lower_y(client_size[1]),                                  # Lower-right Y
          self.lower_x(client_size[0]) + self.thickness(client_size[0]), # Upper-right X
          self.upper_y(client_size[1]),                                  # Upper-right Y
          self.lower_x(client_size[0]),                                  # Upper-left X
          self.upper_y(client_size[1])                                   # Upper-left Y
        )
      )
    )

    # Forward Arm
    pyglet.graphics.draw_indexed(
      4, pyglet.gl.GL_TRIANGLES,
      [0, 1, 2, 0, 2, 3],
      ('v2i',
        (
          self.lower_x(client_size[0]),                                  # Lower-left X
          self.lower_y(client_size[1]),                                  # Lower-left Y
          self.lower_x(client_size[0]) + self.thickness(client_size[0]), # Lower-right X
          self.lower_y(client_size[1]),                                  # Lower-right Y
          self.upper_x(client_size[0]),                                  # Upper-right X
          self.upper_y(client_size[1]),                                  # Upper-right Y
          self.upper_x(client_size[0]) - self.thickness(client_size[0]), # Upper-left X
          self.upper_y(client_size[1])                                   # Upper-left Y
        )
      )
    )
