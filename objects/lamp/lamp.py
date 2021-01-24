from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


class Lamp(GameImage):
    img = Image(source=abstract_path('objects/lamp/img/lamp.png'))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == 'Lamp']

    #
    # def remove_game_objects(self):
    #     self.remove_widgets(self.road.lamps)
