from kivy.graphics import Color, Line


def show_outline(widget):
    rectangle = (widget.x, widget.y, widget.width, widget.height)
    with widget.canvas.before:
        Color(.5, .5, .5, 1, mode='rgb')
        Line(width=1, rectangle=rectangle)
