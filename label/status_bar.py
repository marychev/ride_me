from kivy.properties import StringProperty
from kivy.uix.label import Label
from screen.utils import get_game_screen
from kivy.lang import Builder

Builder.load_file("label/status_bar.kv")


class StatusBar(Label):
    text = StringProperty('Start Game!')

    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)

    @staticmethod
    def get_road():
        return get_game_screen().ids.road

    @staticmethod
    def get_finish():
        return get_game_screen().ids.finish

    @staticmethod
    def get_bike():
        return get_game_screen().ids.bike

    @staticmethod
    def get_background_image_animation():
        return get_game_screen().ids.background_image_animation

    @staticmethod
    def get_status_bar():
        return get_game_screen().ids.status_bar

    def show_status(self, title, bike, road):
        self.text = '{}\r{}{}'.format(title, bike.show_status(), road.show_status())
        return self.text

    def show_status_finished(self):
        self.text = 'FINISH!'
        self.size_hint = .99, .88
        self.valign = 'center'
        self.halign = 'center'
        self.font_size = 42
        return self.text
