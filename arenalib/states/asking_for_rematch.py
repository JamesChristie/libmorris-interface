import pyglet
import libmorris

from arenalib import renderer

from arenalib.entities.label import Label

from arenalib.game_manager import HUMAN_PLAYER
from arenalib.game_manager import COMPUTER_PLAYER

class AskingForRematch:
  def __init__(self, last_state):
    self.game_manager = last_state.game_manager
    self.finished     = False
    self.quitting     = False

    # NOTE (JamesChristie) Clean up after ourselves at the
    # first opportunity to prevent memory leaks in the
    # singleton storage
    libmorris.destroy_game(self.game_manager.game_id)

  def update(self):
    pass

  def on_draw(self):
    renderer.set_hud([
      Label(0.1, 0.9, "Turns: %d" % self.game_manager.played_moves()),
      Label(0.1, 0.5, "Winner:"),
      Label(0.1, 0.4, self.get_winner_name()),
      Label(0.6, 0.1, "The game has ended, play again? (y/n)")
    ])

  def on_mouse_press(self, x, y, button, modifiers):
    pass

  def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.Y:
      self.finished = True
    elif symbol == pyglet.window.key.N:
      self.quitting = True

  def is_finished(self):
    return self.finished

  def is_quitting(self):
    return self.quitting

  def get_winner_name(self):
    winner = self.game_manager.get_winner()

    if winner == HUMAN_PLAYER:
      return "Player"
    elif winner == COMPUTER_PLAYER:
      return "Computer"
    elif winner == None:
      return "Nobody"
