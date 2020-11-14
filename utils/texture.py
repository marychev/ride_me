from kivy.uix.image import Image
from utils.dir import abstract_path
from kivy.graphics import Color, Line, Rectangle


def image_texture(source):
    return Image(source=abstract_path(source)).texture


def redraw_texture(widget, name='texture'):
    texture = widget.property(name)
    texture.dispatch(widget)


def repeat_texture(texture, uvsize_x=1, uvsize_y=-1):
    texture.wrap = 'repeat'
    texture.uvsize = (uvsize_x, uvsize_y)


def set_texture_uvpos(widget, uvpos_x, uvpos_y):
    widget.texture.uvpos = (uvpos_x, uvpos_y)
    widget.canvas.before.clear()
    with widget.canvas.before:
        Color(1, 1, 1, 1)
        Rectangle(texture=widget.texture, size=widget.size, pos=widget.pos)
