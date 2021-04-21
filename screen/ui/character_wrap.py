from typing import Union
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from utils.dir import abstract_path
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from utils.color import Color as UColor

Builder.load_file(abstract_path('screen/ui/character_wrap.kv'))


class CharacterWrap(BoxLayout):
    key = StringProperty()
    title = StringProperty()
    value = NumericProperty()
    max = NumericProperty()
    has_value = BooleanProperty()

    def format_number(self, key=None, value=None, max=None):
        markup = "{key} [color=#{color_sub}][sub]{val}[/sub][/color]:[color=#{color_sup}][sup]{max}[/sup][/color]"
        return markup.format(
            key=key or self.key, val=value or self.value, max=max or self.max,
            color_sub=UColor.GREEN, color_sup=UColor.ORANGE)

    def format_string(self, value: Union[int, str, None] = None):
        return "{}: {}".format(self.key, value or self.value)
