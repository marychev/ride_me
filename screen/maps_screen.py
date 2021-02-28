from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path
# from kivy.properties import ObjectProperty
# from screen.ui.bottom_button import RightPanelBtn

Builder.load_file(abstract_path('screen/maps_screen.kv'))


class MapsScreen(Screen):
    def get_character_wrap_ids(self):
        return (
            self.ids['character_wrap_record'],
            self.ids['character_wrap_level'],
            self.ids['character_wrap_map'],
            self.ids['character_wrap_total_way'])
