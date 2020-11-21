from road.finish import Finish


class BaseFinishLevel:
    def finish(self):
        finishes = Finish.widgets_on_road(self.road)
        return finishes[0] if len(finishes) > 0 else None

    def create_finish(self):
        pos = self.map_objects('finish')[0]['pos']
        size = (120, (self.road.height / 2) + 10)
        return Finish.create(pos, size)

    def add_finish(self):
        if (self.bike and self.road) and not self.road.finish:
            map_finish = self.map_objects('finish')[0]

            if self.road.distance_traveled < map_finish['pos'][0]:
                finish = self.create_finish()
                self.road.total_way = finish.pos[0]
                self.road.finish = finish
                self.road.add_widget(finish)
