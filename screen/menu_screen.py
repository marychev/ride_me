from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path
from kivy.properties import ObjectProperty, StringProperty
from screen.ui.panel_button import LeftPanelMenuBikes
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.app import App
from bike.bikes import get_by_title as get_bike_by_title

# bg_color = ObjectProperty([1, 1, 0, 1])

Builder.load_file(abstract_path('screen/menu_screen.kv'))


class MenuScreen(Screen):
    bike = ObjectProperty()
    level = ObjectProperty()

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

        if self.app.config.get('bike', 'name') != 'None':
            self.init_bike()

    def init_bike(self):
        bike_name = self.app.config.get('bike', 'name')
        if not self.bike and bike_name:
            self.bike = get_bike_by_title(bike_name)

        label = self.ids['center_panel'].children[1]
        self.ids['center_panel'].remove_widget(label)
        self.ids['center_panel'].add_widget(Image(source=self.bike['source']))
