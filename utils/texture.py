from kivy.uix.image import Image
from utils.dir import abstract_path
from kivy.graphics import Color, Line, Rectangle

from kivy.uix.label import Label


def image_texture(source):
    return Image(source=abstract_path(source)).texture


def redraw_texture(widget, name='texture'):
    texture = widget.property(name)
    texture.dispatch(widget)

    if hasattr(widget, 'texture') and widget.texture and not hasattr(widget, 'label'):
        widget.canvas.clear()
        with widget.canvas:
            Color((1, 1, 1, 1))
            Rectangle(pos=widget.pos, size=widget.size, texture=widget.texture)

    elif hasattr(widget, 'label') and widget.label:
        widget.label.pos = widget.pos
        widget.label_canvas_before()

    if name not in ['cloud_big_texture', 'cloud_min_texture', 'cloud_middle_texture']:
        print('.. .. .. redraw_texture', name, widget)


def repeat_texture(texture, uvsize_x=1, uvsize_y=-1):
    texture.wrap = 'repeat'
    texture.uvsize = (uvsize_x, uvsize_y)


def set_texture_uvpos(widget, uvpos_x, uvpos_y):
    widget.texture.uvpos = (uvpos_x, uvpos_y)
    widget.canvas.before.clear()
    with widget.canvas.before:
        Color(1, 1, 1, 1)
        Rectangle(texture=widget.texture, size=widget.size, pos=widget.pos)
