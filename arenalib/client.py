import pyglet

from arenalib import renderer
from arenalib import state_machinery

class Client(pyglet.window.Window):
  def __init__(self):
    super(Client, self).__init__(resizable=True)
    self.set_caption('T3 Arena')
    pyglet.clock.schedule_interval(self.update, 1.0/60.0)
    self.current_state = None

  def on_draw(self):
    renderer.draw(self.get_size())

  def on_mouse_press(self, x, y, button, modifiers):
    self.current_state.on_mouse_press(x, y, button, modifiers)
  
  def update(self, time_differential):
    state_machinery.ensure_state(self)

    if self.current_state:
      self.current_state.update()
    else:
      pyglet.app.exit()
