import pyglet
import arenalib

class Engine:
  def __init__(self):
    self.entities = []
    self.render_width, self.render_height = arenalib.get_client_size()

  def render(self):
    for entity in self.entities:
      entity.update_position(self.render_width, self.render_height)
      entity.draw()

  def update(self):
    raise NotImplementedError

  def is_finished(self):
    raise NotImplementedError

  def update_render_size(self, width, height):
    self.render_width  = width
    self.render_height = height
