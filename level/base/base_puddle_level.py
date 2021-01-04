from objects.puddle.puddle import Puddle


class BasePuddleLevel:

    def puddles(self):
        return Puddle.widgets_on_road(self.road)

    def create_puddle(self, pos):
        if len(self.puddles()) < len(self.init_objects('puddle')):
            pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
            return Puddle.create(pos=(pos[0], pos_y))

    def add_puddle(self, widget):
        if (self.bike and self.road) and (len(self.puddles()) < len(self.init_objects('puddle'))):
            self.road.add_widget(widget)

    def add_puddles(self):
        new_map_objects = self.new_map_objects(road_objects=self.puddles(), map_objects=self.init_objects('puddle'))

        if (len(new_map_objects) > 0) and (len(self.puddles()) < len(self.init_objects('puddle'))):
            create_puddles = [self.create_puddle(obj['pos']) for obj in new_map_objects]
            [self.add_puddle(w) for w in create_puddles]

    def remove_puddles(self):
        self.remove_widgets(road_objects=self.puddles())
