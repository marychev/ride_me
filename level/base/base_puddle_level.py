from objects.puddle.puddle import Puddle


class BasePuddleLevel:

    def puddles(self):
        return Puddle.widgets_on_road(self.road)

    def create_puddle(self, pos):
        road_objects = self.puddles() and self.puddles()[:]
        map_objects = self.init_objects('puddle') and self.init_objects('puddle')[:]

        if len(road_objects) < len(map_objects):
            pos_y = self.road.line_points[-1] if pos[1] <= 0 else pos[1]
            return Puddle.create(pos=(pos[0], pos_y))

    def add_puddle(self, widget):
        road_objects = self.puddles() and self.puddles()[:]
        map_objects = self.init_objects('puddle') and self.init_objects('puddle')[:]

        if (self.bike and self.road) and (len(road_objects) < len(map_objects)):
            self.road.add_widget(widget)

    def add_puddles(self):
        road_objects = self.puddles() and self.puddles()[:]
        map_objects = self.init_objects('puddle') and self.init_objects('puddle')[:]
        new_map_objects = self.new_map_objects(road_objects=road_objects, map_objects=map_objects)

        if new_map_objects and len(new_map_objects) > 0 and len(road_objects) < len(map_objects):
            create_puddles = [self.create_puddle(obj['pos']) for obj in new_map_objects]
            [self.add_puddle(w) for w in create_puddles]

    def remove_puddles(self):
        self.remove_widgets(road_objects=self.puddles())
