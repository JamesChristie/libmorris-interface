from arenalib import renderer

from arenalib.factories import game_board

from arenalib.board_space import BoardSpace

class PlayingGame:
  def __init__(self, last_state):
    renderer.initialize()
    game_board.build_game_board()

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

  def on_mouse_press(self, x, y, button, client_size):
    print(BoardSpace(x, y, client_size).get_position())
