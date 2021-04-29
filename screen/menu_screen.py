from typing import Union

from kivy.core.text import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from bike.bikes import get_by_title as get_bike_by_title
from bike.model import BikeModel
from level.maps import get_by_title as get_map_by_title
from level.model import MapModel
from utils.dir import abstract_path
from utils.init import app_config


Builder.load_file(abstract_path('screen/menu_screen.kv'))


class MenuScreen(Screen):
    bike_model = ObjectProperty()
    level = ObjectProperty()
    map_model = ObjectProperty(allownone=True)

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        if app_config('bike', 'title'):
            self.init_bike()
        if app_config('map', 'title'):
            self.init_map()

    def init_bike(self):
        self.bike_model = get_bike_by_title(app_config('bike', 'title'))
        self.bike_model and self._init_item(self.bike_model, self.get_label_by_text('No bike'))

    def init_map(self):
        self.map_model = get_map_by_title(app_config('map', 'title'))
        self.map_model and self._init_item(self.map_model, self.get_label_by_text('No map'))

    def get_label_by_text(self, text: str) -> Label:
        for w in self.ids['center_panel'].children[:]:
            if w.__class__.__name__ == 'Label' and text == w.text:
                return w

    def _init_item(self, model: Union[BikeModel, MapModel], label: Label) -> None:
        self.ids['center_panel'].remove_widget(label)
        self.ids['center_panel'].add_widget(Image(source=model.source))
