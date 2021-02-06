from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from objects.base.game_image import GameImage
from utils.dir import abstract_path

_dir = 'objects/rock'
Builder.load_file(abstract_path('{}/rock.kv'.format(_dir)))


class Rock(GameImage):
    img = Image(source=abstract_path('{}/img/rock-1.png'.format(_dir)))
    TEXTURE = img.texture
    texture = ObjectProperty(TEXTURE)

    def on_collision(self, bike):
        if bike.collide_widget(self):
            self._collision(bike)
            return True
        return False

    def _collision(self, bike):
        bike.speed = 0
        bike.power = 0
        bike.acceleration = 0
        bike.collected_currency = 0
        bike.anim_collision()
        self.draw_collision_rectangle(bike)

    def draw_collision_rectangle(self, bike):
        with bike.canvas:
            Color(rgba=(1, 0, 0, .2), group="background")
            Rectangle(pos=bike.pos, size=bike.size, group="background")
