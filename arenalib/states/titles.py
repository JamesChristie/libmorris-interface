import pyglet

from arenalib import renderer

from arenalib.factories import titles

class Titles:
  def __init__(self, last_state):
    renderer.initialize()

    for title in titles.build_titles():
      renderer.register_entity(title)
    self.finished  = False

  def update(self):
    pass

  def is_finished(self):
    return self.finished

  def on_mouse_press(self, x, y, button, client_size):
    if button == pyglet.window.mouse.LEFT:
      self.finished = True
