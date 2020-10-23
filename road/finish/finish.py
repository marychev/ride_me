from layout.background_image import BackgroundImageAnimation
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("road/finish/finish.kv")


class Finish(Widget):
    texture = ObjectProperty(Image(source='road/finish/img/finish.jpg').texture)

    def __init__(self, **kwargs):
        super(Finish, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, 4, 8)


