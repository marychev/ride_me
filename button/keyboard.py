from kivy.core.window import Window
from screen.utils import get_game_screen


class KeyboardHandler(object):
    def __init__(self):
        self.on_down_last_time = 0
        self.active_key = None
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def get_left_btn(self):
        return get_game_screen().ids.left_btn_wrap.children[0]

    def get_right_btn(self):
        return get_game_screen().ids.right_btn_wrap.children[0]

    def _keyboard_closed(self):
        print('CLOSED: _keyboard_closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('DOWN: _on_keyboard_down', self.active_key, keycode[1])

        left_btn = self.get_left_btn()
        right_btn = self.get_right_btn()

        if keycode[1] == 'right' and self.active_key is None:
            right_btn.state = 'down'
            right_btn.on_press()
        elif keycode[1] == 'left' and self.active_key is None:
            left_btn.state = 'down'
            left_btn.on_press()
        elif keycode[1] == 'spacebar' and self.active_key is None:
            right_btn.state = 'down'
            right_btn.on_double_press(self._keyboard)

        self.active_key = keycode[1]
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        print('UP: _on_keyboard_up', self.active_key)

        left_btn = self.get_left_btn()
        right_btn = self.get_right_btn()

        if keycode[1] == 'right':
            right_btn.state = 'normal'
            right_btn.on_release()
        elif keycode[1] == 'left':
            left_btn.state = 'normal'
            left_btn.on_release()
        elif keycode[1] == 'spacebar':
            right_btn.state = 'normal'
            right_btn.on_double_release(self._keyboard)

        self.active_key = None
        return True
