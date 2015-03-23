from arenalib import renderer

from arenalib.entities.x     import X
from arenalib.entities.o     import O
from arenalib.entities.label import Label

from arenalib.game_manager import HUMAN_PLAYER
from arenalib.game_manager import COMPUTER_PLAYER

class GamePresenter:
  def __init__(self, game_manager):
    self.game_manager = game_manager

  def place_pieces(self):
    renderer.set_pieces(self.board_as_pieces())

  def set_hud(self):
    renderer.set_hud([
      self.get_bottom_message(),
      self.get_turns_message(),
      self.get_current_label(),
      self.get_player_label()
    ])

  def board_as_pieces(self):
    current_board = self.game_manager.get_current_board()

    return [
      self.piece_for(position, current_board[position])
      for position in current_board if current_board[position]
    ]

  def piece_for(self, position, player):
    if player == HUMAN_PLAYER:
      return X(position)
    elif player == COMPUTER_PLAYER:
      return O(position)

  def get_bottom_message(self):
    if self.game_manager.get_current_player() == HUMAN_PLAYER:
      return Label(0.6, 0.1, "Click a space to move")
    elif self.game_manager.get_current_player() == COMPUTER_PLAYER:
      return Label(0.6, 0.1, "The computer is thinking...")
    else:
      return Label(0.6, 0.1, "No one is playing...")

  def get_turns_message(self):
    return Label(0.1, 0.9, "Turns: %d" % self.game_manager.played_moves())

  def get_current_label(self):
    return Label(0.1, 0.4, "Current:")

  def get_player_label(self):
    if self.game_manager.get_current_player() == HUMAN_PLAYER:
      return Label(0.1, 0.3, "Player")
    elif self.game_manager.get_current_player() == COMPUTER_PLAYER:
      return Label(0.1, 0.3, "Computer")
    else:
      return Label(0.1, 0.3, "Nobody")
