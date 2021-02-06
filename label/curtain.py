from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from utils.get_object import GetObject


class Curtain(Label):
    sid = StringProperty('curtain')
    markup = BooleanProperty(True)
    scene = ObjectProperty(None)
    road = ObjectProperty(None)
    stop = NumericProperty(3)

    def do_start_timer(self):
        self.font_size = 120
        self.text = str(self.stop)
        self.draw_background(0.7)
        return self.text

    def draw_background(self, transparent=0.6):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, transparent)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height))

    def collision_text_rock(self):
        bike = GetObject(self.road).bike
        return 'Collision to {}.\nPress on "Restart Game"\n{:.2f}'.format(
            bike.__class__.__name__,
            bike.finish_dt - bike.start_dt)

    def add_to_game_screen(self):
        self.draw_background()
        screen = GetObject(self.road).screen
        scene = GetObject(self.road).scene
        screen.ids[self.sid] = self
        scene.add_widget(self)

