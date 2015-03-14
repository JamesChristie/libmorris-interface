from arenalib import renderer

from arenalib.states.titles             import Titles
from arenalib.states.playing_game       import PlayingGame
from arenalib.states.asking_for_rematch import AskingForRematch

def ensure_state(client):
  new_state = StateMachinery(client.current_state).get_state()
  client.current_state = new_state

class StateMachinery:
  NEXT_STATES = {
    None.__class__:   Titles,
    Titles:           PlayingGame,
    PlayingGame:      AskingForRematch,
    AskingForRematch: PlayingGame
  }

  def __init__(self, current_state):
    self.current_state = current_state

  def get_state(self):
    if self.should_quit():
      return None
    elif self.should_advance():
      return self.build_next_state()
    else:
      return self.current_state

  def build_next_state(self):
    new_class = self.NEXT_STATES[type(self.current_state)]
    return new_class(self.current_state)

  def should_quit(self):
    is_quitting = getattr(self.current_state, "is_quitting", None)
    return is_quitting and is_quitting()

  def should_advance(self):
    return not self.current_state or self.current_state.is_finished()
