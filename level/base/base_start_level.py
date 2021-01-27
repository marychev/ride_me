from objects import Start


class BaseStartLevel:
    def start(self):
        starts = Start.widgets_on_road(self.road)
        return starts[0] if len(starts) > 0 else None

    def create_start(self):
        pos = self.map_objects('start')[0]['pos']
        size = (50, (self.road.height / 2) + 10)
        return Start.create(pos, size)

    def add_start(self):
        if (self.bike and self.road) and not self.road.start:
            map_start = self.map_objects('start')[0]

            if self.road.distance_traveled < map_start['pos'][0]:
                start = self.create_start()
                self.road.start = start
                self.road.add_widget(start)

    def remove_start(self):
        map_starts = self.map_objects('start')
        map_start = map_starts[0] if len(map_starts) == 1 else None
        if map_start and self.road.distance_traveled > map_start['pos'][0] and self.road.start.x < 0:
            self.road.remove_widget(self.road.start)

    def map_objects(self, name):
        raise NotImplementedError
