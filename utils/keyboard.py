from kivy.core.window import Window


class KeyboardHandler(object):
    def __init__(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def on_move_btn(self, dt):
        raise NotImplementedError

    def on_relax(self, dt):
        raise NotImplementedError

    def on_stop(self, dt):
        raise NotImplementedError

    def _keyboard_closed(self):
        print('_keyboard_closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('_on_keyboard_down')
        if keycode[1] == 'right':
            self.on_move(0)
        elif keycode[1] == 'left':
            self.on_stop(0)
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        print('_on_keyboard_up')
        if keycode[1] == 'right' or keycode[1] == 'left':
            self.on_relax(0)
        return True
