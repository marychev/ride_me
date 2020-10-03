from kivy.core.window import Window
from kivy.clock import Clock


class KeyboardHandler(object):
    def __init__(self):
        self.active_key = None
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        print('CLOSED: _keyboard_closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('DOWN: _on_keyboard_down', self.active_key)
        if keycode[1] == 'right' and self.active_key is None:
            self.right_btn.on_press()
        elif keycode[1] == 'left' and self.active_key is None:
            self.left_btn.on_press()

        self.active_key = keycode[1]
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        print('UP: _on_keyboard_up', self.active_key)
        if keycode[1] == 'right':
            self.right_btn.on_release()
        elif keycode[1] == 'left':
            self.left_btn.on_release()

        self.active_key = None
        return True
