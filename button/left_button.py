from kivy.uix.image import Image
from kivy.clock import Clock
from conf import SECOND_GAME
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
Builder.load_file('button/left_button.kv')


class LeftButtonWidget(ButtonBehavior, Image):
    @staticmethod
    def get_game_screen():
        app = App.get_running_app()
        return app.root.get_screen('game')

    def get_road(self):
        return self.get_game_screen().ids.road

    def get_bike(self):
        return self.get_game_screen().ids.bike

    def button_state_style(self):
        if 'down' in self.state:
            self.canvas.opacity = 0.5
            self.disabled = True
        elif 'normal' in self.state:
            self.canvas.opacity = 1
            self.disabled = False
        else:
            raise 0

    @staticmethod
    def change_text(widget, text='...'):
        widget.text = text

    def on_press(self):
        print('press left', self)
        self.button_state_style()

        # road = self.get_road()
        # Clock.unschedule(road.go)
        # Clock.unschedule(road.relax)
        # Clock.schedule_interval(road.stop, SECOND_GAME)

    def on_release(self):
        self.button_state_style()

        # road = self.get_road()
        # Clock.unschedule(road.go)
        # Clock.unschedule(road.stop)
        # Clock.schedule_interval(road.relax, SECOND_GAME)