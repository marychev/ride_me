from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty, ReferenceListProperty, NumericProperty, BooleanProperty
from kivy.uix.button import Button

from utils.dir import abstract_path

Builder.load_file(abstract_path('screen/ui/panel.kv'))


class MenuButton(Button):
    size_hint_x = NumericProperty(0.8)
    size_hint_y = NumericProperty(0.6)
    size_hint = ReferenceListProperty(size_hint_x, size_hint_y)
    background_color = ListProperty([1, 1, 1, 1])
    app = ObjectProperty()
    empty = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(MenuButton, self).__init__(**kwargs)
        self.app = App.get_running_app()

        if self.empty:
            self.start_pulsing()

    def start_pulsing(self, *args):
        anim = Animation(background_color=[0.1, 0.8, 0.6, 1], duration=.6) \
               + Animation(background_color=[0.6, 0.2, 0.7, 1], duration=.6)
        anim.repeat = True
        anim.start(self)

    def on_press(self, screen_name='menu'):
        Animation.cancel_all(self, 'background_color')  # -? dw
        Animation.stop_all(self, 'background_color')    # -? dw
        self.app.root.current = screen_name


class LeftPanelMenuBikes(MenuButton):
    text = StringProperty('Bikes')

    def on_press(self, screen_name='bikes'):
        super(LeftPanelMenuBikes, self).on_press(screen_name)


class LeftPanelMenuMaps(MenuButton):
    text = StringProperty('Maps')

    def on_press(self, screen_name='maps'):
        super().on_press(screen_name)


class LeftPanelMenuShop(MenuButton):
    text = StringProperty('Shop')
    empty = BooleanProperty(False)

    def on_press(self, screen_name='shop'):
        super().on_press(screen_name)
