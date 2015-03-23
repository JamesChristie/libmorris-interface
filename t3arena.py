#!/usr/bin/env python

import arenalib

# NOTE (JamesChristie) Pyglet implies use of a window
# instance or instance of a subclass to control library
# interaction. Instantiating a Client object is
# sufficient to enter the main game loop.
if __name__ == '__main__':
  arenalib.spawn_client()
