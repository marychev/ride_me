from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from conf import SECOND_GAME
from utils.checks import set_texture_uvpos


class Road(Widget):
    texture = ObjectProperty(Image(source='road/road-2.png').texture)
    distance_traveled = NumericProperty(0)
    acceleration = NumericProperty(0)    # todo: for bike

    def __init__(self, **kwargs):
        super(Road, self).__init__(**kwargs)
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (Window.width / self.texture.width, -1)

    def get_status_bar(self):
        return self.parent.status_bar

    def go(self, dt):
        print('go road')
        self.acceleration += SECOND_GAME
        self.distance_traveled = self.texture.uvpos[0] + self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('Go bike ===>', self.parent.bike, self)

    def relax(self, dt):
        print('relax road')
        self.acceleration -= SECOND_GAME + dt
        if self.acceleration < 0:
            self.acceleration = 0
            return False

        self.distance_traveled = self.texture.uvpos[0] + self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('... Relax ...', self.parent.bike, self)

    def stop(self, dt):
        print('stop road')
        self.acceleration -= SECOND_GAME / dt
        if self.acceleration < 0:
            self.acceleration = 0
            return False

        self.distance_traveled = self.texture.uvpos[0] + self.acceleration
        set_texture_uvpos(self, self.distance_traveled, self.texture.uvpos[1])
        # todo: self.get_status_bar().show_status('S T O P', self.parent.bike, self)

    def show_status(self, title='ROAD'):
        return '''
{}
-----------------------------------------------
UVPos:          {}
Pos:            {}'''.format(
            title,
            self.texture.uvpos, self.pos
        )
