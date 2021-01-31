from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from button.keyboard import KeyboardHandler
from utils.validation import ValidObject
from utils.color import switcher_color


class Tools(BoxLayout, KeyboardHandler):
    bike = ObjectProperty(None)
    right_btn = ObjectProperty(None)
    left_btn = ObjectProperty(None)

    def indicator_power(self, value):
        bike = self.get_bike()
        color = switcher_color(value, bike.max_power)
        return "[color={}]{:3.2f}[/color] [sup]Power[/sup]".format(color, value)

    def indicator_speed(self, value):
        bike = self.get_bike()
        color = switcher_color(bike.speed, bike.max_speed)
        return "[sup]Speed[/sup][color={}]{:3.2f}[/color]".format(color, value)

    def get_bike(self):
        if not self.bike:
            screen = ValidObject.screen(self.parent)
            self.bike = ValidObject.bike(screen.ids['bike'])
        return self.bike
