import pyglet

from .client import Client

__spawned_client__ = None

def spawn_client():
  global __spawned_client__
  __spawned_client__ = Client()
  pyglet.app.run()

def get_client_size():
  global __spawned_client__
  return __spawned_client__.get_size()
