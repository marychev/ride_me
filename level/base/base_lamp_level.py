from objects.lamp.lamp import Lamp
from kivy.core.window import Window


class BaseLampLevel:
    def _road_objects(self):
        return self.lamps() and self.lamps()[:]

    def _map_objects(self):
        return self.init_objects('lamp') and self.init_objects('lamp')[:]

    def lamps(self):
        return Lamp.widgets_on_road(self.road)

    def new_map_lamps(self):
        return self.new_map_objects(self._road_objects(), self._map_objects())

    def create_lamp(self, pos):
        pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
        pos_x = pos[0] - Window.width if pos[0] > Window.width else pos[0]
        return Lamp.create(pos=(pos_x, pos_y))

    def add_lamp(self, lamp):
        if self.bike and self.road and lamp:
            print(' + + + ADD LAMP + + +', lamp.pos)
            self.road.add_widget(lamp)

    def add_lamps(self):
        new_map_lamps = self.new_map_lamps()
        if new_map_lamps and len(new_map_lamps) > 0:
            create_lamps = [self.create_lamp(obj['pos']) for obj in new_map_lamps]
            [self.add_lamp(lamp) for lamp in create_lamps]

    def remove_lamps(self):
        if self.road.distance_traveled > 0:
            self.remove_widgets(self._road_objects())
