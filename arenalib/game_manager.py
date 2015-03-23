import libmorris

from arenalib.player_thread import PlayerThread

HUMAN_PLAYER    = 1
COMPUTER_PLAYER = 2

class GameManager:
  def __init__(self):
    self.game_id        = libmorris.register_game()
    self.reporter       = None
    self.current_action = None

    self.update_reporter()

  def update_reporter(self):
    self.reporter = libmorris.get_game(self.game_id)

  def get_winner(self):
    return self.reporter.winner()

  def is_over(self):
    return self.reporter.is_over()

  def is_thinking(self):
    return self.current_action and self.current_action.is_alive()

  def is_human_move(self):
    return not self.is_over() and \
      self.reporter.current_player() == HUMAN_PLAYER

  def is_computer_move(self):
    return not self.is_over() and \
      self.reporter.current_player() == COMPUTER_PLAYER

  def played_moves(self):
    return self.reporter.played_moves()

  def get_current_board(self):
    return self.reporter.get_current_board()

  def get_current_player(self):
    return self.reporter.current_player()

  def update(self):
    self.update_reporter()
    if self.is_action_done(): self.finish_action()
    if self.need_computer_move(): self.advance_game()

  def advance_game(self, position=None):
    self.current_action = PlayerThread(self.game_id, position=position)
    self.current_action.start()

  def is_action_done(self):
    return self.current_action and (not self.current_action.is_alive())

  def need_computer_move(self):
    return self.is_computer_move() and (not self.current_action)

  def finish_action(self):
    self.current_action.join()
    self.current_action = None
