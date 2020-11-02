import kivy
kivy.require('1.11.1')
from kivy.config import Config
from kivy.utils import platform
from kivy.core.window import Window

SECOND_GAME = 1 / 60
HEIGHT_GAME = 560 + 100
WIDTH_GAME = 860 + 200


if platform not in ('android', 'ios'):
  Config.set('graphics', 'resizable', '1')
  Window.size = (WIDTH_GAME, HEIGHT_GAME)