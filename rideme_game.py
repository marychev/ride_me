from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from label.status_bar import StatusBar
from layout import Tools, Scene
from kivy.core.window import Window
from button.right_button import RightButtonWidget
from button.left_button import LeftButtonWidget


class RideMeGame(BoxLayout):
    status_bar = ObjectProperty(None)
    scene = ObjectProperty(None)
    tool = ObjectProperty(None)
    states = ListProperty(['INIT', 'START', 'PLAY', 'PAUSE', 'FINISH'])

    def __init__(self, **kwargs):
        super(RideMeGame, self).__init__(**kwargs)

        # self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        # self._keyboard.bind(on_key_down=self._on_keyboard_down)
        # self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.status_bar = StatusBar()
        self.scene = Scene(status_bar=self.status_bar)
        self.tool = Tools(status_bar=self.status_bar)

        self.scene.add_widget(self.status_bar)
        self.add_widget(self.scene)
        self.add_widget(self.tool)

    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard.unbind(on_key_up=self._on_keyboard_up)
    #     self._keyboard = None
    #
    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 'right':
    #         self.scene.bike.move()
    #         RightButtonWidget.change_text(self.status_bar, 'Go')
    #     elif keycode[1] == 'left':
    #         self.scene.bike.stop()
    #         LeftButtonWidget.change_text(self.status_bar, '...breakup...')
    #     return True
    #
    # def _on_keyboard_up(self, keyboard, keycode):
    #     if keycode[1] == 'right':
    #         self.scene.bike.relax()
    #         RightButtonWidget.change_text(self.status_bar)
    #     elif keycode[1] == 'left':
    #         self.scene.bike.relax()
    #         LeftButtonWidget.change_text(self.status_bar)
    #     return True
