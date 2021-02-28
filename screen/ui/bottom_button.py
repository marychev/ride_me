from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty
from kivy.uix.button import Button

from bike.bike import Bike
from bike.bikes import get_by_title as get_bike_by_title
from level.base.base_level import BaseLevel
from level.maps import get_by_title as get_map_by_title
from utils.color import BgAnimation
from utils.init import app_config, calc_rest_rm
from utils.validation import ValidObject


class PanelBtn(Button):
    size_hint_x = NumericProperty(0.5)
    size_hint_y = NumericProperty(1)
    disabled = BooleanProperty(True)


class RightPanelBtn(PanelBtn):
    pos_hint = DictProperty({'right': 1, 'bottom': 1})
    text = StringProperty('Ok')

    def _current_screen(self):
        return self.parent.parent.parent

    def on_press(self, *args, **kwargs):
        _screen = self._current_screen()
        menu_screen = ValidObject.menu_screen(_screen.manager.get_screen('menu'))
        bikes_screen = ValidObject.bikes_screen(_screen.manager.get_screen('bikes'))
        maps_screen = ValidObject.maps_screen(_screen.manager.get_screen('maps'))
        shop_screen = ValidObject.shop_screen(_screen.manager.get_screen('shop'))
        screens = [menu_screen, bikes_screen, maps_screen, shop_screen]

        if 'BikesScreen' == _screen.__class__.__name__:
            if not app_config('bike', 'title'):
                bike = get_bike_by_title(bikes_screen.ids['title'].text)
                rest_rm = calc_rest_rm(bike['price'])
                if Bike.buy(bike):
                    self.change_rm(screens, rest_rm)
                    self.change_character_wrap(bikes_screen.ids['character_wrap_power'], bike['power'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_speed'], bike['speed'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_acceleration'], bike['acceleration'])
                    self.change_character_wrap(bikes_screen.ids['character_wrap_agility'], bike['agility'])
                    self.cancel_animation_button(screens, 'left_panel_menu_bikes')

                    self.init_item(menu_screen.init_bike)

        elif 'MapsScreen' == _screen.__class__.__name__:
            if not app_config('map', 'title'):
                map = get_map_by_title(maps_screen.ids['title'].text)
                rest_rm = calc_rest_rm(map['price'])
                if BaseLevel.buy(map):
                    self.change_rm(screens, rest_rm)
                    self.change_character_wrap(maps_screen.ids['character_wrap_level'], map['level'])
                    self.change_character_wrap(maps_screen.ids['character_wrap_map'], map['map'])
                    self.change_character_wrap(maps_screen.ids['character_wrap_total_way'], map['total_way'])
                    self.cancel_animation_button(screens, 'left_panel_menu_maps')

                    self.init_item(menu_screen.init_map)

    def init_item(self, cb_init):
        self.text = 'Ok'
        self.disabled = True
        cb_init()
        Clock.schedule_once(self._create_animation, 0)
        Clock.schedule_once(self._clear_animation, .6)

    def _create_animation(self, dt):
        bg = BgAnimation(widget=self._current_screen())
        bg.anim_color(bg.rgba_success)

    def _clear_animation(self, dt):
        bg = BgAnimation(widget=self._current_screen())
        bg.anim_color(bg.rgba_default)

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

        if type(value) is int:
            character_wrap.value = progress_bar.value = int(value)
            character_wrap.max = progress_bar.max = int(value)
        else:
            character_wrap.title = value
        buttons[0].disabled = buttons[1].disabled = False
        buttons[0].opacity = buttons[1].opacity = 1
