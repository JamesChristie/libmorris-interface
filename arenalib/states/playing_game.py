from arenalib import renderer

from arenalib.factories import game_board

from arenalib.board_space import BoardSpace

from arenalib.entities.o import O

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
    position = BoardSpace(x, y, client_size).get_position()
    print(position)

    if position:
      x = O(position)
      print("Registering O at %d, %d" % (x.x_position(client_size[0]), x.y_position(client_size[1])))
      print("With lower coordinates at %d, %d" % (x.lower_x(client_size[0]), x.lower_y(client_size[1])))
      print("And upper coordinates at %d, %d" % (x.upper_x(client_size[0]), x.upper_y(client_size[1])))
      renderer.register_entity(O(position))
