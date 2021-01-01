from objects.base.game_image import GameImage
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from utils.validation import ValidObject
from utils.dir import abstract_path
from utils.texture import redraw_texture, repeat_texture

Builder.load_file(abstract_path('objects/start/start.kv'))


class Start(GameImage):
    IMG = Image(source=abstract_path('objects/finish/img/finish.jpg'))
    TEXTURE = IMG.texture
    texture = ObjectProperty(TEXTURE)

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        repeat_texture(self.texture, 8, 8)

    @staticmethod
    def widgets_on_road(road):
        widgets = [ValidObject.start(w) for w in road.children if w.__class__.__name__ == 'Start']
        return widgets

    def set_x(self):
        bike = self.get_bike()
        if bike and (self.x + bike.width) > 0:
            self.x = self.get_x()
            redraw_texture(self)
