from objects.rock.rock import Rock


class BaseRockLevel:
    def rocks(self):
        return Rock.widgets_on_road(self.road)

    def create_rock(self, pos):
        if len(self.rocks()) < len(self.init_objects('rock')):
            pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
            return Rock.create(pos=(pos[0], pos_y))

    def add_rock(self, widget):
        if (self.bike and self.road) and (len(self.rocks()) < len(self.init_objects('rock'))):
            self.road.add_widget(widget)

    def add_rocks(self):
        road_objects = self.rocks() and self.rocks()[:]
        map_objects = self.init_objects('rock') and self.init_objects('rock')[:]
        new_map_objects = self.new_map_objects(road_objects=road_objects, map_objects=map_objects)

        if (self.bike and self.road) and (road_objects and len(road_objects) < len(map_objects)):
            create_rocks = [self.create_rock(obj['pos']) for obj in new_map_objects]
            [self.add_rock(w) for w in create_rocks]

    def remove_rock(self):
        self.remove_widgets(self.rocks())
