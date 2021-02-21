from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from utils.dir import abstract_path


Builder.load_file(abstract_path('screen/bikes_screen.kv'))


class BikesScreen(Screen):
    
    def __init__(self, **kwargs):
        super(BikesScreen, self).__init__(**kwargs)




