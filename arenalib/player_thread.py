import threading

import libmorris

from libmorris.errors import InvalidMove
from libmorris.errors import CannotMove

class PlayerThread(threading.Thread):
  def __init__(self, game_id, position=None):
    super(PlayerThread, self).__init__()
    self.game_id  = game_id
    self.position = position

  def run(self):
    try:
      libmorris.advance_game(self.game_id, position=self.position)
    except(InvalidMove, CannotMove):
      pass
