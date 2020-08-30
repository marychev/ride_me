from kivy.core.window import Window


class KeyboardHandler(object):
    def __init__(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def on_move(self):
        raise NotImplementedError

    def on_relax(self):
        raise NotImplementedError

    def on_stop(self):
        raise NotImplementedError

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'right':
            self.on_move()
        elif keycode[1] == 'left':
            self.on_stop()
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'right' or keycode[1] == 'left':
            self.on_relax()
        return True
