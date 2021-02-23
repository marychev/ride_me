from kivy.animation import Animation
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty
from kivy.uix.button import Button
from bike.bikes import get_by_title as get_bike_by_title
from utils.validation import ValidObject
from utils.get_object import app_config
from bike.bike import Bike


class PanelBtn(Button):
    size_hint_x = NumericProperty(0.5)
    size_hint_y = NumericProperty(1)
    disabled = BooleanProperty(True)


class RightPanelBtn(PanelBtn):
    pos_hint = DictProperty({'right': 1, 'bottom': 1})
    text = StringProperty('Ok')

    def on_press(self, *args, **kwargs):
        _screen = self.parent.parent.parent
        app = App.get_running_app()

        menu_screen = ValidObject.menu_screen(_screen.manager.get_screen('menu'))
        bikes_screen = ValidObject.bikes_screen(_screen.manager.get_screen('bikes'))
        maps_screen = ValidObject.maps_screen(_screen.manager.get_screen('maps'))
        shop_screen = ValidObject.shop_screen(_screen.manager.get_screen('shop'))
        screens = [menu_screen, bikes_screen, maps_screen, shop_screen]

        if 'BikesScreen' == _screen.__class__.__name__:
            if app.config.get('bike', 'name') == 'None':
                bike = get_bike_by_title(bikes_screen.ids['title'].text)
                rest_rm = int(app_config('bike', 'rm')) - int(bike['price'])

                if Bike.buy(bike):
                    self.change_rm(screens, rest_rm)
                    self.change_character_wrap(bikes_screen.ids['character_wrap_power'], bike['power'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_speed'], bike['speed'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_acceleration'], bike['acceleration'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_agility'], bike['agility'])

                    self.cancel_animation_button(screens, 'left_panel_menu_bikes')

                    self.text = 'Ok'
                    self.disabled = True

                    menu_screen.init_bike()

    @staticmethod
    def cancel_animation_button(screens, sid):
        [Animation.cancel_all(s.ids[sid], 'background_color') for s in screens]

    @staticmethod
    def change_rm(screens, value):
        for s in screens:
            s.ids['panel_rm'].text = str(value)

    @staticmethod
    def change_character_wrap(character_wrap, value):
        progress_bar = ValidObject.progress_bar(character_wrap.children[1].children[0])
        buttons = [character_wrap.children[2].children[0], character_wrap.children[2].children[2]]
        character_wrap.value = progress_bar.value = int(value)
        character_wrap.max = progress_bar.max = int(value)
        buttons[0].disabled = buttons[1].disabled = False
        buttons[0].opacity = buttons[1].opacity = 1
