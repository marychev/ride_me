from layout.background_image import BackgroundImageAnimation
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.lang import Builder
# from road.road import Road
# from bike.bike import Bike

Builder.load_file("road/finish/finish.kv")


class Finish(Widget):
    texture = ObjectProperty(Image(source='road/finish/img/finish.jpg').texture)

    def __init__(self, **kwargs):
        super(Finish, self).__init__(**kwargs)
        BackgroundImageAnimation.repeat_wrap(self.texture, 8, 8)

    def set_x(self):
        print('x-finish')
        self.x = self.get_x()

    def get_x(self):
        print('get x finish')
        bike = self.parent.parent.children[0]
        road = self.parent.parent.children[1]

        if (road.__class__.__name__ == 'Road') and (bike.__class__.__name__ == 'Bike'):
            return (road.total_way - road.distance_traveled) + bike.x + bike.width



