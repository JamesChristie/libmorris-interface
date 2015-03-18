from arenalib import renderer

from arenalib.entities.vertical_line import VerticalLine
from arenalib.entities.horizontal_line import HorizontalLine

def build_game_board():
  for line in (build_veritcal_lines() + build_horizontal_lines()):
    renderer.register_entity(line)

def build_veritcal_lines():
  return [
    VerticalLine(1.0/3.0),
    VerticalLine(2.0/3.0)
  ]

def build_horizontal_lines():
  return [
    HorizontalLine(1.0/3.0),
    HorizontalLine(2.0/3.0)
  ]
