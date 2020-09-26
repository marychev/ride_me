from kivy.graphics import Color, Line, Rectangle
from kivy.utils import get_color_from_hex


def show_outline(widget, color_hex='2B027A', line_width=1):
    rectangle = (widget.x, widget.y, widget.width, widget.height)
    with widget.canvas.before:
        Color(*get_color_from_hex(color_hex))
        Line(width=line_width, rectangle=rectangle)


def background(widget, color_hex_background, color_hex_outline=None):
    color_hex_outline and show_outline(widget, color_hex_outline)
    with widget.canvas.before:
        Color(*get_color_from_hex(color_hex_background))
        Rectangle(pos=widget.pos, size=widget.size)
