import pyglet

from .client import Client

__spawned_client__ = None

def spawn_client():
  """Create an instance of the Client to begin playing"""
  global __spawned_client__
  __spawned_client__ = Client()
  pyglet.app.run()
