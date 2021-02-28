from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from bike.bikes import get_by_title as get_bike_by_title
from level.maps import get_by_title as get_map_by_title
from utils.dir import abstract_path
from utils.init import app_config


Builder.load_file(abstract_path('screen/menu_screen.kv'))


class MenuScreen(Screen):
    bike = ObjectProperty()
    level = ObjectProperty()
    map = DictProperty(allownone=True)

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        if app_config('bike', 'title'):
            self.init_bike()
        if app_config('map', 'title'):
            self.init_map()

    def init_bike(self):
        _bike = app_config('bike', 'title')
        self.bike = get_bike_by_title(_bike)
        label = self.ids['center_panel'].children[1]
        self.bike and self._init_item(self.bike, label)

    def init_map(self):
        self.map = get_map_by_title(app_config('map', 'title'))
        label = self.ids['center_panel'].children[0]
        self.map and self._init_item(self.map, label)

    def _init_item(self, item, label):
        self.ids['center_panel'].remove_widget(label)
        self.ids['center_panel'].add_widget(Image(source=item['source']))
