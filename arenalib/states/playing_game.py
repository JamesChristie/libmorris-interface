from arenalib import renderer

from arenalib.factories   import game_board
from arenalib.board_space import BoardSpace

from arenalib.game_manager   import GameManager
from arenalib.game_presenter import GamePresenter

class PlayingGame:
  def __init__(self, last_state):
    renderer.initialize()
    game_board.build_game_board()

    self.game_manager   = GameManager()
    self.game_presenter = GamePresenter(self.game_manager)

  def on_draw(self):
    self.game_presenter.place_pieces()
    self.game_presenter.set_hud()

  def update(self):
    self.game_manager.update()

  def is_finished(self):
    return self.game_manager.is_over()

  def on_mouse_press(self, x, y, button, client_size):
    if self.game_manager.is_human_move():
      self.game_manager.advance_game(
        position = BoardSpace(x, y, client_size).get_position()
      )

  def on_key_press(self, symbol, modifiers):
    pass
