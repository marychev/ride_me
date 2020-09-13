from kivy.core.window import Window


class KeyboardHandler(object):
    def __init__(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        print('_keyboard_closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('_on_keyboard_down')
        # bike = self.parent.scene.bike
        if keycode[1] == 'right':
            # bike.on_move(0)
            self.right_btn.on_press()
        elif keycode[1] == 'left':
            self.left_btn.on_press()
            # bike.on_stop(0)
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        print('_on_keyboard_up')
        if keycode[1] == 'right':
            self.right_btn.on_release()
        elif keycode[1] == 'left':
            self.left_btn.on_release()
        return True
