from objects.lamp.lamp import Lamp
from kivy.core.window import Window
from utils.texture import redraw_texture


class BaseLampLevel:

    def lamps(self):
        return Lamp.widgets_on_road(self.road)

    def new_map_lamps(self):
        return self.new_map_objects(road_objects=self.lamps(), map_objects=self.init_objects('lamp'))

    def create_lamp(self, pos):
        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        pos_x = pos[0]

        if pos_x > Window.width:
            pos_x -= Window.width

        print('CREATE:', pos_x, pos_y)
        lamp = Lamp.create(pos=(pos_x, pos_y))
        redraw_texture(lamp)

        return lamp

    def add_lamp(self, lamp):
        if self.bike and self.road and lamp:
            print(' + + + ADD LAMP + + +', lamp.pos)
            self.road.add_widget(lamp)

    def add_lamps(self):
        road_lamps = self.lamps() and self.lamps()[:]
        map_lamps = self.init_objects('lamp') and self.init_objects('lamp')[:]
        new_map_objects = self.new_map_objects(road_objects=road_lamps, map_objects=map_lamps)
        print('>> >> new_map_objects:', new_map_objects)

        if new_map_objects and len(new_map_objects) > 0:
            create_lamps = [self.create_lamp(obj['pos']) for obj in new_map_objects]
            [self.add_lamp(lamp) for lamp in create_lamps]

    def remove_lamps(self):
        if self.road.distance_traveled > 0:
            pass
            # self.remove_widgets(self.lamps())
