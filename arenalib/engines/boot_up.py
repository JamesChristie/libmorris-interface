import pyglet
import arenalib

from arenalib.engine import Engine
from arenalib        import title_factory

class BootUp(Engine):
  def __init__(self):
    super(BootUp, self).__init__()
    self.entities += title_factory.build_titles()
    self.finished  = False

  def update(self):
    pass

  def is_finished(self):
    return self.finished

  def on_mouse_press(self, x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
      self.finished = True
