from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from utils.dir import abstract_path
from kivy.properties import NumericProperty, DictProperty, BooleanProperty

Builder.load_file(abstract_path('screen/ui/character_wrap.kv'))


class CharacterWrap(BoxLayout):
    value = NumericProperty()
    max = NumericProperty()
    has_value = BooleanProperty()

