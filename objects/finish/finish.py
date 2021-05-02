from kivy.lang import Builder
from objects.start.start import Start
from objects.currency.currency import Currency
from utils.dir import abstract_path
from utils.type import TPosN

Builder.load_file(abstract_path('objects/finish/finish.kv'))


class Finish(Start):
    @staticmethod
    def curtain_text(road, bike):
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

    def get_x(self) -> TPosN:
        bike = self.get_bike()
        road = self.get_road()
        return (road.total_way - road.distance_traveled) + bike.x + bike.width
