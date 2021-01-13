from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from objects.base.game_image import GameImage
from utils.dir import abstract_path
from utils.validation import ValidObject


class Lamp(GameImage):
    TEXTURE = Image(source=abstract_path('objects/lamp/img/lamp.png')).texture
    texture = ObjectProperty(TEXTURE)

    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.lamp(w) for w in road.children if w.__class__.__name__ == 'Lamp']

    def lamps(self):
        road = self.get_road()
        if road:
            if road.lamps():
                return road.lamps()
            else:
                return road and Lamp.widgets_on_road(road)

    def pre_validate(self, pos):
        road = self.get_road()
        for ro in road.lamps[:]:
            if ro.pos[0] == pos[0]:
                return False
        return True

    def create_game_object(self, pos):
        road = self.get_road()
        if not self.pre_validate(pos):
            return False
        else:
            pos_y = road.line_points[-1] if pos[1] <= 0 else pos[1]
            return self.create(pos=(pos[0], pos_y))

    def add_game_object(self, widget):
        road = self.get_road()
        bike = self.get_bike()

        if widget:
            for ro in road.lamps[:]:
                if ro.pos[0] == widget.pos[0]:
                    return False

            if bike:
                print(' + + + ADD LAMP + + +', widget.pos)
                road.lamps.append(widget)
                road.add_widget(widget)

    def add_game_objects(self):
        road = self.get_road()
        bike = self.get_bike()
        # zone = VisibleZone.current_visible_zone(road)
        res_map_lamps = self.level_map_objects('lamp')

        if bike and len(road.lamps) <= len(res_map_lamps):
            for mo in res_map_lamps:
                # if zone.collide_point_widget(mo):
                widget = self.create_game_object(mo['pos'])
                self.add_game_object(widget)

    def remove_game_objects(self):
        self.remove_widgets(self.road.lamps)
