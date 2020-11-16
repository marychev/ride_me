from kivy.lang import Builder
from kivy.properties import StringProperty
from road.base.game_image import GameImage
from utils.dir import abstract_path

Builder.load_file(abstract_path('road/lamp/lamp.kv'))


class Lamp(GameImage):
    source = StringProperty(abstract_path('road/lamp/img/lamp.png'))
