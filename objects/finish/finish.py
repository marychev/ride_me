from kivy.lang import Builder
from objects import Start
from objects.currency.currency import Currency
from utils.dir import abstract_path
from utils.validation import ValidObject

Builder.load_file(abstract_path('objects/finish/finish.kv'))


class Finish(Start):
    @staticmethod
    def widgets_on_road(road):
        return [ValidObject.finish(w) for w in road.children if w.__class__.__name__ == 'Finish']

    @staticmethod
    def start_timer_text(road, bike):
        return '''
        [size=80]Finish[/size]
        Level:                      {}
        Total Way:             {}
        Total Time:           {:0.3f}
        {}:                        {}
        '''.format(
            road.level.name,
            road.total_way,
            bike.finish_dt - bike.start_dt,
            Currency.units, bike.currency)

    def get_x(self):
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width
