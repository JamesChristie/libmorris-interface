import pyglet

from pyglet.graphics import GL_COLOR_BUFFER_BIT

from arenalib.engines.boot_up import BootUp

class Client(pyglet.window.Window):
  def __init__(self):
    super(Client, self).__init__(resizable=True)
    pyglet.clock.schedule_interval(self.update, 1.0/60.0)
    pyglet.clock.set_fps_limit(60)
    self.set_caption('T3 Arena')
    pyglet.gl.glClearColor(1, 1, 1, 1)

    self.clock_display = pyglet.clock.ClockDisplay()
    self.engine        = None

  def on_show(self):
    self.engine = self.engine or BootUp()

  def on_draw(self):
    pyglet.graphics.glClear(GL_COLOR_BUFFER_BIT)
    self.engine.render()
    self.clock_display.draw()

  def on_resize(self, width, height):
    super(Client, self).on_resize(width, height)

    if self.engine:
      self.engine.update_render_size(width, height)

  def on_mouse_press(self, x, y, button, modifiers):
    self.engine.on_mouse_press(x, y, button, modifiers)
  
  def update(self, time_differential):
    self.engine.update()

    if self.engine.is_finished():
      quit()
