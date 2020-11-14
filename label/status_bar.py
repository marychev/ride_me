from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from screen.utils import get_game_screen
from utils.dir import abstract_path

Builder.load_file(abstract_path('label/status_bar.kv'))


class StatusBar(Label):
    text = StringProperty('Start Game!')

    @staticmethod
    def get_status_bar():
        # print('[WARNING] Try to get a game object from DOM! get_status_bar')
        return get_game_screen().ids.status_bar if get_game_screen() else None

    @staticmethod
    def get_road():
        # print('[WARNING] Try to get a game object from DOM! get_road')
        return get_game_screen().ids.road if get_game_screen() else None

    @staticmethod
    def get_rock():
        # TODO: TEMP print('[WARNING] Try to get a game object from DOM! get_rock')
        return get_game_screen().ids.get('rock') if get_game_screen() else None

    @staticmethod
    def get_finish():
        # print('[WARNING] Try to get a game object from DOM! get_finish')
        return get_game_screen().ids.finish if get_game_screen() else None

    @staticmethod
    def get_bike():
        # print('[WARNING] Try to get a game object from DOM! get_bike')
        return get_game_screen().ids.bike if get_game_screen() else None

    @staticmethod
    def get_background_image_animation():
        # print('[WARNING] Try to get a game object from DOM! get_background_image_animation')
        return get_game_screen().ids.background_image_animation if get_game_screen() else None

    def show_status(self, title):
        self.text = '{}\r{}{}'.format(title, self.show_status_road(), self.show_status_bike())

    def show_status_finished(self):
        self.text = 'FINISH!'
        self.size_hint = .99, .88
        self.valign = 'center'
        self.halign = 'center'
        self.font_size = 42

    def show_status_bike(self, title='BIKE'):
        bike = self.get_bike()
        if bike:
            return '''
------------------------------------------- [{}]
_acceleration:             {}
_power:                           {} 
Speed:                          {}
Pos:                              {}
'''.format(
                title,
                bike.acceleration, bike.power,
                bike.speed,
                bike.pos,
            )

    def show_status_road(self, title='ROAD'):
        road = self.get_road()
        if road:
            return '''
----------------------------------------------- [{}]
total_way:                    {}
distance_traveled:    {}
*left_go:                          {}'''.format(
                title,
                road.total_way,
                road.distance_traveled,
                road.total_way - road.distance_traveled,
            )
