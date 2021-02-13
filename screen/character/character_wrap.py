from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from utils.dir import abstract_path

Builder.load_file(abstract_path('screen/character/character_wrap.kv'))


class CharacterWrap(BoxLayout):
    pass
