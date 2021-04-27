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
        self.bike = get_bike_by_title(app_config('bike', 'title'))
        label = self.get_label_item('No bike')
        self.bike and self._init_item(self.bike, label)

    def init_map(self):
        self.map = get_map_by_title(app_config('map', 'title'))
        label = self.get_label_item('No map')
        self.map and self._init_item(self.map, label)

    def get_label_item(self, text):
        for w in self.ids['center_panel'].children[:]:
            if w.__class__.__name__ == 'Label' and text == w.text:
                return w

    def _init_item(self, item, label):
        self.ids['center_panel'].remove_widget(label)
        self.ids['center_panel'].add_widget(Image(source=item['source']))

