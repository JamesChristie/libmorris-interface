from arenalib import renderer

class AskingForRematch:
  def __init__(self, last_state):
    renderer.initialize()

    self.finished = False
    self.quitting = False

  def update(self):
    pass

  def on_draw(self):
    pass

  def on_mouse_press(self, x, y, button, modifiers):
    pass

  def is_finished(self):
    pass

  def is_quitting(self):
    pass
