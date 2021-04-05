import kivy
kivy.require('2.0.0')
from kivy.config import Config
from kivy.utils import platform
from kivy.core.window import Window
from utils.size_phones import SizePhones

SECOND_GAME = 1.0 / 60.0

sp = SizePhones()
HEIGHT_GAME = int(sp.height/2)
WIDTH_GAME = int(sp.width/2)


if platform not in ('android', 'ios'):
    Config.set('graphics', 'resizable', '1')
    Window.size = (WIDTH_GAME, HEIGHT_GAME)



