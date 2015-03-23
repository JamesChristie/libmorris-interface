from arenalib import renderer

from arenalib.entities.x import X
from arenalib.entities.o import O

from arenalib.game_manager import HUMAN_PLAYER
from arenalib.game_manager import COMPUTER_PLAYER

class GamePresenter:
  def __init__(self, game_manager):
    self.game_manager = game_manager

  def place_pieces(self):
    renderer.set_pieces(self.board_as_pieces())

  def get_current_board(self):
    return self.game_manager.reporter.get_current_board()

  def board_as_pieces(self):
    current_board = self.get_current_board()

    return [
      self.piece_for(position, current_board[position])
      for position in current_board if current_board[position]
    ]

  def piece_for(self, position, player):
    if player == HUMAN_PLAYER:
      return X(position)
    elif player == COMPUTER_PLAYER:
      return O(position)
