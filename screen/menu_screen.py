from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from bike.bikes import get_by_title as get_bike_by_title
from level.maps import get_by_title as get_map_by_title
from utils.dir import abstract_path

Builder.load_file(abstract_path('screen/menu_screen.kv'))


class MenuScreen(Screen):
    bike = ObjectProperty()
    level = ObjectProperty()
    map = DictProperty()

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()
        if self.app.config.get('bike', 'name') != 'None':
            self.init_bike()
        if self.app.config.get('map', 'name') != 'None':
            self.init_map()

    def init_bike(self):
        self.bike = get_bike_by_title(self.app.config.get('bike', 'name'))
        label = self.ids['center_panel'].children[1]
        self._init_item(self.bike, label)

    def init_map(self):
        self.map = get_map_by_title(self.app.config.get('map', 'name'))
        label = self.ids['center_panel'].children[0]
        self._init_item(self.map, label)

    def _init_item(self, item, label):
        self.ids['center_panel'].remove_widget(label)
        self.ids['center_panel'].add_widget(Image(source=item['source']))