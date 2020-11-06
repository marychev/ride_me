import os.path
from kivy.properties import StringProperty
from kivy.uix.label import Label
from screen.utils import get_game_screen
from kivy.lang import Builder

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'status_bar.kv'))
Builder.load_file(path)


class StatusBar(Label):
    text = StringProperty('Start Game!')

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

    @staticmethod
    def get_road():
        print('[WARNING] Try to get a game object from DOM! get_road')
        return get_game_screen().ids.road if get_game_screen() else None

    @staticmethod
    def get_rock():
        # TODO: TEMP print('[WARNING] Try to get a game object from DOM! get_rock')
        return get_game_screen().ids.get('rock') if get_game_screen() else None

    @staticmethod
    def get_finish():
        #print('[WARNING] Try to get a game object from DOM! get_finish')
        return get_game_screen().ids.finish if get_game_screen() else None

    @staticmethod
    def get_bike():
        #print('[WARNING] Try to get a game object from DOM! get_bike')
        return get_game_screen().ids.bike if get_game_screen() else None

    @staticmethod
    def get_background_image_animation():
        print('[WARNING] Try to get a game object from DOM! get_background_image_animation')
        return get_game_screen().ids.background_image_animation

    @staticmethod
    def get_status_bar():
        #print('[WARNING] Try to get a game object from DOM! get_status_bar')
        return get_game_screen().ids.status_bar if get_game_screen() else None

    def show_status(self, title, bike, road):
        self.text = '{}\r{}{}'.format(title, bike.show_status(), road.show_status())

    def show_status_finished(self):
        self.text = 'FINISH!'
        self.size_hint = .99, .88
        self.valign = 'center'
        self.halign = 'center'
        self.font_size = 42

