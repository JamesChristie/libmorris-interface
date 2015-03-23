import pyglet

entities = []
pieces   = []
hud      = []

clock_display = pyglet.clock.ClockDisplay()

def initialize():
  global entities

  pyglet.clock.set_fps_limit(60)
  pyglet.gl.glClearColor(1, 1, 1, 1)

  entities = []

def register_entity(entity):
  global entities

  entities.append(entity)

def set_hud(hud_element_list):
  global hud

  hud = hud_element_list

def set_pieces(piece_list):
  global pieces

  pieces = piece_list

def draw(client_size):
  global entities
  global hud
  global pieces
  global clock_display

  pyglet.graphics.glClear(pyglet.graphics.GL_COLOR_BUFFER_BIT)

  pyglet.gl.glColor3f(0, 0, 0) # Default drawing color to black
  for entity in entities:
    entity.draw(client_size)

  for element in hud:
    element.draw(client_size)

  for piece in pieces:
    piece.draw(client_size)

  clock_display.draw()
