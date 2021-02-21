from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path
from kivy.properties import ObjectProperty, StringProperty
from screen.ui.panel import LeftPanelMenuBikes
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

# bg_color = ObjectProperty([1, 1, 0, 1])

Builder.load_file(abstract_path('screen/menu_screen.kv'))


class MenuScreen(Screen):
    bike = ObjectProperty()
    level = ObjectProperty()
