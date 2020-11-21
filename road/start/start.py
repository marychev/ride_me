from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from utils.validation import ValidObject
from utils.dir import abstract_path
from utils.texture import redraw_texture, repeat_texture

Builder.load_file(abstract_path('road/start/start.kv'))


class Start(Widget):
    id = StringProperty('start')
    texture = ObjectProperty(Image(source=abstract_path('road/finish/img/finish.jpg')).texture)

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        repeat_texture(self.texture, 8, 8)

    @staticmethod
    def create(pos, size):
        kwargs = {
            "pos": pos,
            "size": size,
            "size_hint": (None, None)}
        return Start(**kwargs)

    def set_x(self):
        bike = self.get_bike()
        if bike and (self.x + bike.width) > 0:
            self.x = self.get_x()
            redraw_texture(self)

    def get_x(self):
        bike = self.get_bike()
        return self.x - bike.speed

    # game objects

    @staticmethod
    def widgets_on_road(road):
        widgets = [ValidObject.start(w) for w in road.children if w.__class__.__name__ == 'Start']
        return widgets

    def get_road(self):
        return ValidObject.road(self.parent.parent.children[1])

    def get_bike(self):
        if self.parent and self.parent.parent and len(self.parent.parent.children) > 0:
            return ValidObject.bike(self.parent.parent.children[0])

    def get_tools(self):
        return ValidObject.tools(self.parent.parent.parent.children[0])
