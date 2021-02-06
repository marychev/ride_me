from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from objects.base.game_image import GameImage
from utils.dir import abstract_path


class Puddle(GameImage):
    img = Image(source=abstract_path('objects/puddle/img/puddle.png'))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)

    def on_collision(self, bike):
        if bike.collide_widget(self):
            bike.anim_collision()
            if bike.speed > 0 or bike.power > 0:
                bike.acceleration -= bike.acceleration / 100
                bike.set_speed(bike.speed - (bike.max_speed / 1000))
                bike.set_power(bike.power - (bike.max_power / 1000))
            return True
        return False
