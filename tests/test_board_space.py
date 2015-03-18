import unittest

from arenalib.board_space import BoardSpace

class TestLowerLeft(unittest.TestCase):
  def setUp(self):
    self.board_space = BoardSpace(201, 201, (1000, 1000))

  def test_get_position(self):
    self.assertEqual(self.board_space.get_position(), (1, 1))

class TestLowerRight(unittest.TestCase):
  def setUp(self):
    self.board_space = BoardSpace(750, 200, (800, 600))

  def test_get_position(self):
    self.assertEqual(self.board_space.get_position(), (3, 1))

class TestUpperMiddle(unittest.TestCase):
  def setUp(self):
    self.board_space = BoardSpace(1375, 975, (1920, 1080))

  def test_get_position(self):
    self.assertEqual(self.board_space.get_position(), (2, 3))

class TestOutOfBounds(unittest.TestCase):
  def setUp(self):
    self.board_space = BoardSpace(0, 0, (1024, 768))

  def test_get_position(self):
    self.assertIsNone(self.board_space.get_position())
