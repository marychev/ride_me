def redraw_texture(widget, name='texture'):
    texture = widget.property(name)
    texture.dispatch(widget)
