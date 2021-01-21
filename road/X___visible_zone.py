# from kivy.uix.widget import Widget
# from kivy.core.window import Window
# from kivy.properties import NumericProperty, ReferenceListProperty
#
#
# class VisibleZone(Widget):
#     x = NumericProperty(20)
#     y = NumericProperty(20)
#     pos = ReferenceListProperty(x, y)
#     width = NumericProperty(Window.width - 20)
#     height = NumericProperty(Window.height - 50)
#     size = ReferenceListProperty(width, height)
#
#     @staticmethod
#     def current_visible_zone(road):
#         _zone = [w for w in road.children if w.__class__.__name__ == 'VisibleZone']
#         return _zone and _zone[0]
#
#     def rectangle(self):
#         return self.x, self.y, self.width, self.height
#
#     def collide_point_widget(self, widget):
#         if type(widget) == dict:
#             return self.collide_point(widget['pos'][0], self.y)
#         elif widget.x:
#             return self.collide_point(widget.x, self.y)
