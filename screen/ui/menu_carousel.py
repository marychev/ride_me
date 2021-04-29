from typing import Union
from kivy.properties import ListProperty, StringProperty
from kivy.uix.carousel import Carousel

from bike.bikes import BIKES, get_by_title as get_bike_by_title
from level.maps import MAPS, get_by_title as get_map_by_title
from screen.ui.bottom_button import RightPanelBtn
from screen.ui.slide import Slide
from utils.color import Color as UColor
from utils.init import app_config
from utils.validation import ValidObject


class MenuCarousel(Carousel):
    objects = ListProperty()
    direction = StringProperty('right')

    def __init__(self, **kwargs):
        super(MenuCarousel, self).__init__(**kwargs)

        slides = [Slide(item=o) for o in self.objects]
        [self.add_widget(slide) for slide in slides]

        self.set_title(self.objects[0]['title'])

    def _screen(self):
        return self.parent.parent

    def define_color(self, section):
        return UColor.hex(UColor.WHITE) if app_config(section, 'title') == self.current_slide.item['title']\
            else UColor.hex(UColor.GRAY)

    def title_active(self):
        screen = self._screen()
        return '{}{}'.format(screen.ids['title'].text, ' *')

    def on_index(self, *args, **kwargs):
        super(MenuCarousel, self).on_index(*args)
        self.set_title(self.current_slide.item['title'])

    def change_prop_title(self, sid: str, value: Union[int, str], color: UColor):
        screen = self._screen()

        if type(value) is int:
            screen.ids[sid].value = value

        RightPanelBtn.change_color_labels_right_panel(screen.ids[sid], color)

        if screen.ids[sid].has_value:
            screen.ids[sid].title = screen.ids[sid].format_number(screen.ids[sid].key, value, screen.ids[sid].max)
        else:
            screen.ids[sid].title = screen.ids[sid].format_string(value)


class BikeMenuCarousel(MenuCarousel):
    objects = ListProperty(BIKES)

    def set_title(self, value):
        if self.parent:
            screen = ValidObject.bikes_screen(self._screen())
            screen.ids['title'].text = value

    def on_index(self, *args, **kwargs):
        super(BikeMenuCarousel, self).on_index(*args, **kwargs)
        bikes_screen = ValidObject.bikes_screen(self._screen())

        if app_config('bike', 'title') == self.current_slide.item['title']:
            bikes_screen.ids['title'].text = self.title_active()
        else:
            self.char_btn_disabled('character_wrap_power')
            self.char_btn_disabled('character_wrap_speed')
            self.char_btn_disabled('character_wrap_acceleration')
            self.char_btn_disabled('character_wrap_agility')

        color = self.define_color('bike')
        bikes_screen.ids['title'].color = color

        bike_model = get_bike_by_title(self.current_slide.item['title'])
        self.change_prop_title('character_wrap_price', str(bike_model.price), color)
        self.change_prop_title('character_wrap_power', str(bike_model.power), color)
        self.change_prop_title('character_wrap_speed', str(bike_model.speed), color)
        self.change_prop_title('character_wrap_acceleration', str(bike_model.acceleration), color)
        self.change_prop_title('character_wrap_agility', str(bike_model.agility), color)

    def char_btn_disabled(self, sid: str):
        bikes_screen = ValidObject.bikes_screen(self._screen())
        box_layout = bikes_screen.ids[sid].children[1]
        btn = box_layout.children[0]
        btn.disabled = True
        btn.opacity = 0.2


class MapMenuCarousel(MenuCarousel):
    objects = ListProperty(MAPS)

    def on_index(self, *args, **kwargs):
        super(MapMenuCarousel, self).on_index(*args, **kwargs)
        maps_screen = ValidObject.maps_screen(self._screen())

        if app_config('map', 'title') == self.current_slide.item['title']:
            maps_screen.ids['title'].text = self.title_active()

        _map = get_map_by_title(self.current_slide.item['title'])
        color = self.define_color('map')
        maps_screen.ids['title'].color = color

        self.change_prop_title('character_wrap_price', _map['price'], color)
        self.change_prop_title('character_wrap_record', '*dev', color)
        self.change_prop_title('character_wrap_level', _map['level'], color)
        self.change_prop_title('character_wrap_map', _map['map'], color)
        self.change_prop_title('character_wrap_total_way', _map['total_way'], color)

    def set_title(self, value):
        if self.parent:
            screen = ValidObject.maps_screen(self._screen())
            if screen.ids['title']:
                if screen.ids:
                    screen.ids['title'].text = value
                    return

