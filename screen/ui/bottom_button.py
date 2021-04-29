from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, DictProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

from bike.bike import Bike
from bike.bikes import get_by_title as get_bike_by_title
from level.base.base_level import BaseLevel
from level.maps import get_by_title as get_map_by_title
from objects.currency.currency import Currency
from utils.color import BgAnimation, Color as UColor
from utils.init import app_config, calc_rest_rm
from utils.validation import ValidObject
from utils.get_object import GetObject
from utils.sizes import GOSize as GOS


class PanelBtn(Button):
    disabled = BooleanProperty(True)
    height = NumericProperty(GOS.WH_PanelBtn.value)
    width = NumericProperty(GOS.WH_PanelBtn.value)
    size_hint = ListProperty([None, None])


class RightPanelBtn(PanelBtn):
    pos_hint = DictProperty({'right': 1, 'bottom': 1})
    text = StringProperty('Ok')

    def _current_screen(self):
        return self.parent if hasattr(self.parent, 'manager') else None

    def on_press(self, *args, **kwargs):
        _screen = self._current_screen()
        menu_screen = ValidObject.menu_screen(_screen.manager.get_screen('menu'))
        bikes_screen = ValidObject.bikes_screen(_screen.manager.get_screen('bikes'))
        maps_screen = ValidObject.maps_screen(_screen.manager.get_screen('maps'))
        shop_screen = ValidObject.shop_screen(_screen.manager.get_screen('shop'))
        screens = [menu_screen, bikes_screen, maps_screen, shop_screen]

        if 'BikesScreen' == _screen.__class__.__name__:
            if not app_config('bike', 'title'):
                bike_model = get_bike_by_title(bikes_screen.ids['title'].text)
                rest_rm = calc_rest_rm(bike_model.price)

                if Bike.buy(bike_model):
                    RightPanelBtn.change_rm(screens, rest_rm)
                    RightPanelBtn.change_character_wrap(bikes_screen.ids['character_wrap_price'], bike_model.price)
                    RightPanelBtn.change_character_wrap(bikes_screen.ids['character_wrap_power'], bike_model.power)
                    RightPanelBtn.change_character_wrap(bikes_screen.ids['character_wrap_speed'], bike_model.speed)
                    RightPanelBtn.change_character_wrap(bikes_screen.ids['character_wrap_acceleration'], bike_model.acceleration)
                    RightPanelBtn.change_character_wrap(bikes_screen.ids['character_wrap_agility'], bike_model.agility)
                    RightPanelBtn.cancel_animation_button(screens, 'left_panel_menu_bikes')

                    self.init_item(menu_screen.init_bike)
                    RightPanelBtn.change_bottom_right_btn(menu_screen)
                    bikes_screen.ids['title'].color = UColor.hex(UColor.WHITE)
                else:
                    Clock.schedule_once(self._create_animation_fail, 0)
                    Clock.schedule_once(self._clear_animation, .5)

        elif 'MapsScreen' == _screen.__class__.__name__:
            if not app_config('map', 'title'):
                map_model = get_map_by_title(maps_screen.ids['title'].text)
                rest_rm = calc_rest_rm(map_model.price)

                if BaseLevel.buy(map_model):
                    RightPanelBtn.change_rm(screens, rest_rm)
                    RightPanelBtn.change_character_wrap(maps_screen.ids['character_wrap_price'], map_model.price)
                    RightPanelBtn.change_character_wrap(maps_screen.ids['character_wrap_record'], '/dev/')
                    RightPanelBtn.change_character_wrap(maps_screen.ids['character_wrap_level'], map_model.level)
                    RightPanelBtn.change_character_wrap(maps_screen.ids['character_wrap_map'], map_model.map)
                    RightPanelBtn.change_character_wrap(maps_screen.ids['character_wrap_total_way'], map_model.total_way)
                    RightPanelBtn.cancel_animation_button(screens, 'left_panel_menu_maps')

                    self.init_item(menu_screen.init_map)
                    RightPanelBtn.change_bottom_right_btn(menu_screen)
                    maps_screen.ids['title'].color = UColor.hex(UColor.WHITE)
                else:
                    Clock.schedule_once(self._create_animation_fail, 0)
                    Clock.schedule_once(self._clear_animation, .5)

    def init_item(self, cb_init):
        self.text = 'Ok'
        self.disabled = True
        cb_init()
        Clock.schedule_once(self._create_animation_success, 0)
        Clock.schedule_once(self._clear_animation, .4)

    def _create_animation_success(self, dt):
        bg = BgAnimation(widget=self._current_screen())
        bg.anim_color(bg.rgba_success)

    def _create_animation_fail(self, dt):
        bg = BgAnimation(widget=self._current_screen())
        bg.anim_color(bg.rgba_error)

    def _clear_animation(self, dt):
        bg = BgAnimation(widget=self._current_screen())
        bg.anim_color(bg.rgba_default)

    @staticmethod
    def cancel_animation_button(screens, sid):
        [Animation.cancel_all(s.ids[sid], 'background_color') for s in screens]

    @staticmethod
    def change_rm(screens, value):
        for s in screens:
            GetObject.get_child(s, 'RMLayout').ids['panel_rm'].text = "{}: {}".format(Currency.units, value)
            return

    @staticmethod
    def change_character_wrap(character_wrap, value, color=UColor.hex(UColor.WHITE)):
        if type(value) is int:
            progress_bar = ValidObject.progress_bar(character_wrap.children[0].children[0])
            character_wrap.value = value
            character_wrap.max = progress_bar.max = value

        if character_wrap.has_value:
            character_wrap.title = character_wrap.format_number()
        else:
            character_wrap.title = character_wrap.format_string()

        RightPanelBtn.prop_buttons_show(character_wrap)
        RightPanelBtn.change_color_labels_right_panel(character_wrap, color)

    @staticmethod
    def prop_buttons_show(character_wrap):
        btn = character_wrap.children[1].children[0]
        btn.disabled = not character_wrap.has_value
        btn.opacity = 1

    @staticmethod
    def change_bottom_right_btn(menu_screen):
        if app_config('bike', 'title') and app_config('map', 'title'):
            menu_screen.ids['right_panel_btn'].text = 'Go'
            menu_screen.ids['right_panel_btn'].disabled = False

    @staticmethod
    def change_color_labels_right_panel(character_wrap, color):
        RightPanelBtn._change_color_labels(character_wrap.children[0], color)
        RightPanelBtn._change_color_labels(character_wrap.children[1], color)

    @staticmethod
    def _change_color_labels(wrap_children, color):
        for lbl in wrap_children.children[:]:
            if type(lbl) is Label:
                lbl.color = color
