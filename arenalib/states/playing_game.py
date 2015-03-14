from arenalib import renderer

class PlayingGame:
  def __init__(self, last_state):
    renderer.initialize()

    pass
    # Build/Register Board
    # Build/Register/Store HUD
    # Initialize Storage for played pieces
    # Register game with libmorris

  def update(self):
    pass
    # update current reporter
    # if player move, pass
    # if computer's move, spawn move thread

  def is_finished(self):
    pass

  def on_mouse_press(self, x, y, button, modifiers):
    pass
