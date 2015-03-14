import unittest

from mock import Mock

from arenalib.state_machinery import StateMachinery

from arenalib.states.titles             import Titles
from arenalib.states.playing_game       import PlayingGame
from arenalib.states.asking_for_rematch import AskingForRematch

class TestStateMachineryFromBlankState(unittest.TestCase):
  def setUp(self):
    self.current_state = None
    self.machinery = StateMachinery(self.current_state)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), Titles)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertTrue(self.machinery.should_advance())

class TestStateMachineryFromTitlesState(unittest.TestCase):
  def setUp(self):
    self.machinery = StateMachinery(Titles(None))

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), Titles)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertFalse(self.machinery.should_advance())

class TestStateMachineryFromFinishedTitlesState(unittest.TestCase):
  def setUp(self):
    self.current_state = Titles(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_finished = Mock(return_value=True)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), PlayingGame)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertTrue(self.machinery.should_advance())

class TestStateMachineryFromPlayingGameState(unittest.TestCase):
  def setUp(self):
    self.current_state = PlayingGame(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_finished = Mock(return_value=False)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), PlayingGame)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertFalse(self.machinery.should_advance())

class TestStateMachineryFromFinishedPlayingGameState(unittest.TestCase):
  def setUp(self):
    self.current_state = PlayingGame(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_finished = Mock(return_value=True)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), AskingForRematch)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertTrue(self.machinery.should_advance())

class TestStateMachineryFromAskingForRematchState(unittest.TestCase):
  def setUp(self):
    self.current_state = AskingForRematch(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_quitting = Mock(return_value=False)
    self.current_state.is_finished = Mock(return_value=False)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), AskingForRematch)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertFalse(self.machinery.should_advance())

class TestStateMachineryFromFinishedAskingForRematchState(unittest.TestCase):
  def setUp(self):
    self.current_state = AskingForRematch(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_quitting = Mock(return_value=False)
    self.current_state.is_finished = Mock(return_value=True)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), PlayingGame)
    )

  def test_should_quit(self):
    self.assertFalse(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertTrue(self.machinery.should_advance())

class TestStateMachineryFromQuittingAskingForRematchState(unittest.TestCase):
  def setUp(self):
    self.current_state = AskingForRematch(None)
    self.machinery = StateMachinery(self.current_state)

    self.current_state.is_quitting = Mock(return_value=True)
    self.current_state.is_finished = Mock(return_value=False)

  def test_get_state(self):
    self.assertTrue(
      isinstance(self.machinery.get_state(), None.__class__)
    )

  def test_should_quit(self):
    self.assertTrue(self.machinery.should_quit())

  def test_should_advance(self):
    self.assertFalse(self.machinery.should_advance())
