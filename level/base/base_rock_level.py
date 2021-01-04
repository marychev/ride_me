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
        new_map_objects = self.new_map_objects(road_objects=self.rocks(), map_objects=self.init_objects('rock'))
        if (self.bike and self.road) and (len(self.rocks()) < len(self.init_objects('rock'))):
            create_rocks = [self.create_rock(obj['pos']) for obj in new_map_objects]
            [self.add_rock(w) for w in create_rocks]

    def remove_rock(self):
        self.remove_widgets(self.rocks())
