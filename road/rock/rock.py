from kivy.lang import Builder
from kivy.properties import StringProperty
from road.base.game_image import GameImage
from utils.dir import abstract_path

Builder.load_file(abstract_path('road/rock/rock.kv'))


class Rock(GameImage):
    source = StringProperty(abstract_path('road/rock/img/rock-1.png'))
