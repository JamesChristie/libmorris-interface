import pyglet

from arenalib.entity import Entity

class Label(Entity):
  def __init__(self, ratio_x, ratio_y, text, large=False):
    super(Label, self).__init__(ratio_x, ratio_y)
    self.large = large

    self.pyglet_label = pyglet.text.Label(
      text=text,
      anchor_x='center',
      anchor_y='center',
      color=(0, 0, 0, 255)
    )

  def draw(self, client_size):
    self.update_position(*client_size)
    self.pyglet_label.draw()

  def update_position(self, width, height):
    self.pyglet_label.x = int(self.ratio_x * width)
    self.pyglet_label.y = int(self.ratio_y * height)
    self.pyglet_label.font_size = self.get_font_size(height)

  def get_font_size(self, height):
    if self.large:
      return height / 5.0
    else:
      return height / 25.0
