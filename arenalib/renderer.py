import pyglet

from pyglet.graphics import GL_COLOR_BUFFER_BIT

entities = []

clock_display = pyglet.clock.ClockDisplay()

def initialize():
  global entities

  pyglet.clock.set_fps_limit(60)
  pyglet.gl.glClearColor(1, 1, 1, 1)

  entities = []

def register_entity(entity):
  global entities

  entities.append(entity)

def get_draw_list():
  global entities
  global clock_display

  return entities + [clock_display]

def draw(client_size):
  global entities

  pyglet.graphics.glClear(GL_COLOR_BUFFER_BIT)
  for entity in entities:
    entity.draw(client_size)
